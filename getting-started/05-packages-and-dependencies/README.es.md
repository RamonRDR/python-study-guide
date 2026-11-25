# Paquetes y gestión de dependencias

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../04-virtual-environments/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../../fundamentals/01-how-python-runs-a-program/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Nivel:** principiante absoluto. **Tiempo estimado:** 30–45 minutos. Usa el entorno creado en el capítulo 04. Una dependencia es software que tu proyecto necesita para funcionar. Python ya ofrece una biblioteca estándar (por ejemplo, pathlib); los paquetes externos se instalan por separado. pip es el instalador de paquetes Python y normalmente obtiene paquetes de Python Package Index (PyPI). Instala solo lo necesario.

## 1. Instala un paquete

Activa la .venv del proyecto y comprueba que `python -m pip --version` apunte a ella. Si no puedes activar, sustituye python por el ejecutable directo indicado en el capítulo 04 en todos los comandos siguientes. Con acceso a internet, instala el paquete oficial Requests:

```shell
python -m pip install requests
python -m pip show requests
python -m pip list
python -m pip check
```

pip también puede instalar dependencias de Requests. El comando check detecta requisitos instalados incoherentes; no demuestra la seguridad del paquete. Comprueba nombre exacto, publicador, documentación oficial y versión Python compatible antes de instalar. Evita comandos no fiables, instalación global y sudo pip.

Crea `check_package.py` junto a first_program.py (no dentro de .venv):

```python
from importlib.metadata import version

print(version("requests"))
```

Ejecuta `python check_package.py`. Debe mostrar la versión instalada (el número varía). No realiza una petición HTTP. Estudiarás imports y HTTP más adelante. El nombre de instalación no siempre es el nombre importado en el código (beautifulsoup4 usa bs4, por ejemplo).

## 2. Registra dependencias

Desde el entorno de práctica limpio, captura las versiones instaladas en un archivo nuevo:

```shell
python -m pip freeze > requirements.txt
```

Esto sobrescribe requirements.txt; revísalo antes de versionar. En Windows PowerShell 5.1 usa `python -m pip freeze | Out-File -Encoding ascii requirements.txt` para esta lista ASCII simple, evitando salida UTF-16. No sobrescribas a ciegas un contrato mantenido manualmente. freeze registra versiones instaladas, incluidas dependencias indirectas; no es un lockfile multiplataforma completo. Registra la versión Python por separado. No incluyas URLs privadas de paquetes, secretos ni rutas de la máquina.

Un proyecto puede mantener requirements.txt con solo dependencias directas y rangos de versiones compatibles, y resolver o fijar el conjunto completo con herramientas adecuadas. El [requirements-external.txt](../../requirements-external.txt) de la guía es un contrato separado y mantenido para los ejemplos existentes; no lo sustituyas por el freeze de práctica.

## 3. Recrea y compara

Sal del shell activado con deactivate. Crea una segunda carpeta de práctica mediante el gestor de archivos. Copia solo código fuente y requirements.txt, no .venv. Abre la carpeta, crea y activa su propio entorno según el capítulo 04 con la misma versión Python, comprueba el ejecutable e instala:

```shell
python -m pip install -r requirements.txt
python -m pip check
python check_package.py
```

Compara las versiones mostradas en ambos entornos. Esto demuestra recreación en tu máquina; la compatibilidad puede variar con otro SO o versión Python. Para eliminar, usa `python -m pip uninstall requests` solo en el entorno deseado; las dependencias no se eliminan automáticamente. No desinstales de un proyecto real solo para practicar.

## 4. Mapa de bibliotecas

| Paquete | Finalidad | Guía |
| --- | --- | --- |
| `pandas` | Análisis de datos | [Capítulo](../../external-libraries/01-pandas/README.es.md) |
| `openpyxl` | Automatización de archivos Excel | [Capítulo](../../external-libraries/02-openpyxl/README.es.md) |
| `requests` | HTTP y APIs | [Capítulo](../../external-libraries/03-requests/README.es.md) |
| `pytest` | Pruebas automatizadas | [Capítulo](../../external-libraries/04-pytest/README.es.md) |
| `numpy` | Arrays numéricos | Candidato futuro |
| `playwright` | Automatización de navegadores | Candidato futuro |
| `selenium` | Automatización de navegadores | Candidato futuro |
| `beautifulsoup4` | Análisis de HTML | Candidato futuro |
| `httpx` | Clientes HTTP, incluso asíncronos | Candidato futuro |
| `fastapi` | Desarrollo de APIs | Candidato futuro |
| `pydantic` | Validación de datos | Candidato futuro |
| `sqlalchemy` | Acceso a bases de datos y ORM | Candidato futuro |
| `matplotlib` | Visualización de datos | Candidato futuro |
| `python-dotenv` | Lectura de configuración de archivos .env | Candidato futuro |

Los cuatro capítulos existentes son el currículo probado. Los demás son candidatos a futuras lecciones, no instalaciones obligatorias ni contratos probados. Algunos necesitan recursos adicionales: Playwright, por ejemplo, descarga binarios de navegadores aparte del paquete Python. Para un experimento opcional y autorizado en un entorno separado, la [guía oficial de la biblioteca](https://playwright.dev/python/docs/library) describe:

```shell
python -m pip install playwright
python -m playwright install chromium
```

Las descargas de navegadores requieren red, almacenamiento y a veces dependencias del SO. Pueden almacenarse en caché fuera de .venv. No ejecutes esto para el ejercicio obligatorio ni añadas Playwright al archivo de dependencias del repositorio solo porque aparece aquí.

## 5. Práctica y referencia rápida

- [ ] Comprobar intérprete activo y ubicación de pip.
- [ ] Instalar Requests en el entorno de práctica y comprobar versión.
- [ ] Guardar requirements.txt y recrear entorno en una segunda carpeta.
- [ ] Explicar por qué se versionan código y requirements pero no .venv.

Si falla la instalación, lee el error, comprueba compatibilidad Python y acceso a internet y verifica el entorno. No eludas comprobaciones de certificados o seguridad. Si falla un import, compara los intérpretes usados para instalar y ejecutar.

**Referencia rápida:** instalar con python -m pip install PACKAGE, inspeccionar con show/list, comprobar con check, registrar con freeze, recrear con install -r requirements.txt. Continúa con Fundamentos para comprender el código Python.

## Referencias oficiales

- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
- [Python Package Index](https://pypi.org/)
- [Navegadores Playwright](https://playwright.dev/python/docs/browsers)

<!-- chapter-navigation:bottom -->
[← Anterior](../04-virtual-environments/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../../fundamentals/01-how-python-runs-a-program/README.es.md)
<!-- /chapter-navigation:bottom -->
