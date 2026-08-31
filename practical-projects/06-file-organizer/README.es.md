<div align="center">

# Proyecto 06 · Organizador de Archivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

> **Fase 10 · Proyectos Prácticos**

Este proyecto organiza archivos hijos directos en carpetas por categoría, manteniendo descubrimiento, planificación, tratamiento de colisiones y mutación del filesystem de forma explícita y comprobable.

## Objetivos de aprendizaje

Al completar este proyecto, deberías poder:

- descubrir archivos con `pathlib` sin recorrer un árbol de forma recursiva;
- clasificar nombres de archivos de manera determinista mediante reglas de sufijo sin distinguir mayúsculas y minúsculas;
- modelar cambios planificados en el filesystem con dataclasses inmutables;
- separar una fase de planificación sin mutación de una fase de ejecución con efectos secundarios;
- detectar colisiones exactas y colisiones de destino ignorando diferencias de mayúsculas/minúsculas;
- elegir una política de colisión explícita en lugar de sobrescribir datos silenciosamente;
- tratar los symlinks como una frontera específica del filesystem;
- revalidar supuestos inmediatamente antes de la mutación;
- garantizar en el propio paso de mutación que un destino exacto nunca sea reemplazado;
- probar código de filesystem con seguridad usando directorios temporales.

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

El desafío importante no es simplemente llamar una función de movimiento. El proyecto debe hacer visibles las decisiones destructivas antes de modificar cualquier cosa.

## Requisitos

La implementación debe:

1. aceptar un directorio de origen existente que no sea symlink;
2. inspeccionar solo los hijos directos de ese directorio;
3. ignorar directorios anidados;
4. registrar symlinks hijos directos por separado, sin seguirlos;
5. clasificar archivos regulares por el sufijo del nombre;
6. conservar exactamente cada nombre de archivo;
7. crear carpetas de destino solo cuando sean necesarias;
8. producir un orden determinista;
9. construir un plan inmutable antes de la mutación;
10. rechazar rutas de categoría inválidas, incluidos directorios de categoría que sean symlinks;
11. detectar colisiones de destino exactas y sin distinción de mayúsculas/minúsculas;
12. ofrecer políticas explícitas `ERROR` y `SKIP` durante la planificación;
13. ejecutar un preflight completo antes de cualquier movimiento;
14. nunca reemplazar silenciosamente un destino exacto que aparezca después del preflight;
15. devolver un resultado estructurado después de una ejecución exitosa.

## Alcance deliberado

El pipeline es:

```text
directorio de origen
    -> descubrimiento de archivos directos
    -> clasificación por sufijo
    -> plan seguro frente a colisiones
    -> preflight de ejecución
    -> carpetas de categoría necesarias
    -> movimientos no-replace
```

Este proyecto intencionalmente **no** incluye:

- organización recursiva;
- inspección MIME o de contenido;
- renombrado automático de duplicados;
- hashing o deduplicación;
- eliminación;
- transacciones de rollback para todo el plan;
- watchers del filesystem;
- interfaz gráfica;
- almacenamiento en la nube;
- organización entre filesystems diferentes.

Mantener estas responsabilidades fuera del alcance hace visibles las reglas de seguridad en lugar de ocultarlas dentro de un gestor de archivos genérico.

## Categorías

`FileCategory` define cinco destinos:

| Categoría | Carpeta | Sufijos representativos |
|---|---|---|
| Documentos | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Datos | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Imágenes | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Archivos comprimidos | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Otros | `other/` | cualquier valor no cubierto por las reglas anteriores |

La coincidencia ignora diferencias entre mayúsculas y minúsculas. La clasificación usa únicamente el nombre del archivo y no abre su contenido.

## Modelos centrales

### `MoveAction`

Representa un movimiento planificado:

```text
archivo de origen -> destino de categoría
```

Sus invariantes exigen rutas absolutas, el mismo nombre en origen y destino y una carpeta de destino correspondiente a la categoría seleccionada.

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

`discover_files()` devuelve solo archivos regulares hijos directos.

No recorre directorios anidados. Esto importa porque el movimiento recursivo introduce preguntas adicionales:

- ¿debe preservarse la ruta relativa?
- ¿deben revisitarse carpetas de categoría dentro de subdirectorios?
- ¿cómo se gestionan nombres duplicados provenientes de subdirectorios distintos?

Esas preguntas son útiles, pero pertenecen a un proyecto mayor.

## Planificar antes de modificar

`plan_organization()` valida el directorio, inspecciona los archivos, clasifica cada uno y calcula los destinos sin cambiar el filesystem.

Esta separación crea un patrón de ingeniería útil:

```text
observar -> decidir -> validar -> modificar
```

Es más fácil probar y revisar una operación propuesta cuando existe como datos antes de que comiencen los efectos secundarios.

## Políticas de colisión

Hay dos políticas explícitas:

### `CollisionPolicy.ERROR`

La planificación se detiene con `FileExistsError` cuando ya existe un nombre de destino.

Úsala cuando cada archivo de origen necesite un destino libre de conflictos.

### `CollisionPolicy.SKIP`

Los archivos cuyo destino colisiona permanecen en el directorio de origen y se registran en `skipped_collisions`.

Úsala cuando sea aceptable organizar de forma segura solo el subconjunto sin conflictos.

La política se aplica durante la planificación. La ejecución sigue rechazando nuevas colisiones exactas que aparezcan después.

## Colisiones sin distinción de mayúsculas/minúsculas

Un directorio puede ser case-sensitive en un sistema operativo y case-insensitive en otro.

Por eso, el proyecto compara nombres de destino con `casefold()` durante planificación y preflight. Por ejemplo, estos nombres se tratan como una colisión lógica:

```text
Report.TXT
report.txt
```

Esto mantiene el plan más portable entre comportamientos habituales de filesystem.

## Frontera de symlink

El organizador no sigue symlinks hijos directos.

También rechaza:

- un directorio de origen que sea symlink;
- una carpeta de categoría implementada como symlink.

Esto evita mover archivos inesperadamente mediante una ruta que apunta fuera del workspace previsto.

## Por qué el preflight no es suficiente

Una primera implementación podría hacer:

```python
if not destination.exists():
    source.rename(destination)
```

Eso contiene una carrera de time-of-check/time-of-use. Otro proceso puede crear el destino después de la comprobación y antes del rename.

En POSIX, `rename()` puede reemplazar un destino existente. Por eso, un organizador aparentemente seguro podría destruir datos recién creados en el destino.

## Mutación exacta no-replace

La ejecución usa una operación de hard link dentro del mismo filesystem como protección en el momento exacto de la mutación:

```text
1. crear hard link en el destino
2. fallar de forma atómica si ese destino exacto ya existe
3. eliminar la ruta de origen original
```

`os.link()` no reemplaza un destino existente. Como todas las carpetas de destino se encuentran dentro del mismo directorio de origen, origen y destino permanecen intencionalmente en el mismo filesystem para este proyecto.

Si el link no puede crearse, el origen queda intacto. Si la eliminación del origen falla después de crear el link, la implementación intenta eliminar el link de destino antes de propagar el error.

Esto no convierte todo el plan de múltiples archivos en una transacción. Resuelve una garantía más estrecha e importante: un destino exacto nunca es sobrescrito silenciosamente por la primitiva de mutación.

## Flujo de ejecución

`execute_plan()` realiza:

1. validación de tipo;
2. revalidación del directorio de origen;
3. revalidación de rutas de categoría;
4. revalidación de orígenes planificados;
5. preflight de colisiones de destino;
6. creación de solo las carpetas de categoría necesarias;
7. cada movimiento exacto no-replace;
8. construcción de `OrganizationResult`.

Un plan antiguo, por lo tanto, nunca se acepta a ciegas.

## Determinismo

Archivos y acciones se ordenan por una clave basada en:

```python
(path.name.casefold(), path.name)
```

Esto mantiene ejemplos, pruebas y revisiones estables en lugar de depender del orden de iteración del filesystem.

## Ejecutar la demo

Desde la raíz del repositorio:

```bash
python practical-projects/06-file-organizer/demo.py
```

La demo usa `TemporaryDirectory`, crea únicamente archivos ficticios, muestra los movimientos planificados, ejecuta el plan y presenta el layout final. No toca directorios personales.

## Ejecutar las pruebas

Suite enfocada:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

La suite enfocada actual contiene **57 escenarios pytest**.

La cobertura incluye:

- clasificación por sufijo;
- validación de rutas;
- descubrimiento determinista;
- recorrido superficial;
- tratamiento de symlinks;
- invariantes de modelos inmutables;
- colisiones exactas y sin distinción de mayúsculas/minúsculas;
- políticas `ERROR` y `SKIP`;
- orígenes ausentes u obsoletos;
- cambios en rutas de categoría;
- preflight de colisiones;
- un destino creado entre preflight y mutación;
- ejecución exitosa;
- preservación de archivos de destino no relacionados;
- planes vacíos.

## Caminos de fallo importantes

### Directorio de origen ausente

Genera `FileNotFoundError`.

### La ruta de origen es un archivo regular

Genera `NotADirectoryError`.

### El directorio de origen es symlink

Se rechaza antes del escaneo.

### La ruta de categoría es archivo o symlink

Se rechaza antes de la planificación o ejecución.

### El destino existe durante la planificación

Se gestiona según la política de colisión seleccionada.

### El destino aparece después de la planificación

El preflight genera `FileExistsError` antes de cualquier movimiento.

### El destino exacto aparece después del preflight

La operación hard-link no-replace falla con `FileExistsError`; el destino recién creado se conserva y el origen permanece en su lugar.

## Errores comunes

### Mover mientras se escanea

Mezclar descubrimiento y mutación hace que los fallos parciales sean difíciles de razonar.

Es preferible construir primero un plan.

### Usar solo `Path.exists()` antes de `rename()`

La comprobación puede quedar obsoleta inmediatamente y la semántica POSIX de rename puede reemplazar el destino.

### Inventar nombres nuevos silenciosamente

Renombrar colisiones como `report_2.txt` oculta una decisión de política. Este proyecto mantiene ese comportamiento explícito.

### Seguir symlinks sin darse cuenta

Una ruta aparentemente simple puede apuntar fuera del workspace previsto.

### Suponer el orden de iteración del directorio

El orden de iteración del filesystem no es un contrato de orden de la aplicación. Ordena explícitamente cuando el determinismo sea importante.

### Tratar un preflight exitoso como una transacción

El filesystem puede cambiar después del preflight. La revalidación reduce el riesgo, pero no convierte una operación de múltiples archivos en una transacción.

## Ejercicio

Extiende el organizador con un **renderizador de dry run** sin cambiar el comportamiento de ejecución.

Requisitos:

1. aceptar un `OrganizationPlan`;
2. devolver texto determinista y legible;
3. mostrar movimientos planificados, colisiones omitidas y symlinks ignorados;
4. nunca acceder ni modificar el filesystem;
5. añadir pruebas para planes vacíos y no vacíos.

El objetivo es practicar la separación entre presentación, dominio y lógica de mutación.

## Desafíos de extensión

Después del ejercicio, considera:

- un mapeo configurable de sufijos a categorías;
- una alternativa con categorías definidas por el usuario;
- exportación/importación JSON del plan con validación cuidadosa de planes obsoletos;
- un journal de operaciones;
- descubrimiento recursivo con reglas explícitas de rutas relativas;
- detección de duplicados por checksum;
- una estrategia de rollback para planes ejecutados parcialmente.

Cada extensión introduce nuevas invariantes. Define el contrato antes de añadir el código.

## Discusión de portafolio

Una explicación débil sería “escribí un script que mueve archivos”.

Una explicación más fuerte sería:

> Diseñé un flujo de filesystem con una fase de planificación sin mutación, clasificación determinista, políticas explícitas de colisión, fronteras de symlink, revalidación en el momento de ejecución y protección exacta no-replace del destino. El comportamiento está cubierto por pruebas con filesystem temporal, incluida una carrera simulada entre preflight y mutación.

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
| Garantizar mutación exacta no-replace | `os.link()` + `unlink()` del origen |

## Qué viene después

El Proyecto 05 generó archivos. El Proyecto 06 asume la siguiente frontera: descubrir y organizar archivos con seguridad.

El Proyecto 07 vuelve a subir de nivel, combinando registros de dominio validados y estados explícitos en un **flujo ficticio de conciliación**.
