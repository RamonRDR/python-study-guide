<div align="center">

# Ingeniería de Pruebas Automatizadas con `pytest`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Bibliotecas Externas](../README.es.md) · [← Anterior: `requests`](../03-requests/README.es.md)

El software resulta más fácil de cambiar cuando el comportamiento esperado puede verificarse de forma repetible y automática. `pytest` ofrece un modelo de pruebas conciso basado en funciones normales de Python, instrucciones `assert`, fixtures reutilizables, parametrización, informes de fallo detallados y un sistema extensible de plugins.

Este capítulo apunta a **pytest 9.1.x** y fue investigado con la documentación y los metadatos de la versión estable actual, **pytest 9.1.1**. pytest 9.1.1 requiere Python 3.10 o posterior; este repositorio valida los ejemplos con Python 3.13.

**Tiempo estimado de estudio:** 300–390 minutos.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar qué demuestra una prueba automatizada y qué no demuestra;
- organizar pruebas para que pytest las descubra de forma predecible;
- escribir assertions legibles e interpretar la introspección de assertions;
- probar valores de punto flotante, excepciones y warnings de forma deliberada;
- reducir duplicación con parametrización;
- modelar setup, teardown y dependencias mediante fixtures;
- aislar filesystem y entorno con `tmp_path` y `monkeypatch`;
- capturar salida estándar y logs con `capsys` y `caplog`;
- usar marks, skips, fallos esperados y selección de pruebas intencionalmente;
- configurar pytest sin ocultar warnings ni omisiones accidentales de pruebas;
- distinguir fronteras de pruebas unitarias, de integración y end-to-end;
- evitar pruebas flaky causadas por tiempo, aleatoriedad, red, estado compartido o supuestos de orden;
- integrar pytest en CI como un contrato ejecutable de calidad.

## 1. Por qué existen las pruebas automatizadas

Una comprobación manual responde una pregunta una vez. Una prueba automatizada convierte esa pregunta en código ejecutable que puede repetirse después de cambios futuros.

Una buena prueba describe un comportamiento, proporciona entradas controladas, observa una salida o efecto secundario y falla cuando el comportamiento observado viola el contrato esperado.

Las pruebas reducen incertidumbre. No demuestran que el software esté libre de bugs.

## 2. Qué añade `pytest`

Python incluye `unittest` en la biblioteca estándar. `pytest` es un framework externo capaz de ejecutar funciones de prueba simples y añadir recursos como:

- introspección de assertions;
- fixtures;
- parametrización;
- marks y selección de pruebas;
- rutas temporales;
- monkeypatch del entorno;
- captura de salida, warnings y logs;
- plugins y hooks.

El objetivo no es hacer pruebas ingeniosas. El objetivo es hacer visible la intención y barata la repetición.

## 3. Las bibliotecas externas necesitan un contrato de versión

Este repositorio declara las dependencias de la Fase 9 en `requirements-external.txt`.

Para este capítulo el contrato es:

```text
pytest >= 9.1 and < 9.2
```

El límite superior importa porque el changelog de pytest ya contiene un draft no publicado de la versión 9.2 con cambios incompatibles. Un currículo publicado debe describir comportamiento ya lanzado y no seguir silenciosamente una versión futura.

## 4. Instala el conjunto de dependencias del repositorio

Crea y activa un entorno virtual y luego instala:

```bash
python -m pip install -r requirements-external.txt
```

Para experimentar de forma aislada:

```bash
python -m pip install pytest
```

Aun así, un proyecto debería registrar qué rango de pytest soporta.

## 5. Prefiere `python -m pytest` cuando importa la identidad del intérprete

Una invocación común es:

```bash
python -m pytest
```

Usar `python -m` hace explícito el intérprete. Esto resulta especialmente útil cuando existen varias instalaciones de Python o entornos virtuales en la misma máquina.

El comando `pytest` también es válido cuando el entorno no es ambiguo.

## 6. Una prueba es especificación ejecutable, no código de producción

Considera una función pequeña:

```python
def calculate_total(unit_price: int, quantity: int) -> int:
    return unit_price * quantity
```

Una prueba puede declarar un comportamiento esperado:

```python
def test_calculate_total_multiplies_price_by_quantity() -> None:
    assert calculate_total(12, 3) == 36
```

El nombre de la prueba comunica el contrato antes de leer la assertion.

## 7. pytest descubre pruebas por convención

Por defecto, pytest descubre módulos y funciones de prueba mediante convenciones de nombres.

Una estructura común es:

```text
project/
├── src/
│   └── calculator.py
└── tests/
    └── test_calculator.py
```

Dentro de `test_calculator.py`, las funciones llamadas `test_*` se recopilan como pruebas.

## 8. La colección es una fase de la ejecución

Antes de ejecutar pruebas, pytest primero las descubre y recopila.

Puedes inspeccionar la colección sin ejecutar nada:

```bash
python -m pytest --collect-only
```

Esto ayuda cuando una prueba esperada no aparece.

Una suite verde que recopiló las pruebas equivocadas no es una señal confiable.

## 9. Mantén los nombres de pruebas orientados al comportamiento

Prefiere nombres que expliquen una regla observable:

```python
def test_discount_is_zero_for_empty_cart() -> None:
    ...
```

Evita nombres que solo reflejen detalles de implementación:

```python
def test_function_2() -> None:
    ...
```

Buenos nombres facilitan el diagnóstico de fallos en CI.

## 10. El `assert` simple es el estilo normal de assertion en pytest

```python
def test_status_is_ready() -> None:
    status = "ready"
    assert status == "ready"
```

pytest reescribe assertions durante la colección para producir diagnósticos más ricos que un `AssertionError` puro.

## 11. La introspección de assertions ayuda a explicar fallos

Una comparación como:

```python
def test_summary() -> None:
    actual = {"count": 2, "status": "ready"}
    expected = {"count": 3, "status": "ready"}
    assert actual == expected
```

puede mostrar los valores diferentes cuando falla.

Por ello, expresiones directas suelen ser mejores que mensajes vagos construidos manualmente en todas las assertions.

## 12. Añade un mensaje solo cuando aporte contexto de dominio

```python
def test_inventory_never_becomes_negative() -> None:
    remaining = 4
    assert remaining >= 0, "inventory contract requires a non-negative balance"
```

El mensaje debe explicar por qué importa la condición, no limitarse a repetir `remaining >= 0`.

## 13. Usa Arrange, Act, Assert cuando aclare la prueba

Una prueba legible suele tener tres etapas conceptuales:

```python
def test_normalize_name_removes_outer_whitespace() -> None:
    raw_name = "  Nova  "

    normalized = raw_name.strip()

    assert normalized == "Nova"
```

No toda prueba pequeña necesita comentarios nombrando las etapas. La propia estructura puede hacerlas evidentes.

## 14. Prueba un comportamiento coherente

Una prueba puede contener varias assertions cuando describen un único resultado, pero evita convertir una sola prueba en un recorrido por comportamientos no relacionados.

Pruebas más pequeñas producen fallos más locales y fáciles de diagnosticar.

## 15. Las pruebas deterministas son repetibles

Una prueba determinista produce el mismo resultado cuando el código y las entradas relevantes no han cambiado.

Amenazas comunes incluyen:

- hora actual;
- valores aleatorios sin control;
- servicios de red;
- archivos o bases compartidos;
- variables de entorno;
- locale y zona horaria;
- dependencia del orden de ejecución.

El aislamiento es una habilidad de diseño, no solo una función del framework.

## 16. Compara resultados de punto flotante con tolerancia explícita

Los valores binarios de punto flotante muchas veces no son adecuados para igualdad exacta después de cálculos.

pytest ofrece `approx()`:

```python
import pytest


def test_ratio() -> None:
    result = 1 / 3
    assert result == pytest.approx(0.333333, rel=1e-5)
```

Elige tolerancias según el dominio y no copiando valores arbitrarios.

## 17. Los valores exactos deben seguir usando assertions exactas

No uses `pytest.approx()` cuando el contrato sea exacto.

```python
def test_item_count() -> None:
    assert len(["a", "b", "c"]) == 3
```

Las herramientas de prueba deben aclarar contratos, no difuminarlos.

## 18. Prueba excepciones esperadas con `pytest.raises`

```python
import pytest


def parse_positive(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise ValueError("value must be positive")
    return number


def test_zero_is_rejected() -> None:
    with pytest.raises(ValueError):
        parse_positive("0")
```

La prueba pasa solo si el tipo de excepción esperado se lanza dentro del context manager.

## 19. Haz match del mensaje cuando forme parte del contrato

```python
def test_zero_has_clear_message() -> None:
    with pytest.raises(ValueError, match="must be positive"):
        parse_positive("0")
```

`match` se interpreta como expresión regular. Escapa caracteres especiales cuando quieras una coincidencia literal.

## 20. Inspecciona la información de la excepción capturada cuando sea necesario

```python
def test_invalid_value_context() -> None:
    with pytest.raises(ValueError) as exc_info:
        parse_positive("-4")

    assert "positive" in str(exc_info.value)
```

Hazlo cuando el detalle adicional importe. No inspecciones internals solo porque pytest los expone.

## 21. Prueba warnings explícitamente con `pytest.warns`

```python
import warnings

import pytest


def old_api() -> None:
    warnings.warn("old API", DeprecationWarning, stacklevel=2)


def test_old_api_warns() -> None:
    with pytest.warns(DeprecationWarning, match="old API"):
        old_api()
```

Los warnings pueden representar contratos de migración que merecen pruebas propias.

## 22. pytest 9.1 puede imponer un presupuesto de warnings

pytest 9.1 añadió `--max-warnings`.

Por ejemplo:

```bash
python -m pytest --max-warnings=10
```

Si todas las pruebas pasan pero la cantidad de warnings no filtrados supera el límite, pytest devuelve un estado dedicado distinto de cero.

Un presupuesto de warnings ayuda a reducir deuda gradualmente en vez de ocultarla toda.

## 23. La parametrización convierte variación de datos en casos de prueba

Cuando el mismo comportamiento debe cumplirse para varias entradas, usa `@pytest.mark.parametrize`:

```python
import pytest


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(-5, 0), (40, 40), (130, 100)],
)
def test_normalize_score(raw: int, expected: int) -> None:
    result = max(0, min(raw, 100))
    assert result == expected
```

pytest crea un caso recopilado separado para cada conjunto de parámetros.

## 24. Separa lógica de prueba y datos de prueba

La parametrización funciona mejor cuando el cuerpo expresa una regla y los datos representan casos interesantes.

Incluye fronteras significativas, no solo muchos ejemplos aleatorios.

Una tabla de diez filas no es automáticamente mejor que tres casos de frontera bien elegidos.

## 25. Da IDs útiles a los parámetros cuando el informe los necesite

```python
@pytest.mark.parametrize(
    ("value", "expected"),
    [(0, "empty"), (1, "single"), (2, "many")],
    ids=["zero", "one", "multiple"],
)
def test_classification(value: int, expected: str) -> None:
    result = "empty" if value == 0 else "single" if value == 1 else "many"
    assert result == expected
```

IDs legibles mejoran los informes para valores de parámetros complejos.

## 26. Usa `pytest.param` para metadatos por caso

```python
@pytest.mark.parametrize(
    "value",
    [
        1,
        pytest.param(-1, marks=pytest.mark.xfail(reason="known limitation")),
    ],
)
def test_positive_only(value: int) -> None:
    assert value > 0
```

Las marks por caso mantienen excepciones visibles sin duplicar toda la prueba.

## 27. pytest 9.1 depreca iterables que no son collections en parametrización

La documentación actual de pytest depreca pasar directamente un iterable que no sea `Collection`, como un generator, en `argvalues`.

Prefiere una lista o tupla concreta en pruebas publicadas:

```python
cases = [(1, 2), (2, 4), (3, 6)]
```

Esto también facilita revisar los datos de prueba.

## 28. Las fixtures modelan dependencias de prueba

Una fixture es un valor o recurso que pytest entrega a una prueba por nombre.

```python
import pytest


@pytest.fixture
def sample_user() -> dict[str, str]:
    return {"name": "Nova", "role": "reader"}


def test_user_role(sample_user: dict[str, str]) -> None:
    assert sample_user["role"] == "reader"
```

La prueba solicita la fixture declarando un parámetro con ese nombre.

## 29. Las fixtures pueden devolver objetos

Las fixtures pueden devolver valores simples, estructuras, clientes configurados, repositorios temporales, conexiones u otros recursos.

Mantén las fixtures enfocadas. Una fixture gigante que prepara toda la aplicación puede ocultar dependencias en vez de aclararlas.

## 30. Las fixtures pueden hacer teardown con `yield`

```python
import pytest


@pytest.fixture
def opened_resource():
    resource = {"open": True}
    yield resource
    resource["open"] = False
```

El código antes de `yield` hace setup. El código posterior hace teardown cuando pytest finaliza la fixture.

Usa context managers reales cuando el recurso de producción ya proporcione uno.

## 31. El scope de la fixture controla su duración

Scopes habituales:

```text
function -> one test invocation
class    -> one test class
module   -> one test module
package  -> one test package
session  -> the whole pytest session
```

El valor predeterminado es `function`.

## 32. Un scope más amplio intercambia aislamiento por reutilización

Un recurso de scope `session` puede ser más rápido al crearse una vez, pero también vive más tiempo y puede transportar estado mutable compartido entre pruebas.

No amplíes el scope solo para acelerar la suite. Primero comprueba que la vida compartida conserva independencia.

## 33. Las fixtures pueden depender de otras fixtures

```python
import pytest


@pytest.fixture
def base_url() -> str:
    return "https://example.invalid"


@pytest.fixture
def endpoint(base_url: str) -> str:
    return f"{base_url}/items"
```

La composición de dependencias suele ser más clara que una fixture que conoce todo el setup.

## 34. Evita dependencias ocultas con exceso de `autouse`

Una fixture `autouse=True` se ejecuta sin aparecer en la firma de cada prueba.

Puede ser útil para una invariante real de toda la suite, pero el uso excesivo dificulta rastrear el comportamiento.

Prefiere parámetros explícitos salvo que la aplicación automática forme parte genuina del contrato del entorno.

## 35. `conftest.py` comparte configuración local y fixtures

Una estructura común es:

```text
tests/
├── conftest.py
├── test_api.py
└── test_reports.py
```

Fixtures definidas en `tests/conftest.py` pueden ser descubiertas por pruebas debajo de ese directorio sin importar `conftest` directamente.

## 36. `conftest.py` sigue reglas de visibilidad por directorio

Para una prueba, pytest consulta archivos `conftest.py` relevantes en el directorio de la prueba y en sus directorios padre.

Eso hace jerárquica la visibilidad.

Coloca fixtures compartidas en el nivel más estrecho que realmente las necesite.

## 37. No importes desde `conftest.py`

Trata `conftest.py` como configuración de pytest, no como módulo de aplicación.

Si los helpers necesitan imports normales, colócalos en un módulo o paquete regular e importa ese módulo desde pruebas y fixtures.

## 38. `tmp_path` proporciona un `Path` temporal a cada prueba

```python
from pathlib import Path


def test_export(tmp_path: Path) -> None:
    report = tmp_path / "report.txt"
    report.write_text("ready\n", encoding="utf-8")

    assert report.read_text(encoding="utf-8") == "ready\n"
```

`tmp_path` es un `pathlib.Path` único para cada invocación de prueba.

Esto evita ensuciar el repositorio con artefactos de pruebas.

## 39. `tmp_path_factory` sirve para scopes más amplios

Una fixture de scope `session` o `module` no puede depender de un `tmp_path` de scope función.

Para recursos temporales de mayor duración, pytest ofrece `tmp_path_factory`.

Elige una vida más amplia solo cuando forme parte del diseño.

## 40. `monkeypatch` cambia estado y lo restaura automáticamente

La fixture `monkeypatch` puede modificar temporalmente:

- atributos de objetos;
- elementos de diccionarios;
- variables de entorno;
- `sys.path`;
- directorio de trabajo actual.

Los cambios se revierten después de finalizar la prueba o fixture solicitante.

## 41. Parchea variables de entorno con `setenv` y `delenv`

```python
import os


def read_mode() -> str:
    return os.getenv("STUDY_MODE", "default")


def test_configured_mode(monkeypatch) -> None:
    monkeypatch.setenv("STUDY_MODE", "focused")
    assert read_mode() == "focused"
```

El código dependiente del entorno se vuelve determinista cuando la prueba controla explícitamente el entorno.

## 42. Parchea donde el código busca la dependencia

Supón que `service.py` contiene:

```python
from client import fetch_status


def is_ready() -> bool:
    return fetch_status() == "ready"
```

La prueba normalmente necesita parchear `service.fetch_status`, porque ese es el nombre que `is_ready()` resuelve en runtime.

Parchear la definición original en `client` puede no reemplazar una referencia ya importada en `service`.

## 43. `monkeypatch.context()` puede limitar aún más la duración del parche

Cuando una prueba necesita el parche solo dentro de un bloque pequeño, `monkeypatch.context()` crea un contexto anidado cuyos cambios se revierten al salir.

Una vida más corta del parche reduce interacciones sorprendentes en pruebas complejas.

## 44. Usa test doubles para sustituir fronteras, no todo

Un test double puede representar un colaborador lento, no determinista, destructivo o no disponible.

Categorías informales habituales:

```text
stub  -> returns controlled values
fake  -> lightweight working implementation
spy   -> records how it was used
mock  -> verifies expected interactions
```

El vocabulario importa menos que dejar claro el propósito de la sustitución.

## 45. `unittest.mock` de la biblioteca estándar funciona con pytest

pytest no exige un estilo separado de mocking.

Puedes combinar assertions y fixtures de pytest con `unittest.mock.Mock`, `MagicMock` o `patch` cuando encajen.

No hagas mock de cálculos puros solo porque la herramienta existe.

## 46. `capsys` captura stdout y stderr a nivel Python

```python
def announce(topic: str) -> None:
    print(f"Studying: {topic}")


def test_announce(capsys) -> None:
    announce("pytest")
    captured = capsys.readouterr()
    assert captured.out == "Studying: pytest\n"
    assert captured.err == ""
```

Resulta útil para interfaces de línea de comandos y funciones cuya salida forma parte del contrato.

## 47. `capfd` captura a nivel de file descriptor

`capsys` se centra en `sys.stdout` y `sys.stderr` de Python.

`capfd` captura los file descriptors 1 y 2, útil cuando la salida proviene de código de nivel inferior que evita los streams normales de Python.

Usa el mecanismo más estrecho que coincida con el comportamiento probado.

## 48. `caplog` captura registros de logging

```python
import logging


def test_log_message(caplog) -> None:
    logger = logging.getLogger("study")

    with caplog.at_level(logging.INFO, logger="study"):
        logger.info("session ready")

    assert "session ready" in caplog.text
```

Las pruebas también pueden inspeccionar registros estructurados en lugar de limitarse al texto renderizado.

## 49. Cuidado al reconfigurar el root logger durante `caplog`

La documentación de pytest advierte que cambiar handlers del root logger durante una prueba puede interferir con la captura.

Prefiere configuración dirigida a un logger específico y evita reemplazar todo el conjunto de handlers salvo que la prueba valide precisamente esa configuración.

## 50. Las marks añaden metadatos a las pruebas

Las marks pueden clasificar o modificar comportamiento.

```python
import pytest


@pytest.mark.slow
def test_large_report() -> None:
    assert True
```

Las custom marks deben representar categorías útiles, no sustituir una organización clara de la suite.

## 51. Registra las custom marks

Las marks no registradas pueden generar warnings y los errores de escritura pueden crear categorías no deseadas silenciosamente.

Un `pyproject.toml` puede registrarlas:

```toml
[tool.pytest.ini_options]
markers = [
    "slow: tests that intentionally take longer",
    "integration: tests that cross component boundaries",
]
```

Registrar nombres convierte las marks en un contrato documentado del proyecto.

## 52. `strict_markers` puede convertir marks desconocidas en errores

```toml
[tool.pytest.ini_options]
strict_markers = true
```

Esto resulta útil cuando una marca mal escrita debe fallar inmediatamente en lugar de convertirse en una nueva categoría.

## 53. pytest 9 introdujo un strict mode más amplio

pytest 9 ofrece la opción `strict`, que activa conjuntamente comprobaciones de configuración, markers, xfail e IDs de parametrización.

La documentación avisa de que futuras versiones pueden añadir más opciones de strictness. Usa el modo global con una versión controlada o cuando el proyecto quiera adoptar nuevas verificaciones deliberadamente.

## 54. Salta pruebas solo por una razón ambiental real

```python
import sys

import pytest


@pytest.mark.skipif(sys.platform == "win32", reason="POSIX-only contract")
def test_posix_behavior() -> None:
    assert True
```

Una prueba saltada no verifica el comportamiento. Demasiados skips pueden crear puntos ciegos.

## 55. `xfail` registra un fallo esperado conocido

```python
import pytest


@pytest.mark.xfail(reason="known parser limitation", strict=True)
def test_future_case() -> None:
    assert False
```

Con `strict=True`, un pase inesperado falla la suite y obliga a notar que la limitación conocida puede haberse corregido.

No uses `xfail` como estacionamiento permanente para pruebas rotas.

## 56. Selecciona pruebas con `-k`

`-k` filtra pruebas recopiladas mediante una expresión de nombre:

```bash
python -m pytest -k "report and not slow"
```

Es cómodo durante desarrollo local, pero CI debería seguir ejecutando la suite completa pretendida o particiones documentadas explícitamente.

## 57. Selecciona grupos marcados con `-m`

```bash
python -m pytest -m "integration"
```

o:

```bash
python -m pytest -m "not slow"
```

Las marks hacen explícitas las particiones cuando están registradas y mantenidas de forma consistente.

## 58. Detén pronto con `-x` o `--maxfail`

```bash
python -m pytest -x
```

se detiene tras el primer fallo.

```bash
python -m pytest --maxfail=3
```

se detiene después de tres fallos.

Estas opciones aceleran feedback, pero no sustituyen ejecutar la suite completa antes de un release.

## 59. Vuelve a ejecutar fallos anteriores con `--lf`

```bash
python -m pytest --lf
```

pytest puede usar su caché para seleccionar pruebas que fallaron en la ejecución previa.

Trátalo como acelerador local. Un job limpio de CI no debe depender del estado de la ejecución anterior de un desarrollador.

## 60. La verbosidad cambia el informe, no la corrección

Opciones comunes:

```bash
python -m pytest -q
python -m pytest -v
```

La salida quiet puede ayudar en logs automatizados; la salida verbose ayuda a identificar casos parametrizados.

El contrato de prueba no debe depender de la decoración del terminal.

## 61. La configuración pertenece al control de versiones

pytest soporta configuración en archivos como `pyproject.toml`, `pytest.ini` y otros documentados por el proyecto.

Una configuración mínima en `pyproject.toml` podría ser:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
strict_markers = true
```

La configuración debe volver la suite más predecible, no ocultar comportamiento que falla.

## 62. `testpaths` limita la detección predeterminada

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

Cuando pytest se ejecuta sin rutas explícitas, esto indica dónde espera el proyecto encontrar pruebas.

Si hay pruebas en otros lugares, configúralas o ejecútalas de forma intencional.

## 63. Ten cuidado con `addopts` global

Un proyecto puede configurar opciones predeterminadas, por ejemplo:

```toml
[tool.pytest.ini_options]
addopts = "-ra"
```

Evita defaults que salten silenciosamente categorías importantes o supriman diagnósticos necesarios.

## 64. Entiende el root que selecciona pytest

pytest determina un directorio raíz y un contexto de configuración para la colección.

Ejecutarlo desde un directorio inesperado puede cambiar qué configuración y qué archivos `conftest.py` son visibles.

Al depurar problemas de descubrimiento, revisa el rootdir y el archivo de configuración reportados.

## 65. Mantén imports predecibles

Las pruebas siguen siendo módulos Python, por lo que las reglas de import importan.

Un proyecto debería usar un layout deliberado y probar el código que pretende distribuir, sin depender de imports accidentales por el directorio actual.

El layout `src/` puede ayudar a separar código instalado de rutas locales del repositorio.

## 66. No des un `__init__` personalizado a clases de prueba de pytest

Las clases de prueba se recopilan por convención y no deberían comportarse como objetos de aplicación que requieren argumentos de constructor.

Usa fixtures para dependencias de pruebas en lugar de construcción personalizada de clases.

Las funciones de prueba simples suelen ser el punto de partida más claro.

## 67. Los valores de fixtures deben corresponder a su nombre

Si una fixture se llama `authenticated_client`, debería proporcionar ese estado de forma confiable.

Evita fixtures cuyo resultado cambie inesperadamente por configuraciones globales no relacionadas. Fixtures ambiguas convierten las pruebas en acertijos.

## 68. Evita bosques de fixtures

La composición de fixtures es potente, pero una prueba que depende de una fixture que depende de otras seis puede resultar difícil de entender.

Si el setup se convierte en un laberinto, considera builders simples, helper functions o fronteras de integración más pequeñas.

## 69. Las pruebas unitarias aíslan una pequeña unidad de comportamiento

Una prueba unitaria normalmente ejercita una función, clase o pequeño componente con colaboradores controlados.

Son valiosas para feedback rápido, pero la definición exacta de “unidad” depende de la arquitectura.

No conviertas la etiqueta en una regla doctrinal.

## 70. Las pruebas de integración cruzan fronteras reales

Una prueba de integración puede ejercitar combinaciones como:

```text
application code + database adapter
application code + local HTTP server
parser + real file format
repository + temporary filesystem
```

Estas pruebas validan contratos que los mocks no pueden demostrar por completo.

## 71. Las pruebas end-to-end validan flujos mayores

Las pruebas end-to-end recorren un camino amplio del sistema y pueden detectar problemas que las pruebas pequeñas no ven.

También suelen ser más lentas, caras de diagnosticar y sensibles al estado del entorno.

Una suite saludable suele combinar varias capas.

## 72. Prueba comportamiento observable antes que detalles de implementación

Si un refactor conserva el comportamiento público, las buenas pruebas normalmente siguen pasando.

Las pruebas que verifican cada llamada a un helper privado encarecen innecesariamente la limpieza interna.

Las assertions de interacción son apropiadas cuando la propia interacción forma parte del contrato, como “no envíes la solicitud dos veces”.

## 73. Haz mock de servicios externos en la frontera correcta

Una prueba unitaria no debe llamar a una API pública real.

Para código HTTP, estrategias útiles incluyen:

- parchear tu propia abstracción de cliente;
- usar un servidor de prueba local;
- usar un plugin específico de testing HTTP cuando el proyecto lo adopte.

Las pruebas no deberían depender de internet pública salvo que sean pruebas deliberadas de sistema externo.

## 74. Mantén secretos fuera de los datos de prueba

Nunca pongas tokens, contraseñas, cookies, URLs privadas ni datos personales reales en pruebas.

Usa valores ficticios como:

```python
fake_token = "test-token-not-a-secret"
```

Las fixtures suelen terminar en logs e informes de fallo, por lo que merecen la misma disciplina de privacidad que el código de producción.

## 75. Controla el tiempo en vez de competir con el reloj

Evita pruebas como:

```python
import time


def test_waits() -> None:
    time.sleep(2)
    assert True
```

Si el comportamiento depende del tiempo, inyecta un clock o parchea la fuente estrecha de tiempo que usa el código.

Dormir vuelve lenta la suite y no garantiza que el estado asíncrono esté listo.

## 76. Controla la aleatoriedad

Para código aleatorio, algunas opciones son:

- inyectar un generador de números aleatorios;
- usar una seed conocida cuando el contrato lo permita;
- probar invariantes con entradas controladas.

Una prueba que falla solo en algunas ejecuciones aleatorias es difícil de reproducir y diagnosticar.

## 77. Las pruebas no deben depender del orden de ejecución

Una prueba no debería necesitar que otra se ejecute primero.

El estado mutable compartido a nivel de módulo o sesión es una causa habitual de dependencia del orden.

Si las pruebas fallan solo cuando cambia el orden, la suite ha revelado un problema real de aislamiento.

## 78. Una prueba flaky es un defecto de confiabilidad

Una prueba flaky alterna entre pasar y fallar sin un cambio relevante de código.

Causas comunes:

- carreras de timing;
- servicios externos;
- estado compartido;
- orden no determinista;
- limpieza insuficiente;
- agotamiento de recursos.

Repetir hasta que quede verde oculta la señal en vez de repararla.

## 79. Coverage y corrección son métricas distintas

La cobertura de código puede revelar código que las pruebas nunca ejecutan.

No demuestra que las assertions sean significativas, que las fronteras estén representadas o que los requisitos sean correctos.

Trata coverage como evidencia de ejecución, no como sustituto del diseño de pruebas.

## 80. Los plugins extienden pytest

pytest tiene un gran ecosistema de plugins para coverage, código asíncrono, frameworks, ejecución paralela y pruebas HTTP.

Los plugins también son dependencias. Limita versiones importantes, revisa compatibilidad y evita añadir un plugin cuando pytest core ya resuelve claramente el problema.

## 81. pytest core no hace que cualquier `async def` funcione automáticamente

Las funciones de prueba asíncronas suelen requerir un plugin o integración de framework apropiado.

No supongas que instalar pytest define por sí solo la política de event loop que necesita la aplicación.

El plugin pasa a formar parte del contrato de dependencias de testing.

## 82. `required_plugins` puede exigir la presencia de plugins

La configuración de pytest puede declarar plugins obligatorios para que la ejecución falle pronto si falta uno.

Esto resulta útil cuando la suite de otro modo podría recopilarse mal o fallar después con errores confusos de fixtures ausentes.

Usa requisitos reales del proyecto, no listas copiadas de otros repositorios.

## 83. pytest puede ejecutar muchas pruebas estilo `unittest`

Adoptar pytest no exige necesariamente reescribir inmediatamente una suite existente de `unittest`.

pytest soporta muchas pruebas escritas con `unittest.TestCase` y permite una migración gradual.

La migración debería mejorar mantenimiento, no crear churn por sí misma.

## 84. Trata los códigos de salida como contratos de CI

Un sistema CI debe fallar cuando el runner de pruebas reporta fallo.

No escribas wrappers de shell que descarten el exit status de pytest.

Los ejemplos ejecutables de este capítulo convierten el código de salida programático en entero solo para mostrar el resultado de forma determinista.

## 85. Ejemplo ejecutable: assertions y parametrización

[`examples/assertions_and_parametrize.py`](examples/assertions_and_parametrize.py) crea un módulo pytest temporal, lo ejecuta con el runner real y muestra solo un resumen determinista.

Salida esperada:

```text
exit code: 0
passed: 4
```

La suite temporal demuestra una assertion normal y tres casos de frontera parametrizados.

## 86. Ejemplo ejecutable: fixtures y `tmp_path`

[`examples/fixtures_and_tmp_path.py`](examples/fixtures_and_tmp_path.py) demuestra una fixture que depende de la fixture integrada `tmp_path`.

Salida esperada:

```text
exit code: 0
passed: 2
```

Cada prueba recibe su propia invocación de fixture y frontera temporal de filesystem.

## 87. Ejemplo ejecutable: `monkeypatch`

[`examples/monkeypatch_environment.py`](examples/monkeypatch_environment.py) controla una variable de entorno sin dejar estado global del proceso.

Salida esperada:

```text
exit code: 0
passed: 2
```

El ejemplo verifica tanto el estado fallback como un estado configurado explícitamente.

## 88. Ejemplo ejecutable: excepciones y warnings

[`examples/exceptions_and_warnings.py`](examples/exceptions_and_warnings.py) usa `pytest.raises` y `pytest.warns` para hacer explícito el comportamiento de fallo y migración.

Salida esperada:

```text
exit code: 0
passed: 2
```

Se verifican tipo/mensaje de excepción y categoría/mensaje del warning.

## 89. Ejemplo ejecutable: captura de salida y logs

[`examples/capture_output_and_logs.py`](examples/capture_output_and_logs.py) demuestra `capsys` y `caplog`.

Salida esperada:

```text
exit code: 0
passed: 2
```

La suite valida tanto salida de línea de comandos como un mensaje dirigido de logger.

## 90. Errores comunes

### Error 1: tratar una suite verde como prueba de ausencia de bugs

Las pruebas solo cubren comportamientos e entradas que realmente ejercitan.

### Error 2: probar detalles triviales de implementación

Las pruebas demasiado acopladas encarecen refactors inofensivos.

### Error 3: compartir estado mutable entre pruebas

Esto genera dependencia de orden y flakiness.

### Error 4: llamar a servicios públicos desde pruebas unitarias

La disponibilidad de red y los datos remotos vuelven la suite no determinista.

### Error 5: ocultar todos los warnings

Los warnings suelen revelar migraciones que el proyecto debe realizar.

### Error 6: abusar de mocks

Una suite de mocks puede demostrar que los mocks se comportan exactamente como se configuraron y aun así perder errores reales de integración.

### Error 7: crear fixtures gigantes

Grafos enormes de setup ocultan lo que cada prueba realmente necesita.

### Error 8: aceptar reruns flaky como normales

Una prueba flaky es un defecto del sistema de feedback.

## 91. Tabla de decisión

| Necesidad | Herramienta útil | Principal cuidado |
| --- | --- | --- |
| Comparar valores normales | `assert` | mantén explícito el contrato esperado |
| Comparar floats | `pytest.approx()` | elige tolerancia apropiada al dominio |
| Esperar una excepción | `pytest.raises()` | no captures fallos no relacionados |
| Esperar un warning | `pytest.warns()` | prueba categoría/mensaje deliberadamente |
| Repetir una regla en varios casos | `@pytest.mark.parametrize` | elige datos de frontera significativos |
| Reutilizar setup | fixture | evita grafos ocultos y gigantes |
| Archivos temporales | `tmp_path` | no dependas de artefactos del repositorio |
| Cambios temporales de entorno | `monkeypatch` | parchea donde el código busca el nombre |
| Capturar stdout/stderr | `capsys` | verifica solo salida que forme parte del contrato |
| Capturar logs | `caplog` | evita alterar handlers del root logger |
| Clasificar pruebas | marks registradas | evita errores silenciosos de escritura |
| Fallo esperado conocido | `xfail` | prefiere strict y elimina cuando se corrija |

## 92. Referencia rápida

```bash
python -m pytest
python -m pytest -q
python -m pytest -v
python -m pytest --collect-only
python -m pytest -k "name_expression"
python -m pytest -m "marker_expression"
python -m pytest -x
python -m pytest --maxfail=3
python -m pytest --lf
python -m pytest --max-warnings=10
```

Patrones principales en Python:

```python
assert actual == expected

with pytest.raises(ValueError, match="message"):
    operation()

with pytest.warns(DeprecationWarning):
    old_operation()
```

## 93. Checklist de revisión

Antes de considerar confiable una suite, pregunta:

- ¿Las pruebas previstas realmente se recopilan?
- ¿Los nombres explican comportamientos?
- ¿Las assertions son específicas para fallar por la razón correcta?
- ¿Están representados casos de frontera y error?
- ¿Los archivos se escriben en rutas temporales?
- ¿Los cambios de entorno se restauran automáticamente?
- ¿Red, reloj y aleatoriedad están controlados?
- ¿Las pruebas pueden ejecutarse independientemente y en cualquier orden?
- ¿Los warnings son visibles e intencionales?
- ¿Las custom marks están registradas?
- ¿Los fallos esperados se revisan y son temporales?
- ¿CI conserva el exit status de fallo de pytest?
- ¿Datos y logs de prueba están libres de secretos y datos personales?

## 94. Ejercicio práctico

Crea un pequeño paquete ficticio que valide registros de sesiones de estudio.

Requisitos:

1. Crea una función que reciba un tema y una duración en minutos.
2. Rechaza un tema vacío con `ValueError`.
3. Rechaza duración cero o negativa con `ValueError`.
4. Devuelve un diccionario normalizado para entrada válida.
5. Escribe pruebas de éxito con `assert` simple.
6. Parametriza al menos tres duraciones inválidas.
7. Usa `pytest.raises(..., match=...)` para un error de validación.
8. Escribe una fixture con datos válidos de ejemplo.
9. Añade una función que guarde una sesión como texto o JSON y pruébala con `tmp_path`.
10. Añade una función que lea una configuración de una variable de entorno y pruébala con `monkeypatch`.
11. Añade una función estilo CLI y valida su salida con `capsys`.
12. Añade un logger y valida con `caplog`.
13. Registra una custom marker para pruebas de integración.
14. Ejecuta `python -m pytest --collect-only` y confirma los casos esperados.
15. Ejecuta la suite completa desde un proceso limpio.

Desafíos de extensión:

- mueve fixtures compartidas a un `conftest.py` cuidadosamente limitado;
- añade un warning para una forma de entrada deprecada y pruébalo con `pytest.warns`;
- usa `pytest.approx` para una razón calculada con tolerancia documentada;
- construye una prueba de integración HTTP local usando conceptos del capítulo anterior de `requests`;
- añade CI que instale las dependencias declaradas y ejecute la suite desde cero.

## 95. Conexiones con conceptos anteriores

`pytest` conecta casi todas las fases anteriores:

- **funciones:** prueba comportamiento mediante entradas y salidas explícitas;
- **colecciones:** construye tablas de parámetros y valores esperados estructurados;
- **flujo de programa:** ejercita ramas y condiciones de frontera;
- **excepciones:** valida contratos de fallo deliberado;
- **archivos:** aísla filesystem con rutas temporales;
- **módulos y paquetes:** organiza código e imports de forma predecible;
- **`pathlib`:** trabaja naturalmente con `tmp_path`;
- **`datetime`:** inyecta o parchea límites temporales en lugar de competir con el reloj real;
- **logging:** valida señales operativas con `caplog`;
- **`decimal`:** prueba reglas monetarias exactas sin tolerancia de float inapropiada;
- **pandas/openpyxl/requests:** convierte comportamiento de bibliotecas externas en regresiones repetibles.

## 96. Referencias primarias

- [pytest documentation](https://docs.pytest.org/)
- [Get Started](https://docs.pytest.org/en/stable/getting-started.html)
- [How to invoke pytest](https://docs.pytest.org/en/stable/how-to/usage.html)
- [Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Temporary directories](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- [Monkeypatching](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [Logging](https://docs.pytest.org/en/stable/how-to/logging.html)
- [Warnings](https://docs.pytest.org/en/stable/how-to/capture-warnings.html)
- [Skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [API reference](https://docs.pytest.org/en/stable/reference/reference.html)
- [pytest changelog](https://docs.pytest.org/en/stable/changelog.html)
- [pytest on PyPI](https://pypi.org/project/pytest/)

Cuando se preparó este capítulo, PyPI listaba pytest 9.1.1 como la release estable más reciente. El currículo apunta a la serie 9.1.x en lugar del draft no publicado 9.2 o de una versión futura sin límite.

## 97. Fase 9 completada

La Fase 9 conecta ahora cuatro fronteras importantes de terceros:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
requests -> communicate with HTTP services
pytest   -> verify behavior repeatedly and automatically
```

Esto cierra la **Fase 9: Bibliotecas Externas**.

La siguiente fase deja las habilidades aisladas de bibliotecas y pasa al trabajo integrado de portafolio: **Fase 10: Proyectos Prácticos**.

Antes de continuar, practica escribiendo pruebas que hagan informativos los fallos. Una suite es más valiosa cuando te da confianza para cambiar el código y no cuando solamente produce un número verde.
