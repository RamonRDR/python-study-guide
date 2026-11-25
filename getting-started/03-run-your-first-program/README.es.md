# Ejecutar tu primer programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-configure-vscode/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-virtual-environments/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo y requisitos previos

**Nivel:** principiante absoluto. **Tiempo estimado:** 15–25 minutos. Python instalado y comando comprobado; carpeta de práctica abierta en el editor. Vas a escribir, guardar, ejecutar, modificar y ejecutar de nuevo un archivo manualmente. Fundamentos explicará el significado del código con más detalle.

## 1. Crea un archivo Python

En Explorer de VS Code, elige New File y nómbralo `first_program.py` dentro de `python-practice`. Alternativamente, usa un editor de texto plano y guárdalo con ese nombre exacto. Asegúrate de que la extensión sea .py, no .py.txt. Escribe tú mismo el código:

```python
print("Python is ready!")
```

Guarda con `Ctrl+S` (Windows/Linux) o `Cmd+S` (macOS). Usa comillas rectas, no comillas tipográficas. Guardar no ejecuta el programa.

## 2. Ejecuta desde la terminal

Abre la terminal integrada o la terminal del sistema. Comprueba que estás en la carpeta de práctica. En Windows PowerShell, usa `Get-Location` y `Get-ChildItem`; en macOS/Linux, usa `pwd` y `ls`. El archivo debe aparecer en la lista. Si es necesario, usa `cd` seguido de la ruta entre comillas a tu carpeta, sustituyéndola por tu propia ruta.

Ejecuta con el comando del intérprete comprobado anteriormente:

Windows:

```powershell
py -3.13 first_program.py
```

macOS (instalación oficial 3.13):

```bash
python3.13 first_program.py
```

Linux (u otra instalación Python 3 comprobada en macOS):

```bash
python3 first_program.py
```

Si comprobaste otro comando, sustitúyelo manteniendo el nombre del archivo. Salida esperada:

```text
Python is ready!
```

También puedes usar la acción **Run Python File in Terminal** de la extensión Python en VS Code. Ejecuta el archivo con el intérprete seleccionado. Prefiere escribir el comando de terminal al menos una vez para entender cómo comienza la ejecución.

## 3. Modifica y repite

Cambia el mensaje a `My first program!`, guarda y ejecuta de nuevo con el mismo comando. Predice la salida antes de ejecutar. Escribir, guardar y ejecutar son acciones independientes. No necesitas cuenta Git, conexión a internet, paquete externo ni asistente de IA para ejecutar este ejemplo una vez instalado Python.

## 4. Resolución de problemas

| Síntoma | Acción |
| --- | --- |
| Can't open file / No such file | Comprueba carpeta actual y nombre exacto; usa comillas para rutas con espacios. |
| La salida no cambió | Guarda el archivo y comprueba que ejecutaste el archivo deseado. |
| `SyntaxError` | Comprueba pares de comillas y paréntesis; lee la línea indicada. |
| Comando no encontrado | Regresa a la comprobación del intérprete; no escribas comandos del shell en el prompt Python `>>>`. |
| La terminal muestra `>>>` | Escribe `exit()` y vuelve al shell antes de ejecutar el archivo. |

## Práctica y lista de finalización

- [ ] Creé y guardé un archivo .py por mi cuenta.
- [ ] Puedo localizarlo en la carpeta actual de la terminal.
- [ ] Lo ejecuté con un intérprete comprobado y vi la salida esperada.
- [ ] Modifiqué el mensaje, predije el resultado y ejecuté de nuevo.

Para comparar, el repositorio incluye [el mismo ejemplo original](examples/first_program.py). Desde la raíz del repositorio, ejecútalo con tu intérprete comprobado seguido de `getting-started/03-run-your-first-program/examples/first_program.py`. Este archivo no es necesario para completar el ejercicio manual.

## Siguiente paso

Continúa con [Entornos virtuales](../04-virtual-environments/README.es.md) para aislar las dependencias del proyecto. La lección conceptual [Cómo Python ejecuta un programa](../../fundamentals/01-how-python-runs-a-program/README.es.md) sigue al módulo introductorio.

## Referencias oficiales

- [Uso del intérprete Python](https://docs.python.org/3.13/tutorial/interpreter.html)
- [Ejecución de Python en VS Code](https://code.visualstudio.com/docs/python/run)

<!-- chapter-navigation:bottom -->
[← Anterior](../02-configure-vscode/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../04-virtual-environments/README.es.md)
<!-- /chapter-navigation:bottom -->
