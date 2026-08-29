<div align="center">

# Diseñando Operaciones de Sistema Operativo y Archivos con `os` y `shutil`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Standard Library](../README.es.md) · [← Anterior: `decimal`](../08-decimal/README.es.md)

El capítulo anterior de `pathlib` presentó los objetos de ruta como la forma predeterminada de alto nivel para representar y manipular rutas del sistema de archivos. Este capítulo baja un nivel y amplía el alcance.

El módulo `os` expone interfaces del sistema operativo como estado del entorno del proceso, directorio de trabajo actual, exploración de directorios, metadatos de archivos, renombrado, recorrido de árboles, capacidades relacionadas con permisos y operaciones de rutas de nivel más bajo. El módulo `shutil` construye operaciones de archivos y directorios de nivel más alto sobre esas primitivas, incluyendo copia, movimiento, eliminación recursiva, manejo de archivos comprimidos, descubrimiento de ejecutables e inspección del uso de disco.

El objetivo no es reemplazar `pathlib`. Es comprender los contratos que aparecen cuando un programa cruza la frontera del sistema operativo.

**Tiempo estimado de estudio:** 220–300 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar los diferentes roles de `pathlib`, `os`, `os.path` y `shutil`;
- leer y modificar variables de entorno del proceso de forma deliberada;
- explicar por qué el directorio de trabajo actual es estado compartido del proceso;
- usar `os.PathLike` y `os.fspath()` en fronteras de APIs del sistema de archivos;
- distinguir separadores de rutas de separadores de `PATH`;
- crear directorios de forma segura con `mkdir()` y `makedirs()`;
- elegir entre `listdir()` y `scandir()`;
- usar metadatos de `DirEntry` sin asumir que permanecen actualizados indefinidamente;
- inspeccionar metadatos de archivos con `stat()`;
- eliminar archivos y directorios vacíos con la primitiva correcta;
- distinguir `rename()` de `replace()`, orientado a sustitución;
- recorrer árboles de directorios con `walk()` y podar recursión de forma segura;
- entender el riesgo de seguir enlaces simbólicos durante recorridos recursivos;
- reconocer APIs avanzadas de `dir_fd` y detección de capacidades sin asumir soporte universal entre plataformas;
- distinguir `copyfile()`, `copy()` y `copy2()`;
- copiar árboles de directorios con políticas explícitas de mezcla, exclusión y enlaces simbólicos;
- mover archivos y directorios entendiendo el comportamiento en el mismo sistema de archivos y los fallbacks;
- usar `rmtree()` únicamente detrás de una frontera cuidadosamente validada para operaciones destructivas;
- explicar por qué la preservación de metadatos nunca es una garantía total;
- inspeccionar uso de disco y resolver ejecutables mediante `PATH`;
- crear y extraer archivos comprimidos con una política explícita de confianza;
- usar excepciones en lugar de precomprobaciones sujetas a carreras al realizar I/O del sistema de archivos;
- hacer determinista el procesamiento de archivos cuando el orden de enumeración de directorios no está especificado;
- diseñar flujos de administración de archivos seguros y revisables.

## 1. `os` es un puente hacia servicios del sistema operativo

`os` contiene interfaces para varias categorías de comportamiento del sistema operativo. Este capítulo se concentra en las partes más relevantes para código de aplicación portable:

```text
process environment
current working directory
filesystem paths
files and directories
metadata
directory traversal
filesystem capabilities
```

El módulo también expone APIs de gestión de procesos y específicas de plataforma. Son partes reales de `os`, pero están intencionalmente fuera del alcance de este capítulo.

## 2. `shutil` opera a un nivel más alto del sistema de archivos

`shutil` proporciona operaciones sobre archivos y colecciones de archivos:

```text
copy one file
copy a directory tree
move files or trees
remove directory trees
inspect disk usage
find executables
create and unpack archives
```

Un modelo mental útil es:

```text
pathlib  -> model paths and perform convenient path-oriented operations
os       -> operating-system primitives and lower-level filesystem interfaces
shutil   -> high-level file and directory workflows
```

## 3. No trates los tres módulos como competidores

Se superponen porque resuelven problemas vecinos.

Para composición e inspección comunes de rutas, `pathlib.Path` suele ser la interfaz más clara. `os` sigue siendo importante cuando necesitas estado del entorno, descriptores de directorio, rutas en bytes, conjuntos de capacidades o APIs de nivel más bajo. `shutil` sigue siendo útil para copia recursiva, eliminación recursiva, operaciones de archive, uso de disco y descubrimiento de ejecutables.

Python 3.14 también añadió `Path.copy()`, `Path.copy_into()`, `Path.move()` y `Path.move_into()`. Esto aumenta la superposición, pero no vuelve obsoletos a `os` ni `shutil`.

## 4. Muchas APIs del sistema de archivos aceptan objetos path-like

Desde la introducción del protocolo de rutas, muchas funciones de `os` y `shutil` aceptan objetos que implementan `os.PathLike`.

```python
import os
from pathlib import Path


path = Path("reports") / "summary.txt"
print(os.fspath(path))
```

Por lo tanto, los objetos `Path` pueden pasar directamente a muchas APIs de nivel más bajo sin conversión manual a strings.

## 5. `os.fspath()` expone la representación del sistema de archivos

```python
import os
from pathlib import Path


path = Path("data") / "input.csv"
raw_path = os.fspath(path)
print(type(raw_path).__name__)
```

Para un `Path` normal, el resultado es una string.

Usa `os.fspath()` cuando una frontera de API realmente requiera la representación de bajo nivel en `str` o `bytes`. No disperses conversiones por código que ya puede aceptar objetos path-like.

## 6. `os.PathLike` es un protocolo, no un modelo concreto de ruta

Un objeto path-like implementa `__fspath__()` y devuelve `str` o `bytes`.

```python
import os


class ReportPath:
    def __fspath__(self):
        return "reports/output.txt"


print(os.fspath(ReportPath()))
```

En código de aplicación, `pathlib.Path` normalmente es preferible a inventar clases de ruta propias. El protocolo importa principalmente porque explica la interoperabilidad entre APIs del sistema de archivos.

## 7. Las rutas `str` suelen ser el valor predeterminado más portable

Muchas funciones de `os` admiten rutas en `str` y `bytes`. Las rutas en bytes son útiles en situaciones especializadas de bajo nivel, especialmente en Unix, pero introducen complejidad de codificación.

Prefiere strings Unicode y objetos `Path`, salvo que el programa tenga una razón específica para preservar bytes crudos del sistema de archivos.

## 8. `fsencode()` y `fsdecode()` son fronteras explícitas de codificación

```python
import os


encoded = os.fsencode("notes.txt")
decoded = os.fsdecode(encoded)

print(decoded)
```

Estas funciones usan la codificación del sistema de archivos y el manejador de errores configurados por Python.

Son herramientas de frontera, no una recomendación para convertir todas las rutas a bytes.

## 9. `os.name` ofrece información amplia sobre la plataforma

```python
import os


print(os.name)
```

Valores comunes incluyen `"posix"` y `"nt"`.

No construyas grandes ramas por plataforma cuando la detección de capacidades sea más precisa. El sistema operativo exacto puede importar menos que saber si una operación específica admite `dir_fd`, manejo de enlaces simbólicos u otra capacidad.

## 10. El directorio de trabajo actual es estado del proceso

```python
import os


current = os.getcwd()
print(type(current).__name__)
```

Las rutas relativas se interpretan respecto al directorio de trabajo actual del proceso.

Eso significa que una ruta relativa no es autocontenida. Su significado depende del estado ambiental.

## 11. `os.chdir()` modifica ese estado ambiental

```python
import os


original = os.getcwd()
# os.chdir("another-directory")
# work happens relative to the new current directory
# os.chdir(original)
```

Cambiar el directorio de trabajo afecta operaciones posteriores con rutas relativas en el proceso. En código concurrente o reutilizable, un cambio oculto del directorio puede volver difícil razonar sobre el comportamiento.

Prefiere rutas absolutas o bases explícitas cuando sea posible.

## 12. Restaurar el directorio de trabajo no elimina el riesgo de concurrencia

Un patrón de restauración con `try/finally` evita una clase de error:

```python
import os


original = os.getcwd()
try:
    pass
    # os.chdir(target)
finally:
    os.chdir(original)
```

Pero mientras el directorio está cambiado, otro código del mismo proceso aún puede observar ese estado. Restaurarlo al final es útil, pero no es aislamiento.

## 13. `os.environ` modela el entorno del proceso

`os.environ` es un mapping mutable de nombres de variables de entorno a valores string.

```python
import os


mode = os.environ.get("APP_MODE", "development")
print(mode)
```

Las variables de entorno suelen ser fronteras de configuración. Trátalas como entrada externa, no como constantes automáticamente confiables.

## 14. `os.getenv()` es cómodo para lecturas con valor predeterminado

```python
import os


timeout_text = os.getenv("APP_TIMEOUT", "30")
print(timeout_text)
```

El resultado sigue siendo texto. Convierte y valida según el contrato de la aplicación.

```python
import os


timeout = int(os.getenv("APP_TIMEOUT", "30"))
```

Una variable ausente y una variable inválida son condiciones diferentes. Un valor predeterminado solo resuelve la ausencia.

## 15. Modifica `os.environ` en lugar de llamar `putenv()` directamente

```python
import os


KEY = "APP_MODE"
previous_value = os.environ.get(KEY)

try:
    os.environ[KEY] = "test"
    print(os.getenv(KEY))
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value
```

El ejemplo restaura cualquier valor preexistente, por lo que ejecutarlo en un REPL, notebook u otro proceso de larga duración no elimina el estado de entorno del código que lo invocó.

Las asignaciones en `os.environ` actualizan el entorno del proceso mediante el mecanismo apropiado de la plataforma.

Las llamadas directas a `os.putenv()` no actualizan el mapping Python `os.environ`, por lo que modificar el mapping normalmente expresa mejor el contrato.

## 16. Los cambios de entorno no reescriben el proceso padre

Un proceso Python puede modificar su propio entorno y el entorno heredado por procesos hijos creados después. No puede modificar retroactivamente el mapping de entorno del shell o proceso padre que lo inició.

Piensa en la herencia del entorno como configuración descendente de procesos, no como almacenamiento mutable compartido entre procesos independientes.

## 17. Los valores del entorno son strings

```python
import os


KEY = "WORKER_COUNT"
previous_value = os.environ.get(KEY)

try:
    os.environ[KEY] = "4"
    worker_count = int(os.environ[KEY])
    print(worker_count + 1)
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value
```

La misma regla de restauración se aplica cuando un valor de entorno se cambia temporalmente solo para demostrar el parsing.

Usa parsing explícito para enteros, booleanos, listas, rutas, URLs y otras configuraciones estructuradas.

## 18. `os.environ` es un mapping en caché

El mapping se captura cuando se importa `os`, normalmente durante el inicio del intérprete. Los cambios realizados mediante `os.environ` permanecen sincronizados, pero modificaciones del entorno realizadas fuera de ese mapping pueden no aparecer automáticamente.

Esta distinción importa principalmente en escenarios avanzados de embedding o integración nativa.

## 19. `os.reload_environ()` es nuevo en Python 3.14

Python 3.14 añade:

```python
import os


# os.reload_environ()
```

Actualiza `os.environ` y `os.environb` desde el entorno actual del proceso.

La documentación oficial advierte que `os.reload_environ()` **no es thread-safe**. No lo uses casualmente en un proceso donde otros threads puedan leer o modificar el entorno al mismo tiempo.

## 20. `os.sep` y `os.pathsep` resuelven problemas diferentes

```python
import os


print(repr(os.sep))
print(repr(os.pathsep))
```

`os.sep` es el separador de componentes de ruta, como `/` o `\`.

`os.pathsep` separa entradas en variables de entorno que contienen listas de rutas, como `PATH`, normalmente `:` en POSIX y `;` en Windows.

Confundirlos es un bug clásico de portabilidad.

## 21. Prefiere composición consciente de rutas a separadores manuales

Evita:

```python
base = "reports"
filename = "summary.txt"
path = base + "/" + filename
```

Prefiere `Path` o, cuando trabajes con la interfaz procedural de `os.path`, `os.path.join()`:

```python
import os


path = os.path.join("reports", "summary.txt")
print(path)
```

El separador es una preocupación de la plataforma, no una regla de concatenación de strings.

## 22. `os.path` sigue siendo un toolkit útil de bajo nivel

Funciones comunes incluyen:

```text
os.path.join()
os.path.basename()
os.path.dirname()
os.path.splitext()
os.path.abspath()
os.path.realpath()
os.path.exists()
os.path.isfile()
os.path.isdir()
```

Usa `pathlib` cuando el código orientado a objetos de rutas sea más claro. Usa `os.path` al trabajar con APIs existentes basadas en strings, rutas en bytes o código de nivel más bajo donde su estilo procedural sea natural.

## 23. La normalización no es una única operación universal

`abspath()`, `realpath()` y la manipulación lexical de rutas responden preguntas distintas. Los enlaces simbólicos pueden volver semánticamente importante una aparente limpieza de segmentos `..`.

No normalices una ruta solo para que se vea más bonita. Decide si necesitas una ruta lexical, absoluta o resuelta a través de los enlaces del sistema de archivos.

## 24. Crea un directorio con `os.mkdir()`

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "reports")
    os.mkdir(path)
    print(os.path.isdir(path))
```

`mkdir()` crea un nivel de directorio. Padres ausentes provocan error.

## 25. Crea directorios padres ausentes con `os.makedirs()`

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "year", "month", "reports")
    os.makedirs(path)
    print(os.path.isdir(path))
```

`makedirs()` crea recursivamente los directorios intermedios necesarios.

## 26. `exist_ok=True` expresa creación idempotente de directorio

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "output")
    os.makedirs(path, exist_ok=True)
    os.makedirs(path, exist_ok=True)
    print(os.path.isdir(path))
```

Úsalo cuando un directorio ya existente sea una precondición aceptable. No lo uses cuando la existencia previa deba tratarse como conflicto.

## 27. `os.listdir()` devuelve nombres en orden arbitrario

```python
import os


names = os.listdir(".")
print(type(names).__name__)
```

La API no promete resultados ordenados.

Cuando salida, tests, archives, manifests u orden de procesamiento deban ser deterministas, ordena explícitamente:

```python
import os


for name in sorted(os.listdir(".")):
    pass
```

## 28. `os.scandir()` produce entradas de directorio más ricas

```python
import os


with os.scandir(".") as entries:
    for entry in entries:
        if entry.is_file():
            pass
```

`scandir()` produce objetos `os.DirEntry` que pueden exponer tipo de archivo y metadatos eficientemente. El código que necesita esos atributos puede evitar búsquedas repetidas de ruta comparado con `listdir()` seguido de llamadas separadas a `stat()`.

## 29. Usa el iterador de `scandir()` como context manager

```python
import os


with os.scandir(".") as entries:
    first_names = sorted(entry.name for entry in entries)[:3]

print(type(first_names).__name__)
```

El context manager garantiza que los recursos de exploración del directorio se cierren pronto incluso si la iteración termina antes.

## 30. Los metadatos de `DirEntry` pueden almacenarse en caché

Un `DirEntry` puede almacenar en caché información obtenida del sistema operativo.

Eso es bueno para una exploración corta. No es una promesa de que el objeto permanezca como una vista viva para siempre.

Si los metadatos pueden haber cambiado desde la exploración, llama `os.stat(entry.path)` de nuevo en lugar de tratar un `DirEntry` antiguo como verdad actual.

## 31. `os.stat()` devuelve metadatos estructurados del sistema de archivos

```python
import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as temp_file:
    info = os.stat(temp_file.name)
    print(info.st_size)
```

Campos útiles incluyen tamaño del archivo y varios timestamps. Su significado exacto y disponibilidad pueden variar por plataforma y sistema de archivos.

## 32. Prefiere campos de timestamp en nanosegundos cuando importe la precisión entera exacta

`stat_result` expone variantes en nanosegundos como `st_mtime_ns` donde están disponibles.

```python
import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as temp_file:
    info = os.stat(temp_file.name)
    print(isinstance(info.st_mtime_ns, int))
```

Los campos de timestamp en punto flotante son cómodos, pero nanosegundos enteros evitan un paso innecesario de representación binaria en float.

## 33. No interpretes `st_ctime` como tiempo universal de creación

La semántica de timestamps varía entre plataformas. Históricamente, `st_ctime` representa tiempo de cambio de metadatos en Unix e información relacionada con creación en Windows.

Cuando el tiempo de creación o nacimiento sea requisito, consulta campos específicos de la plataforma y la documentación en lugar de asignar un significado universal a `ctime`.

## 34. Elimina un archivo con `os.remove()` o `os.unlink()`

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "temporary.txt"
    path.write_text("temporary", encoding="utf-8")
    os.remove(path)
    print(path.exists())
```

Para rutas normales del sistema de archivos, `os.remove()` y `os.unlink()` son aliases con el mismo comportamiento.

## 35. `os.rmdir()` elimina solo un directorio vacío

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    child = Path(temp_dir) / "empty"
    child.mkdir()
    os.rmdir(child)
    print(child.exists())
```

Esa restricción es útil. La eliminación recursiva es una operación mucho mayor y pertenece a una API más explícita como `shutil.rmtree()`.

## 36. `os.rename()` no tiene el mismo comportamiento de sobrescritura en todas las plataformas

```python
import os


# os.rename(source, destination)
```

Renombrar depende de reglas del sistema operativo, tipo del destino y fronteras del sistema de archivos. El comportamiento ante un destino existente varía entre plataformas.

Si sobrescribir el destino forma parte del contrato, usa una API cuyas semánticas de sustitución expresen esa intención.

## 37. `os.replace()` expresa intención de sustitución

```python
import os


# os.replace(source, destination)
```

Si el destino es un archivo existente y los permisos permiten reemplazarlo, `replace()` está diseñado para sustituirlo sin requerir una etapa separada de eliminación.

La operación puede fallar entre sistemas de archivos diferentes. En POSIX, una sustitución exitosa con semántica de rename debe ser atómica.

## 38. Evita carreras de check-then-act

Este patrón es frágil:

```python
import os


path = "report.txt"
if os.path.exists(path):
    pass
    # open(path)
```

El sistema de archivos puede cambiar entre la comprobación y la operación.

Prefiere ejecutar la operación y manejar la excepción relevante:

```python
try:
    with open("report.txt", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    content = ""
```

Este es un ejemplo de EAFP: es más fácil pedir perdón que permiso.

## 39. `os.access()` no es una comprobación general de autorización previa

`os.access()` tiene usos especializados, incluyendo comprobaciones de permisos con IDs reales en Unix.

No lo uses como una precomprobación universal de "¿puedo abrir este archivo de forma segura?". La documentación oficial advierte que check-then-open crea una ventana de carrera, y sistemas de archivos de red pueden tener semánticas de permisos adicionales al modelo local de bits.

## 40. `os.walk()` recorre un árbol de directorios

```python
import os


for root, dirnames, filenames in os.walk("."):
    print(root, len(dirnames), len(filenames))
    break
```

Cada iteración produce:

```text
(root path, child directory names, child file names)
```

Las listas de hijos contienen nombres, no rutas completas.

## 41. El recorrido top-down permite podar la recursión

Cuando `topdown=True`, modifica `dirnames` in-place para controlar qué directorios serán visitados:

```python
import os


for root, dirnames, filenames in os.walk(".", topdown=True):
    dirnames[:] = [name for name in dirnames if name != "__pycache__"]
```

Asignar una nueva lista local sin modificar `dirnames` no poda el recorrido.

## 42. Ordena nombres de directorios cuando importe el orden del recorrido

```python
import os


for root, dirnames, filenames in os.walk("."):
    dirnames.sort()
    filenames.sort()
```

El orden de enumeración de directorios no es un contrato determinista. Ordena cuando el comportamiento posterior dependa del orden.

## 43. Seguir symlinks de directorios puede crear ciclos

Por defecto, `os.walk()` no sigue enlaces simbólicos que apuntan a directorios.

Con `followlinks=True`, un enlace puede apuntar a un ancestro y crear recursión sin límite. `os.walk()` no mantiene automáticamente un registro completo de todos los directorios visitados.

Seguir enlaces debe ser una decisión deliberada de recorrido de grafo, no una flag de conveniencia.

## 44. `onerror` hace explícita la política de fallo durante el recorrido

```python
import os


def handle_error(error: OSError) -> None:
    print(type(error).__name__)


for _ in os.walk(".", onerror=handle_error):
    break
```

Sin `onerror`, `walk()` ignora errores de exploración. Un callback puede registrar el error y continuar, o volver a lanzarlo para abortar.

## 45. `os.fwalk()` añade un descriptor de archivo de directorio

`fwalk()` produce:

```text
(dirpath, dirnames, filenames, dirfd)
```

El descriptor permite operaciones relativas al directorio visitado sin reconstruir rutas completas.

Es una herramienta avanzada. El descriptor producido solo es válido hasta el siguiente paso de la iteración, salvo que se duplique.

## 46. El soporte de `dir_fd` depende de las capacidades de la plataforma

Varias APIs de `os` pueden operar respecto a un descriptor de directorio abierto.

No asumas que todas las plataformas admiten toda combinación de `dir_fd`. Python expone conjuntos de capacidades como:

```python
import os


print(isinstance(os.supports_dir_fd, set))
print(isinstance(os.supports_follow_symlinks, set))
```

La detección de capacidades es mejor que fingir que todos los sistemas operativos exponen primitivas idénticas del sistema de archivos.

## 47. El comportamiento de enlaces simbólicos necesita una política explícita

Muchas APIs del sistema de archivos aceptan `follow_symlinks` u opciones equivalentes.

La elección cambia si una operación apunta a:

```text
the symbolic link itself
or
the object referenced by the link
```

Esa distinción puede afectar metadatos, fronteras de eliminación, seguridad y portabilidad.

## 48. Usa `shutil.copyfile()` solo para contenido de archivo

```python
import shutil


# shutil.copyfile("source.txt", "destination.txt")
```

`copyfile()` copia los datos a un nombre completo de archivo de destino. No promete preservar metadatos.

Si origen y destino identifican el mismo archivo, se lanza `SameFileError`.

## 49. `shutil.copy()` también copia el modo de permisos

```python
import shutil


# shutil.copy("source.txt", "backup/")
```

`copy()` puede aceptar un directorio de destino. Además de los datos del archivo, copia el modo de permisos.

No intenta la preservación más amplia de metadatos de `copy2()`.

## 50. `shutil.copy2()` intenta preservar más metadatos

```python
import shutil


# shutil.copy2("source.txt", "destination.txt")
```

`copy2()` usa `copystat()` para intentar preservar metadatos como bits de permisos, tiempo de acceso, tiempo de modificación, flags y algunos atributos extendidos donde estén disponibles.

La palabra **intenta** importa.

## 51. Ninguna copia de `shutil` es un clon completo de metadatos

La documentación oficial advierte explícitamente que las funciones de copia de alto nivel no pueden preservar todos los tipos de metadatos en todas las plataformas.

Ejemplos que pueden perderse incluyen propietario, ACLs, resource forks o alternate data streams según el sistema operativo.

Si la replicación exacta de metadatos del sistema de archivos es un requisito, verifica la plataforma objetivo y utiliza herramientas diseñadas para ese contrato.

## 52. `follow_symlinks` cambia la semántica de la copia

Con una fuente que es symlink:

```text
follow_symlinks=True  -> copy the referenced object's contents
follow_symlinks=False -> recreate a symbolic link where supported
```

No elijas la flag después de escribir el código. Primero decide si los enlaces representan topología o indirección en el modelo de datos.

## 53. `copymode()` y `copystat()` separan operaciones de metadatos

```python
import shutil


# shutil.copymode(source, destination)
# shutil.copystat(source, destination)
```

`copymode()` copia bits de permisos.

`copystat()` intenta copiar un conjunto más amplio de metadatos sin copiar contenido, propietario o grupo.

Estos helpers son útiles cuando copiar datos y copiar metadatos son pasos distintos del flujo.

## 54. `shutil.copytree()` copia un árbol de directorios

```python
import shutil


# shutil.copytree(source_dir, destination_dir)
```

Por defecto, `copytree()` crea recursivamente el árbol de destino y usa `copy2()` para archivos individuales.

Una copia recursiva es un flujo, no una sola operación de archivo. Define deliberadamente políticas sobre existencia del destino, symlinks, exclusiones y errores.

## 55. `dirs_exist_ok` controla la mezcla con el destino

```python
import shutil


# shutil.copytree(source, destination, dirs_exist_ok=True)
```

Cuando es `False`, el valor predeterminado, un directorio de destino ya existente es un conflicto.

Cuando es `True`, pueden reutilizarse directorios existentes y archivos correspondientes del destino pueden sobrescribirse.

Esa opción puede convertir una operación de "crear backup" en "mezclar en un árbol existente", así que nombra y documenta la política claramente.

## 56. `ignore_patterns()` crea un filtro de copia reutilizable

```python
import shutil


ignore = shutil.ignore_patterns("*.tmp", "__pycache__")
# shutil.copytree(source, destination, ignore=ignore)
```

Los patrones de exclusión se aplican recursivamente por nombre en cada directorio visitado por `copytree()`.

Trata los datos ignorados como parte del contrato de backup o despliegue. Un patrón que omite silenciosamente archivos necesarios sigue siendo un bug de corrección.

## 57. `copytree()` puede agregar errores de múltiples archivos

Una copia recursiva puede encontrar más de un fallo. `shutil.Error` puede contener múltiples tuplas `(source, destination, exception)` recopiladas durante la operación.

Cuando importe la fiabilidad, no reduzcas un fallo multiarchivo a un mensaje genérico de "copy failed". Conserva suficiente contexto para diagnosticar qué rutas fallaron.

## 58. `shutil.move()` maneja archivos y árboles de directorios

```python
import shutil


# final_path = shutil.move(source, destination)
```

Si el destino es un directorio existente, la fuente normalmente se mueve dentro de él.

El contrato exacto del destino debe estar explícito en el código porque "mover a esta ruta" y "mover dentro de este directorio" son operaciones distintas.

## 59. Mover puede convertirse en copiar-y-eliminar

`shutil.move()` prefiere una operación tipo rename cuando es posible. Cuando no puede usarse, como entre sistemas de archivos, puede hacer fallback a copiar y luego eliminar la fuente.

Eso significa que un move no es universalmente una única operación atómica de metadatos.

Para flujos que requieren sustitución atómica, garantías de mismo sistema de archivos y una API como `os.replace()` pueden ser más apropiadas.

## 60. La eliminación recursiva merece una frontera rígida

```python
import shutil


# shutil.rmtree(target_directory)
```

`rmtree()` elimina un árbol completo de directorios.

Antes de llamarlo en software real, valida el objetivo desde estado confiable. Un typo, valor de configuración vacío, directorio base incorrecto o error de frontera con symlinks puede convertir limpieza en pérdida de datos.

## 61. Prefiere validación positiva del objetivo antes de operaciones destructivas

Un flujo destructivo puede validar que el objetivo resuelto pertenece a un workspace esperado antes de eliminarlo.

```python
from pathlib import Path


workspace = Path("build").resolve()
target = (workspace / "temporary").resolve()

if target.parent != workspace:
    raise ValueError("unexpected cleanup target")
```

Este ejemplo es intencionalmente estricto. Políticas reales con niveles anidados pueden necesitar `Path.is_relative_to()` u otra regla explícita de contención.

La validación reduce errores accidentales de alcance, pero las carreras del sistema de archivos y el comportamiento de symlinks aún requieren diseño cuidadoso en entornos hostiles.

## 62. `rmtree()` tiene resistencia a ataques de symlink dependiente de la plataforma

En plataformas con las APIs necesarias basadas en descriptores de archivo, Python usa por defecto una implementación de `rmtree()` resistente a ataques de symlink.

Puedes inspeccionar:

```python
import shutil


print(isinstance(shutil.rmtree.avoids_symlink_attacks, bool))
```

Una aplicación sensible a seguridad no debe asumir que todas las plataformas soportadas ofrecen la misma protección.

## 63. `onexc` es el callback moderno de errores de `rmtree()`

Python 3.12 añadió `onexc` y deprecó el callback anterior `onerror`.

```python
import shutil


def handle_remove_error(function, path, exception):
    print(type(exception).__name__)


# shutil.rmtree(target, onexc=handle_remove_error)
```

El callback puede inspeccionar operación, ruta y excepción. Las excepciones lanzadas por el callback se propagan.

## 64. `rmtree()` cambió el manejo de archivos ausentes en Python 3.13

Desde Python 3.13, `rmtree()` ignora `FileNotFoundError` para entradas por debajo del objetivo de nivel superior mientras el recorrido está en progreso.

Una ruta raíz solicitada y ausente sigue importando.

Esto hace menos disruptiva la desaparición concurrente de entradas internas sin convertir una raíz ausente en éxito silencioso.

## 65. `shutil.disk_usage()` informa la capacidad del sistema de archivos

```python
import shutil


usage = shutil.disk_usage(".")
print(hasattr(usage, "free"))
```

La named tuple contiene cantidades de bytes totales, usados y libres.

Los valores reales dependen del entorno. No los fijes en tests ni ejemplos de documentación.

## 66. `shutil.which()` resuelve ejecutables mediante una ruta de búsqueda

```python
import shutil


python_path = shutil.which("python")
print(python_path is None or isinstance(python_path, str))
```

Por defecto, `which()` consulta la variable de entorno `PATH` del proceso y usa `os.pathsep` para interpretar la lista de directorios.

El resultado exacto depende del entorno, así que el código de aplicación debe manejar `None`.

## 67. `copyfileobj()` copia entre objetos file-like abiertos

```python
import io
import shutil


source = io.StringIO("alpha\nbeta\n")
destination = io.StringIO()
shutil.copyfileobj(source, destination)
print(destination.getvalue())
```

Esto trabaja al nivel de streams en lugar de recibir nombres de rutas.

Para objetos de archivo reales con buffer, `copyfileobj()` no garantiza que el destino haya sido flushed al regresar. Haz flush o cierra antes de que otro consumidor necesite observar los datos copiados.

## 68. Las funciones de copia de alto nivel pueden usar llamadas rápidas del sistema

Desde Python 3.8, varias operaciones de copia de `shutil` pueden usar internamente syscalls específicas de plataforma para copiar más eficientemente.

La optimización es un detalle de implementación detrás de la misma API pública. No dupliques manualmente un bucle read/write solo suponiendo que será más rápido.

Python 3.14 amplió algunas de estas optimizaciones, incluyendo posibilidades adicionales de copy-on-write o copia del lado del servidor en sistemas compatibles.

## 69. `make_archive()` crea un árbol empaquetado

```python
import shutil


# archive_path = shutil.make_archive("backup", "zip", root_dir="workspace")
```

La ruta devuelta incluye la extensión seleccionada por el formato.

Crear un archive es diferente de clonar el sistema de archivos byte a byte. Metadatos y capacidades del formato varían.

## 70. La extracción de archives es una frontera de confianza

```python
import shutil


# shutil.unpack_archive("backup.zip", "restored")
```

Nunca trates la extracción de un archive no confiable como una copia inocua.

Las entradas del archive pueden intentar influir en rutas de destino, enlaces, permisos u otros comportamientos del sistema de archivos. Los valores predeterminados incorporados de Python 3.14 bloquean los casos de ruta más peligrosos, pero la documentación oficial sigue recomendando inspección y una política explícita de confianza.

## 71. Los filtros de extracción tar son más seguros por defecto en Python 3.14

Para formatos basados en tar, `shutil.unpack_archive()` pasa el filtrado de extracción a la implementación tar subyacente. El filtro `"data"` es el predeterminado desde Python 3.14.

```python
import shutil


# shutil.unpack_archive("backup.tar", "restored", filter="data")
```

La extracción ZIP no acepta ese argumento `filter`.

Un valor predeterminado más seguro reduce riesgo. No vuelve automáticamente seguros todos los archives no confiables para cualquier aplicación.

## 72. Las excepciones del sistema de archivos forman parte del diseño

Excepciones comunes incluyen:

```text
FileNotFoundError
FileExistsError
PermissionError
NotADirectoryError
IsADirectoryError
OSError
shutil.SameFileError
shutil.SpecialFileError
shutil.Error
```

Captura la excepción más estrecha que represente una rama esperada del flujo. Deja visibles los fallos inesperados.

## 73. Un contrato práctico de entorno

```python
import os


KEY = "PYTHON_STUDY_GUIDE_MODE"
MISSING_KEY = "PYTHON_STUDY_GUIDE_MISSING"
previous_value = os.environ.get(KEY)
previous_missing = os.environ.pop(MISSING_KEY, None)

try:
    os.environ[KEY] = "practice"
    print(f"configured: {os.getenv(KEY)}")
    print(f"fallback: {os.getenv(MISSING_KEY, 'default')}")
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value

    if previous_missing is not None:
        os.environ[MISSING_KEY] = previous_missing
```

```text
configured: practice
fallback: default
```

El ejemplo modifica únicamente el entorno de su propio proceso y restaura cualquier valor previo.

## 74. Una exploración determinista de directorio

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "alpha.txt").write_text("alpha\n", encoding="utf-8")
    (workspace / "data").mkdir()
    (workspace / "data" / "values.txt").write_text("1\n2\n", encoding="utf-8")

    with os.scandir(workspace) as entries:
        for entry in sorted(entries, key=lambda item: item.name):
            kind = "dir" if entry.is_dir() else "file"
            print(f"{entry.name}: {kind}")
```

```text
alpha.txt: file
data: dir
```

El detalle importante es el sort explícito. `scandir()` por sí mismo no promete orden de directorio.

## 75. Un `walk` práctico con poda

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "src").mkdir()
    (workspace / "src" / "app.py").write_text("print('ready')\n", encoding="utf-8")
    (workspace / "cache").mkdir()
    (workspace / "cache" / "ignored.bin").write_bytes(b"ignored")

    for root, dirnames, filenames in os.walk(workspace, topdown=True):
        dirnames[:] = sorted(name for name in dirnames if name != "cache")
        filenames.sort()

        relative_root = Path(root).relative_to(workspace)
        label = "." if relative_root == Path(".") else relative_root.as_posix()
        print(f"{label}: {filenames}")
```

```text
.: []
src: ['app.py']
```

El directorio `cache` se elimina de `dirnames` antes de que la recursión llegue a él.

## 76. Un flujo práctico de copia de árbol y movimiento

```python
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "source"
    destination = workspace / "backup"
    archive = workspace / "archive"

    (source / "reports").mkdir(parents=True)
    (source / "reports" / "summary.txt").write_text("ready\n", encoding="utf-8")
    (source / "scratch.tmp").write_text("temporary\n", encoding="utf-8")

    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("*.tmp"))
    archive.mkdir()
    moved_path = Path(shutil.move(destination / "reports" / "summary.txt", archive))

    copied_names = sorted(path.name for path in destination.iterdir())
    print(f"backup entries: {copied_names}")
    print(f"moved file: {moved_path.name}")
    print(f"content: {moved_path.read_text(encoding='utf-8').strip()}")
```

```text
backup entries: ['reports']
moved file: summary.txt
content: ready
```

El archivo temporal ignorado nunca entra al árbol copiado, y la ruta devuelta por el move se trata como dato en lugar de adivinarla.

## 77. Errores comunes

### Error: separadores manuales de ruta

```python
path = "reports/" + "summary.txt"
```

Prefiere `Path` u `os.path.join()`.

### Error: cambiar el directorio de trabajo dentro de un helper reutilizable

Un `os.chdir()` oculto puede cambiar el significado de rutas relativas en código no relacionado.

### Error: tratar strings del entorno como configuración ya validada

```python
import os


workers = os.getenv("WORKERS", "4")
# workers + 1  # TypeError
```

Convierte el texto externo al tipo requerido y valida su rango.

### Error: depender del orden de enumeración de directorios

No debes asumir que `listdir()`, `scandir()` y el recorrido del sistema de archivos devuelven orden alfabético.

### Error: usar `os.access()` antes de `open()` como garantía de seguridad

La ruta puede cambiar entre comprobación y uso. Intenta el I/O y maneja la excepción.

### Error: decir que `copy2()` copia todo

Intenta preservar más metadatos que `copy()`, pero las garantías siguen dependiendo de la plataforma.

### Error: usar `dirs_exist_ok=True` sin notar que hace merge

Esa flag puede sobrescribir archivos en un árbol de destino existente.

### Error: activar `followlinks=True` sin manejar ciclos

Un symlink hacia un ancestro puede producir recorrido ilimitado.

### Error: llamar `rmtree()` con una ruta construida desde entrada externa no comprobada

La eliminación recursiva debe operar sobre un objetivo validado bajo una base confiable.

### Error: extraer archives no confiables directamente en un directorio sensible

La extracción de archives es una frontera de validación de entrada y seguridad del sistema de archivos.

## 78. Tabla de decisión

| Requisito | Prefiere |
|---|---|
| modelar y componer rutas | `pathlib.Path` |
| manipulación procedural de bajo nivel | `os.path` |
| leer entorno del proceso | `os.environ` / `os.getenv()` |
| convertir objeto path-like a `str` o `bytes` | `os.fspath()` |
| crear un directorio | `os.mkdir()` |
| crear directorios padres recursivamente | `os.makedirs()` |
| listar solo nombres | `os.listdir()` |
| explorar nombres más pistas de tipo o metadatos | `os.scandir()` |
| inspeccionar metadatos | `os.stat()` |
| eliminar un archivo | `os.remove()` / `os.unlink()` |
| eliminar un directorio vacío | `os.rmdir()` |
| sustituir destino con semántica de rename | `os.replace()` |
| recorrer un árbol de directorios | `os.walk()` |
| copiar solo contenido de archivo | `shutil.copyfile()` |
| copiar archivo más modo de permisos | `shutil.copy()` |
| intentar preservación más amplia de metadatos | `shutil.copy2()` |
| copiar árbol de directorios | `shutil.copytree()` |
| mover archivo o árbol | `shutil.move()` |
| eliminar recursivamente un árbol | `shutil.rmtree()` con validación estricta del objetivo |
| inspeccionar capacidad | `shutil.disk_usage()` |
| resolver un ejecutable | `shutil.which()` |
| crear archive | `shutil.make_archive()` |
| extraer archive confiable o validado | `shutil.unpack_archive()` |

## 79. Referencia rápida

```text
os.getcwd()
os.chdir(path)

os.environ["KEY"]
os.environ.get("KEY")
os.getenv("KEY", default)
os.reload_environ()                 # Python 3.14+, not thread-safe

os.fspath(path)
os.fsencode(path)
os.fsdecode(path)
os.sep
os.pathsep
os.path.join(...)
os.path.abspath(path)
os.path.realpath(path)

os.mkdir(path)
os.makedirs(path, exist_ok=True)
os.listdir(path)
os.scandir(path)
os.stat(path)
os.remove(path)
os.unlink(path)
os.rmdir(path)
os.rename(src, dst)
os.replace(src, dst)
os.walk(path)
os.fwalk(path)

os.supports_dir_fd
os.supports_follow_symlinks
os.supports_fd

shutil.copyfile(src, dst)
shutil.copy(src, dst)
shutil.copy2(src, dst)
shutil.copymode(src, dst)
shutil.copystat(src, dst)
shutil.copytree(src, dst)
shutil.ignore_patterns(...)
shutil.move(src, dst)
shutil.rmtree(path)
shutil.disk_usage(path)
shutil.which(command)
shutil.copyfileobj(source, destination)
shutil.make_archive(...)
shutil.unpack_archive(...)
```

## 80. Checklist de diseño

Antes de que un flujo de sistema de archivos cruce hacia `os` o `shutil`, pregunta:

- ¿`Path` ya es suficiente para la parte de modelado de rutas?
- ¿La ruta de entrada es confiable, validada o suministrada externamente?
- ¿La operación depende del directorio de trabajo actual?
- ¿Podría hacer explícita la ruta base?
- ¿El texto del entorno se convierte y valida antes de usarlo?
- ¿La salida determinista requiere ordenar entradas de directorio?
- ¿Estoy conservando datos de `DirEntry` más allá de sus supuestos de frescura?
- ¿El sistema de archivos podría cambiar entre una precomprobación y la operación real?
- ¿Debería intentar la operación y manejar una excepción en su lugar?
- ¿El destino puede existir previamente?
- ¿La sobrescritura o sustitución es intencional?
- ¿Origen y destino pueden estar en sistemas de archivos diferentes?
- ¿Cuál es la política de enlaces simbólicos?
- ¿El recorrido puede seguir un ciclo?
- ¿La copia recursiva mezcla con un árbol existente?
- ¿Qué metadatos realmente deben preservarse?
- ¿La eliminación recursiva está restringida a una base validada positivamente?
- ¿El archive es confiable, inspeccionado o extraído en un lugar aislado?
- ¿La plataforma objetivo soporta la capacidad avanzada que quiero usar?
- ¿Está documentado un comportamiento específico de versión de Python?
- ¿Se probaron primero las rutas destructivas con directorios temporales?

## 81. Ejercicio

Construye una herramienta ficticia de backup de workspace con estos requisitos:

1. Lee los directorios base de origen y destino mediante argumentos de función, no mediante `chdir()`.
2. Acepta una variable de entorno opcional `BACKUP_MODE` con un valor predeterminado documentado.
3. Valida que el modo pertenezca a un pequeño conjunto permitido.
4. Recorre recursivamente el árbol de origen.
5. Omite directorios llamados `cache` y `__pycache__` podando `dirnames` en un `os.walk()` top-down.
6. Ordena directorios y archivos antes de producir un manifest.
7. Rechaza copiar si el directorio de origen no existe.
8. Copia el árbol con `shutil.copytree()` y una política explícita que ignore `*.tmp`.
9. Decide si un destino existente es error o merge y documenta la elección.
10. Devuelve un resumen con cantidad de archivos copiados y ruta de destino.
11. No elimines nada recursivamente salvo que se compruebe que el objetivo está dentro de un workspace temporal dedicado.
12. Captura solo excepciones esperadas del sistema de archivos y deja visibles los errores inesperados.

Desafíos de extensión:

- añade un modo dry-run que enumere acciones planificadas sin modificar el sistema de archivos;
- registra tamaños de archivos con `os.stat()`;
- resuelve un compresor externo opcional con `shutil.which()` y maneja `None`;
- crea un ZIP con `shutil.make_archive()`;
- escribe tests usando `tempfile.TemporaryDirectory()` para no tocar archivos reales del usuario;
- documenta cómo deben tratarse los enlaces simbólicos.

## 82. Conexiones con conceptos anteriores de Python

`os` y `shutil` conectan muchos temas anteriores:

- **Archivos y context managers:** las operaciones del sistema de archivos siguen dependiendo del ciclo de vida correcto de recursos.
- **Excepciones:** las subclases de `OSError` son fronteras normales de control para fallos esperados de I/O.
- **`pathlib`:** los objetos de ruta se integran naturalmente con APIs de `os` y `shutil` que aceptan path-like.
- **Strings:** las variables de entorno y muchas fronteras de rutas llegan como texto.
- **Colecciones:** `os.environ` se comporta como mapping, `walk()` produce listas y los recorridos suelen construir manifests.
- **Funciones:** las operaciones seguras de archivos se benefician de helpers pequeños con origen, destino y políticas explícitas.
- **Logging:** los flujos recursivos de copia, movimiento y limpieza son lugares naturales para evidencia operacional estructurada.
- **`datetime`:** los metadatos de archivo contienen timestamps cuya semántica de plataforma debe interpretarse con cuidado.
- **`json` y `csv`:** las utilidades de sistema de archivos suelen descubrir, mover o archivar archivos que luego se analizan bajo contratos separados de formato.
- **`itertools`:** grandes listas de archivos pueden procesarse de forma lazy después del descubrimiento, pero el sistema de archivos puede seguir cambiando durante la iteración.
- **`decimal`:** los timestamps enteros `st_*_ns` muestran de nuevo que la elección de representación forma parte del contrato de datos.

## Referencias

Referencias principales utilizadas en este capítulo:

- [Documentación de Python 3.14: `os` - interfaces diversas del sistema operativo](https://docs.python.org/3.14/library/os.html)
- [Documentación de Python 3.14: `shutil` - operaciones de archivos de alto nivel](https://docs.python.org/3.14/library/shutil.html)
- [Documentación de Python 3.14: `pathlib` - rutas del sistema de archivos orientadas a objetos](https://docs.python.org/3.14/library/pathlib.html)
- [Documentación de Python 3.14: `os.path` - manipulaciones comunes de rutas](https://docs.python.org/3.14/library/os.path.html)
- [Glosario de Python: EAFP](https://docs.python.org/3.14/glossary.html#term-EAFP)

## Fase 8 completada

Este capítulo cierra la **Fase 8: Standard Library**.

La fase comenzó con modelado de rutas orientado a objetos en `pathlib` y avanzó por contratos de fecha y hora, formatos estructurados de datos, logging, colecciones especializadas, iteración lazy, aritmética decimal y finalmente la propia frontera del sistema operativo.

Continúa con la **Fase 9: Bibliotecas Externas**: [`pandas` — Trabajando con Datos Tabulares](../../external-libraries/01-pandas/README.es.md).
