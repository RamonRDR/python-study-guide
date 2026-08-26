<div align="center">

# Abrir Archivos de Forma Segura con `open()` y `with`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Errores, Archivos y Módulos](../README.es.md) · [← Anterior: Lanzar Excepciones y Crear Excepciones Personalizadas](../02-raise-and-custom-exceptions/README.es.md)

Los programas suelen necesitar que los datos sigan existiendo después de que el proceso termina. Un archivo de texto puede almacenar notas, configuración, exportaciones, logs o resultados intermedios que una ejecución posterior podrá leer de nuevo.

La función incorporada `open()` de Python crea un **objeto archivo** para una ruta del sistema de archivos o para un descriptor de archivo entero. No envuelve arbitrariamente un objeto similar a archivo que ya exista. La instrucción `with` da al recurso abierto un tiempo de vida claro, de modo que se cierre incluso cuando el bloque termina debido a una excepción.

Este capítulo se centra en **archivos de texto simples y gestión segura de recursos**. El Capítulo 04 utilizará esta base para trabajar con TXT, CSV y JSON como formatos de datos.

**Tiempo estimado de estudio:** 100–130 minutos.

**Requisito de Python:** Python 3.10 o posterior. El comportamiento de archivos enseñado aquí se verificó con la documentación oficial de Python 3.14.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué devuelve `open()` y por qué un objeto archivo es un recurso que debe cerrarse;
- abrir archivos de texto con modos explícitos y una codificación explícita;
- explicar las diferencias prácticas entre `r`, `w`, `a` y `x`;
- leer un archivo pequeño completo, una línea o líneas de forma incremental;
- escribir y añadir texto controlando deliberadamente los caracteres de nueva línea;
- usar `with` para que un archivo se cierre tanto en salidas normales como excepcionales;
- conectar `with` con el papel de limpieza visto anteriormente con `finally`;
- manejar excepciones comunes de archivos en el límite apropiado;
- explicar por qué las rutas relativas dependen del directorio de trabajo actual;
- evitar truncados accidentales, sorpresas de codificación y lecturas completas innecesarias;
- distinguir modo texto de modo binario a nivel introductorio;
- elegir un patrón básico seguro para tareas comunes con archivos.

## 1. Los archivos introducen persistencia

Las variables viven en memoria mientras un proceso de Python está en ejecución. Cuando el proceso termina, las variables locales normales desaparecen.

Un archivo da al programa un lugar donde almacenar datos fuera de ese proceso:

```text
memoria del programa
        ↓ escritura
archivo de texto en almacenamiento
        ↓ lectura posterior
otra ejecución del programa
```

Esa persistencia es útil, pero también introduce nuevas posibilidades de fallo: una ruta puede no existir, el permiso puede ser denegado, el texto puede usar una codificación inesperada o el programa puede abrir un archivo existente en un modo destructivo.

## 2. `open()` devuelve un objeto archivo

Una llamada común en modo texto se parece a esta:

```python
file = open("notes.txt", "r", encoding="utf-8")
```

`open()` no devuelve directamente el texto del archivo. Devuelve un **objeto archivo** que ofrece operaciones como `read()`, iteración, `write()` y `close()`.

El objeto también mantiene estado, como si está abierto y cuál es la posición actual de lectura o escritura.

## 3. El modelo simplificado de `open()`

La función incorporada completa tiene más parámetros, pero un buen modelo para principiantes es:

```python
open(file, mode="r", encoding=None)
```

Para archivos de texto, piensa en tres preguntas antes de abrir nada:

1. **¿Qué ruta?**
2. **¿Qué operación se pretende: leer, reemplazar, añadir o crear solo si no existe?**
3. **¿Qué codificación de texto utiliza el archivo?**

Hacer explícitas esas decisiones es más seguro que tratar `open()` como una operación mágica para "obtener el contenido del archivo".

## 4. Modo `r`: leer un archivo existente

`"r"` significa lectura de texto. También es el modo predeterminado cuando se omite el argumento de modo.

```python
file = open("notes.txt", "r", encoding="utf-8")
```

El destino debe existir. Si no existe, `open()` lanza `FileNotFoundError`.

Ser explícito con `"r"` suele ser útil en código educativo y de aplicación porque la operación pretendida queda visible de inmediato.

## 5. Modo `w`: escribir y reemplazar

`"w"` abre un archivo de texto para escritura.

```python
file = open("notes.txt", "w", encoding="utf-8")
```

Si el archivo no existe, se crea. Si ya existe, su contenido anterior se **trunca** antes de escribir los nuevos datos.

Ese comportamiento destructivo hace que la elección del modo sea una decisión de corrección, no un detalle cosmético.

```text
archivo existente + "w"
        ↓
contenido anterior eliminado
        ↓
las nuevas escrituras son el contenido
```

## 6. Modo `a`: añadir al final

`"a"` abre para añadir. Las nuevas escrituras se colocan al final en lugar de reemplazar el contenido existente.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Files\n")
```

Si el archivo no existe, el modo de adición lo crea.

El modo append es útil cuando el contenido anterior debe mantenerse intacto y cada nueva escritura pertenece al final.

## 7. Modo `x`: crear solo si el archivo es nuevo

`"x"` solicita creación exclusiva.

```python
with open("notes.txt", "x", encoding="utf-8") as file:
    file.write("First version\n")
```

Si la ruta ya existe, Python lanza `FileExistsError` en lugar de reemplazarla.

Usa este modo cuando sobrescribir accidentalmente un archivo existente sería un error.

## 8. Elige el modo según la intención

Una tabla compacta de decisión:

| Intención | Modo típico | Archivo existente |
|---|---|---|
| Leer | `r` | se conserva |
| Reemplazar contenido | `w` | se trunca |
| Añadir al final | `a` | se conserva |
| Crear solo si no existe | `x` | lanza `FileExistsError` |

Existen combinaciones como `r+`, `w+` y `a+` para leer y escribir con el mismo objeto archivo. Son válidas, pero también combinan reglas de posición y de modo que los principiantes rara vez necesitan.

Prefiere el modo más simple que corresponda al trabajo real.

## 9. El modo texto requiere una decisión de codificación

Los archivos de texto almacenan bytes, mientras que las strings de Python contienen texto Unicode. Una **codificación** define cómo se relacionan esas dos representaciones.

```text
str en Python
    ↓ codificar
bytes en el archivo
    ↓ decodificar
str en Python
```

Si se omite `encoding`, `open()` usa un valor predeterminado que depende del entorno de ejecución. Eso puede hacer que el mismo código fuente se comporte de forma diferente en distintos sistemas.

Cuando se sabe que el formato es UTF-8, indícalo explícitamente:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## 10. Por qué `with` es el patrón normal para archivos

Un objeto archivo utiliza un recurso del sistema operativo. Debe cerrarse cuando el programa termina de usarlo.

El patrón manual funciona:

```python
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

Pero hay un problema: si ocurre una excepción entre `open()` y `close()`, la llamada final puede no ejecutarse.

La solución habitual es `with`:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Cuando la ejecución sale del bloque `with`, el protocolo de gestor de contexto del archivo realiza el trabajo de salida necesario y cierra el archivo.

## 11. `with` se conecta directamente con `finally`

El Capítulo 01 introdujo `finally` para la limpieza. Un gestor de contexto empaqueta ese patrón de limpieza detrás de un protocolo reutilizable.

Conceptualmente:

```text
adquirir recurso
      ↓
ejecutar bloque
      ↓
liberar recurso
```

Incluso si el bloque lanza una excepción, el gestor de contexto tiene la oportunidad de realizar su trabajo de salida antes de que la excepción continúe hacia afuera.

Para objetos archivo normales, eso significa cerrar el archivo. `with` **no** significa "ignorar errores de archivo"; significa "gestionar de forma confiable el tiempo de vida del recurso".

## 12. El archivo queda cerrado después del bloque

El nombre asignado por `as file` sigue existiendo después del bloque, pero el objeto archivo subyacente está cerrado:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(file.closed)
```

Salida:

```text
True
```

Intentar realizar I/O normal sobre ese objeto archivo cerrado lanza `ValueError`.

No diseñes código esperando seguir usando el archivo fuera de su bloque `with`. Pasa los datos que necesitas a objetos normales de Python.

## 13. Lee un archivo pequeño con `read()`

`read()` sin un argumento de tamaño lee desde la posición actual hasta el final del archivo.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Esto es simple y apropiado para un archivo que se sabe que es pequeño.

Para un archivo muy grande o de tamaño desconocido, leerlo todo de una vez puede usar memoria innecesaria. En ese caso, procesa el archivo de forma incremental.

## 14. `read(size)` avanza la posición actual

Un tamaño positivo solicita como máximo esa cantidad de caracteres en modo texto:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first = file.read(5)
    second = file.read(5)
```

La segunda llamada continúa donde terminó la primera. Las lecturas de archivo mantienen estado.

Al final del archivo, otro `read()` en modo texto devuelve una string vacía.

Este modelo de posición se vuelve importante siempre que se realizan varias lecturas mediante el mismo objeto archivo.

## 15. Lee una línea con `readline()`

`readline()` lee una línea cada vez:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
```

Cuando una línea termina con una nueva línea en el archivo, ese `\n` normalmente forma parte de la string devuelta.

Al final del archivo, `readline()` devuelve `""`.

Una línea en blanco que contiene solo el salto de línea es `"\n"`, lo que es diferente del final del archivo.

## 16. Itera sobre el archivo para trabajar por líneas

Para el procesamiento habitual línea por línea, itera sobre el objeto archivo:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

Esto evita crear primero una lista con todas las líneas y es el patrón simple preferido para el procesamiento incremental por líneas.

El objeto archivo es un iterable. El bucle consume líneas desde su posición actual.

## 17. Sé deliberado al quitar saltos de línea

Un patrón tentador es:

```python
clean = line.strip()
```

Pero `strip()` elimina espacios en blanco al principio y al final, no solo el salto de línea. Eso puede cambiar datos significativos.

Si el único cambio pretendido es eliminar un carácter de nueva línea final, sé más específico:

```python
clean = line.rstrip("\n")
```

Eliminar o no otros espacios en blanco es una decisión del formato de datos, no una regla universal de archivos.

## 18. `readlines()` crea una lista

`readlines()` devuelve las líneas restantes como una lista:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

Puede ser conveniente cuando el conjunto completo de líneas es pequeño y realmente necesitas operaciones de lista después.

No lo uses automáticamente. Si cada línea puede procesarse de forma independiente, iterar sobre el archivo mantiene el uso de memoria más simple y escalable.

## 19. Escribe texto con `write()`

En modo texto, `write()` espera una string:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Functions\n")
    file.write("Exceptions\n")
```

`write()` **no** añade un salto de línea automáticamente. Si el archivo debe contener saltos de línea, inclúyelos de forma explícita.

El método devuelve la cantidad de caracteres escritos en modo texto:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    count = file.write("Python\n")

print(count)
```

## 20. Convierte valores no string antes de escribir texto

`write()` en modo texto no formatea objetos arbitrarios de Python por ti:

```python
score = 92

with open("score.txt", "w", encoding="utf-8") as file:
    file.write(str(score))
```

Una f-string suele ser más clara cuando se necesitan etiquetas o formato:

```python
with open("score.txt", "w", encoding="utf-8") as file:
    file.write(f"score={score}\n")
```

El Capítulo 04 introducirá formatos estructurados que ofrecen mejores convenciones para almacenar datos más complejos.

## 21. `writelines()` no inventa separadores

`writelines()` escribe strings de un iterable, pero no añade caracteres de nueva línea entre ellas:

```python
lines = ["Functions\n", "Exceptions\n", "Files\n"]

with open("notes.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

Si las strings no contienen ya separadores, el resultado quedará unido.

Para principiantes, llamadas repetidas a `write()` suelen ser más fáciles de inspeccionar hasta que la forma exacta de los datos esté clara.

## 22. Las rutas relativas dependen del directorio de trabajo actual

Una ruta como:

```python
open("data/notes.txt", "r", encoding="utf-8")
```

es **relativa**. Python la resuelve desde el directorio de trabajo actual del proceso, que no tiene por qué ser el mismo directorio que contiene el archivo `.py`.

Eso explica una sorpresa común para principiantes:

```text
mismo código fuente
+ directorio de trabajo diferente
= ruta resuelta diferente
```

Capítulos posteriores introducirán `pathlib`, que ofrece una API de rutas más rica. Por ahora, conoce siempre desde qué directorio se ejecuta tu proceso al usar rutas relativas.

## 23. Las rutas absolutas identifican una ubicación desde una raíz del sistema de archivos

Una ruta absoluta no depende del directorio de trabajo actual de la misma forma. Su sintaxis exacta es específica de la plataforma.

Codificar de forma fija una ruta absoluta de un solo equipo dentro de código reutilizable suele ser un problema de portabilidad.

Prefiere recibir rutas mediante configuración, argumentos o una estrategia de construcción de rutas apropiada para el programa en lugar de incrustar en el código la estructura de la máquina de un desarrollador.

## 24. Excepciones comunes de archivos

Las operaciones de archivo pueden lanzar varios tipos útiles de excepción:

| Excepción | Significado típico |
|---|---|
| `FileNotFoundError` | el archivo o directorio solicitado no existe |
| `FileExistsError` | la creación exclusiva apuntó a una ruta existente |
| `PermissionError` | la operación no está permitida |
| `IsADirectoryError` | una operación de archivo apuntó a un directorio |
| `UnicodeDecodeError` | los bytes no pudieron decodificarse con la codificación de texto elegida |
| `OSError` | fallos más amplios de I/O del sistema operativo |

Estos tipos son señales, no instrucciones para capturarlo todo. Maneja una excepción solo donde el programa tenga una respuesta significativa.

## 25. Coloca `try` alrededor del límite que puedes manejar

Si un archivo opcional ausente tiene un fallback claro, captura ese fallo específico:

```python
try:
    with open("preferences.txt", "r", encoding="utf-8") as file:
        preferences = file.read()
except FileNotFoundError:
    preferences = ""
```

El `with` sigue encargándose del cierre siempre que la apertura tenga éxito.

Un `except OSError:` amplio puede ser apropiado cuando varios fallos del sistema operativo realmente comparten la misma política, pero no debe usarse solo para hacer desaparecer todos los problemas de archivo.

## 26. Si el cuerpo falla, la limpieza ocurre antes de la propagación

Considera:

```python
with open("scores.txt", "r", encoding="utf-8") as file:
    score = int(file.readline())
```

Si la línea contiene texto inválido para un entero, `int()` lanza `ValueError`.

El gestor de contexto del archivo realiza su trabajo de salida mientras se abandona el bloque, y la excepción continúa hacia afuera salvo que algún código circundante la maneje.

Esa es la composición clave:

```text
apertura correcta
    ↓
el cuerpo lanza una excepción
    ↓
el archivo se cierra
    ↓
la excepción se propaga
```

## 27. Separa el acceso al archivo de la interpretación de datos cuando sea útil

Un diseño útil consiste en dejar que una función lea el texto y otra lo interprete:

```python
def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def parse_score(text: str) -> int:
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score
```

Ahora los fallos de archivo y los fallos de validación del contenido son conceptualmente distintos.

Esa separación se vuelve especialmente útil en el Capítulo 04 al interpretar datos estructurados.

## 28. Valida antes de escrituras destructivas cuando sea práctico

Como `"w"` trunca un archivo existente cuando se abre, valida los datos que puedan validarse **antes** de abrir el destino en modo escritura.

Prefiere este orden:

```text
construir o validar datos de salida
        ↓
abrir destino con "w"
        ↓
escribir texto validado
```

en lugar de abrir primero el destino y descubrir después que los datos son inválidos.

Esto no hace que la escritura sea atómica ni protege contra todos los fallos posibles, pero reduce una clase evitable de pérdida accidental de datos.

## 29. El modo texto y el modo binario son interfaces diferentes

El modo texto es el predeterminado y trabaja con `str`.

El modo binario añade `"b"` al modo y trabaja con `bytes`:

```python
with open("image.bin", "rb") as file:
    data = file.read()
```

En modo binario no se usa codificación de texto porque Python no está convirtiendo entre `str` y bytes del archivo.

Este capítulo se concentra en el modo texto. Usa modo binario cuando el formato de datos es fundamentalmente bytes, como muchas imágenes, archivos comprimidos o cargas útiles de protocolos.

## 30. No pases `encoding` en modo binario

Esta combinación es conceptualmente incorrecta:

```python
open("data.bin", "rb", encoding="utf-8")
```

El modo binario expone bytes directamente, por lo que un parámetro de codificación no forma parte de esa interfaz.

Elige un modelo:

```text
modo texto   → str + encoding
modo binario → bytes
```

## 31. Varios gestores de contexto pueden compartir un `with`

Python puede gestionar más de un contexto en una sola instrucción:

```python
with (
    open("input.txt", "r", encoding="utf-8") as source,
    open("output.txt", "w", encoding="utf-8") as destination,
):
    destination.write(source.read())
```

Ambos recursos reciben su tratamiento de salida correspondiente.

Para principiantes, las instrucciones `with` anidadas o con varios elementos son más útiles cuando la operación realmente necesita ambos recursos al mismo tiempo. No abras archivos antes de tiempo ni los mantengas abiertos más de lo necesario.

## 32. Ejemplo práctico: escribir y luego leer

El primer ejemplo ejecutable crea un directorio temporal solo para que la prueba del repositorio ejercite I/O real de archivos sin dejar archivos generados.

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Exceptions\n")
        file.write("Files\n")

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
```

Salida:

```text
Functions
Exceptions
Files
```

Los auxiliares `tempfile` y `os.path` sirven solo para mantener limpio el ejemplo ejecutable. El objetivo de aprendizaje del capítulo son los dos bloques `with open(...)`.

Versión ejecutable: [`examples/write_and_read_text.py`](examples/write_and_read_text.py).

## 33. Ejemplo práctico: añadir sin reemplazar

El segundo ejemplo hace visible la diferencia entre `"w"` y `"a"`:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "history.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Chapter 01\n")

    with open(path, "a", encoding="utf-8") as file:
        file.write("Chapter 02\n")
        file.write("Chapter 03\n")

    with open(path, "r", encoding="utf-8") as file:
        print(file.read(), end="")
```

Salida:

```text
Chapter 01
Chapter 02
Chapter 03
```

Versión ejecutable: [`examples/append_text.py`](examples/append_text.py).

## 34. Ejemplo práctico: manejar un archivo opcional ausente

El tercer ejemplo conecta el acceso a archivos con el modelo de excepciones de los Capítulos 01 y 02:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "optional.txt")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = "default settings"

    print(content)
```

Salida:

```text
default settings
```

El fallback es significativo porque este archivo es explícitamente opcional. Un archivo obligatorio normalmente necesitaría una política diferente.

Versión ejecutable: [`examples/handle_missing_file.py`](examples/handle_missing_file.py).

## 35. Error común: abrir con `w` cuando querías `a`

Esto reemplaza el contenido anterior:

```python
with open("history.txt", "w", encoding="utf-8") as file:
    file.write("new entry\n")
```

Si la intención era conservar el historial anterior y añadir una entrada, usa `"a"`.

Antes de cada `open()` capaz de escribir, pregúntate si el contenido existente debe reemplazarse, conservarse o protegerse contra sobrescritura.

## 36. Error común: olvidar la codificación

Esto depende de la codificación de texto predeterminada del entorno:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

Si el formato del archivo está definido como UTF-8, indícalo:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

La codificación explícita hace visible la intención y evita una fuente importante de sorpresas entre plataformas.

## 37. Error común: cierre manual con una brecha para excepciones

Esto tiene una brecha de limpieza:

```python
file = open("scores.txt", "r", encoding="utf-8")
score = int(file.readline())
file.close()
```

Si `int()` lanza una excepción, `close()` se omite.

Prefiere:

```python
with open("scores.txt", "r", encoding="utf-8") as file:
    score = int(file.readline())
```

Ahora la limpieza del recurso está ligada al tiempo de vida del bloque.

## 38. Error común: tratar todos los problemas de archivo como si fueran iguales

Evita agrupar fallos no relacionados sin motivo:

```python
try:
    with open("settings.txt", "r", encoding="utf-8") as file:
        settings = file.read()
except Exception:
    settings = ""
```

Esto puede ocultar errores de programación y fallos inesperados.

Elige una excepción específica cuando la política de recuperación sea específica. Si varias subclases de `OSError` realmente comparten la misma política, documenta esa decisión más amplia.

## 39. Error común: usar `read()` automáticamente para todo archivo

Leer el archivo completo es conveniente, no universalmente óptimo.

Si la tarea es "procesar cada línea de forma independiente", esto suele ser mejor:

```python
with open("events.txt", "r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

que cargar primero todas las líneas en una string enorme.

Elige la estrategia de lectura a partir del tamaño y del modelo de procesamiento de los datos.

## 40. Las rutas provenientes de usuarios son un límite de entrada

Si un programa acepta una ruta de un usuario, una solicitud de API, un archivo de configuración o un argumento de línea de comandos, esa ruta es una entrada.

Una operación con capacidad de escritura puede modificar o crear datos en la ubicación resuelta.

Las aplicaciones con requisitos de seguridad o protección de datos deben validar o limitar las ubicaciones permitidas según su propia política. La política exacta depende del programa y queda fuera de este capítulo introductorio.

La lección general es simple: **una ruta no es metadato inofensivo cuando el programa va a leer o escribir en ella.**

## 41. Cuándo no usar archivos de texto sin estructura como todo el modelo de datos

El texto simple es excelente para contenido simple, pero inventar manualmente separadores y reglas de parsing se vuelve frágil a medida que los datos ganan estructura.

Por ejemplo:

```text
name|score|date|notes
```

plantea preguntas sobre escape de `|`, campos ausentes, tipos y saltos de línea incrustados.

El Capítulo 04 introduce TXT, CSV y JSON para que la elección del formato corresponda a la forma de los datos en lugar de forzar cada problema a un parsing de texto improvisado.

## 42. Ejercicio

Crea un pequeño programa llamado `study_notes.py` con estos requisitos:

1. Empieza con tres nombres de temas en una lista.
2. Abre `study_notes.txt` con `"w"` y `encoding="utf-8"`.
3. Escribe un tema por línea.
4. Vuelve a abrir el archivo con `"a"` y añade un tema más.
5. Vuelve a abrirlo con `"r"` e itera sobre las líneas.
6. Muestra cada tema sin una línea en blanco adicional.
7. Usa `with` para cada operación de archivo.
8. Explica en un comentario por qué `"w"` es apropiado en la primera apertura y `"a"` en la segunda.

Preguntas extra:

- ¿Qué ocurriría si el primer modo fuera `"x"` y el archivo ya existiera?
- ¿Qué excepción esperarías al intentar leer un archivo ausente?
- ¿Por qué `read()` podría ser una mala elección si el archivo pudiera contener millones de líneas?

## 43. Lista de revisión

Antes de continuar, comprueba que puedes responder sin adivinar:

- ¿Qué devuelve `open()`?
- ¿Por qué `with open(...)` es más seguro que un par manual `open()` / `close()`?
- ¿Qué hace `"w"` con un archivo existente?
- ¿En qué se diferencia `"a"`?
- ¿Cuándo `"x"` lanza `FileExistsError`?
- ¿Por qué UTF-8 suele escribirse explícitamente como `encoding="utf-8"`?
- ¿Qué devuelve `read()` al final del archivo en modo texto?
- ¿Por qué iterar sobre un archivo puede ser preferible a `readlines()`?
- ¿`write()` añade `\n` automáticamente?
- ¿Qué ocurre con el archivo cuando una excepción sale del cuerpo de `with`?
- ¿Desde qué directorio se resuelve una ruta relativa?
- ¿Cuál es la diferencia básica entre modo texto y modo binario?

## 44. Referencia rápida

| Necesidad | Patrón |
|---|---|
| Leer texto UTF-8 | `with open(path, "r", encoding="utf-8") as file:` |
| Reemplazar texto UTF-8 | `with open(path, "w", encoding="utf-8") as file:` |
| Añadir texto UTF-8 | `with open(path, "a", encoding="utf-8") as file:` |
| Crear solo si no existe | `with open(path, "x", encoding="utf-8") as file:` |
| Leer todo el texto restante | `file.read()` |
| Leer una línea | `file.readline()` |
| Procesar líneas incrementalmente | `for line in file:` |
| Escribir texto | `file.write(text)` |
| Quitar solo `\n` final | `line.rstrip("\n")` |
| Archivo o directorio solicitado ausente | `FileNotFoundError` |
| Ruta existente con `x` | `FileExistsError` |
| Categoría general de I/O del SO | `OSError` |
| Lectura binaria | `with open(path, "rb") as file:` |

Patrón inicial recomendado:

```python
with open(path, "r", encoding="utf-8") as file:
    content = file.read()
```

Elige el modo según la intención, especifica una codificación de texto conocida, mantén corto el tiempo de vida del archivo y captura solo fallos para los que el código circundante tenga una política real.

## Qué sigue

El Capítulo 03 establece acceso seguro a archivos de texto y tiempo de vida de recursos. El siguiente capítulo, **TXT, CSV y JSON**, se centrará en cómo se representan los datos dentro de los archivos y qué parser o escritor debe ser responsable de cada límite de formato.

```text
excepciones
    ↓
lanzamiento deliberado
    ↓
tiempo de vida seguro con open() + with
    ↓
formatos TXT / CSV / JSON
    ↓
módulos y paquetes
```

## Referencias oficiales

- Documentación de Python 3.14 para `open()` incorporado: <https://docs.python.org/3.14/library/functions.html#open>
- Tutorial de Python 3.14, Reading and Writing Files: <https://docs.python.org/3.14/tutorial/inputoutput.html#reading-and-writing-files>
- Referencia del lenguaje Python 3.14, instrucción `with`: <https://docs.python.org/3.14/reference/compound_stmts.html#the-with-statement>
- Documentación `io` de Python 3.14, Text Encoding: <https://docs.python.org/3.14/library/io.html#text-encoding>
