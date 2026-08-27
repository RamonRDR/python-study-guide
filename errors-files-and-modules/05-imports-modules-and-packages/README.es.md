<div align="center">

# Organizar Código con Imports, Módulos y Paquetes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Errores, Archivos y Módulos](../README.es.md) · [← Anterior: Trabajar con TXT, CSV y JSON](../04-txt-csv-and-json/README.es.md)

A medida que los programas crecen, mantener cada función, constante, parser y flujo de trabajo en un único archivo se vuelve más difícil de comprender y mantener. El sistema de importación de Python permite dividir el código en **módulos** y organizar módulos relacionados en **paquetes**.

El objetivo de este capítulo no es memorizar cada detalle del mecanismo de importación de Python. Es construir un modelo mental confiable para programas pequeños y medianos: de dónde vienen los nombres importados, qué código se ejecuta durante un import, cómo los paquetes organizan módulos, por qué importa el contexto de ejecución y qué hábitos mantienen comprensibles las dependencias.

**Tiempo estimado de estudio:** 120–160 minutos.

**Requisito de Python:** Python 3.10 o posterior. El comportamiento de importación enseñado aquí fue verificado con el tutorial, la referencia del lenguaje y la documentación de línea de comandos oficiales de Python 3.14.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué es un módulo de Python en proyectos comunes de código fuente;
- distinguir un objeto módulo de los nombres importados en otro módulo;
- usar `import module`, `from module import name` y `as` de forma deliberada;
- explicar por qué el acceso calificado por módulo suele mejorar la claridad;
- describir qué ocurre con el código de nivel superior cuando se importa un módulo;
- explicar el papel introductorio de `sys.modules` en el caché de imports;
- usar `if __name__ == "__main__":` para separar definiciones importables de la ejecución directa;
- describir el propósito de `sys.path` sin tratarlo como una lista que deba parchearse casualmente;
- distinguir `ModuleNotFoundError` de la familia más amplia de `ImportError`;
- explicar qué es un paquete regular y qué hace `__init__.py`;
- usar nombres punteados de paquetes e imports absolutos básicos;
- reconocer imports relativos y explicar por qué importa el contexto de ejecución;
- usar `python -m` cuando un módulo debe ejecutarse dentro de su contexto de paquete/import;
- distinguir un paquete de importación de una distribución instalable;
- evitar imports con comodín, colisiones accidentales de nombres de módulos, efectos secundarios en el import y diseños simples con imports circulares;
- organizar un pequeño programa Python de varios archivos con dependencias explícitas.

## 1. ¿Por qué dividir el código entre archivos?

Un único archivo es útil mientras el programa es pequeño. A medida que se acumulan responsabilidades, ese archivo puede convertirse en una sala llena donde ideas no relacionadas compiten por atención.

Los módulos crean límites:

```text
manejo de entrada
      ↓
validación
      ↓
cálculo
      ↓
formateo
```

Cada responsabilidad puede vivir en un archivo cuyo nombre comunica su propósito.

Dividir código no es automáticamente mejor. Una función auxiliar de tres líneas no necesita su propio módulo solo porque Python admita módulos. Crea un límite cuando mejore la reutilización, navegación, pruebas, propiedad de una responsabilidad o claridad de las dependencias.

## 2. En código fuente Python común, un archivo `.py` puede ser un módulo

El tutorial de Python presenta un módulo como un archivo que contiene definiciones e instrucciones de Python.

Por ejemplo:

```text
study_tools.py
```

puede contener:

```python
def build_label(topic: str, level: int) -> str:
    return f"{topic} | level {level}"
```

y otro archivo puede importar ese módulo.

Este modelo basado en archivos es el punto de partida adecuado para principiantes. El sistema completo de importación de Python también puede cargar módulos implementados de otras formas, incluidos módulos incorporados y de extensión, por lo que en el modelo completo del lenguaje "módulo" es más amplio que "un archivo `.py`".

## 3. `import module` vincula el nombre del módulo

Supongamos que `grade_tools.py` contiene:

```python
def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"
```

Otro archivo puede importarlo:

```python
import grade_tools

status = grade_tools.classify_score(84)
print(status)
```

El nombre `grade_tools` ahora se refiere al objeto módulo importado dentro del namespace del módulo importador.

## 4. El acceso calificado por módulo hace visible el origen de un nombre

Con:

```python
import grade_tools
```

llamas:

```python
grade_tools.classify_score(84)
```

Ese prefijo adicional aporta información útil. Quien lee puede ver inmediatamente que `classify_score` proviene de otro módulo.

Esta es una razón por la que `import module` suele ser un buen valor predeterminado cuando el nombre del módulo es corto y significativo.

## 5. `from module import name` vincula directamente nombres seleccionados

Python también permite:

```python
from grade_tools import classify_score

status = classify_score(84)
```

Aquí `classify_score` queda vinculado directamente en el namespace del módulo importador. El nombre `grade_tools` no queda vinculado automáticamente por esta instrucción.

El módulo de origen aún debe encontrarse y cargarse. `from ... import ...` cambia qué nombres se vinculan en el importador; no evita el sistema de importación.

## 6. `as` crea un alias local deliberado

Un módulo puede importarse con otro nombre local:

```python
import statistics as stats

mean_score = stats.mean([80, 90, 100])
```

Un nombre seleccionado también puede recibir un alias:

```python
from math import sqrt as square_root

print(square_root(81))
```

Usa aliases cuando sean convencionales o realmente mejoren la legibilidad. Evita aliases crípticos que hagan el código más difícil de buscar y comprender.

## 7. Elige el estilo de import por legibilidad, no por escribir menos

Compara:

```python
import decimal

value = decimal.Decimal("0.1")
```

con:

```python
from decimal import Decimal

value = Decimal("0.1")
```

Ambos pueden ser apropiados.

Preguntas útiles:

- ¿El nombre del módulo aporta contexto importante?
- ¿Se usarán varios nombres del mismo módulo?
- ¿Un nombre importado directamente podría colisionar con otro nombre local?
- ¿La forma más corta ya es una convención fuerte en ese ecosistema?

La línea más corta no siempre representa la dependencia más clara.

## 8. Los imports son instrucciones ejecutables

Un import no es una operación de copiar texto. Python localiza y carga un módulo, crea u obtiene un objeto módulo y ejecuta el código de nivel superior cuando se requiere inicialización.

Considera un módulo que contiene:

```python
print("Loading helpers")


def build_message() -> str:
    return "Ready"
```

Importar ese módulo puede imprimir `Loading helpers` durante la inicialización.

Por eso el trabajo ejecutable en el nivel superior debe ser intencional.

## 9. Las definiciones del módulo se crean ejecutando su código

Una definición de función también es una instrucción. Cuando se inicializa un módulo, Python ejecuta instrucciones que vinculan nombres como funciones, clases y constantes en el namespace de ese módulo.

Un flujo simplificado útil es:

```text
localizar módulo
    ↓
crear/obtener objeto módulo
    ↓
ejecutar código de inicialización si hace falta
    ↓
el namespace del módulo contiene sus definiciones
```

Este modelo mental explica por qué errores de sintaxis, dependencias ausentes y excepciones de nivel superior pueden hacer fallar un import.

## 10. Los imports normales reutilizan módulos mediante `sys.modules`

Durante una sesión normal del intérprete, los módulos importados se almacenan en caché en `sys.modules`.

Eso significa que instrucciones repetidas como:

```python
import math
import math
```

normalmente no vuelven a ejecutar desde cero la inicialización del módulo cada vez.

Este es un modelo introductorio útil, no una regla que diga que el código de un módulo nunca puede volver a ejecutarse. Operaciones avanzadas como recarga explícita o cambios manuales del estado de importación pueden alterar ese comportamiento.

## 11. Evita usar efectos secundarios de import como flujo oculto de la aplicación

Esto es frágil:

```python
# settings.py
print("Connecting to something...")
```

porque cualquier código que importe `settings` ahora dispara ese trabajo.

Prefiere definiciones en el nivel del módulo y ejecución explícita mediante funciones:

```python
def initialize_settings() -> None:
    print("Settings initialized")
```

Así el llamador decide cuándo esa acción pertenece al flujo del programa.

Algunos módulos realizan legítimamente una pequeña inicialización durante el import. La advertencia de diseño se refiere a trabajo sorprendente, costoso, irreversible o dependiente del orden.

## 12. Todo módulo tiene un `__name__`

Un módulo puede inspeccionar su propio valor global `__name__`.

Cuando un módulo se importa normalmente, `__name__` refleja su nombre de importación.

Por ejemplo, dentro de `grade_tools.py` importado como `grade_tools`, el valor normalmente es:

```text
grade_tools
```

Cuando el código se ejecuta como programa de nivel superior, Python da a ese entorno de ejecución el nombre:

```text
__main__
```

## 13. El main guard separa definiciones de la ejecución directa

Un patrón común es:

```python
def main() -> None:
    print("Program started")


if __name__ == "__main__":
    main()
```

Si el archivo se ejecuta como programa principal, `main()` se ejecuta.

Si el archivo se importa, la función se define, pero la llamada protegida no se ejecuta.

## 14. Coloca el trabajo reutilizable en funciones antes del main guard

Prefiere:

```python
def build_report() -> str:
    return "Study report"


def main() -> None:
    print(build_report())


if __name__ == "__main__":
    main()
```

a colocar toda la aplicación directamente dentro del guard.

Las funciones siguen siendo reutilizables y fáciles de probar, mientras el guard responde solo una pregunta: ¿debe comenzar ahora el comportamiento de entrada directa?

## 15. `__name__ == "__main__"` no bloquea el import

El guard no impide que el archivo sea importado.

Solo evita que el bloque protegido se ejecute cuando el módulo se importa con otro nombre.

Las definiciones anteriores al guard todavía se ejecutan como instrucciones del módulo y quedan disponibles en su namespace.

## 16. Python necesita ubicaciones de búsqueda para encontrar módulos

Cuando escribes:

```python
import study_tools
```

Python debe determinar a qué se refiere `study_tools`.

El sistema completo de importación admite varios tipos de finders y loaders. A nivel introductorio, la idea importante es que Python busca ubicaciones de importación según su mecanismo de import y el entorno de ejecución.

Esas ubicaciones de búsqueda se reflejan en `sys.path` para imports comunes basados en rutas.

## 17. `sys.path` es una lista de ubicaciones de búsqueda de módulos

Puedes inspeccionarla:

```python
import sys

for location in sys.path:
    print(location)
```

Su contenido exacto depende de cómo se inició Python, del entorno, de la configuración de la instalación y de otros ajustes.

No memorices un orden universal de `sys.path` a partir de una captura de pantalla. Aprende el concepto: indica al mecanismo de importación basado en rutas dónde pueden encontrarse módulos y paquetes.

## 18. No trates `sys.path.append(...)` como la solución normal para la estructura del proyecto

Esto puede parecer una solución rápida a un import:

```python
import sys

sys.path.append("../somewhere")
```

pero hace que los imports dependan de una cirugía de rutas en runtime y a menudo oculta una estructura de proyecto o un comando de ejecución poco claros.

Prefiere una estructura coherente de paquetes, un entorno de trabajo/instalación adecuado y una forma de ejecución que proporcione a Python el contexto de import esperado.

Existen casos avanzados para personalizar rutas de importación, pero modificar `sys.path` casualmente no debería ser la primera herramienta de diseño.

## 19. Los nombres de módulos pueden colisionar con otros módulos

Imagina crear un archivo de estudio llamado:

```text
json.py
```

y luego escribir:

```python
import json
```

Según el contexto de búsqueda, tu archivo local puede ocultar el módulo de la biblioteca estándar que querías importar.

Evita poner a tus archivos nombres de módulos de la biblioteca estándar o de dependencias importantes utilizadas por el mismo proyecto.

## 20. `ModuleNotFoundError` normalmente significa que el módulo solicitado no se encontró

Por ejemplo:

```python
import module_that_does_not_exist
```

normalmente lanza `ModuleNotFoundError`.

`ModuleNotFoundError` es una subclase de `ImportError`.

El mensaje y el nombre exacto que falló importan porque un import puede encontrar tu primer módulo y aun así fallar al importar una dependencia de ese módulo.

## 21. `ImportError` es la excepción más amplia relacionada con imports

Un módulo puede existir mientras un nombre solicitado no existe:

```python
from math import name_that_does_not_exist
```

Esto lanza `ImportError` porque `math` está disponible, pero el nombre importado solicitado no lo está.

No captures `ImportError` alrededor de un bloque grande solo para hacer desaparecer los fallos. Captura excepciones de importación únicamente cuando el programa tenga una política deliberada, como una dependencia realmente opcional con un fallback documentado.

## 22. Un paquete organiza módulos bajo un namespace punteado

Los paquetes permiten que módulos relacionados usen nombres jerárquicos como:

```text
study_tools.formatting
study_tools.validation
study_tools.reports
```

Un paquete puede contener módulos y subpaquetes.

En el modelo completo de importación de Python, un paquete es un tipo especial de módulo que puede contener submódulos. La analogía con directorios es útil para proyectos comunes de código fuente, pero el modelo del lenguaje se basa en objetos módulo/paquete, no solo en carpetas.

## 23. Un paquete regular suele usar `__init__.py`

Un paquete regular simple puede verse así:

```text
study_tools/
├── __init__.py
├── formatting.py
└── validation.py
```

La presencia de `__init__.py` hace que este directorio sea un paquete regular en el diseño convencional basado en sistema de archivos.

`__init__.py` puede estar vacío. También puede definir comportamiento de inicialización o exponer deliberadamente nombres seleccionados a nivel del paquete.

## 24. Los namespace packages son una excepción avanzada a la regla de `__init__.py`

Python moderno también admite **namespace packages**, que pueden existir sin `__init__.py` y abarcar varias ubicaciones.

Por eso esta afirmación es demasiado amplia:

```text
"Todo paquete Python debe tener __init__.py."
```

Para proyectos de principiantes, los paquetes regulares con `__init__.py` suelen ser el punto de partida más claro. Los namespace packages pueden esperar hasta que un proyecto realmente necesite ese modelo.

## 25. `__init__.py` es código, así que mantén deliberado su comportamiento

Esto es válido:

```python
from .formatting import build_label

__all__ = ["build_label"]
```

Ahora el paquete puede proporcionar intencionalmente un nombre público conveniente:

```python
from study_tools import build_label
```

Pero un `__init__.py` grande, lleno de configuración costosa e imports sorprendentes, puede volver más difícil de entender el comportamiento del paquete.

Trata la inicialización del paquete como parte de tu diseño de dependencias.

## 26. Los nombres punteados expresan la jerarquía del paquete

Este import:

```python
import study_tools.formatting
```

carga el submódulo usando su nombre punteado completo.

Luego accedes mediante:

```python
study_tools.formatting.build_label("Modules", 2)
```

Otro estilo es:

```python
from study_tools import formatting

print(formatting.build_label("Modules", 2))
```

Ambos dejan explícita la relación con el paquete.

## 27. Importa la interfaz estable más estrecha que mantenga clara la intención

Supongamos que un paquete expone intencionalmente `build_label` desde `__init__.py`:

```python
from study_tools import build_label
```

Eso puede ser una API de paquete limpia.

Si el paquete no promete ese atajo público, importar el módulo que define el nombre puede ser más honesto:

```python
from study_tools.formatting import build_label
```

La mejor elección depende de la interfaz documentada por el paquete, no de cuántos caracteres ahorra el import.

## 28. Un paquete de importación no es lo mismo que una distribución

La palabra **paquete** está sobrecargada en conversaciones sobre Python.

Un **paquete de importación** forma parte del namespace de módulos de Python, por ejemplo:

```text
study_tools
```

Una **distribución** es algo instalado y gestionado por herramientas de empaquetado y puede proporcionar uno o más paquetes de importación o módulos.

El nombre de instalación y el nombre de importación incluso pueden ser diferentes.

Este capítulo enseña paquetes de importación. Empaquetar y publicar distribuciones son temas separados.

## 29. Los imports absolutos nombran explícitamente la ruta del paquete

Dentro de un paquete del proyecto, un import absoluto puede verse así:

```python
from study_tools.formatting import build_label
```

Nombra el paquete desde el namespace de importación de nivel superior.

Los imports absolutos suelen ser fáciles de buscar y comprender porque la ruta de la dependencia queda explícita.

## 30. Los imports relativos usan puntos iniciales dentro de paquetes

Un módulo dentro de `study_tools` puede importar un módulo hermano con:

```python
from .formatting import build_label
```

Un punto inicial se refiere al paquete actual. Puntos adicionales pueden referirse a niveles de paquetes padres.

Los imports relativos son útiles para relaciones internas de un paquete, pero dependen de que Python conozca el contexto de paquete del módulo.

## 31. Los imports relativos no se basan en el directorio de trabajo actual

Esta distinción es importante.

Un import relativo como:

```python
from .formatting import build_label
```

se resuelve a partir de la información de paquete del módulo actual, no caminando desde cualquier directorio en el que esté el terminal.

Por eso "estoy en la carpeta correcta" no es una explicación completa de si un import relativo funcionará.

## 32. Ejecutar directamente un módulo de paquete puede eliminar el contexto de paquete que espera

Supongamos que un módulo contiene un import relativo y está pensado para vivir dentro de un paquete.

Ejecutarlo por la ruta del archivo:

```text
python study_tools/cli.py
```

puede ejecutarlo como el módulo de nivel superior `__main__` en lugar de como `study_tools.cli`. Entonces un import relativo puede fallar porque no se conoce el paquete padre esperado.

Cuando el módulo está diseñado para ejecutarse en contexto de paquete, `python -m` suele ser la herramienta correcta.

## 33. `python -m` localiza un módulo mediante el sistema de importación y lo ejecuta

Por ejemplo:

```text
python -m study_tools.cli
```

Python localiza `study_tools.cli` mediante el mecanismo de importación estándar y ejecuta su contenido como el módulo `__main__`.

Esto preserva el hecho de que el código pertenece al paquete `study_tools` mientras lo convierte en el punto de entrada del programa.

El comando usa un **nombre de módulo**, no un nombre de archivo `.py`.

## 34. Un paquete puede definir `__main__.py` para `python -m package_name`

Si un paquete contiene:

```text
study_tools/
├── __init__.py
├── __main__.py
└── formatting.py
```

entonces:

```text
python -m study_tools
```

ejecuta `study_tools.__main__` como el módulo principal.

Esto resulta útil cuando el propio paquete tiene un comportamiento de entrada por línea de comandos. Un paquete no adquiere ese comportamiento solo porque exista `__init__.py`.

## 35. Los imports hacen visibles las dependencias

Si `reports.py` importa `formatting.py`, entonces `reports` depende de `formatting`.

Un esquema útil de dependencias es:

```text
cli
 ↓
reports
 ↓
formatting
```

Mantener comprensible la dirección de las dependencias ayuda a evitar módulos enredados donde todo importa todo lo demás.

## 36. Los imports circulares suelen ser una señal de diseño

Una relación circular simple se ve así:

```text
module_a importa module_b
        ↑         ↓
        └─────────┘
```

Python puede encontrar un módulo mientras todavía está solo parcialmente inicializado, produciendo errores de nombres ausentes o comportamientos confusos.

Soluciones comunes de diseño incluyen:

- mover definiciones compartidas a un tercer módulo;
- pasar valores o callables como parámetros en vez de volver a importar hacia arriba;
- aclarar qué módulo es propietario de una responsabilidad;
- reducir trabajo de nivel superior que dependa de que el otro módulo esté completamente inicializado.

Mover un import dentro de una función a veces puede romper un ciclo, pero también puede limitarse a ocultar el problema arquitectónico. Comprende la dependencia antes de aplicar esa solución.

## 37. Los imports dentro de funciones están permitidos, pero los imports de nivel superior son el valor predeterminado legible habitual

Esto es Python válido:

```python
def calculate_root(value: float) -> float:
    import math

    return math.sqrt(value)
```

La mayoría de las dependencias comunes se ven con mayor facilidad cuando los imports aparecen cerca de la parte superior del módulo.

Los imports locales pueden ser deliberados para dependencias opcionales, carga retrasada o ciclos bien comprendidos. Úsalos por una razón, no por reflejo.

## 38. Evita imports con comodín en módulos comunes

Esta sintaxis existe:

```python
from math import *
```

pero hace menos explícito el namespace local. Quien lee debe saber qué nombres exporta el origen, y nuevos nombres exportados pueden crear colisiones.

Prefiere imports explícitos:

```python
from math import pi, sqrt
```

`__all__` puede influir en lo que expone un import con comodín, pero no convierte los wildcard imports en el valor predeterminado más claro para código de aplicación.

## 39. Agrupa imports para mejorar la legibilidad

Una organización común y legible es:

```python
import csv
import json

from study_tools import build_label
```

La convención de PEP 8 separa imports de la biblioteca estándar, de terceros y locales de la aplicación cuando existen esos grupos.

El objetivo más profundo es la visibilidad: quien lee debería poder comprender las principales dependencias de un módulo sin buscar entre código no relacionado.

## 40. Ejemplo práctico: importar la biblioteca estándar

```python
import math


number = 81
root = math.sqrt(number)

print(f"Square root: {root}")
```

Salida:

```text
Square root: 9.0
```

Versión ejecutable: [`examples/import_standard_library.py`](examples/import_standard_library.py).

## 41. Ejemplo práctico: importar tu propio módulo

Módulo auxiliar `grade_tools.py`:

```python
def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"
```

Módulo ejecutable `module_demo.py`:

```python
import grade_tools


score = 84
status = grade_tools.classify_score(score)

print(f"Score {score}: {status}")
```

Salida:

```text
Score 84: ready
```

Versión ejecutable: [`examples/module_demo.py`](examples/module_demo.py). Módulo de apoyo: [`examples/grade_tools.py`](examples/grade_tools.py).

## 42. Ejemplo práctico: importar desde un paquete regular

Estructura del paquete:

```text
examples/
├── package_demo.py
└── study_tools/
    ├── __init__.py
    └── formatting.py
```

`formatting.py` define la función reutilizable:

```python
def build_label(topic: str, level: int) -> str:
    return f"{topic} | level {level}"
```

`__init__.py` la expone intencionalmente a nivel del paquete:

```python
from .formatting import build_label

__all__ = ["build_label"]
```

El archivo ejecutable importa la API del paquete:

```python
from study_tools import build_label


print(build_label("Modules", 2))
```

Salida:

```text
Modules | level 2
```

Versión ejecutable: [`examples/package_demo.py`](examples/package_demo.py). Paquete de apoyo: [`examples/study_tools/`](examples/study_tools/).

## 43. Ejemplo práctico: main guard

```python
def main() -> None:
    print("Main guard executed")


if __name__ == "__main__":
    main()
```

Salida cuando se ejecuta directamente:

```text
Main guard executed
```

Versión ejecutable: [`examples/main_guard.py`](examples/main_guard.py).

## 44. Error común: nombrar un archivo igual que una dependencia

Archivos como estos pueden crear sombreados confusos:

```text
json.py
csv.py
math.py
random.py
```

si el mismo proyecto también espera los módulos de la biblioteca estándar con esos nombres.

Elige nombres de módulos que representen tu propia responsabilidad y no colisionen con dependencias que importas.

## 45. Error común: ocultar el inicio de la aplicación dentro de un import

Evita convertir esto en la arquitectura de la aplicación:

```text
import app
    ↓
app lee archivos, conecta servicios e inicia bucles inmediatamente
```

Prefiere un punto de entrada explícito:

```text
importar definiciones
    ↓
main() inicia deliberadamente el comportamiento de la aplicación
```

Un inicio explícito es más fácil de probar, reutilizar y comprender.

## 46. Error común: asumir que ejecutar un archivo y ejecutar un módulo son idénticos

Estos comandos pueden crear contextos de import distintos:

```text
python path/to/tool.py
python -m package.tool
```

Ambos ejecutan código Python, pero `-m` localiza un módulo nombrado mediante el sistema de importación y lo ejecuta como `__main__`.

La diferencia importa especialmente para paquetes e imports relativos.

## 47. Error común: usar paquetes solo para crear árboles profundos de carpetas

Esto no es automáticamente un buen diseño:

```text
app/core/services/helpers/utils/common/
```

Una jerarquía de paquetes debería comunicar namespaces y responsabilidades significativas.

Más niveles añaden más rutas de importación, navegación y límites que comprender. Crea niveles que justifiquen su complejidad.

## 48. Un proyecto pequeño puede crecer por etapas

Comienza simple:

```text
app.py
```

Después extrae una responsabilidad realmente reutilizable:

```text
app.py
grade_tools.py
```

Luego agrupa módulos relacionados cuando el namespace sea útil:

```text
app.py
study_tools/
├── __init__.py
├── grades.py
└── formatting.py
```

La estructura debe seguir las responsabilidades, no el deseo de parecer "enterprise" antes de que el programa lo necesite.

## 49. Ejercicio

Crea una pequeña aplicación de estudio basada en paquetes con esta estructura:

```text
study_app/
├── __init__.py
├── grading.py
└── formatting.py
run_study_app.py
```

Requisitos:

1. En `grading.py`, crea `classify_score(score: int) -> str`, que devuelva `"ready"` para puntuaciones de al menos 80 y `"review"` en caso contrario.
2. En `formatting.py`, crea `format_result(topic: str, status: str) -> str`.
3. En `study_app/__init__.py`, mantén mínima la inicialización. Puedes dejarlo vacío o exponer deliberadamente un nombre documentado a nivel del paquete.
4. En `run_study_app.py`, importa explícitamente la funcionalidad del paquete e imprime resultados para al menos tres temas ficticios.
5. Coloca el comportamiento ejecutable en una función `main()`.
6. Llama a `main()` solo bajo `if __name__ == "__main__":`.
7. No modifiques `sys.path`.
8. No uses `from ... import *`.
9. Cambia el nombre de cualquier archivo que sombree un módulo de la biblioteca estándar que utilices.

Preguntas extra:

- ¿Qué nombres vincula `import study_app.grading`?
- ¿Cómo cambiaría el namespace local con `from study_app.grading import classify_score`?
- ¿Qué se ejecuta cuando `study_app.grading` se importa por primera vez en una sesión normal del intérprete?
- ¿Qué contiene `__name__` en el archivo de entrada ejecutado directamente?
- ¿Por qué un import relativo puede comportarse de manera diferente cuando un módulo de paquete se ejecuta por su ruta de archivo?
- ¿Cuándo sería preferible `python -m package.module`?
- ¿Por qué `__init__.py` de un paquete regular puede estar vacío?

## 50. Lista de revisión

Antes de pasar a la fase de biblioteca estándar, confirma que puedes responder sin adivinar:

- ¿Qué es un módulo en un proyecto común basado en archivos `.py`?
- ¿Qué nombre vincula `import grade_tools`?
- ¿Qué cambia con `from grade_tools import classify_score`?
- ¿Qué cambia un alias con `as`?
- ¿Puede ejecutarse código de nivel superior durante un import?
- ¿Cuál es el papel introductorio de `sys.modules`?
- ¿Cuál es el valor de `__name__` cuando un archivo es el programa de nivel superior?
- ¿Qué problema resuelve el main guard?
- ¿Qué representa `sys.path`?
- ¿Por qué nombrar tu archivo `json.py` puede causar problemas?
- ¿Cómo se relacionan `ModuleNotFoundError` e `ImportError`?
- ¿Qué hace reconocible un paquete regular basado en directorios en el diseño convencional?
- ¿Los namespace packages deben contener `__init__.py`?
- ¿Qué significan los puntos iniciales en un import relativo?
- ¿Por qué puede ser útil `python -m package.module`?
- ¿Cuál es la diferencia entre un paquete de importación y una distribución?
- ¿Por qué suelen evitarse los wildcard imports?
- ¿Qué pueden revelar los imports circulares sobre el diseño de módulos?

## 51. Consulta rápida

| Necesidad | Patrón o idea |
|---|---|
| Importar un módulo | `import module_name` |
| Acceder a un nombre del módulo | `module_name.item` |
| Importar nombre seleccionado | `from module_name import item` |
| Asignar alias a un módulo | `import module_name as alias` |
| Asignar alias a un nombre seleccionado | `from module_name import item as alias` |
| Guard de entrada directa | `if __name__ == "__main__":` |
| Ubicaciones de búsqueda de módulos | inspeccionar `sys.path` |
| Caché normal de imports | `sys.modules` |
| Módulo solicitado ausente | normalmente `ModuleNotFoundError` |
| Fallo de import más amplio | `ImportError` |
| Marcador convencional de paquete regular | `__init__.py` |
| Importar submódulo de paquete | `import package.submodule` |
| Import absoluto de paquete | `from package.module import item` |
| Import relativo de módulo hermano | `from .module import item` |
| Ejecutar módulo por nombre de import | `python -m package.module` |
| Ejecutar entrada del paquete | `python -m package` con `package/__main__.py` |
| Evitar namespace oculto | preferir nombres explícitos a `import *` |
| Evitar cirugía casual de rutas | no usar modificación de `sys.path` como estructura normal |

Un modelo útil de dependencias es:

```text
punto de entrada
    ↓ importa
módulos coordinadores
    ↓ importan
módulos reutilizables enfocados
```

Busca una dirección de dependencias que el estudiante pueda dibujar sin crear un nudo.

## Fase 7 completada

Este capítulo cierra la **Fase 7: Errores, Archivos y Módulos**.

La fase ahora conecta manejo de fallos, límites de persistencia, datos textuales estructurados y organización del código:

```text
excepciones
    ↓
señalización deliberada de excepciones
    ↓
tiempo de vida seguro de archivos
    ↓
límites de datos TXT / CSV / JSON
    ↓
imports / módulos / paquetes
```

Ahora puedes construir un pequeño programa que falla deliberadamente cuando se rompe un contrato, maneja fallos externos esperados, persiste datos textuales con seguridad, analiza formatos comunes y separa código reutilizable entre módulos y paquetes.

## Qué sigue

La **Fase 8: Biblioteca Estándar** aprovechará el modelo de importación para explorar herramientas útiles que vienen con Python, comenzando por módulos como `pathlib` y `datetime` según el roadmap del proyecto.

La transición importante es:

```text
aprender cómo los imports organizan dependencias
        ↓
usar deliberadamente módulos de la biblioteca estándar de Python
```

## Referencias oficiales

- Tutorial de Python 3.14, Modules: <https://docs.python.org/3.14/tutorial/modules.html>
- Referencia del lenguaje Python 3.14, The import system: <https://docs.python.org/3.14/reference/import.html>
- Referencia del lenguaje Python 3.14, The import statement: <https://docs.python.org/3.14/reference/simple_stmts.html#import>
- Documentación de línea de comandos de Python 3.14, `-m`: <https://docs.python.org/3.14/using/cmdline.html#cmdoption-m>
- Documentación de Python 3.14 sobre `__main__`: <https://docs.python.org/3.14/library/__main__.html>