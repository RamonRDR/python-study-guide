# Configurar VS Code

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../01-install-python/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../03-run-your-first-program/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo y requisitos previos

**Nivel:** principiante absoluto. **Tiempo estimado:** 20–30 minutos, sin contar descargas. Completa la lección anterior y conserva el comando Python comprobado. VS Code es un editor de código de escritorio gratuito. Su extensión Python ayuda al editor a comunicarse con el intérprete; no sustituye al intérprete. Puedes usar otro editor de texto plano y una terminal. No necesitas cuenta, herramienta de IA ni paquete adicional.

## 1. Instala Visual Studio Code

Usa la [página oficial de descarga de VS Code](https://code.visualstudio.com/download). Elige la versión para tu sistema y arquitectura.

- **Windows:** descarga el User Installer, ábrelo y sigue las instrucciones. Añadir VS Code a PATH, si se ofrece, es opcional en esta guía; habilita el comando independiente `code`.
- **macOS:** descarga la versión adecuada, abre el archivo descargado si es necesario y mueve Visual Studio Code a Aplicaciones.
- **Linux:** elige el paquete compatible con tu distribución (por ejemplo, .deb para Debian/Ubuntu o .rpm para Fedora). Sigue las instrucciones oficiales de configuración para Linux, incluidos los pasos necesarios del gestor de paquetes.

No uses descargas no oficiales ni concedas privilegios administrativos innecesariamente. Abre VS Code tras instalarlo.

## 2. Instala la extensión Python

1. Abre la vista Extensions en la barra de actividades (icono formado por cuadrados).
2. Busca **Python**.
3. Elige la extensión publicada por **Microsoft** (identificador `ms-python.python`) y pulsa Install.
4. Sigue las indicaciones de reinicio/recarga si son necesarias. Pueden instalarse extensiones complementarias automáticamente; no necesitas extensión de IA independiente.

## 3. Abre una carpeta de estudio

Crea una carpeta vacía llamada `python-practice` en una ubicación personal con permisos de escritura, usando el gestor de archivos del sistema. En VS Code, elige **File > Open Folder** y selecciónala. Este es tu espacio de trabajo, no el directorio de instalación de Python. Si Workspace Trust pregunta por la carpeta, confía en ella solo si la creaste o entiendes su contenido; no confíes automáticamente en código descargado desconocido.

## 4. Selecciona el intérprete

Abre la Command Palette con `Ctrl+Shift+P` (Windows/Linux) o `Cmd+Shift+P` (macOS). Busca **Python: Select Interpreter** y selecciona el intérprete instalado que comprobaste antes. Si es necesario, elige Enter interpreter path y localiza el ejecutable indicado en la lección anterior. La versión mostrada en el editor debe corresponder al Python deseado. Si ya usas un entorno virtual, selecciona su intérprete deliberadamente; no necesitas crear otro entorno para esta lección.

## 5. Comprueba en la terminal integrada

Elige **Terminal > New Terminal**. La terminal permite escribir comandos del shell y ver su salida. Usa el mismo comando comprobado antes:

Windows:

```powershell
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

macOS (instalación oficial 3.13):

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

Linux (u otra instalación Python 3 comprobada en macOS):

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

Si comprobaste otro comando, úsalo. Compara el ejecutable con el intérprete seleccionado en VS Code. Seleccionar un intérprete controla las acciones de la extensión, pero un comando del shell aún puede elegir otro Python instalado. Cierra y reabre la terminal integrada tras cambiar el intérprete; si las rutas siguen siendo distintas, elige el comando comprobado adecuado o usa la ruta del ejecutable seleccionado.

## 6. Resolución de problemas

| Síntoma | Acción |
| --- | --- |
| Python funciona solo fuera de VS Code | Reinicia VS Code completamente para heredar el entorno actualizado. |
| Python: Select Interpreter no aparece | Comprueba que la extensión Python de Microsoft esté instalada y habilitada. |
| Intérprete incorrecto | Selecciona el ejecutable deseado y compara de nuevo la ruta. |
| No puedes guardar | Abre una carpeta personal con permisos de escritura; no trabajes dentro de la instalación Python. |
| Interfaz o idioma distinto | Usa la Command Palette y busca el comando traducido equivalente. |

## Práctica y referencia rápida

Abre la carpeta de práctica, localiza Explorer y terminal integrada, selecciona el intérprete y comprueba versión y ruta. Explica la diferencia entre editor, intérprete y terminal. Deja la carpeta abierta para la próxima lección.

## Referencias oficiales

- [Descargas VS Code](https://code.visualstudio.com/download)
- [Instalación VS Code](https://code.visualstudio.com/docs/getstarted/overview)
- [Configuración VS Code en Linux](https://code.visualstudio.com/docs/setup/linux)
- [Tutorial Python en VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Entornos Python en VS Code](https://code.visualstudio.com/docs/python/environments)
- [Extensión Python de Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<!-- chapter-navigation:bottom -->
[← Anterior](../01-install-python/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../03-run-your-first-program/README.es.md)
<!-- /chapter-navigation:bottom -->
