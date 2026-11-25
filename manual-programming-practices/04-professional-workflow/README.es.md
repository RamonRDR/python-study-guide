# Flujo profesional de Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-test-driven-development/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Tiempo estimado:** 35–50 minutos. Aplica las lecciones anteriores a un cambio Python pequeño. Necesitas Git local, repositorio de práctica e intérprete comprobado. Consulta [Git básico](../../getting-started/06-git-and-version-control/README.es.md). Cuenta de alojamiento opcional; no crees servicio de pago ni uses el repositorio real de la guía para experimentos.

## 1. Haz el trabajo revisable

Usa tu propio repositorio local con baseline registrado. Guarda requisitos, plan y ADR de progreso de lectura de la lección SDD en el repositorio de práctica. Si aún no están registrados, revisa y crea commit en baseline antes de crear rama. Comprueba `git status` limpio. Crea rama enfocada:

```shell
git switch -c feat/reading-progress
```

Implementa y prueba manualmente según lección anterior. Mantén archivos generados y secretos fuera de Git. Antes del commit, ejecuta pruebas en carpeta de práctica:

```shell
python -m unittest discover -s . -p 'test_*.py' -v
git status
git diff
git add reading_progress.py test_reading_progress.py
git diff --cached
git commit -m "feat: calculate remaining reading pages"
```

Usa archivos reales que deseas cambiar; inspecciona staging primero. Si hay fallo, investiga y ejecuta otra vez en vez de informar éxito.

## 2. Escribe descripción revisable

En nota local, prepara pull request: propósito; requisitos R1–R4; resumen de implementación; evidencias AC1–AC5; comandos y resultados reales; limitaciones; fuera de alcance. Code review es ejercicio de razonamiento: compara código con especificación, comprueba límites, nombres, manejo de errores, pruebas y privacidad. CI aprobado es necesario cuando se exige, no garantía de corrección.

## 3. Práctica GitHub opcional

Solo si posees remoto de práctica y entiendes su visibilidad, envía rama con `git push -u origin feat/reading-progress`. Abre pull request hacia main de práctica. En GitLab, revisión equivalente es merge request. Nunca envíes a repositorio ajeno sin permiso. Profundidad de Git y plataformas pertenece a la futura Git Study Guide; esta lección ejemplifica flujo Python.

CI ejecuta comprobaciones configuradas sobre cambios. Un workflow mínimo ilustrativo de GitHub Actions para ese repositorio aislado puede guardarse como .github/workflows/python-tests.yml **en la rama de funcionalidad**:

```yaml
name: Python tests
on: [pull_request]
permissions:
  contents: read
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
      - run: python -m unittest discover -s . -p 'test_*.py' -v
```

Es workflow mínimo ilustrativo, no instrucción para sustituir el [workflow existente](../../.github/workflows/quality-checks.yml) de la guía. Supone archivos de prueba en raíz de práctica y ausencia de dependencias externas. Revisa archivo antes de añadirlo y crear commit separado; vuelve a enviarlo. Comprueba disponibilidad y cuotas del alojamiento antes de ejecutar CI remoto; las pruebas locales bastan para el ejercicio obligatorio. No informes que el workflow ilustrativo se ejecutó si no ocurrió. Revisa resultados, atiende feedback, vuelve a ejecutar pruebas y fusiona solo con aprobación. Si CI falla o hay conflictos de historial, detente e investiga; no eludas protecciones. Sin remoto, simula revisión local con `git diff main...HEAD`; mantén rama sin fusionar hasta revisión.

## 4. Trabajo independiente y límites de IA

Primero resuelve y explica sin implementación ni corrección generada por IA. Usa documentación oficial, pruebas, depuración y feedback humano. Si usas IA para aprender, pide pista tras intento genuino; verifica respuestas y no compartas datos privados. La [guía de mantenimiento asistido por IA](../../docs/ai-assisted-development/README.es.md) separada explica cómo colaboradores pueden usar ChatGPT/Codex con responsabilidad humana. Mantenimiento asistido no es práctica independiente del estudiante.

## 5. Lista de finalización

- Requisito y criterios explícitos.
- Escribí y entendí código; pruebas demuestran casos normales, límites e inválidos.
- Comprobé diff, commit y resultados reales de pruebas.
- Puedo explicar una decisión y una contrapartida.
- Feedback atendido; fusionar exige aprobación.
- Puedo reproducir flujo en otro problema pequeño.

**Referencia rápida:** necesidad → spec → plan → rama → prueba/código/refactorización → revisión del diff → commit → PR/CI opcionales → aprobación humana → fusión. Para reglas de contribución, lee [CONTRIBUTING](../../docs/localized/CONTRIBUTING.es.md).

<!-- chapter-navigation:bottom -->
[← Anterior](../03-test-driven-development/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:bottom -->
