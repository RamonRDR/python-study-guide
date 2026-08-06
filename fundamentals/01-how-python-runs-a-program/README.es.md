<div align="center">

# Cómo Ejecuta Python un Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md)

Un programa de Python comienza como texto escrito por una persona. Guardar ese texto en un archivo `.py` no lo ejecuta. El programa solo se ejecuta cuando se le pide al intérprete de Python que lea y ejecute el archivo.

Este capítulo te lleva desde un archivo vacío hasta un programa funcional y después muestra cómo modificarlo, volver a ejecutarlo y corregir un error básico de sintaxis.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante absoluto |
| Prerrequisitos | Python instalado; acceso a un editor de texto y a una terminal |
| Tiempo estimado de estudio | 40 a 60 minutos |
| Conceptos principales | Programa, código fuente, archivo `.py`, editor, terminal, intérprete, orden de ejecución, error de sintaxis |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué son un programa y el código fuente;
- identificar la finalidad de un archivo `.py`;
- distinguir un editor, una terminal y el intérprete de Python;
- describir la diferencia entre escribir, guardar y ejecutar código;
- crear y ejecutar un archivo de Python desde la terminal;
- explicar cómo las instrucciones comunes de nivel superior se ejecutan de arriba hacia abajo;
- localizar las partes útiles de un mensaje básico de `SyntaxError`;
- modificar, guardar y volver a ejecutar un programa.

## 1. ¿Qué es un programa?

Un programa es un conjunto de instrucciones que una computadora puede ejecutar.

Una receta de cocina también contiene instrucciones ordenadas, pero una computadora necesita instrucciones escritas en un lenguaje que pueda procesar. En esta guía, ese lenguaje es Python.

Un programa puede contener una instrucción o millones de instrucciones. Tu primer programa contiene solo una:

```python
print("Hello, World!")
```

Esta instrucción le pide a Python que muestre un texto.

## 2. ¿Qué es el código fuente?

El **código fuente** es el texto legible por personas que se usa para describir un programa.

El siguiente texto es código fuente de Python:

```python
print("Hello, World!")
```

El código fuente no es una captura de pantalla, un documento con formato ni el resultado mostrado por el programa. Es el texto que escribes y guardas para que una implementación del lenguaje pueda procesarlo.

## 3. ¿Qué es un archivo `.py`?

Un archivo que termina en `.py` se usa habitualmente para almacenar código fuente de Python.

Por ejemplo:

```text
hello_world.py
```

El nombre tiene dos partes:

- `hello_world` es el nombre del archivo;
- `.py` es la extensión asociada a los archivos de código fuente de Python.

La extensión ayuda a las personas y a las herramientas a reconocer el tipo de archivo. No ejecuta el archivo por sí sola.

## 4. Editor, terminal e intérprete tienen funciones diferentes

Estas tres herramientas suelen aparecer en la misma pantalla, pero no son lo mismo.

| Herramienta | Función principal |
|---|---|
| Editor | Escribir y modificar el código fuente |
| Terminal | Introducir comandos y ver la salida de los comandos |
| Intérprete de Python | Leer código de Python y ejecutarlo |

Un editor puede incluir una terminal integrada. Una terminal puede iniciar el intérprete de Python. Las herramientas pueden trabajar juntas sin convertirse en la misma herramienta.

## 5. Escribir, guardar y ejecutar son acciones separadas

Una persona principiante suele realizar estas acciones rápidamente y asumir que son un solo paso. En realidad, son tres:

1. **Escribir:** introducir o modificar el código fuente en el editor.
2. **Guardar:** almacenar el texto actual en un archivo.
3. **Ejecutar:** pedirle al intérprete de Python que ejecute el archivo guardado.

Si modificas el contenido en el editor, pero no lo guardas, el intérprete normalmente ejecutará la versión guardada anteriormente. El texto sin guardar todavía existe solo en el editor.

## 6. Crea `hello_world.py`

Abre un editor de texto plano o un editor de código y crea un archivo nuevo llamado:

```text
hello_world.py
```

Escribe exactamente este código:

```python
print("Hello, World!")
```

Usa comillas rectas normales (`"`), no comillas decorativas como `“` y `”`.

Guarda el archivo en una carpeta que puedas encontrar de nuevo.

## 7. Abre la terminal en la carpeta del archivo

La terminal trabaja con un **directorio actual**, que es la carpeta donde se ejecutan los comandos.

Antes de ejecutar el programa, comprueba que la terminal esté en la carpeta que contiene `hello_world.py`.

Muchos editores ofrecen un comando como **Abrir en la terminal integrada**. También puedes abrir una terminal del sistema y navegar hasta la carpeta.

Para ver los archivos de la carpeta actual, un comando habitual es:

```text
dir
```

en Windows, o:

```text
ls
```

en macOS y Linux.

Deberías ver `hello_world.py` en el resultado.

## 8. Ejecuta el archivo

Ejecuta:

```bash
python hello_world.py
```

Dependiendo de cómo se instaló Python, el comando puede ser:

```bash
python3 hello_world.py
```

o, en algunas instalaciones de Windows:

```bash
py hello_world.py
```

La salida esperada es:

```text
Hello, World!
```

La salida no forma parte del archivo de código fuente. Se produce cuando se ejecuta el programa.

## 9. ¿Qué sucede después del comando?

Para este comando:

```bash
python hello_world.py
```

una ruta de ejecución simplificada es:

1. la terminal recibe el comando;
2. el sistema operativo inicia el intérprete de Python;
3. el intérprete abre `hello_world.py`;
4. Python comprueba si el código fuente sigue la gramática del lenguaje;
5. Python ejecuta en orden las instrucciones de nivel superior del programa;
6. `print()` envía texto a la salida estándar del programa;
7. el intérprete finaliza porque no quedan instrucciones.

Las implementaciones de Python realizan trabajo interno que esta descripción para principiantes no muestra. No necesitas entender bytecode ni máquinas virtuales para crear y ejecutar tus primeros scripts.

## 10. Las instrucciones de nivel superior normalmente se ejecutan de arriba hacia abajo

Considera este archivo:

```python
print("First")
print("Second")
print("Third")
```

Su salida es:

```text
First
Second
Third
```

Los efectos visibles ocurren en el mismo orden que las instrucciones de nivel superior.

Los capítulos posteriores introducirán condiciones, bucles, funciones, excepciones e importaciones. Esos recursos pueden repetir, omitir, posponer o redirigir la ejecución. Para un archivo simple con llamadas consecutivas a `print()`, el modelo correcto es de arriba hacia abajo.

## 11. Un archivo es diferente del modo interactivo

Ejecutar un archivo:

```bash
python hello_world.py
```

le pide a Python que ejecute el script guardado.

Ejecutar Python sin indicar un archivo:

```bash
python
```

normalmente abre el intérprete interactivo y muestra un indicador como:

```text
>>>
```

El modo interactivo es útil para pequeños experimentos. Un archivo `.py` es mejor cuando quieres guardar, revisar, volver a ejecutar, compartir o versionar el programa.

Para salir del modo interactivo, usa `exit()` o el atajo de salida que muestre tu terminal.

## 12. Modifica y vuelve a ejecutar el programa

Cambia el archivo a:

```python
print("Hello, World!")
print("I changed my first program.")
```

Después:

1. guarda el archivo;
2. vuelve a la terminal;
3. ejecuta nuevamente el mismo comando.

```bash
python hello_world.py
```

Salida esperada:

```text
Hello, World!
I changed my first program.
```

Python no usa automáticamente el contenido sin guardar del editor. Guarda antes de volver a ejecutar.

## 13. ¿Qué es un error de sintaxis?

El código fuente de Python debe seguir la gramática del lenguaje. Un **error de sintaxis** significa que Python no pudo entender la estructura del programa lo suficiente como para ejecutarlo.

Por ejemplo, a esta línea le falta la comilla de cierre:

```python
print("Hello, World!)
```

Cuando Python lee el archivo, se detiene antes de ejecutar el programa e informa un `SyntaxError`.

Un mensaje de error simplificado puede verse así:

```text
  File "hello_world.py", line 1
    print("Hello, World!)
          ^
SyntaxError: unterminated string literal
```

El texto exacto, la ruta y la posición del signo pueden variar según la versión de Python y el entorno.

## 14. Lee un mensaje básico de error desde abajo hacia arriba

Para un error básico de sintaxis, examina estas partes:

1. **Tipo y mensaje del error:** la última línea indica `SyntaxError` y describe el problema.
2. **Archivo y línea:** Python identifica el archivo y una línea aproximada donde falló el análisis.
3. **Fragmento del código fuente:** Python muestra la línea relevante.
4. **Signo (`^`):** apunta cerca del lugar donde Python detectó que algo estaba mal.

La posición de detección no siempre es la causa original. Un símbolo ausente antes, en la misma línea o en una línea anterior, puede hacer que Python se queje más tarde.

Corrige el primer error de sintaxis informado, guarda el archivo y vuelve a ejecutarlo.

## 15. Corrige el programa

Restaura la comilla que falta:

```python
print("Hello, World!")
```

Guarda el archivo y ejecuta:

```bash
python hello_world.py
```

El programa debería mostrar:

```text
Hello, World!
```

Los errores forman parte de la programación. El hábito útil no es evitar todos los errores, sino leer la evidencia, cambiar una causa y probar de nuevo.

## 16. Problemas comunes del primer programa

### El comando no encuentra Python

Prueba el comando usado por tu instalación: `python`, `python3` o `py`. Si ninguno funciona, es posible que Python no esté instalado o no esté disponible en la ruta de búsqueda de comandos de la terminal.

### Python no puede abrir el archivo

La terminal puede estar en el directorio equivocado o el nombre del archivo puede ser diferente. Comprueba la carpeta actual y la escritura del nombre.

### La salida no cambió

Guarda el archivo antes de ejecutarlo de nuevo. Confirma también que estás editando y ejecutando el mismo archivo.

### El archivo en realidad es `hello_world.py.txt`

Algunos sistemas ocultan extensiones conocidas. Comprueba el nombre completo en el editor o en las propiedades del archivo.

### Las comillas parecen curvas

Sustituye las comillas decorativas por comillas rectas ASCII.

### El editor muestra un botón de ejecución

Ese botón puede ser práctico, pero aprende también el comando de la terminal. Así resulta más fácil distinguir editor, terminal, intérprete, archivo y directorio actual.

## 17. Ejercicio práctico

Crea un archivo nuevo llamado:

```text
first_steps.py
```

Añade estas instrucciones:

```python
print("Python is running.")
print("I wrote this program.")
print("I saved the file.")
print("I ran it from the terminal.")
```

Completa la secuencia:

1. guarda el archivo;
2. ejecútalo desde la terminal;
3. confirma que las cuatro líneas aparecen en orden;
4. cambia la tercera instrucción por:

```python
print("I changed the program.")
```

5. guarda y vuelve a ejecutar el archivo;
6. elimina deliberadamente la comilla final de la última instrucción;
7. guarda y ejecuta el archivo;
8. identifica el nombre del archivo, el número de línea, el tipo y el mensaje del error;
9. restaura la comilla;
10. guarda y ejecuta el programa corregido.

Tu programa final debe ejecutarse sin errores de sintaxis y mostrar cuatro líneas.

## 18. Autoevaluación

Estás preparado para el siguiente capítulo cuando puedas responder estas preguntas:

- ¿Cuál es la diferencia entre código fuente y salida del programa?
- ¿Por qué cambiar texto en un editor no cambia necesariamente la siguiente ejecución?
- ¿Qué herramienta recibe `python hello_world.py`?
- ¿Qué herramienta entiende el código fuente de Python?
- ¿En qué orden se ejecutan las instrucciones simples de `print()` de nivel superior?
- ¿Qué parte de un mensaje básico de error identifica el tipo de error?
- ¿Qué debes hacer después de corregir el código fuente?

## 19. Resumen de consulta rápida

| Situación | Acción |
|---|---|
| Escribir código | Usa un editor de texto plano o de código |
| Almacenar los cambios actuales | Guarda el archivo `.py` |
| Ejecutar un script | `python file_name.py` |
| Comandos alternativos | `python3 file_name.py` o `py file_name.py` |
| Experimentar de forma interactiva | Ejecuta `python` sin indicar un archivo |
| La salida no se actualizó | Guarda y confirma el archivo ejecutado |
| No se encontró el archivo | Comprueba el directorio y el nombre |
| Error de sintaxis | Lee la última línea, el archivo, la línea, el fragmento y el `^` |
| Después de una corrección | Guarda y vuelve a ejecutar |
| Orden de ejecución simple | Las instrucciones de nivel superior se ejecutan en orden, normalmente de arriba hacia abajo |

## 20. Ejecuta el ejemplo del repositorio

Desde la raíz del repositorio:

```bash
python fundamentals/01-how-python-runs-a-program/examples/hello_world.py
```

Salida esperada:

```text
Hello, World!
```

## 21. Ejecuta las comprobaciones del repositorio

Desde la raíz del repositorio:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## Referencias oficiales

- [Tutorial de Python — Usando el intérprete de Python](https://docs.python.org/es/3/tutorial/interpreter.html)
- [Tutorial de Python — Errores de sintaxis](https://docs.python.org/es/3/tutorial/errors.html#errores-de-sintaxis)
- [Documentación de Python — Línea de comandos y entorno](https://docs.python.org/es/3/using/cmdline.html)

[← Volver al índice de la sección](../README.es.md)
