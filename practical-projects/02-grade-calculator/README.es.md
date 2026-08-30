<div align="center">

# Proyecto 02 · Calculadora de Calificaciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el segundo proyecto de la **Fase 10: Proyectos Prácticos**. Se centra en reglas configurables, agregación ponderada, validación, seguimiento parcial y pruebas deterministas, sin repetir los límites de persistencia del Proyecto 01.

**Tiempo estimado de estudio e implementación:** 150–210 minutos.

## Objetivos de aprendizaje

Al finalizar este proyecto, deberías poder:

- convertir reglas de calificación en contratos de datos explícitos;
- modelar evaluaciones y bandas de calificación inmutables con dataclasses;
- validar notas y pesos antes de modificar el estado de la calculadora;
- calcular promedios ponderados sin depender de punto flotante binario;
- distinguir un promedio de progreso de un resultado final del curso;
- hacer configurables las reglas de letra y aprobación;
- devolver un informe estructurado antes de formatearlo para mostrarlo;
- probar valores límite, configuraciones inválidas y políticas personalizadas.

## 1. Resumen del proyecto

Construye una calculadora de calificaciones que pueda:

1. registrar evaluaciones calificadas;
2. asignar un peso porcentual a cada evaluación;
3. rechazar pesos acumulados superiores al 100%;
4. calcular el promedio ponderado actual con las evaluaciones ingresadas;
5. mostrar el peso completado y el restante;
6. clasificar el promedio con una política configurable;
7. informar aprobado/reprobado solo cuando el curso alcance exactamente el 100% del peso;
8. aceptar bandas y nota mínima de aprobación personalizadas;
9. generar un informe de texto determinista;
10. demostrar el comportamiento importante con pruebas automatizadas.

## 2. Requisitos funcionales

Cada evaluación contiene:

```text
name   -> texto no vacío
score  -> porcentaje de 0.00 a 100.00
weight -> porcentaje mayor que 0.00 y como máximo 100.00
```

La calculadora conserva el orden de inserción y nunca permite que el peso combinado supere `100.00`.

## 3. Política de calificación predeterminada

La política predeterminada es:

```text
A -> 90.00 a 100.00
B -> 80.00 a 89.99
C -> 70.00 a 79.99
D -> 60.00 a 69.99
F ->  0.00 a 59.99

nota mínima de aprobación -> 60.00
```

Estos límites son una convención del proyecto, no un estándar académico universal. Otra institución puede proporcionar una `GradePolicy` diferente.

## 4. Por qué los porcentajes usan `Decimal`

Notas y pesos se normalizan a dos decimales con `ROUND_HALF_UP`.

```python
Assessment.create("Midterm", "91", "30")
```

El proyecto no usa `float` para valores de calificación. La conversión también usa un contexto decimal local explícito para que la precisión, el redondeo o los traps del código llamador no alteren el contrato de validación.

## 5. Agregación ponderada exacta

Después de validar notas y pesos a dos decimales, la calculadora los convierte a centésimos enteros.

```text
91.00 -> 9100
30.00 -> 3000
```

La agregación ponderada usa enteros de Python, evitando pérdida de precisión por un contexto aritmético externo de `Decimal`. La razón final se redondea half up a dos decimales.

## 6. El modelo `Assessment`

`Assessment` es inmutable:

```python
@dataclass(frozen=True, slots=True)
class Assessment:
    name: str
    score: Decimal
    weight: Decimal
```

La validación se ejecuta incluso si se usa directamente el constructor de la dataclass.

## 7. Bandas y políticas de calificación

Una banda contiene una etiqueta y una puntuación mínima:

```python
GradeBand.create("A", "90")
```

Una política contiene bandas ordenadas y una nota mínima de aprobación. Las bandas deben:

- usar etiquetas únicas;
- usar puntuaciones mínimas únicas;
- estar ordenadas de mayor a menor;
- terminar en `0.00` para cubrir cualquier nota válida.

## 8. Agregar evaluaciones

```python
calculator = GradeCalculator()
calculator.add("Homework", "82.50", "20")
calculator.add("Midterm", "91", "30")
```

Si una nueva evaluación hace que el peso total supere `100.00`, la operación lanza `ValueError` y no agrega la evaluación rechazada.

## 9. Promedio de progreso

`average()` calcula el promedio ponderado normalizado solo sobre las evaluaciones ingresadas hasta el momento.

Si solo se calificó el 40% del curso, el promedio actual describe ese 40%. **No** trata el 60% restante como nota cero.

## 10. Informe parcial frente a informe final

`report()` puede utilizarse antes de completar el curso. En ese estado:

```text
complete -> False
passed   -> None
```

`final_report()` exige que el peso total sea exactamente `100.00`. Solo entonces aprobado/reprobado se considera final.

Esta distinción evita presentar un curso incompleto como un resultado terminado.

## 11. Informe estructurado

La calculadora devuelve primero una dataclass `GradeReport` con:

```text
assessment_count
total_weight
remaining_weight
average
letter_grade
complete
passed
```

El formato se separa en `format_report(...)`. Así las reglas pueden probarse sin interpretar texto impreso.

## 12. Política personalizada

El código llamador puede sustituir las reglas A–F:

```python
policy = GradePolicy(
    bands=(
        GradeBand.create("Excellent", "85"),
        GradeBand.create("Satisfactory", "70"),
        GradeBand.create("Needs Improvement", "0"),
    ),
    passing_score=Decimal("70"),
)
```

La lógica de la calculadora no necesita cambiar cuando cambia la política.

## 13. Estructura del proyecto

```text
02-grade-calculator/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── grade_calculator.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_grade_calculator.py
```

## 14. Ejecutar la demostración determinista

Desde la raíz del repositorio:

```bash
python practical-projects/02-grade-calculator/demo.py
```

Salida esperada:

```text
assessments: 4
weight: 100.00
remaining: 0.00
average: 89.65
letter: B
status: complete
passed: yes
```

## 15. Ejecutar las pruebas

```bash
python -m pytest -q practical-projects/02-grade-calculator/tests
```

La suite inicial cubre validación, aislamiento del contexto decimal, límites de políticas, reglas personalizadas, informes parciales, agregación ponderada exacta, seguridad ante mutaciones, reglas de finalización y formato determinista.

## 16. Rutas de error para inspeccionar manualmente

Prueba:

```python
calculator.add("Quiz", "101", "10")
calculator.add("Quiz", "90", "0")
calculator.add("Project", "90", "100.01")
calculator.final_report()
```

Lee cada excepción y confirma que las evaluaciones rechazadas no cambian la calculadora.

## 17. Nota de diseño: la configuración es dato

Los límites de letras se representan mediante valores `GradeBand` en lugar de una cadena de `if` fija dentro de `GradeCalculator`.

Esto hace que los cambios de política sean explícitos, comprobables e independientes de la lógica de agregación.

## 18. Nota de diseño: incompleto es un estado real

Un curso parcial no es un error. Es un estado válido con promedio actual, peso restante y todavía sin resultado final de aprobación.

Modelar ese estado directamente es más claro que inventar calificaciones para evaluaciones no realizadas.

## 19. Nota de diseño: validar antes de modificar

`add()` crea y valida un `Assessment`, comprueba el peso combinado futuro y solo entonces agrega el registro.

Una operación rechazada deja intacta la colección existente.

## 20. Estrategia de pruebas

Las pruebas se concentran en contratos públicos y límites importantes:

- notas `0.00`, `60.00`, `90.00` y `100.00`;
- exceso de peso por encima de `100.00`;
- finalización exacta en `100.00`;
- comportamiento de curso parcial;
- errores de configuración de políticas;
- comportamiento de políticas personalizadas;
- aislamiento del contexto decimal externo.

## 21. Lo que este proyecto no incluye

Esta versión no incluye:

- cuentas de estudiantes;
- persistencia o base de datos;
- reglas de asistencia;
- eliminación de la nota más baja;
- puntos extra;
- múltiples cursos;
- interfaz gráfica;
- gráficos.

Estas funciones ocultarían la lección central: convertir reglas configurables en contratos de datos y cálculos pequeños y confiables.

## 22. Desafío de extensión: eliminar la nota más baja

Agrega un grupo de evaluaciones donde la nota más baja pueda excluirse antes de la agregación. Define el comportamiento de empates y pesos antes de programar.

## 23. Desafío de extensión: calcular la nota necesaria

Con el peso restante, calcula la nota necesaria en el trabajo pendiente para alcanzar un promedio final objetivo.

Define qué debe ocurrir cuando el objetivo sea matemáticamente imposible.

## 24. Desafío de extensión: múltiples estudiantes

Crea una colección separada que aplique una misma `GradePolicy` a calculadoras de varios estudiantes y produzca un resumen de la clase.

Mantén la identidad del estudiante separada de las reglas de cálculo.

## 25. Desafío de extensión: política de redondeo

Haz configurable el redondeo. Compara redondear cada contribución por separado con redondear solo el promedio ponderado final y documenta las consecuencias.

## 26. Discusión de portafolio

Al presentar este proyecto, explica las decisiones, no solo que “calcula notas”:

- política de calificación configurable;
- registros inmutables y validados;
- normalización exacta de porcentajes;
- agregación ponderada basada en enteros;
- estado parcial frente a final explícito;
- ausencia de mutación tras entradas rechazadas;
- informe estructurado separado de la presentación;
- pruebas automatizadas centradas en límites.

## 27. Lista de revisión

Antes de considerar completa tu implementación, verifica:

- ¿Pueden entrar notas o pesos inválidos en la colección?
- ¿Puede el peso acumulado superar el 100%?
- ¿El informe parcial evita declarar aprobado/reprobado como final?
- ¿El informe final exige exactamente el 100% del peso?
- ¿Los límites de las letras funcionan en los valores exactos?
- ¿Puede suministrarse otra política sin editar la lógica de la calculadora?
- ¿Los cálculos son independientes del contexto decimal externo?
- ¿Las pruebas demuestran rutas de éxito y error?

## 28. Próximo proyecto

El Proyecto 02 añade reglas configurables y agregación ponderada al patrón de la Fase 10.

El siguiente proyecto planificado es **Registro de Usuarios**, centrado en validación de datos similares a identidad, prevención de duplicados, búsquedas y límites de servicio más claros, sin introducir autenticación real ni datos personales.
