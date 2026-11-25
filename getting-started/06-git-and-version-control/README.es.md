# Git y fundamentos del control de versiones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../05-packages-and-dependencies/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../../fundamentals/01-how-python-runs-a-program/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Nivel:** principiante absoluto. **Tiempo estimado:** 30–45 minutos, sin contar instalación y configuración de cuenta. Usa un proyecto personal de práctica, no un repositorio de trabajo. Al final puedes registrar e inspeccionar una versión de código Python y entender cómo sincronizarla con un repositorio remoto.

Git es una herramienta de control de versiones. Registra versiones (commits) de archivos seleccionados para inspeccionar cambios y colaborar. GitHub y GitLab alojan repositorios Git y ofrecen herramientas de colaboración. Git funciona localmente sin cuenta ni internet. Una cuenta remota solo es necesaria para el ejercicio opcional de publicación.

## 1. Instala y configura Git

Usa la [página oficial de instalación de Git](https://git-scm.com/install/). En Windows, instala Git for Windows y reabre PowerShell o VS Code. En macOS, sigue las opciones documentadas, incluidas las herramientas de línea de comandos Xcode cuando corresponda. En Linux, usa el gestor de paquetes oficial de tu distribución.

```shell
git --version
```

En la terminal, abre la carpeta python-practice existente. Comprueba la carpeta actual con Get-Location (PowerShell) o pwd (macOS/Linux). Ejecuta primero git status. Si ya pertenece a un repositorio, usa otra carpeta de práctica fuera de él; no crees accidentalmente un repositorio anidado. Si Git informa que la carpeta no es un repositorio, inicializa:

```shell
git init -b main
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

Sustituye la identidad ilustrativa por el nombre deseado en commits y un correo apropiado (una dirección no-reply verificada por el proveedor es una opción). Estos comandos de configuración afectan solo a este repositorio. Los nombres y correos de commits quedan registrados en el historial; evita exponer datos personales. Si tu versión de Git no reconoce -b, actualízala mediante instrucciones oficiales.

## 2. Decide qué debe versionarse

Crea un archivo de texto plano llamado .gitignore en la raíz del proyecto (sin extensión .txt), con:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

Estos patrones excluyen entornos generados, cachés Python y un archivo común de configuración local. No protegen archivos ya rastreados ni eliminan secretos del historial. Revisa cada cambio; nunca versiones credenciales, datos privados ni un .env real.

Conserva first_program.py, .gitignore y requirements.txt revisado del capítulo 05. No versiones .venv. Si requirements.txt contiene URLs privadas o rutas locales, corrígelo antes de seleccionar el archivo.

## 3. Registra el primer commit

Ejecuta git status para inspeccionar los archivos. Selecciona solo los archivos deseados por nombre:

```shell
git add .gitignore first_program.py requirements.txt
git diff --cached
git status
git commit -m "feat: add first Python program"
git log --oneline
```

Si omitiste el ejercicio opcional de dependencias, crea un requirements.txt revisado con solo las dependencias necesarias (un archivo vacío sirve para el primer programa). Un archivo en staging está seleccionado para el siguiente commit. El commit registra una versión y mensaje localmente. Nada se ha subido.

Cambia el mensaje de first_program.py, guarda y ejecútalo con el intérprete comprobado del entorno. Después inspecciona y crea el commit:

```shell
git diff
git add first_program.py
git diff --cached
git commit -m "feat: update greeting"
git log --oneline
git status
```

Deberías ver dos commits y, si no hay otros cambios, un árbol de trabajo limpio. git diff muestra cambios no seleccionados; git diff --cached muestra cambios seleccionados; git log muestra historial. Si el resultado es distinto, inspecciona status en vez de repetir comandos a ciegas.

## 4. Entiende los remotos (práctica opcional)

Un remoto es una conexión nombrada con otro repositorio. GitHub y GitLab tienen interfaces web distintas, pero usan los mismos comandos básicos Git. Si quieres publicar, crea un repositorio vacío en el proveedor elegido, sin README, licencia ni .gitignore inicial. Prefiere un repositorio privado de práctica, comprueba visibilidad y contenido y sigue las indicaciones de autenticación del proveedor. Nunca pongas contraseñas ni tokens de acceso en URLs de remotos o commits.

Copia la URL HTTPS de clonación de tu propio repositorio. Sustituye el marcador antes de ejecutar:

```shell
git remote add origin YOUR_REPOSITORY_HTTPS_URL
git remote -v
git push -u origin main
```

Si origin ya existe, inspecciónalo en vez de sobrescribirlo. El primer push envía commits locales y configura la rama upstream. La autenticación puede abrir un navegador o gestor de credenciales. Si el remoto ya tiene historial o el push es rechazado, detente e investiga; no fuerces el push.

Para actualizaciones posteriores, comprueba primero que git status está limpio y estás en la rama deseada. En este repositorio simple de práctica con una sola rama:

```shell
git pull --ff-only
git log --oneline
```

pull obtiene commits remotos y los integra; --ff-only rechaza crear un merge cuando los historiales han divergido. Si rechaza, detente y pide ayuda en vez de resetear o sobrescribir trabajo. Tras otro commit local revisado, git push lo publica. git clone copia un repositorio remoto existente en otra carpeta; ejecútalo fuera del repositorio original:

```shell
git clone YOUR_REPOSITORY_HTTPS_URL python-practice-copy
```

Recrea el entorno virtual desde requirements.txt en la copia usando los capítulos 04–05; Git no transfiere la .venv ignorada.

## 5. El flujo profesional, brevemente

En un proyecto compartido, una rama aísla un cambio, un pull request (GitHub) o merge request (GitLab) lo propone, la revisión lo verifica y CI ejecuta comprobaciones automáticas. Merge integra cambios aprobados. No envíes directamente a la main protegida de un proyecto compartido. El material posterior de prácticas de ingeniería aplicará estas ideas a Python. Ramas en profundidad, conflictos, recuperación de historial, GitHub Actions, GitLab CI y colaboración pertenecen al futuro Git Study Guide independiente; aquí no se exige ningún curso externo.

## Práctica y referencia rápida

- [ ] Comprobar Git y configurar repositorio de práctica.
- [ ] Crear .gitignore y confirmar que .venv no está seleccionada.
- [ ] Revisar y versionar el primer programa, modificarlo y crear otro commit.
- [ ] Inspeccionar los dos commits y explicar diferencia entre commit local y push remoto.
- [ ] Opcionalmente publicar en tu repositorio vacío de práctica y clonarlo en otra carpeta.

Si falla un comando, lee el mensaje, comprueba la carpeta actual, consulta git status y documentación oficial. No uses reset destructivo, force-push ni alternativas inseguras de credenciales.

## Referencias oficiales

- [Instalación Git](https://git-scm.com/install/)
- [Fundamentos Git: registrar cambios](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Repositorios remotos Git](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Autenticación GitHub](https://docs.github.com/en/authentication)
- [Autenticación GitLab](https://docs.gitlab.com/user/gitlab_com/#authentication)

<!-- chapter-navigation:bottom -->
[← Anterior](../05-packages-and-dependencies/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../../fundamentals/01-how-python-runs-a-program/README.es.md)
<!-- /chapter-navigation:bottom -->
