<div align="center">

# Proyecto 06 · Organizador de Archivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

> **Fase 10 · Proyectos Prácticos**

Este proyecto organiza archivos hijos directos en carpetas por categoría, manteniendo descubrimiento, planificación, manejo de colisiones y mutación del filesystem explícitos y comprobables.

## Objetivos de aprendizaje

Al finalizar este proyecto, deberías poder:

- descubrir archivos con `pathlib` sin recorrer recursivamente un árbol;
- clasificar nombres de archivo de forma determinista con reglas de sufijo sin distinguir mayúsculas y minúsculas;
- modelar cambios planificados del filesystem con dataclasses inmutables;
- separar una fase de planificación sin mutación de una fase de ejecución con efectos secundarios;
- detectar colisiones exactas y colisiones de destino ignorando diferencias de mayúsculas/minúsculas;
- elegir una política de colisión explícita en lugar de sobrescribir datos silenciosamente;
- tratar los symlinks como una frontera específica del filesystem;
- revalidar supuestos inmediatamente antes de mutar;
- garantizar en el propio paso de mutación que un destino exacto nunca sea reemplazado;
- verificar la identidad del origen a través de fronteras time-of-check/time-of-use;
- conservar un estado de destino incierto en lugar de hacer rollback destructivo;
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

El desafío importante no es simplemente llamar a una función de movimiento. El proyecto debe hacer visibles las decisiones destructivas antes de cambiar nada.

## Requisitos

La implementación debe:

1. aceptar un directorio de origen existente que no sea symlink;
2. inspeccionar solo hijos directos de ese directorio;
3. ignorar directorios anidados;
4. registrar symlinks hijos directos por separado sin seguirlos;
5. clasificar archivos regulares por el sufijo del nombre;
6. conservar exactamente cada nombre de archivo;
7. crear carpetas de destino solo cuando sean necesarias;
8. producir un orden determinista;
9. construir un plan inmutable antes de mutar;
10. rechazar rutas de categoría inválidas, incluidos directorios de categoría que sean symlinks;
11. detectar colisiones de destino exactas y sin distinción de mayúsculas/minúsculas;
12. ofrecer políticas explícitas `ERROR` y `SKIP` durante la planificación;
13. ejecutar un preflight completo antes de cualquier movimiento;
14. nunca reemplazar silenciosamente un destino exacto que aparezca después del preflight;
15. rechazar un origen planificado cuya identidad de filesystem cambie antes del commit;
16. nunca eliminar un destino no verificado al manejar un fallo al eliminar el origen;
17. devolver un resultado estructurado después de una ejecución exitosa.

## Alcance deliberado

El pipeline es:

```text
directorio de origen
    -> descubrimiento de archivos directos
    -> clasificación por sufijo
    -> plan seguro contra colisiones
    -> preflight de ejecución
    -> carpetas de categoría necesarias
    -> movimientos no-replace con identidad verificada
```

Este proyecto intencionalmente **no** incluye:

- organización recursiva;
- inspección MIME o de contenido;
- renombrado automático de duplicados;
- hashing o deduplicación;
- eliminación;
- transacciones de rollback para el plan completo;
- watchers de filesystem;
- interfaz gráfica;
- almacenamiento en la nube;
- organización entre filesystems distintos.

Mantener estas responsabilidades fuera de alcance hace visibles las reglas de seguridad en lugar de esconderlas dentro de un gestor de archivos genérico.

## Categorías

`FileCategory` define cinco destinos:

| Categoría | Carpeta | Sufijos representativos |
|---|---|---|
| Documentos | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Datos | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Imágenes | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Archivos comprimidos | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Otros | `other/` | todo lo que no coincida con las reglas anteriores |

La coincidencia ignora diferencias de mayúsculas y minúsculas. La clasificación usa solo el nombre del archivo y no abre su contenido.

## Modelos centrales

### `MoveAction`

Representa un movimiento planificado:

```text
archivo de origen -> destino de categoría
```

Sus invariantes exigen rutas absolutas, el mismo nombre en origen y destino y una carpeta de destino que corresponda a la categoría seleccionada.

### `OrganizationPlan`

Almacena:

- el directorio de origen absoluto;
- valores `MoveAction` ordenados;
- archivos omitidos por colisión;
- symlinks hijos directos ignorados.

El plan es inmutable. Crearlo no crea directorios ni mueve archivos.

### `OrganizationResult`

Registra exactamente los destinos planificados que se movieron con éxito.

## Descubrimiento intencionalmente superficial

`discover_files()` devuelve solo archivos regulares que son hijos directos.

Los directorios anidados no se recorren. El movimiento recursivo introduce preguntas adicionales sobre rutas relativas, carpetas de categoría anidadas y nombres duplicados provenientes de subdirectorios distintos. Esas preguntas pertenecen a un proyecto mayor.

## Planificar antes de mutar

`plan_organization()` valida el directorio, escanea los archivos, clasifica cada uno y calcula destinos sin modificar el filesystem.

Esto produce un patrón de ingeniería útil:

```text
observar -> decidir -> validar -> mutar
```

Es más fácil probar y revisar una operación propuesta cuando existe como datos antes de que comiencen los efectos secundarios.

## Políticas de colisión

### `CollisionPolicy.ERROR`

La planificación se detiene con `FileExistsError` cuando ya existe un nombre de destino.

### `CollisionPolicy.SKIP`

Los archivos cuyo destino colisiona permanecen en el directorio de origen y se listan en `skipped_collisions`.

La política se aplica durante la planificación. La ejecución sigue rechazando nuevas colisiones exactas que aparezcan después.

## Colisiones sin distinción de mayúsculas/minúsculas

El proyecto compara nombres de destino con `casefold()` durante planificación y preflight. Por ejemplo:

```text
Report.TXT
report.txt
```

Estos nombres se consideran una colisión lógica.

## Frontera de symlink

El organizador no sigue symlinks hijos directos.

También rechaza:

- un directorio de origen que sea symlink;
- una carpeta de categoría implementada como symlink.

En plataformas con soporte de descriptores de directorio, la ejecución fija origen y carpetas de categoría usando `O_DIRECTORY | O_NOFOLLOW`. Así, una categoría que se convierta en symlink después del preflight no puede redirigir la mutación fuera del workspace.

## Por qué el preflight no basta

Una implementación inicial podría hacer:

```python
if not destination.exists():
    source.rename(destination)
```

Eso contiene una carrera time-of-check/time-of-use. Otro proceso puede crear el destino después de la comprobación y antes del rename.

En POSIX, `rename()` puede reemplazar un destino existente. Además, un origen planificado puede ser sustituido después del preflight. Por eso la ejecución debe validar tanto la disponibilidad del destino como la identidad del origen en la frontera de mutación.

## Mutación exacta no-replace

La ejecución usa un hard link en el mismo filesystem como protección del destino:

```text
1. capturar la identidad del origen durante el preflight
2. revalidar que el origen siga siendo el mismo archivo regular
3. crear el hard link de destino sin reemplazo
4. verificar que el destino referencia la identidad esperada del origen
5. revalidar otra vez la identidad del origen
6. eliminar la ruta de origen original
```

La identidad del filesystem se representa mediante el par `(device, inode)` devuelto por `stat`. Esto permite distinguir “el mismo nombre” de “el mismo objeto del filesystem”. Una sustitución tardía por symlink o por otro archivo regular aborta la ejecución en vez de aparecer como movimiento exitoso.

`os.link()` no reemplaza un destino existente. Como cada carpeta de destino está dentro del mismo directorio de origen, origen y destino permanecen intencionalmente en el mismo filesystem para este proyecto.

Si la creación del link falla, el origen permanece intacto. Si la eliminación del origen falla después de crear el destino, la implementación conserva deliberadamente **el destino** y genera un error. No ejecuta un `unlink()` de rollback incondicional porque otro proceso podría haber reemplazado esa entrada de directorio durante el intervalo. Conservar estado incierto es más seguro que eliminar algo cuya identidad ya no puede demostrarse.

Esto no convierte el plan completo en una transacción. Las garantías son más estrechas: los destinos exactos no se sobrescriben silenciosamente, los orígenes planificados se revalidan por identidad y el manejo de fallos no elimina intencionalmente un destino no verificado.

## Flujo de ejecución

`execute_plan()` realiza:

1. validación de tipo;
2. revalidación del directorio de origen;
3. revalidación de rutas de categoría;
4. captura de identidades de los orígenes planificados;
5. preflight de colisiones de destino;
6. creación/apertura solo de las carpetas necesarias;
7. movimientos exactos no-replace con identidad verificada;
8. construcción de `OrganizationResult`.

Un plan obsoleto no se acepta a ciegas.

## Determinismo

Archivos y acciones se ordenan con:

```python
(path.name.casefold(), path.name)
```

Esto mantiene ejemplos, pruebas y revisión estables en lugar de depender del orden de iteración del filesystem.

## Ejecutar el demo

Desde la raíz del repositorio:

```bash
python practical-projects/06-file-organizer/demo.py
```

El demo usa `TemporaryDirectory`, crea solo archivos ficticios, muestra los movimientos planificados, ejecuta el plan y enseña el layout final. No toca directorios personales.

## Ejecutar las pruebas

Suite enfocada:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

Este capítulo evita incrustar un número fijo de escenarios porque la cobertura de regresión crece a medida que se endurecen findings de revisión.

La cobertura incluye:

- clasificación por sufijo;
- validación de rutas;
- descubrimiento determinista;
- escaneo superficial;
- manejo de symlinks;
- invariantes de modelos inmutables;
- colisiones exactas y sin distinción de mayúsculas/minúsculas;
- políticas `ERROR` y `SKIP`;
- orígenes ausentes u obsoletos;
- cambios en rutas de categoría;
- preflight de colisiones;
- destino creado entre preflight y mutación;
- categoría convertida en symlink durante la mutación;
- origen planificado convertido en symlink durante la mutación;
- fallo al eliminar origen sin rollback destructivo del destino;
- ejecución exitosa;
- preservación de archivos de destino no relacionados;
- planes vacíos.

## Rutas de fallo importantes

### Directorio de origen ausente

Genera `FileNotFoundError`.

### Ruta de origen es un archivo regular

Genera `NotADirectoryError`.

### Directorio de origen es symlink

Se rechaza antes del escaneo.

### Ruta de categoría es archivo o symlink

Se rechaza antes de planificar o ejecutar.

### Destino existe durante la planificación

Se maneja según la política de colisión seleccionada.

### Destino aparece después de la planificación

El preflight genera `FileExistsError` antes de cualquier movimiento.

### Destino exacto aparece después del preflight

La operación hard-link no-replace falla con `FileExistsError`; el destino recién creado se conserva y el origen permanece en su lugar.

### La identidad del origen planificado cambia durante la ejecución

La ejecución genera un error en lugar de eliminar la entrada modificada o informar el movimiento como exitoso.

### Falla la eliminación del origen después de crear el destino

La ejecución genera un error y conserva el destino. Evita deliberadamente eliminar un destino cuya identidad actual no puede demostrarse de forma segura durante rollback.

## Errores comunes

### Mover mientras se escanea

Mezclar descubrimiento y mutación hace que los fallos parciales sean difíciles de razonar. Construye primero un plan.

### Usar solo `Path.exists()` antes de `rename()`

La comprobación puede quedar obsoleta inmediatamente, y la semántica POSIX de rename puede reemplazar el destino.

### Tratar el nombre como identidad del objeto

Una entrada de directorio puede ser reemplazada conservando el mismo nombre. Cuando importa la concurrencia, compara identidad del filesystem y tipo de archivo en la frontera de mutación.

### Hacer rollback eliminando ciegamente el destino

El rollback también es una ruta de mutación. Si otro actor puede reemplazar la entrada de destino, una eliminación incondicional puede destruir datos no relacionados.

### Inventar nombres nuevos silenciosamente

Renombrar colisiones a valores como `report_2.txt` oculta una decisión de política.

### Seguir symlinks accidentalmente

Una ruta aparentemente simple puede apuntar fuera del workspace previsto.

### Asumir el orden de iteración del directorio

El orden del filesystem no es un contrato de orden de la aplicación.

### Tratar un preflight exitoso como una transacción

El filesystem puede cambiar después del preflight. La revalidación reduce riesgo, pero no vuelve transaccional una operación de varios archivos.

## Ejercicio

Extiende el organizador con un **renderizador dry-run** sin cambiar el comportamiento de ejecución.

Requisitos:

1. aceptar un `OrganizationPlan`;
2. devolver texto legible y determinista;
3. mostrar movimientos planificados, colisiones omitidas y symlinks ignorados;
4. nunca acceder ni modificar el filesystem;
5. agregar pruebas para planes vacíos y no vacíos.

## Desafíos de extensión

Después del ejercicio, considera:

- mapeo configurable de sufijos a categorías;
- categorías definidas por el usuario;
- exportación/importación JSON del plan con validación cuidadosa de obsolescencia;
- journal de operaciones;
- descubrimiento recursivo con reglas explícitas de ruta relativa;
- detección de duplicados por checksum;
- una primitiva condicional de eliminación de origen aún más fuerte y específica de plataforma;
- una estrategia de rollback para planes parcialmente ejecutados.

Cada extensión añade nuevas invariantes. Define el contrato antes de añadir código.

## Discusión de portfolio

Una explicación más fuerte sería:

> Diseñé un flujo de filesystem con planificación sin mutación, clasificación determinista, políticas explícitas de colisión, fronteras de symlink, validación de identidad durante la ejecución, protección exacta no-replace del destino y manejo conservador de fallos que nunca elimina ciegamente un objetivo de rollback no verificado.

Eso comunica decisiones de ingeniería, no solo uso de API.

## Referencia rápida

| Tarea | Función/tipo |
|---|---|
| Clasificar un nombre de archivo | `classify_path()` |
| Descubrir archivos regulares directos | `discover_files()` |
| Construir una propuesta segura | `plan_organization()` |
| Elegir comportamiento de colisión | `CollisionPolicy` |
| Describir un movimiento | `MoveAction` |
| Mantener el plan inmutable | `OrganizationPlan` |
| Ejecutar el plan | `execute_plan()` |
| Mantener destinos exitosos | `OrganizationResult` |
| Verificar identidad del filesystem | `(st_dev, st_ino)` de `stat` |
| Garantizar mutación exacta no-replace | `os.link()` + `unlink()` del origen verificado |

## Qué viene después

El Proyecto 05 generó archivos. El Proyecto 06 toma la siguiente frontera: descubrir y organizar archivos de forma segura.

El Proyecto 07 vuelve a subir de nivel, combinando registros de dominio validados y estados explícitos de workflow en un **flujo ficticio de conciliación**.
