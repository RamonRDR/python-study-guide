<div align="center">

# Proyecto 06 · Organizador de Archivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

> **Fase 10 · Proyectos Prácticos**

Este proyecto organiza archivos hijos directos en carpetas por categoría, manteniendo descubrimiento, planificación, manejo de colisiones y mutación del filesystem explícitos y comprobables.

## Objetivos de aprendizaje

Al finalizar este proyecto, deberías poder:

- descubrir archivos directos con `pathlib` sin recorrido recursivo;
- clasificar nombres de archivo de forma determinista con reglas de sufijo sin distinguir mayúsculas y minúsculas;
- modelar cambios planificados del filesystem con dataclasses inmutables;
- separar una fase de planificación sin mutación de una fase de ejecución con efectos secundarios;
- detectar colisiones de destino exactas y sin distinción de mayúsculas/minúsculas;
- elegir políticas de colisión explícitas en lugar de sobrescribir datos silenciosamente;
- tratar los symlinks y archivos especiales como fronteras del filesystem;
- razonar sobre carreras time-of-check/time-of-use;
- comparar objetos del filesystem mediante identidad `(device, inode)`;
- anclar directorios con file descriptors en Linux;
- fijar orígenes sin bloquear ante sustituciones tardías por FIFO;
- usar semántica atómica no-replace en la frontera final de commit del nombre exacto;
- distinguir comprobaciones lógicas con `casefold()` de garantías atómicas de nombre exacto;
- conservar estado incierto en lugar de borrar entradas a ciegas durante recuperación;
- probar código de filesystem de forma segura con directorios temporales.

## Problema

Imagina un workspace ficticio con:

```text
workspace/
├── notes.txt
├── rows.csv
├── photo.png
├── backup.tar.gz
└── script.py
```

El organizador debería producir:

```text
workspace/
├── documents/
│   └── notes.txt
├── data/
│   └── rows.csv
├── images/
│   └── photo.png
├── archives/
│   └── backup.tar.gz
└── other/
    └── script.py
```

El desafío importante no es solo mover archivos. El proyecto hace visibles las decisiones del filesystem antes de mutar y se niega a afirmar garantías de seguridad que la plataforma actual no puede hacer cumplir.

## Requisitos

La implementación debe:

1. aceptar un directorio de origen existente que no sea symlink;
2. inspeccionar únicamente hijos directos;
3. ignorar directorios anidados;
4. registrar symlinks hijos directos por separado sin seguirlos;
5. clasificar archivos regulares por el sufijo del nombre;
6. conservar exactamente los nombres de archivo;
7. crear carpetas de destino solo cuando sean necesarias;
8. producir un orden determinista;
9. construir un plan inmutable antes de mutar;
10. rechazar rutas de categoría inválidas, incluidos directorios de categoría que sean symlinks;
11. detectar colisiones de destino exactas y sin distinción de mayúsculas/minúsculas durante planificación/preflight;
12. ofrecer políticas explícitas `ERROR` y `SKIP` durante la planificación;
13. ejecutar un preflight completo;
14. capturar la identidad de los orígenes planificados;
15. nunca reemplazar silenciosamente un destino exacto;
16. volver a comprobar nombres de destino equivalentes por `casefold()` inmediatamente antes del commit;
17. rechazar supuestos obsoletos sobre origen, raíz o categoría durante la ejecución;
18. nunca ejecutar `unlink()` a ciegas sobre staging o rollback cuya identidad pueda haber cambiado;
19. devolver un resultado estructurado solo después de verificar el destino planificado.

## Alcance deliberado

El pipeline es:

```text
directorio de origen
    -> descubrimiento de archivos directos
    -> clasificación por sufijo
    -> plan seguro contra colisiones
    -> preflight de ejecución
    -> carpetas de categoría ancladas
    -> claim del origen
    -> nueva comprobación casefold durante la mutación
    -> commit atómico no-replace del nombre exacto en el destino
```

Este proyecto excluye intencionalmente:

- organización recursiva;
- inspección MIME o de contenido;
- renombrado automático de duplicados;
- hashing o deduplicación;
- eliminación como función expuesta al usuario;
- transacciones de rollback para el plan completo;
- watchers de filesystem;
- interfaz gráfica;
- almacenamiento en la nube;
- movimientos entre filesystems distintos.

Mantener estas responsabilidades fuera de alcance hace que las reglas de seguridad sean más fáciles de inspeccionar.

## Categorías

`FileCategory` define cinco destinos:

| Categoría | Carpeta | Sufijos representativos |
|---|---|---|
| Documentos | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Datos | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Imágenes | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Archivos comprimidos | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Otros | `other/` | todo lo que no coincida arriba |

La coincidencia ignora diferencias de mayúsculas y minúsculas. La clasificación usa solo nombres de archivo y nunca abre su contenido.

## Modelos centrales

### `MoveAction`

Representa un movimiento planificado:

```text
archivo de origen -> destino de categoría
```

Sus invariantes exigen rutas absolutas, el mismo nombre en origen y destino y una carpeta que corresponda a la categoría seleccionada.

### `OrganizationPlan`

Almacena:

- el directorio de origen absoluto;
- valores `MoveAction` ordenados;
- archivos omitidos por colisión;
- symlinks hijos directos ignorados.

El plan es inmutable. Crearlo no crea directorios ni mueve archivos.

### `OrganizationResult`

Registra exactamente los destinos planificados devueltos tras una ejecución exitosa.

## Descubrimiento intencionalmente superficial

`discover_files()` devuelve solo archivos regulares hijos directos.

El movimiento recursivo introduce contratos adicionales para rutas relativas, categorías anidadas y nombres duplicados entre directorios. Esos temas pertenecen a un proyecto mayor.

## Planificar antes de mutar

`plan_organization()` valida el workspace, escanea archivos directos, los clasifica y calcula destinos sin modificar el filesystem.

```text
observar -> decidir -> validar -> mutar
```

La propuesta existe como datos antes de que comiencen los efectos secundarios, lo que facilita revisión y pruebas.

## Políticas de colisión

### `CollisionPolicy.ERROR`

La planificación genera `FileExistsError` cuando ya existe un nombre de destino.

### `CollisionPolicy.SKIP`

Los archivos conflictivos permanecen en el origen y aparecen en `skipped_collisions`.

La ejecución vuelve a comprobar colisiones después de planificar. La existencia del nombre exacto se hace cumplir de forma atómica en el commit final de Linux; los nombres equivalentes por `casefold()` se vuelven a comprobar inmediatamente antes de ese commit.

## Colisiones sin distinción de mayúsculas/minúsculas

Los filesystems difieren en sensibilidad de caja. El organizador compara nombres lógicos de destino usando `casefold()`.

```text
Report.TXT
report.txt
```

Estos nombres se consideran una colisión lógica durante planificación, preflight y la comprobación inmediatamente anterior al commit, incluso en un filesystem case-sensitive.

Hay una frontera importante: en un filesystem case-sensitive, la primitiva del kernel `RENAME_NOREPLACE` protege únicamente el **nombre exacto del destino**. Un proceso externo no cooperativo todavía puede crear otro nombre equivalente por `casefold()` en el pequeño intervalo posterior al último escaneo. Por ello, el proyecto no afirma unicidad atómica case-insensitive donde el filesystem no ofrece esa garantía.

## Fronteras de symlink y anclaje de directorios

El organizador no sigue symlinks hijos directos. También rechaza un directorio de origen o carpeta de categoría que sea symlink.

En la ruta segura de Linux, la raíz y las categorías necesarias se abren con `O_DIRECTORY | O_NOFOLLOW`. Sus identidades `(device, inode)` se comparan repetidamente con las rutas que todavía deberían alcanzarlas.

Esto importa porque un file descriptor permanece unido al mismo directorio aunque otro proceso renombre ese directorio. El pinning evita redirección mediante symlink; la validación del anclaje evita continuar silenciosamente dentro de un directorio que ya no es alcanzable por la ruta planificada.

## Por qué el preflight no basta

Una implementación ingenua podría hacer:

```python
if not destination.exists():
    source.rename(destination)
```

La comprobación puede quedar obsoleta inmediatamente. Otro proceso puede crear el destino o sustituir un origen o directorio después de la validación.

El preflight reduce estados inseguros, pero las garantías sensibles a concurrencia también deben existir en la frontera de mutación.

## Identidad del filesystem

La implementación representa identidad con:

```text
(st_dev, st_ino)
```

El nombre `notes.txt` es una entrada de directorio, no la identidad del objeto del filesystem.

Durante la ejecución segura en Linux, el origen planificado se abre con `O_NOFOLLOW | O_NONBLOCK` cuando `O_NONBLOCK` está disponible. La flag nonblocking impide que una sustitución tardía por FIFO bloquee `open()`, mientras el `fstat()` posterior sigue exigiendo un archivo regular con la identidad `(device, inode)` planificada. El descriptor abierto fija el inode esperado durante el commit.

## Nombres de staging de longitud fija

La ruta segura de Linux reclama temporalmente la entrada pública del origen bajo un nombre interno:

```text
.fo-stage-<32 caracteres hexadecimales>
```

El staging tiene longitud fija y nunca incorpora el nombre original. Así, un filename válido y largo no hace que el nombre interno supere un límite típico `NAME_MAX`.

## Commit atómico no-replace en Linux

La ruta segura de Linux usa `renameat2(..., RENAME_NOREPLACE)` mediante file descriptors anclados.

Conceptualmente:

```text
1. ejecutar preflight y capturar identidad del origen
2. abrir y anclar la raíz
3. abrir y anclar las categorías necesarias
4. fijar el inode del origen con O_NOFOLLOW | O_NONBLOCK
5. reclamar atómicamente origen -> staging corto
6. verificar identidad del staging y anclajes
7. escanear de nuevo la categoría anclada buscando un destino equivalente por casefold
8. renombrar atómicamente staging -> destino exacto con RENAME_NOREPLACE
9. verificar identidad del destino y anclajes
10. informar éxito
```

`RENAME_NOREPLACE` convierte la existencia del **nombre exacto del destino** en parte de la propia operación atómica. No existe una comprobación `exists()` separada seguida de un rename que pueda reemplazar. El escaneo `casefold()` previo detecta colisiones lógicas visibles en esa frontera, pero se documenta como una nueva comprobación y no como un lock atómico case-insensitive.

La ruta segura normal no finaliza el movimiento con `unlink()` del staging. Así no se traslada la misma ventana check-to-unlink del nombre público a un nombre interno.

## Recuperación conservadora

Los errores concurrentes pueden dejar estado incierto. La recuperación prioriza conservación frente a limpieza destructiva.

Si la ejecución ya movió el origen al staging y después detecta una condición insegura, puede crear un hard link no-replace de vuelta al nombre de origen cuando sea posible. No elimina a ciegas el staging.

Un pathname de staging no funciona como lock de inode. Si el rename final consume una entrada de reemplazo y la verificación de identidad del destino detecta la divergencia, la ejecución conserva intacto el destino ajeno y, antes de cerrar el descriptor aún anclado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`. Esta recuperación conserva datos recuperables sin afirmar que el inode original haya sobrevivido a la carrera.

Por ello, la ejecución segura en Linux exige deliberadamente permiso de lectura para cada archivo regular planificado. La legibilidad se valida antes de crear los directorios de categoría y de nuevo al fijar el inode del origen para la mutación; los fallos de permisos se informan como `PermissionError`, no como un falso cambio de identidad del origen.

En escenarios raros de carrera/fallo, esto puede dejar una entrada interna de recuperación. Es preferible a borrar datos cuya identidad actual no puede demostrarse.

El plan completo de varios archivos no es transaccional.

## Contrato de plataforma

La implementación hace explícitas las garantías por plataforma:

- **Linux:** ejecución segura con FDs anclados usa `renameat2(RENAME_NOREPLACE)` cuando está disponible, con protección atómica no-replace para el nombre exacto del destino y nuevas comprobaciones `casefold()` durante la mutación;
- **Windows:** el fallback usa el comportamiento de `os.rename()` que rechaza un destino existente y realiza una nueva comprobación `casefold()` best-effort junto con validaciones de identidad alrededor de la operación;
- **otros POSIX:** la ejecución genera `NotImplementedError` cuando no puede aplicar de forma segura la semántica no-replace requerida.

Un ejemplo orientado a seguridad debe fallar honestamente en vez de degradar su contrato de forma silenciosa.

## Flujo de ejecución

`execute_plan()` realiza:

1. validación del tipo del plan;
2. revalidación del directorio de origen;
3. revalidación de rutas de categoría;
4. captura de identidades de los orígenes planificados;
5. preflight de colisiones;
6. selección de capacidades de plataforma;
7. preparación de directorios anclados;
8. pinning nonblocking y claim del origen;
9. nueva comprobación de colisión por `casefold()` durante la mutación;
10. commit atómico no-replace del nombre exacto;
11. verificación de destino y anclajes;
12. construcción de `OrganizationResult`.

## Determinismo

Archivos y acciones se ordenan por:

```python
(path.name.casefold(), path.name)
```

Esto mantiene ejemplos, pruebas y revisión estables.

## Ejecutar el demo

Desde la raíz del repositorio:

```bash
python practical-projects/06-file-organizer/demo.py
```

El demo usa `TemporaryDirectory`, crea solo archivos ficticios, imprime el plan, lo ejecuta y muestra las carpetas resultantes.

## Ejecutar las pruebas

Suite enfocada:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

El capítulo evita un conteo fijo de pruebas porque la cobertura de regresión evoluciona con los reviews.

La cobertura incluye:

- clasificación por sufijo;
- descubrimiento superficial y determinista;
- manejo de symlinks;
- invariantes de modelos inmutables;
- colisiones exactas y sin distinción de mayúsculas/minúsculas;
- políticas `ERROR` y `SKIP`;
- orígenes ausentes u obsoletos;
- destinos exactos tardíos;
- destinos tardíos equivalentes por `casefold()` antes del commit final;
- sustitución tardía del origen por symlink/archivo/FIFO;
- pinning nonblocking del origen;
- carreras de symlink y rename de categoría;
- carreras de rename de la raíz;
- staging de longitud fija;
- finalización del staging sin `unlink()`;
- verificación de identidad del destino;
- ejecución exitosa y planes vacíos.

## Rutas de fallo importantes

### Directorio de origen ausente

Genera `FileNotFoundError`.

### Ruta de origen es archivo regular

Genera `NotADirectoryError`.

### Directorio de origen es symlink

Se rechaza antes del escaneo.

### Ruta de categoría es archivo o symlink

Se rechaza antes de planificar o ejecutar.

### Destino aparece después de la planificación

El preflight y la nueva comprobación `casefold()` durante la mutación generan `FileExistsError` para las colisiones que observan. El `RENAME_NOREPLACE` final de Linux rechaza de forma atómica un destino con nombre exacto que aparezca en la frontera del commit.

### El origen planificado se convierte en FIFO u otro archivo especial

El pinning de Linux usa flags nonblocking y luego `fstat()` rechaza la sustitución por no ser un archivo regular, en lugar de bloquear la ejecución.

### Origen planificado cambia

La ejecución genera error en vez de tratar la sustitución como el archivo planificado.

### Raíz o categoría se renombra/sustituye

La validación del anclaje genera error en vez de devolver una ruta que ya no identifica el destino comprometido.

### Primitiva atómica no-replace no disponible

La plataforma no compatible genera error en vez de debilitar silenciosamente el contrato.

## Errores comunes

### Mover mientras se escanea

Mezclar descubrimiento y mutación hace difícil razonar sobre fallos parciales. Construye primero el plan.

### Tratar un nombre como identidad

Las entradas de directorio pueden sustituirse conservando el mismo nombre. Usa identidad del filesystem cuando esa diferencia importe.

### Abrir una ruta sustituible en modo bloqueante

`O_NOFOLLOW` rechaza symlinks, pero no evita que un FIFO bloquee un `open()` de solo lectura. Usa pinning nonblocking antes de validar el tipo de archivo.

### Suponer que un escaneo `casefold()` es un lock atómico

Un escaneo en user space puede detectar colisiones lógicas sin distinción de caja, pero en un filesystem case-sensitive no puede impedir que aparezca después otro nombre con distinta combinación de mayúsculas/minúsculas. Mantén la garantía atómica limitada al nombre exacto aplicado por la primitiva del kernel.

### Comprobar inmediatamente antes de `unlink()`

Sigue existiendo una ventana check-to-unlink. Cuando importa la identidad de la eliminación, reestructura la operación en vez de añadir otra comprobación.

### Suponer que un FD abierto conserva el mismo pathname

El descriptor sigue el inode del directorio tras un rename. Verifica su anclaje contra la ruta planificada.

### Incluir el nombre completo del origen en el staging

Los nombres válidos pueden estar ya cerca de `NAME_MAX`. Mantén los nombres internos acotados de forma independiente.

### Limpiar a ciegas después de una carrera

El cleanup también muta. Conserva entradas inciertas en vez de borrar algo que puede pertenecer a otro actor.

### Tratar preflight como transacción

El filesystem puede cambiar después. Un plan de varios archivos sigue siendo una secuencia de commits individualmente protegidos.

## Ejercicio

Extiende el organizador con un **renderizador dry-run** sin cambiar el comportamiento de ejecución.

Requisitos:

1. aceptar un `OrganizationPlan`;
2. devolver texto legible y determinista;
3. mostrar movimientos planificados, colisiones omitidas y symlinks ignorados;
4. nunca acceder ni modificar el filesystem;
5. añadir pruebas para planes vacíos y no vacíos.

## Desafíos de extensión

Considera:

- mapeo configurable de sufijos;
- categorías definidas por el usuario;
- exportación/importación JSON con validación de plan obsoleto;
- journal de operaciones;
- descubrimiento recursivo con reglas explícitas de ruta relativa;
- deduplicación por checksum;
- herramientas de recuperación/auditoría para entradas de staging conservadas;
- diseño transaccional para otro dominio de problema.

Cada extensión introduce nuevas invariantes. Define el contrato antes de añadir código.

## Discusión de portafolio

Una explicación útil no es “escribí un script que mueve archivos”.

Una versión más fuerte es:

> Diseñé un flujo de filesystem con planificación determinista, políticas explícitas de colisión, fronteras de symlink/archivo especial, identidad por inode, directorios anclados por descriptors, nombres de staging acotados, nuevas comprobaciones `casefold()` durante la mutación y commit atómico no-replace del nombre exacto en Linux mediante `renameat2(RENAME_NOREPLACE)`. El manejo de fallos conserva estado incierto en lugar de borrar entradas a ciegas.

Eso comunica decisiones de ingeniería, no solo uso de APIs.

## Referencia rápida

| Tarea | Función/tipo |
|---|---|
| Clasificar filename | `classify_path()` |
| Descubrir archivos regulares directos | `discover_files()` |
| Construir una propuesta segura | `plan_organization()` |
| Elegir comportamiento de colisión | `CollisionPolicy` |
| Describir un movimiento | `MoveAction` |
| Mantener el plan inmutable | `OrganizationPlan` |
| Ejecutar el plan | `execute_plan()` |
| Mantener destinos exitosos | `OrganizationResult` |
| Identificar objetos del filesystem | `(st_dev, st_ino)` |
| Nueva comprobación lógica por `casefold()` | `listdir()` sobre el directorio anclado |
| Commit seguro del nombre exacto en Linux | `renameat2(RENAME_NOREPLACE)` |

## Qué sigue

El Proyecto 05 generó archivos. El Proyecto 06 toma la siguiente frontera: descubrir y organizar archivos con seguridad.

El Proyecto 07 vuelve a subir de nivel, combinando registros de dominio validados y estados explícitos de workflow en un **flujo ficticio de conciliación**.