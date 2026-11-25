# Entornos virtuales

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-run-your-first-program/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../05-packages-and-dependencies/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Nivel:** principiante absoluto. **Tiempo estimado:** 25–40 minutos. Completa la lección del primer programa. Un entorno virtual es un entorno Python específico de un proyecto. Normalmente mantiene los paquetes externos instalados separados de otros proyectos. No es una máquina virtual, sandbox de seguridad ni copia independiente del sistema operativo.

Imagina dos proyectos que necesitan versiones distintas del mismo paquete. Da a cada uno su entorno en lugar de cambiar el Python del sistema:

```text
workspace/
├── project_a/
│   ├── .venv/
│   └── main.py
└── project_b/
    ├── .venv/
    └── main.py
```

## 1. Crea el entorno dentro del proyecto

Abre la carpeta existente `python-practice` en VS Code o una terminal. Comprueba la carpeta actual con `Get-Location` en PowerShell o `pwd` en macOS/Linux. Crea **un** entorno allí con el intérprete comprobado en el capítulo 01.

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
```

macOS (instalación oficial 3.13):

```bash
python3.13 -m venv .venv
```

Linux (u otra instalación comprobada en macOS):

```bash
python3 -m venv .venv
```

Sustituye el comando del intérprete base comprobado si es distinto. No crees otro entorno dentro de .venv. En Debian/Ubuntu, si la creación falla porque ensurepip no está disponible, instala el paquete venv correspondiente de la distribución (para el intérprete predeterminado, normalmente `sudo apt install python3-venv`) con acceso administrativo autorizado. Para una versión instalada por separado, usa su paquete correspondiente documentado. Nunca sustituyas el Python del sistema.

## 2. Activa y comprueba

La activación cambia la búsqueda de comandos del shell actual. No es obligatoria si llamas directamente al Python del entorno.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Símbolo del sistema Windows (cmd.exe, no PowerShell):

```bat
.venv\Scripts\activate.bat
```

macOS/Linux (bash o zsh):

```bash
source .venv/bin/activate
```

El prompt puede mostrar `(.venv)`, pero comprueba:

```shell
python --version
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip --version
```

El ejecutable y la ubicación de pip deben referirse a la .venv de este proyecto; la comparación debe imprimir True. Usa `python -m pip` con ese intérprete comprobado, no pip solo ni el launcher base. Si PowerShell bloquea scripts, no debilites la política de seguridad; usa el ejecutable directamente:

```powershell
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe first_program.py
```

En macOS/Linux sin activación:

```bash
.venv/bin/python -m pip --version
.venv/bin/python first_program.py
```

## 3. Selecciona .venv en VS Code

Abre Command Palette > **Python: Select Interpreter**. Selecciona el intérprete dentro de la .venv de este proyecto (Windows: .venv/Scripts/python.exe; macOS/Linux: .venv/bin/python). Abre otra terminal integrada y repite la comprobación. Si no se activa automáticamente, actívalo manualmente o usa la ruta directa. Ejecuta tu first_program.py existente con ese intérprete.

## 4. Sal y recrea

En un shell activado, escribe `deactivate`. Cerrar el shell también termina su activación. La carpeta y los paquetes permanecen. No copies ni muevas .venv entre máquinas; recréalo con Python base y el archivo de dependencias. Para recrearlo, cierra las terminales que lo usan, confirma la carpeta exacta y elimina solo el entorno mediante el gestor de archivos; conserva el código y requirements.

Añade `.venv/` al .gitignore de la raíz del proyecto (este repositorio ya ignora .venv). Nunca versiones el entorno generado. Mantén tu código fuera de él. Variables de entorno, binarios de navegador, bibliotecas del SO y servicios pueden estar en otros lugares; venv aísla paquetes Python, no todos los recursos.

## 5. Práctica y resolución de problemas

Crea dos carpetas de práctica separadas, cada una con su .venv. Selecciona y comprueba la ruta de cada ejecutable y ejecuta el primer programa en una. No necesitas descargar paquetes para este ejercicio. Si aparece el intérprete equivocado, reabre la carpeta correcta, selecciona de nuevo y comprueba. Si falta pip, consulta las instrucciones de instalación Python correspondientes; no instales en el Python del sistema como alternativa.

**Referencia rápida:** crear con intérprete base comprobado + `-m venv .venv`; activar o usar ruta directa; comprobar ejecutable y pip; desactivar al terminar. A continuación, aprende a instalar y registrar paquetes.

## Referencias oficiales

- [Python venv](https://docs.python.org/es/3.13/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Entornos en VS Code](https://code.visualstudio.com/docs/python/environments)

<!-- chapter-navigation:bottom -->
[← Anterior](../03-run-your-first-program/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../05-packages-and-dependencies/README.es.md)
<!-- /chapter-navigation:bottom -->
