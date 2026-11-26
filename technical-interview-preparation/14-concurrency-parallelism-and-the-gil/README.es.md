# Concurrencia, paralelismo y GIL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../13-context-managers/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../15-exceptions-testing-and-debugging-review/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [technical-interview-preparation/10-python-memory-management](../../technical-interview-preparation/10-python-memory-management/README.es.md)
- [technical-interview-preparation/13-context-managers](../../technical-interview-preparation/13-context-managers/README.es.md)

## Concurrencia y paralelismo

Concurrencia significa que varias tareas pueden progresar en períodos superpuestos; paralelismo significa ejecutar trabajo simultáneamente. Trabajo I/O-bound espera principalmente entrada/salida; CPU-bound dedica tiempo a computar. Los hilos comparten memoria del proceso; los procesos normalmente tienen espacios de direcciones separados y requieren comunicación o serialización. Asyncio usa planificación cooperativa de corrutinas: `async def` crea función corrutina, llamarla produce objeto corrutina, y `await` puede suspenderla para que otra tarea planificada ejecute. Trabajo síncrono bloqueante puede detener el event loop.

## GIL en Python 3.13

En builds convencionales CPython, global interpreter lock (GIL) permite solo un hilo a la vez ejecutar bytecode Python en el mismo intérprete. I/O y algunas extensiones nativas lo liberan, así que hilos pueden solapar espera y trabajo nativo. No hace atómicas operaciones compuestas de la aplicación ni garantiza ausencia de carreras. CPython 3.13 también ofrece build experimental free-threaded; código compatible puede ejecutar hilos Python en paralelo, y algunas extensiones pueden reactivar GIL. Depende de implementación/build, no es garantía del lenguaje Python.

| Enfoque | Buen punto de partida | Compromiso |
| --- | --- | --- |
| Hilos | I/O bloqueante con colaboradores thread-safe | Sincronización de estado compartido |
| Procesos | Cómputo pesado en Python puro | Inicio, memoria, serialización |
| Asyncio | Muchas operaciones I/O cooperativas | APIs async y cancelación |

Mide cargas antes de elegir; trabajo secuencial pequeño puede añadir sobrecarga sin beneficio.

## Ejemplo de estado compartido

Una condición de carrera ocurre cuando comportamiento depende de intercalación no sincronizada. Ejemplo compartido usa `Lock` con gestor de contexto alrededor de incremento lectura-modificación-escritura. Espera todos futures y propaga excepciones de workers con result. No se comprueba orden de hilos. Locks protegen invariante elegido, no accesos externos arbitrarios; evita mantener locks durante I/O lento y adquiere varios locks en orden consistente para reducir riesgo de interbloqueo.

## Práctica

Ejecuta cuatro workers con 250 actualizaciones cada uno; total esperado 1000. Prueba cero actualizaciones y conteos inválidos. Explica por qué observar resultado correcto sin lock no demuestra seguridad y por qué contador protegido demuestra corrección, no benchmark de velocidad. Usa Python 3.13 local; soporte de hilos y procesos en navegador no se presupone ni verifica.

**Referencia rápida:** concurrencia solapa; paralelismo simultáneo; GIL depende del build; sincroniza invariantes compartidos; elige por carga.

## Ejemplo ejecutable compartido

[safe_counter.py](examples/safe_counter.py)

`python technical-interview-preparation/14-concurrency-parallelism-and-the-gil/examples/safe_counter.py`

## Referencias oficiales (Python 3.13)

- [Python 3.13: library/threading.html](https://docs.python.org/3.13/library/threading.html)
- [Python 3.13: howto/free-threading-python.html](https://docs.python.org/3.13/howto/free-threading-python.html)
- [Python 3.13: library/concurrent.futures.html](https://docs.python.org/3.13/library/concurrent.futures.html)
- [Python 3.13: library/asyncio-task.html](https://docs.python.org/3.13/library/asyncio-task.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../13-context-managers/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../15-exceptions-testing-and-debugging-review/README.es.md)
<!-- /chapter-navigation:bottom -->
