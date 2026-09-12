# Flujo Simulado de Automatización

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el **Proyecto 08 de la Fase 10: Proyectos Prácticos** y el último proyecto planificado de la fase.

El proyecto modela un pequeño orquestador de automatización con validación real, transiciones de estado, logs, evidencias, propagación de fallos y contratos del resultado final, manteniendo simuladas todas las integraciones externas.

El escenario es original y ficticio. No reproduce ninguna empresa, cliente, sistema, credencial o flujo privado real.

## Qué practicarás

Este proyecto combina conceptos de toda la ruta:

- modelado inmutable con `dataclass`;
- estados controlados con `StrEnum`;
- contratos explícitos de entrada y normalización;
- orquestación determinista;
- planes de ejecución ordenados;
- comportamiento fail-fast;
- logs estructurados de eventos;
- evidencias estructuradas;
- validación de invariantes;
- simulación local pura en lugar de integraciones externas;
- renderizado de texto estable;
- cobertura de regresión con pytest.

## Escenario ficticio

Una solicitud local contiene un identificador y una tupla de elementos ficticios de trabajo:

```python
AutomationRequest(
    request_id="DEMO-001",
    items=("alpha", "beta", "gamma"),
)
```

El orquestador ejecuta cuatro pasos fijos:

```text
prepare
   ↓
process
   ↓
verify
   ↓
finalize
```

Una ejecución exitosa publica los elementos en mayúsculas. Una política controlada de simulación puede forzar el fallo de un paso para demostrar propagación de fallos sin depender de APIs, archivos, credenciales, planificadores o sistemas remotos reales.

## Requisitos

El flujo debe:

1. aceptar solamente un `AutomationRequest` validado;
2. exigir un identificador imprimible y no vacío;
3. exigir una tupla no vacía de elementos imprimibles;
4. eliminar espacios externos del identificador y de los elementos;
5. rechazar elementos duplicados después de la normalización;
6. ejecutar el orden canónico `prepare → process → verify → finalize`;
7. emitir eventos deterministas de `started` y finalización para los pasos ejecutados;
8. producir evidencia estructurada solo para pasos exitosos;
9. permitir inyección determinista de fallo en exactamente un paso seleccionado;
10. detener la ejecución tras un fallo y marcar los pasos posteriores como `skipped`;
11. preservar la evidencia producida antes del fallo;
12. publicar salida solamente cuando toda la ejecución sea exitosa;
13. validar invariantes del resultado incluso cuando los objetos se construyan directamente;
14. renderizar un informe de texto estable sin timestamps, aleatoriedad ni direcciones de memoria.

## Alcance deliberado

El proyecto usa esta regla:

> **Orquestador real, integraciones simuladas.**

El flujo de control es real y comprobable. El mundo externo queda fuera intencionalmente.

Fuera de alcance:

- SAP o cualquier sistema empresarial;
- APIs HTTP;
- credenciales o secretos;
- bases de datos;
- acceso a red;
- automatización por subprocess;
- GUI o RPA;
- threads o `asyncio`;
- planificadores;
- retry y backoff;
- aleatoriedad;
- esperas reales.

Así el objetivo se mantiene en los contratos de orquestación y no en la infraestructura.

## Estructura

```text
08-simulated-automation-flow/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── automation_flow.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_automation_flow.py
```

## Modelo principal

### `AutomationRequest`

Almacena la entrada inmutable y validada:

```python
AutomationRequest("RUN-001", ("alpha", "beta"))
```

El modelo elimina espacios externos, rechaza texto vacío o no imprimible, exige una tupla con al menos un elemento y rechaza duplicados tras normalización.

### `StepName`

El plan canónico es fijo:

```text
PREPARE
PROCESS
VERIFY
FINALIZE
```

Un orden fijo hace deterministas la ejecución y las pruebas.

### `StepStatus`

Cada paso termina en exactamente un estado:

```text
SUCCEEDED
FAILED
SKIPPED
```

Un paso `skipped` no se ejecutó porque un paso anterior falló.

### `RunStatus`

La ejecución completa es:

```text
SUCCEEDED
FAILED
```

El éxito exige que todos los pasos tengan éxito. Un fallo exige exactamente un paso fallido, todos los anteriores exitosos y todos los posteriores omitidos.

### `AutomationEvent`

Los eventos funcionan como log determinista.

En lugar de timestamps, cada evento recibe una secuencia continua:

```text
001 prepare started
002 prepare succeeded
003 process started
004 process succeeded
```

Esto evita que dos ejecuciones idénticas produzcan logs diferentes solo por el reloj.

### `Evidence`

Los pasos exitosos producen evidencia estructurada, por ejemplo:

```text
prepare.input_count=3
process.transformation=uppercase
verify.verification=count-and-uniqueness
finalize.result=ready
```

Los pasos fallidos u omitidos no pueden publicar evidencia.

### `AutomationResult`

El resultado inmutable contiene:

- la solicitud validada original;
- estado final;
- resultados de los cuatro pasos;
- log ordenado de eventos;
- elementos de salida cuando hay éxito.

La propiedad `evidence` expone todas las evidencias exitosas en orden de ejecución.

## Pipeline de automatización

```text
entrada
  ↓
validación de solicitud
  ↓
plan canónico
  ↓
prepare
  ↓
process
  ↓
verify
  ↓
finalize
  ↓
estado + eventos + evidencia + salida
```

Si un paso falla:

```text
pasos anteriores exitosos
           ↓
      paso fallido
           ↓
 pasos restantes omitidos
           ↓
    resultado failed
```

La evidencia previa se conserva, pero la salida no se publica.

## Contrato de procesamiento

En esta simulación educativa, `process` transforma cada elemento a mayúsculas:

```text
alpha -> ALPHA
beta  -> BETA
```

La transformación es simple a propósito. El aprendizaje está en la orquestación alrededor del trabajo.

## Inyección controlada de fallo

`SimulationPolicy` puede seleccionar un paso para fallar:

```python
SimulationPolicy(fail_at=StepName.VERIFY)
```

La política es explícita y determinista. Sustituye fallos aleatorios o timeouts artificiales.

Ejemplo:

```text
prepare   -> succeeded
process   -> succeeded
verify    -> failed
finalize  -> skipped
run       -> failed
```

La evidencia de `prepare` y `process` permanece disponible.

## Ejemplo básico

```python
from automation_flow import AutomationRequest, run_automation

request = AutomationRequest(
    request_id="RUN-001",
    items=("alpha", "beta"),
)

result = run_automation(request)

print(result.status)
print(result.output_items)
```

Salida lógica:

```text
succeeded
('ALPHA', 'BETA')
```

## Demo

Ejecuta desde este directorio:

```bash
python demo.py
```

El demo ejecuta dos escenarios deterministas:

1. una ejecución completa exitosa;
2. un fallo controlado en `verify`.

Es no interactivo, sin red y usa únicamente datos ficticios en memoria.

## Caminos de fallo

La entrada inválida falla antes de comenzar la orquestación:

```python
AutomationRequest("", ("alpha",))
```

lanza `ValueError`.

```python
AutomationRequest("RUN-001", [])
```

lanza `TypeError` porque las listas mutables no se aceptan silenciosamente.

```python
AutomationRequest("RUN-001", (" alpha ", "alpha"))
```

lanza `ValueError` porque la normalización crearía un duplicado.

Un fallo simulado durante la ejecución es diferente de una entrada inválida. Devuelve un `AutomationResult` válido con `RunStatus.FAILED`.

La distinción es importante:

- **contrato inválido** → excepción;
- **solicitud válida con fallo de ejecución** → resultado estructurado de fallo.

## Invariantes del resultado

El propio resultado valida su consistencia.

Se rechazan estados imposibles como:

- éxito con un paso fallido;
- fallo sin exactamente un paso fallido;
- un paso exitoso después del fallo;
- salida publicada por una ejecución fallida;
- orden incorrecto de pasos;
- secuencia de eventos no continua;
- eventos incompatibles con los estados de los pasos;
- evidencia en pasos fallidos u omitidos.

El objetivo es dificultar la representación de estados inválidos.

## Errores comunes

### Usar `print()` como único log

El texto impreso ayuda a las personas, pero es débil como contrato de programa. Guarda eventos estructurados primero y renderízalos después.

### Añadir timestamps reales a un ejercicio determinista

El tiempo crea ruido en pruebas de igualdad. Los números de secuencia muestran orden sin introducir no determinismo.

### Continuar tras un fallo sin una política declarada

Si pasos posteriores dependen de los anteriores, continuar silenciosamente puede producir resultados engañosos. Este proyecto usa fail-fast explícito.

### Perder evidencia anterior

Un fallo no debe borrar lo que ya tuvo éxito. Conservar evidencia hace explicable la ejecución.

### Mezclar validación con fallo de runtime

La entrada incorrecta debe fallar inmediatamente. Una solicitud válida que falla durante la ejecución debe devolver un resultado de fallo estructurado.

### Simular sistemas externos de forma demasiado literal

Credenciales falsas, pantallas SAP falsas, `sleep()` y mocks de red pueden desviar la atención de la lección principal. Este proyecto modela el límite de orquestación en lugar de imitar sistemas externos.

## Pruebas

Ejecuta la suite enfocada desde la raíz del repositorio:

```bash
python -m pytest -q practical-projects/08-simulated-automation-flow/tests
```

La suite inicial cubre normalización, duplicados, fronteras inmutables, éxito determinista, los cuatro puntos de fallo, fail-fast, pasos omitidos, conservación de evidencia, reglas de salida, invariantes, secuencia de eventos, contratos de tipo y renderizado estable.

## Ejercicio

Cambia los elementos del demo a:

```python
("north", "south", "west", "east")
```

Antes de ejecutar, predice:

1. `input_count`;
2. `processed_count`;
3. la tupla final de salida;
4. la cantidad de eventos de una ejecución exitosa.

Luego inyecta un fallo en `PROCESS` y predice qué pasos se omitirán y qué evidencia permanecerá.

## Desafíos de extensión

1. Añade un quinto paso y actualiza las invariantes.
2. Sustituye uppercase por una función pura de procesamiento configurable.
3. Añade una política de retry manteniendo determinista el orden de eventos.
4. Añade duraciones suministradas por un reloj falso.
5. Añade serialización JSON del resultado.
6. Añade otro renderer sin cambiar la orquestación.
7. Evoluciona del flujo lineal a dependencias explícitas entre pasos.

## Discusión para portafolio

Este proyecto muestra cómo modelar automatización como contratos de software en lugar de una secuencia de efectos secundarios improvisados.

Puntos útiles para explicar:

- estado explícito de orquestación;
- modelos inmutables de solicitud y resultado;
- ejecución determinista;
- logs y evidencias estructurados;
- propagación fail-fast;
- semántica de pasos omitidos;
- distinción entre validación y fallo de ejecución;
- diseño orientado a invariantes;
- límites seguros de simulación;
- pruebas de rutas de éxito y fallo.

## Referencia rápida

```text
Entrada:       AutomationRequest
Pasos:         prepare -> process -> verify -> finalize
Procesamiento: transformación a mayúsculas
Estados paso:  succeeded / failed / skipped
Estados run:   succeeded / failed
Logs:          AutomationEvent ordenado
Evidencia:     solo pasos exitosos
Fallo:         SimulationPolicy determinista
Tras fallo:    pasos restantes se omiten
Salida:        se publica solo tras éxito completo
I/O externo:   ninguno
```

## Línea de llegada de la Fase 10

Este es el último proyecto práctico planificado de la Fase 10. Cuando implementación, documentación, CI y ciclo de revisión estén completos, la fase de proyectos prácticos podrá marcarse como completada.
