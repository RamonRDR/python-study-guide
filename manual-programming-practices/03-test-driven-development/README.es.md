# Desarrollo guiado por pruebas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-specification-driven-development/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-professional-workflow/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Tiempo estimado:** 45–60 minutos. Sigue requisitos de la [lección de especificación](../02-specification-driven-development/README.es.md). TDD significa escribir una prueba que falla para un comportamiento pequeño, implementar lo suficiente para pasar y mejorar código sin cambiar comportamiento. Es un ciclo de feedback, no sustituto de requisitos. Usamos unittest de la biblioteca estándar; consulta [pytest](../../external-libraries/04-pytest/README.es.md) para la alternativa existente.

## 1. Red: escribe primero una prueba

En nueva carpeta de práctica, crea reading_progress.py con implementación provisional intencional:

```python
def remaining_pages(total_pages, pages_read):
    raise NotImplementedError
```

Crea test_reading_progress.py junto a él:

```python
import unittest
from reading_progress import remaining_pages


class ReadingProgressTests(unittest.TestCase):
    def test_remaining_pages(self):
        self.assertEqual(remaining_pages(20, 7), 13)
```

Desde esa carpeta ejecuta:

```shell
python -m unittest discover -s . -p 'test_*.py' -v
```

En shell compatible descubre la prueba; usa comillas dobles para el patrón si es necesario. Usa el Python del entorno comprobado. Espera una prueba con error (NotImplementedError): falta el comportamiento. Una prueba que no importa el módulo por motivo ajeno no demuestra el red previsto; corrige el entorno primero.

## 2. Green: implementa solo el primer comportamiento

Sustituye el provisional por `return total_pages - pages_read`. Ejecuta otra vez. Debe pasar. Añade pruebas AC2, después AC3 y AC4 en incrementos pequeños. Usa `self.assertRaises(ValueError)` o `self.assertRaises(TypeError)` como gestores de contexto. Ejecuta cada prueba nueva antes de implementar el comportamiento faltante; la resta sola fallará en pruebas de rangos inválidos. Valida los tipos exactos antes de los rangos con type(value) is int; esto excluye deliberadamente bool (subclase de int) y otras subclases de int. Añade prueba sin salida (AC5) con stdout/stderr redirigidos, luego comprueba precedencia de error de tipo y rechazo de una subclase de int. No debilites una prueba que falla para que pase.

## 3. Refactor: mejora y comprueba

Mejora nombres o elimina repetición solo manteniendo pruebas verdes. Por ejemplo, agrupa casos límite equivalentes con subTest. Refactorizar cambia estructura, no comportamiento especificado. Ejecuta la suite completa tras cada cambio.

Intenta por tu cuenta antes de abrir la [implementación de referencia](examples/reading_progress.py) y las [pruebas de referencia](examples/test_reading_progress.py). El código final es compartido entre idiomas. La referencia tiene siete métodos de prueba, incluidos grupos de límites; un método puede comprobar varios casos. Desde la raíz del repositorio ejecuta:

```shell
python -m unittest discover -s manual-programming-practices/03-test-driven-development/examples -p 'test_*.py' -v
python manual-programming-practices/03-test-driven-development/examples/reading_progress.py
```

Salida esperada del demo: 13. La suite final debe pasar; el provisional rojo solo está en la lección, no en código ejecutable versionado. El CI ejecuta la suite dedicada y el demo aprobado.

## 4. Práctica independiente

Sin leer referencia, implementa contrato, escribe pruebas y registra observaciones red/green/refactor. Cambia temporalmente resta por suma o elimina una validación en tu copia. Comprueba que falla una prueba relevante; restaura implementación correcta y ejecuta otra vez. Explica por qué aprobación no demuestra todos los casos posibles ni calidad del código. Para una función nueva, actualiza primero la especificación si cambia comportamiento.

**Referencia rápida:** definir comportamiento → prueba que falla → mínima implementación correcta → prueba que pasa → refactorizar → repetir. Consulta [unittest](https://docs.python.org/3.13/library/unittest.html) para aserciones y descubrimiento.

<!-- chapter-navigation:bottom -->
[← Anterior](../02-specification-driven-development/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-professional-workflow/README.es.md)
<!-- /chapter-navigation:bottom -->
