# Instalar Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[Índice del módulo](../README.es.md) · [Siguiente →](../02-configure-vscode/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo y requisitos previos

**Nivel:** principiante absoluto. **Tiempo estimado:** 20–40 minutos, sin contar descargas. Necesitas un sistema de escritorio compatible y permiso para instalar software. Terminarás con un comando de terminal que identifica Python y su ejecutable.

Python es el lenguaje; el intérprete es la aplicación que ejecuta código Python. Descargar solo un editor no instala el intérprete. Usa fuentes oficiales, no anuncios de descargas de terceros. Esta guía prueba Python 3.13 en CI. Prefiere una versión de corrección 3.13 con soporte para mantener la coherencia; otra versión compatible de Python 3 puede ejecutar este ejercicio introductorio, pero los capítulos y dependencias posteriores pueden diferir.

## 1. Comprueba antes de instalar

Abre PowerShell en Windows, Terminal en macOS o una terminal en Linux. Escribe el comando y pulsa Enter. No escribas símbolos del prompt como `PS>` o `$`.

Windows:

```powershell
py -3.13 --version
```

macOS o Linux:

```bash
python3 --version
```

Si ya tienes la versión deseada, omite la instalación. Si falta el comando o la versión difiere, sigue las instrucciones de tu sistema. Una versión como `Python 3.13.x` es ilustrativa; el último número identifica la versión de corrección.

## 2. Windows

Abre la [página oficial de descargas de Python](https://www.python.org/downloads/). Elige el gestor de instalación de Python para Windows en un sistema compatible, instálalo y sigue sus indicaciones de configuración. Abre una nueva ventana de PowerShell. Con el gestor instalado, ejecuta:

```powershell
py install 3.13
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

El segundo comando informa la versión; el tercero muestra la ruta real del intérprete. En una máquina con un instalador tradicional anterior, `py -3.13` puede funcionar sin el gestor. Si utilizas un instalador tradicional oficial que ofrece **Add Python to PATH**, selecciona la opción antes de instalar para facilitar la búsqueda de comandos. No instales una versión antigua insegura solo por esa opción. Si el launcher existente no reconoce `py install`, consulta la guía de resolución de problemas del gestor antes de modificarlo.

`PATH` es una lista de directorios en los que el shell busca comandos. El launcher puede elegir una versión instalada concreta aunque `python` se refiera a otra. Sigue usando el comando comprobado.

## 3. macOS

Descarga el instalador macOS de una versión 3.13 con soporte desde [Python.org](https://www.python.org/downloads/), compatible con el sistema y la arquitectura. Abre el instalador, sigue los pasos y, cuando lo proporcione, ejecuta `Install Certificates.command` desde la carpeta de la aplicación Python instalada para completar la configuración de certificados. Abre una nueva ventana de Terminal:

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

Si utilizas otra instalación compatible, su comando puede ser `python3`. Comprueba versión y ruta. No sustituyas ni elimines el Python del sistema operativo.

## 4. Linux

Muchas distribuciones ya incluyen Python. Comprueba primero `python3 --version`. Si falta, utiliza el gestor de paquetes oficial de tu distribución. Para Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3
```

Para Fedora (si no está instalado):

```bash
sudo dnf install python3
```

Usa comandos administrativos solo en una máquina que tengas autorización para administrar. Confirma:

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

La distribución puede ofrecer otra versión compatible de Python 3. Si no es 3.13, consulta opciones documentadas de instalación paralela o al administrador; no sustituyas el intérprete del sistema, cambies enlaces simbólicos del sistema ni ejecutes instaladores no fiables. Si existe un `python3.13` independiente, compruébalo y úsalo. El primer programa funciona en versiones compatibles de Python 3; ejemplos posteriores pueden necesitar la versión probada por la guía.

## 5. Resolución de problemas

| Síntoma | Qué comprobar |
| --- | --- |
| Comando no encontrado | Reabre la terminal; verifica la instalación y el comando del sistema. |
| Windows abre una tienda u otro Python | Usa `py -3.13 --version`; consulta la resolución oficial de alias/launcher si falla. |
| Versión distinta de la esperada | Comprueba la ruta del ejecutable; elige el intérprete deseado en vez de reinstalar a ciegas. |
| Aparece `>>>` | Entraste en el prompt interactivo de Python. Escribe `exit()` y pulsa Enter para regresar al shell. |
| Fallo de permisos o instalación | Consulta instrucciones oficiales o al administrador; nunca eludas controles de seguridad. |

## Práctica y referencia rápida

Ejecuta las comprobaciones de versión y ruta en tu sistema y anota el resultado. Explica con tus palabras qué hace el intérprete. Conserva el comando verificado para las siguientes lecciones. No necesitas instalar paquetes para este módulo.

## Referencias oficiales

- [Descargas Python](https://www.python.org/downloads/)
- [Gestor de instalación y resolución de problemas en Windows](https://docs.python.org/3.14/using/windows.html)
- [Instalación y launcher Python 3.13 en Windows](https://docs.python.org/3.13/using/windows.html)
- [Python 3.13 en macOS](https://docs.python.org/3.13/using/mac.html)
- [Configuración Python en Ubuntu](https://documentation.ubuntu.com/ubuntu-for-developers/howto/python-setup/)
- [Python en Fedora](https://developer.fedoraproject.org/tech/languages/python/python-installation.html)

<!-- chapter-navigation:bottom -->
[Índice del módulo](../README.es.md) · [Siguiente →](../02-configure-vscode/README.es.md)
<!-- /chapter-navigation:bottom -->
