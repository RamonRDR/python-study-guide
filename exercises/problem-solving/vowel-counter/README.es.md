# Contador de vocales

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.vowel-counter` · **Dificultad:** Fácil · **Tiempo estimado:** 10 min

## Requisitos previos

- [Cadenas y acceso a caracteres](../../../strings-and-numbers/01-string-creation-and-indexing/README.es.md)
- [Pertenencia y normalización de cadenas](../../../strings-and-numbers/02-common-string-methods/README.es.md)
- [Pertenencia y condiciones booleanas](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)
- [Iteración con for](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [Definición de funciones](../../../functions/01-defining-and-calling-functions/README.es.md)
- [Parámetros](../../../functions/02-parameters-and-arguments/README.es.md)
- [Valores de retorno](../../../functions/03-return-values/README.es.md)
- [Anotaciones de tipo](../../../functions/05-type-hints/README.es.md)
- [Acumulador y descomposición](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [Pruebas límite](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [Complejidad](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)

## Objetivo

Implementa count_vowels(text) y devuelve la cantidad de vocales ASCII A, E, I, O, U (mayúsculas o minúsculas) en la cadena de entrada. Cuenta apariciones repetidas; ignora todos los demás caracteres.

- La entrada es una str de Python, incluso vacía; otros tipos están fuera del contrato.
- Solo cuentan los diez caracteres ASCII literales aeiouAEIOU. Las letras acentuadas, y/Y, dígitos, puntuación, espacios y otros caracteres Unicode no cuentan.
- Devuelve un int, no una cadena, booleano ni salida impresa. No se necesitan dependencias externas ni operaciones de entrada/salida.

Inténtalo de forma independiente primero. Copia el código inicial a un directorio personal de práctica; no edites la solución de referencia del repositorio. Python 3.13 es la base; el ejercicio usa solo el lenguaje estándar. No se ha verificado la ejecución en navegador. Las pruebas y soluciones públicas son visibles, no secretas.

[Código inicial](starter.py) · [Registro estructurado](exercise.json)

```python
def count_vowels(text: str) -> int:
    raise NotImplementedError("Implement count_vowels")
```

## Ejemplos

| Entrada | Esperado | Motivo |
| --- | ---: | --- |
| `"Hello, World!"` | 3 | e, o y o cuentan. |
| `"AEIOU"` | 5 | Las cinco vocales mayúsculas cuentan. |
| `""` | 0 | No hay caracteres que contar. |
| `"Aéİu🙂"` | 2 | Solo A y u cuentan. |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

¿Qué valor debe tener el contador antes de leer cualquier carácter?

</details>

<details>
<summary>Pista 2</summary>

Recorre la cadena original con for; comprueba pertenencia en la cadena literal de vocales ASCII.

</details>

<details>
<summary>Pista 3</summary>

Incrementa solo si hay coincidencia y devuelve el contador después del bucle.

</details>

## Referencia y explicación

<details>
<summary>Mostrar después de tu intento</summary>

[Solución de referencia](solution.py)

Empieza en cero. Por cada carácter original, incrementa una vez si pertenece a aeiouAEIOU. Devuelve el conteo acumulado después del bucle. Esto cuenta repeticiones y trata mayúsculas sin convertir el caso Unicode. Convertir toda la cadena con lower() puede transformar U+0130 (İ) en i ASCII seguido de una marca combinante, cambiando el contrato. Devolver dentro del bucle ignoraría caracteres posteriores.

- Tiempo: O(n), una pasada por los n caracteres de la cadena Python; la pertenencia en una cadena fija de diez caracteres tiene coste acotado.
- Espacio: O(1) variables auxiliares en el modelo habitual de coste fijo; el contador usa O(log n) bits si se contabiliza almacenamiento de enteros arbitrarios.

</details>

## Validación

Prueba tu propio archivo manualmente llamando a count_vowels con las entradas anteriores y comparando los enteros devueltos. Añade al menos dos casos antes de mirar la referencia. El comando siguiente, ejecutado desde la raíz, verifica la referencia y las implementaciones incorrectas conocidas, no tu archivo personal. No ejecuta código arbitrario de estudiantes.

```bash
python -m unittest discover -s tests -p "test_problem_solving_pilot.py"
```

[Código de pruebas](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.es.md) · [Índice de ejercicios](../../README.es.md)
