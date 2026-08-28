# Trabajar con Rutas del Sistema de Archivos Usando `pathlib`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

`pathlib` es el módulo de la biblioteca estándar para representar y manipular rutas del sistema de archivos como objetos.

En capítulos anteriores usamos strings como `"notes.txt"` y `"reports/data.csv"` al abrir archivos. Eso funciona, pero las rutas tienen estructura: directorios, nombres, stems, sufijos, padres y separadores dependientes de la plataforma. `pathlib` ofrece una API específica para esa estructura.

Para la mayoría del trabajo cotidiano, comienza con:

```python
from pathlib import Path
```

Después crea objetos `Path` y combínalos en lugar de concatenar strings manualmente.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- explicar qué representa un objeto `Path`;
- crear rutas relativas y absolutas;
- combinar segmentos con `/`;
- inspeccionar nombres, sufijos, padres y partes;
- usar `Path.cwd()` y `Path.home()` de forma deliberada;
- crear directorios con `mkdir()`;
- leer y escribir texto mediante un objeto de ruta;
- comprobar si una ruta apunta actualmente a un archivo o directorio;
- recorrer directorios con `iterdir()`;
- buscar con `glob()` y `rglob()`;
- transformar nombres con `with_name()` y `with_suffix()`;
- entender por qué una comprobación de existencia no garantiza que una operación posterior tendrá éxito;
- distinguir `Path` de las clases de rutas puras a nivel introductorio;
- evitar separadores de ruta fijos cuando importa la portabilidad.

## 1. ¿Qué problema resuelve `pathlib`?

Una ruta es más que texto.

Considera:

```text
reports/2026/summary.txt
```

Esa ruta contiene varias piezas con significado:

- `reports` es un segmento de directorio;
- `2026` es otro segmento;
- `summary.txt` es el nombre final;
- `summary` es el stem;
- `.txt` es el sufijo.

Podrías manipular todo con métodos de strings, pero el código también tendría que comprender separadores y convenciones del sistema operativo.

`pathlib` coloca el comportamiento de las rutas en objetos específicos para rutas.

```python
from pathlib import Path

report_path = Path("reports") / "2026" / "summary.txt"

print(report_path)
print(report_path.name)
print(report_path.stem)
print(report_path.suffix)
print(report_path.parent)
```

El separador mostrado por `print(report_path)` depende del sistema operativo. Ese es precisamente uno de los beneficios: el código expresa la estructura de la ruta sin insertar manualmente `/` o `\\`.

## 2. `Path` suele ser la clase que necesitas

El módulo `pathlib` contiene varias clases.

Para trabajo normal con el sistema de archivos, usa `Path`:

```python
from pathlib import Path

config_path = Path("config") / "settings.json"
```

`Path` es una clase de ruta concreta. Puede manipular la estructura de la ruta y también realizar operaciones del sistema de archivos, como leer un archivo, crear un directorio o consultar qué existe.

También existen clases puras como `PurePath`, `PurePosixPath` y `PureWindowsPath`. Las rutas puras manipulan sintaxis de rutas sin tocar el sistema de archivos.

Normalmente **no** necesitas elegir `PosixPath` o `WindowsPath` directamente. `Path` selecciona la variante concreta apropiada para la plataforma en ejecución.

## 3. Crear rutas

Una ruta puede crearse desde un string:

```python
from pathlib import Path

file_path = Path("notes.txt")
```

También puede crearse con varios segmentos:

```python
from pathlib import Path

file_path = Path("reports", "2026", "summary.txt")
```

O puedes combinar objetos y segmentos con `/`:

```python
from pathlib import Path

reports_dir = Path("reports")
file_path = reports_dir / "2026" / "summary.txt"
```

Aquí `/` no realiza una división. `Path` define ese operador como una forma conveniente de unir segmentos.

Prefiere:

```python
file_path = Path("reports") / "2026" / "summary.txt"
```

en lugar de construir separadores manualmente:

```python
file_path = "reports/" + "2026/" + "summary.txt"
```

La versión con `Path` comunica intención y evita incrustar el separador de una sola plataforma.

## 4. Rutas relativas y absolutas

Una **ruta relativa** se interpreta en relación con algún contexto, normalmente el directorio de trabajo actual del proceso.

```python
from pathlib import Path

relative_path = Path("reports") / "summary.txt"

print(relative_path.is_absolute())
```

Una **ruta absoluta** identifica una ubicación desde la raíz o desde el contexto de unidad del sistema de archivos.

No asumas que una ruta relativa es relativa al archivo `.py`. Normalmente se interpreta desde el directorio de trabajo actual del proceso.

Esa diferencia explica muchos casos de "el archivo existe, pero Python no lo encuentra".

## 5. Directorio de trabajo y directorio home

`Path.cwd()` devuelve el directorio de trabajo actual:

```python
from pathlib import Path

current_dir = Path.cwd()
print(current_dir)
```

`Path.home()` devuelve el directorio home del usuario actual:

```python
from pathlib import Path

home_dir = Path.home()
print(home_dir)
```

Usa estos métodos cuando el programa dependa intencionalmente de esas ubicaciones.

No los utilices solo para hacer que una ruta "parezca absoluta". Primero decide con respecto a qué ubicación debe existir la ruta.

## 6. Inspeccionar la estructura de una ruta

`Path` expone componentes comunes como atributos.

```python
from pathlib import Path

path = Path("archive") / "report.final.csv"

print(path.name)
print(path.stem)
print(path.suffix)
print(path.suffixes)
print(path.parent)
print(path.parts)
```

Significados habituales:

| Atributo | Significado |
|---|---|
| `.name` | componente final de la ruta |
| `.stem` | nombre final sin su último sufijo |
| `.suffix` | último sufijo |
| `.suffixes` | lista de sufijos |
| `.parent` | ruta padre lógica |
| `.parents` | secuencia de ancestros lógicos |
| `.parts` | tupla con los componentes |

El sufijo se basa en la sintaxis de la ruta, no en el contenido real del archivo. Un archivo llamado `table.csv` no necesariamente contiene CSV válido.

## 7. Transformar nombres sin cirugía de strings

Usa métodos de rutas cuando la operación se refiera a la estructura de la ruta.

```python
from pathlib import Path

source = Path("exports") / "report.csv"

print(source.with_suffix(".json"))
print(source.with_name("summary.csv"))
```

`with_suffix()` devuelve una nueva ruta. No renombra un archivo en el disco.

Del mismo modo, `with_name()` devuelve otro objeto de ruta con un nombre final distinto.

La distinción es:

```text
construir o transformar un Path
        !=
modificar el sistema de archivos
```

## 8. Leer y escribir texto

`Path.read_text()` y `Path.write_text()` son atajos convenientes para archivos de texto pequeños.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    notes_dir = workspace / "notes"
    notes_dir.mkdir()

    notes_path = notes_dir / "pathlib.txt"
    notes_path.write_text("Paths are objects.\n", encoding="utf-8")

    print(notes_path.read_text(encoding="utf-8").strip())
```

Indica un encoding explícito cuando el formato o contrato de la aplicación lo requiera.

Para datos portables del proyecto, UTF-8 suele ser una buena elección explícita:

```python
text = path.read_text(encoding="utf-8")
```

y:

```python
path.write_text(text, encoding="utf-8")
```

### Importante: `write_text()` reemplaza el contenido existente

`Path.write_text()` abre el destino para escritura. Si el archivo ya existe, su contenido anterior se reemplaza.

Eso es peligroso cuando el archivo existente debe conservarse.

Usa este método solo cuando el reemplazo sea intencional.

Para añadir contenido o usar modos de apertura especializados, utiliza `open()` o `Path.open()` con el modo adecuado.

## 9. `Path.open()` y el `open()` incorporado

Un objeto `Path` puede pasarse directamente al `open()` incorporado porque implementa el protocolo path-like de Python.

```python
from pathlib import Path

path = Path("notes.txt")

with open(path, "r", encoding="utf-8") as file:
    text = file.read()
```

También puedes usar el método del propio objeto:

```python
with path.open("r", encoding="utf-8") as file:
    text = file.read()
```

Ambas formas son válidas. Intenta mantener un estilo coherente dentro de un mismo proyecto.

## 10. Crear directorios con `mkdir()`

`Path.mkdir()` crea un directorio.

```python
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir()
```

Para crear también padres ausentes:

```python
output_dir = Path("build") / "reports" / "daily"
output_dir.mkdir(parents=True)
```

Cuando un directorio ya existente sea aceptable:

```python
output_dir.mkdir(parents=True, exist_ok=True)
```

Sé preciso con `exist_ok=True`: significa que un directorio ya existente en esa ruta es aceptable. No convierte cualquier problema del sistema de archivos en éxito. Los errores de permisos y objetos incompatibles todavía pueden fallar.

## 11. Consultar el sistema de archivos

Consultas comunes:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    file_path = workspace / "lesson.txt"
    file_path.write_text("pathlib", encoding="utf-8")

    print(file_path.exists())
    print(file_path.is_file())
    print(workspace.is_dir())
```

Métodos centrales:

| Método | Pregunta |
|---|---|
| `.exists()` | ¿esta ruta existe ahora? |
| `.is_file()` | ¿apunta actualmente a un archivo regular? |
| `.is_dir()` | ¿apunta actualmente a un directorio? |
| `.is_symlink()` | ¿es un enlace simbólico? |

Estos métodos informan el resultado de la consulta al sistema de archivos en el momento en que se ejecuta, pero un resultado `False` no siempre demuestra que una entrada esté ausente. En Python 3.14, métodos booleanos de estado como `exists()`, `is_file()` e `is_dir()` devuelven `False` cuando un `OSError` impide la inspección. Con el valor predeterminado `follow_symlinks=True`, `exists()` también devuelve `False` cuando falta el destino de un enlace simbólico. Si necesitas distinguir entre una ruta ausente, inaccesible, inválida u otro fallo al consultar su estado, usa `stat()` y maneja su excepción en lugar de depender únicamente de la consulta booleana.

Por lo tanto, estas comprobaciones son instantáneas útiles de lo que la consulta pudo establecer, no garantías autoritativas sobre el sistema de archivos. La operación que realmente necesitas ejecutar, y cualquier excepción que produzca, sigue siendo la frontera autoritativa.

## 12. Una comprobación no es una garantía

Este código parece prudente:

```python
if path.exists():
    text = path.read_text(encoding="utf-8")
```

Pero el sistema de archivos puede cambiar entre la comprobación y la lectura. Los permisos pueden cambiar. Otro proceso puede eliminar o reemplazar el archivo. Un sistema de archivos de red puede dejar de estar disponible.

Por eso `exists()` es útil cuando importa el **estado actual**, pero no debe tratarse como una promesa de que la siguiente operación no puede fallar.

En la frontera de la operación, maneja la excepción que la propia operación puede producir:

```python
from pathlib import Path

settings_path = Path("settings.json")

try:
    text = settings_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Settings file is missing")
else:
    print(text)
```

Esto conecta directamente con la Fase 7: las APIs del sistema de archivos y el manejo de excepciones están diseñados para trabajar juntos.

## 13. Recorrer un directorio

`iterdir()` produce los hijos directos de un directorio.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)

    for name in ("gamma.txt", "alpha.txt", "beta.txt"):
        (workspace / name).write_text(name, encoding="utf-8")

    for path in sorted(workspace.iterdir()):
        print(path.name)
```

El sistema de archivos no promete un orden útil. Si el orden determinista importa, ordena explícitamente.

Esto es especialmente importante en:

- pruebas;
- informes generados;
- tutoriales;
- automatizaciones reproducibles.

`iterdir()` no es recursivo.

## 14. Buscar con `glob()` y `rglob()`

`glob()` encuentra rutas mediante un patrón relativo a la ruta actual.

```python
from pathlib import Path

for path in Path("src").glob("*.py"):
    print(path)
```

La búsqueda se limita al nivel indicado por el patrón.

`rglob()` busca recursivamente:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source_dir = workspace / "src"
    nested_dir = source_dir / "tools"
    nested_dir.mkdir(parents=True)

    (source_dir / "app.py").write_text("print('app')\n", encoding="utf-8")
    (nested_dir / "helper.py").write_text("VALUE = 1\n", encoding="utf-8")
    (nested_dir / "notes.txt").write_text("notes\n", encoding="utf-8")

    for path in sorted(source_dir.rglob("*.py")):
        print(path.relative_to(workspace))
```

De nuevo, el orden no está garantizado. Usa `sorted()` cuando el orden forme parte del contrato de salida.

Las búsquedas recursivas pueden ser costosas en árboles grandes. Restringe el patrón y la raíz de búsqueda tanto como permita la tarea.

## 15. Hacer una ruta relativa a otra

`relative_to()` expresa una ruta con respecto a un padre conocido:

```python
from pathlib import Path

workspace = Path("/project")
file_path = Path("/project/docs/guide.md")

print(file_path.relative_to(workspace))
```

Conceptualmente, el resultado es:

```text
docs/guide.md
```

`relative_to()` trabaja con una relación entre rutas. No es lo mismo que consultar el directorio de trabajo actual.

Puede generar `ValueError` cuando la relación solicitada no puede formarse según sus reglas.

## 16. Resolver rutas

`resolve()` devuelve una ruta absoluta resolviendo componentes `..` y enlaces simbólicos según la semántica del sistema de archivos.

```python
from pathlib import Path

path = Path("docs") / ".." / "README.md"
resolved = path.resolve()

print(resolved)
```

Como `resolve()` puede involucrar semántica del sistema de archivos, no lo confundas con una simple limpieza de strings.

Úsalo cuando realmente necesites una ruta resuelta, no automáticamente en cada `Path`.

## 17. Rutas puras

Las clases de rutas puras son útiles cuando quieres semántica de rutas sin acceso al sistema de archivos.

Por ejemplo, un programa que se ejecuta en Linux puede analizar sintaxis de rutas de Windows:

```python
from pathlib import PureWindowsPath

windows_path = PureWindowsPath("C:/Users/Ana/Documents/report.txt")

print(windows_path.name)
print(windows_path.parent)
```

`PureWindowsPath` no comprueba si esa ruta existe.

Para código normal que trabaja con el sistema de archivos local, `Path` sigue siendo el punto de partida.

## 18. Pensar en portabilidad

Evita separadores fijos cuando la ruta deba ser portable.

Frágil:

```python
path = "reports\\2026\\summary.txt"
```

Mejor:

```python
from pathlib import Path

path = Path("reports") / "2026" / "summary.txt"
```

Pero "multiplataforma" no significa que toda ruta tenga el mismo significado en cualquier sistema. Unidades, rutas UNC, permisos, sensibilidad a mayúsculas, enlaces simbólicos, nombres reservados y reglas del filesystem pueden variar.

`pathlib` ofrece una abstracción consciente de la plataforma. No elimina al sistema operativo.

## 19. Los objetos `Path` funcionan con muchas APIs de Python

Las APIs modernas de Python suelen aceptar objetos path-like.

```python
from pathlib import Path
import json

path = Path("config.json")

with path.open("r", encoding="utf-8") as file:
    data = json.load(file)
```

Por eso `pathlib` encaja bien con los capítulos anteriores de archivos y módulos.

Normalmente no necesitas convertir cada `Path` a `str`.

Convierte solo cuando una API externa exija específicamente una representación textual.

## 20. Excepciones comunes

Las operaciones del sistema de archivos todavía pueden fallar.

| Excepción | Situación típica |
|---|---|
| `FileNotFoundError` | falta el archivo solicitado o alguna ruta padre |
| `FileExistsError` | la creación requería ausencia, pero ya existe una entrada |
| `PermissionError` | la operación no está permitida |
| `IsADirectoryError` | una operación de archivo recibe un directorio |
| `NotADirectoryError` | un componente esperado como directorio no lo es |
| `OSError` | fallos más amplios del sistema operativo o filesystem |

Captura la excepción más específica que realmente puedas manejar.

No envuelvas cada llamada a `Path` en `except Exception:` solo porque las operaciones del filesystem pueden fallar.

## 21. Cuándo usar `pathlib`

Usa `pathlib` cuando:

- construyas rutas a partir de segmentos;
- necesites nombres, stems, sufijos o relaciones de parentesco;
- leas o escribas archivos;
- crees directorios;
- descubras archivos;
- necesites construcción portable de rutas;
- quieras que la intención de ruta sea explícita en interfaces.

Ejemplo:

```python
from pathlib import Path

def load_template(template_path: Path) -> str:
    return template_path.read_text(encoding="utf-8")
```

Un type hint `Path` puede hacer más claro un contrato que espera específicamente un objeto `Path`.

Según la interfaz, aceptar una entrada path-like más amplia también puede ser adecuado. Es una decisión de diseño de API, no una regla universal.

## 22. Cuándo no forzar `pathlib`

No introduzcas objetos de ruta donde no exista un problema de rutas.

Algunas APIs de bajo nivel o heredadas siguen diseñadas alrededor de `os`, `os.path`, descriptores de archivo o strings.

La Fase 8 cubrirá más adelante `os` y `shutil`. Esos módulos no quedan obsoletos porque exista `pathlib`. Hay superposición, pero también responsabilidades en niveles diferentes.

## 23. Errores comunes

### Error 1: asumir que relativo significa relativo al archivo fuente

```python
Path("data.json")
```

normalmente parte del directorio de trabajo del proceso.

### Error 2: comprobar `exists()` y asumir que la siguiente operación está garantizada

El estado del sistema de archivos puede cambiar.

### Error 3: olvidar que `write_text()` reemplaza contenido

Si debes preservar datos existentes, elige otra estrategia de apertura.

### Error 4: concatenar separadores manualmente

Prefiere composición estructural.

### Error 5: suponer que el sufijo valida el formato

`.json` en el nombre no demuestra JSON válido.

### Error 6: depender del orden de iteración del directorio

Ordena cuando la salida deba ser determinista.

### Error 7: llamar `resolve()` automáticamente en todas partes

Resuelve solo cuando necesites esa semántica.

### Error 8: convertir cada `Path` a `str`

Muchas APIs de Python aceptan objetos path-like directamente.

## 24. Ejemplo práctico

Imagina un pequeño programa que crea un workspace, escribe un informe y descubre archivos de texto generados.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    reports_dir = workspace / "reports"
    reports_dir.mkdir()

    report_path = reports_dir / "summary.txt"
    report_path.write_text("status=ready\n", encoding="utf-8")

    for path in sorted(reports_dir.glob("*.txt")):
        print(path.name, path.read_text(encoding="utf-8").strip())
```

La idea importante no es solo una sintaxis más corta.

El programa usa una sola abstracción de rutas para:

```text
construir
    ↓
crear
    ↓
escribir
    ↓
descubrir
    ↓
leer
```

Eso deja visible la intención del filesystem de principio a fin.

## 25. Ejercicio

Crea un programa usando `TemporaryDirectory` y `Path` que:

1. cree un directorio llamado `study`;
2. cree `notes` y `archive` dentro de él;
3. escriba dos archivos `.txt` dentro de `notes`;
4. liste los hijos directos de `notes` en orden;
5. encuentre todos los `.txt` bajo `study` recursivamente;
6. muestre cada ruta encontrada con respecto a `study`;
7. lea un archivo usando UTF-8;
8. no deje archivos permanentes.

Después responde:

- ¿Qué rutas son relativas?
- ¿Qué operaciones de este ejercicio realmente acceden o modifican el sistema de archivos y cuáles son solo operaciones estructurales de rutas, como componer rutas o usar `relative_to()`?
- ¿Por qué comprobar `.exists()` primero no garantiza que `.read_text()` funcione después?
- ¿Cuándo sería útil `PureWindowsPath` en lugar de `Path`?

## 26. Lista de revisión

Antes de avanzar, asegúrate de poder explicar:

- qué representa un objeto `Path`;
- por qué `/` es útil para componer rutas;
- rutas relativas y absolutas;
- directorio de trabajo frente a ubicación del archivo fuente;
- `.name`, `.stem`, `.suffix`, `.parent` y `.parts`;
- `read_text()` y `write_text()`;
- `mkdir(parents=True, exist_ok=True)`;
- `.exists()`, `.is_file()` y `.is_dir()`;
- por qué las comprobaciones no son garantías;
- `iterdir()`, `glob()` y `rglob()`;
- por qué una salida determinista puede requerir `sorted()`;
- `with_name()` y `with_suffix()`;
- el propósito de `resolve()`;
- la diferencia entre `Path` y rutas puras;
- por qué `pathlib` complementa en vez de sustituir totalmente a `os` y `shutil`.

## Referencia rápida

```python
from pathlib import Path

path = Path("reports") / "summary.txt"

path.name
path.stem
path.suffix
path.parent
path.parts

Path.cwd()
Path.home()

path.exists()
path.is_file()
path.is_dir()

path.read_text(encoding="utf-8")
path.write_text("text\n", encoding="utf-8")

directory.mkdir(parents=True, exist_ok=True)

list(directory.iterdir())
list(directory.glob("*.txt"))
list(directory.rglob("*.txt"))

path.with_name("other.txt")
path.with_suffix(".json")
path.resolve()
```

## Ejemplos ejecutables

- [`examples/path_parts.py`](examples/path_parts.py)
- [`examples/text_workspace.py`](examples/text_workspace.py)
- [`examples/discover_python_files.py`](examples/discover_python_files.py)
- [`examples/inspect_paths.py`](examples/inspect_paths.py)

Los ejemplos son deterministas y usan solo operaciones estructurales de rutas o directorios temporales, por lo que no dejan archivos persistentes.

## Próximo capítulo

Continúa con **[Capítulo 02: `datetime` y Cálculos de Tiempo](../02-datetime/README.es.md)**, donde la biblioteca estándar añade objetos explícitos para fechas, horas, duraciones, parsing, formato y aritmética de fechas.

## Referencias oficiales

- [Python 3.14 `pathlib` - rutas de sistema de archivos orientadas a objetos](https://docs.python.org/3.14/library/pathlib.html)
- [Python 3.14 `os.PathLike` y `os.fspath()`](https://docs.python.org/3.14/library/os.html#os.PathLike)
- [Python 3.14 función incorporada `open()`](https://docs.python.org/3.14/library/functions.html#open)
