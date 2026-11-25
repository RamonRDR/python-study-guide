# Instrucciones del repositorio

[🇺🇸 English](../../AGENTS.md) · [🇧🇷 Português](AGENTS.pt-BR.md) · [🇪🇸 Español](AGENTS.es.md)

## Propósito del proyecto

Python Study Guide es un proyecto educativo independiente, público, colaborativo y multilingüe. Su objetivo es ayudar a estudiar Python, entender cómo se conectan sus conceptos y practicar con ejemplos claros, precisos, originales y ejecutables. Supón que algunos lectores no tienen experiencia en programación. Explica términos necesarios, evita saltos sin explicación y no confundas brevedad con claridad.

## Responsabilidad del proyecto

Python Study Guide fue creado y es mantenido por [Ramon Estevez Rodriguez](https://github.com/RamonRDR). Preserva registros de autoría y licencia. No elimines, sobrescribas ni tergiverses créditos de colaboradores en metadatos de commits, historial Git o PR. Consulta [AUTHORS](AUTHORS.es.md).

## Orden de prioridades

1. Precisión técnica
2. Claridad educativa
3. Privacidad y seguridad
4. Coherencia entre idiomas
5. Mantenibilidad
6. Velocidad de entrega

No sacrifiques precisión, verificación ni claridad para acabar antes. La velocidad solo gana prioridad si el mantenedor solicita un resultado rápido o provisional; información confidencial, afirmaciones inventadas y cambios sin revisión siguen siendo inaceptables.

## Idiomas

La documentación se mantiene en inglés, portugués brasileño y español. El inglés es estándar para directorios, archivos, ramas, identificadores, comentarios de código y mensajes de commit. Las traducciones deben preservar significado técnico, ejemplos, advertencias, requisitos previos, objetivos y enlaces sin exigir literalidad.

Toda documentación pública de este repositorio, incluida arquitectura, ingeniería, gobernanza y orientación a colaboradores, debe estar disponible y conceptualmente alineada en los tres idiomas. Actualiza versiones afectadas en el mismo PR; traducciones ausentes bloquean finalización. Notas realmente privadas quedan fuera del repositorio público, preferiblemente en inglés (se permite portugués). Identificadores técnicos, archivos, código, claves JSON y valores enum no cambian entre idiomas.

## Contenido educativo

Los capítulos deben explicar: qué es el concepto, por qué existe, sintaxis, cuándo usarlo, cuándo evitarlo, conexiones, ejemplo básico, ejemplo práctico, errores comunes, ejercicio y referencia rápida. Distinguir hechos verificables de recomendaciones o convenciones; no presentar opiniones como reglas Python.

Preferir fuentes primarias y oficiales: documentación Python, PEP y documentación oficial de bibliotecas/productos. Verificar documentación actual para información cambiante; evitar fijar precios, límites de planes, disponibilidad de versiones y otros detalles cambiantes, salvo documentos destinados a seguirlos.

## Ejemplos, originalidad y privacidad

Usar solo ejemplos originales, genéricos, ficticios y no confidenciales. Nunca incluir, reproducir, resumir ni adaptar:

- Información privada de empleadores/clientes o procesos internos de empresas.
- Material de proyectos personales/familiares.
- Credenciales, secretos, tokens o URLs privadas.
- Código propietario, datos personales o documentos confidenciales.
- Detalles identificadores de conversaciones privadas o archivos subidos.
- Ejemplos protegidos por derechos de autor sin permiso/licencia adecuada.

Cambiar un nombre real por ficticio no basta si reglas, fechas, roles, sistemas o flujo identifican la fuente. Crea un ejemplo independiente.

## Calidad del código

- Seguir PEP 8, identificadores descriptivos en inglés y type hints cuando mejoren comprensión.
- Ejemplos pequeños para estudiar y realistas para utilizar; evitar dependencias innecesarias.
- No depender de comportamiento específico de versión sin identificar y verificar la versión Python.
- Comentar decisiones, restricciones y motivos no obvios; no narrar código autoexplicativo.
- Ejecutar o validar ejemplos cuando sea posible; nunca afirmar ejecuciones o pruebas no realizadas.

## Flujo del repositorio

- Nunca modificar main directamente; crear rama enfocada desde main actual.
- PR con un propósito claro; ramas y commits en inglés; evitar formato/refactorización ajenos.
- Revisar todos los archivos cambiados antes de solicitar fusión; resolver comentarios antes de cerrar conversaciones.
- No eludir protecciones; usar squash merge salvo cambio de configuración.

## Trabajo asistido por IA

IA puede apoyar investigación, planificación, redacción, traducción, explicación, generación de código, pruebas, revisión y mantenimiento. El resultado de IA es una propuesta, no autoridad; fluidez, detalles o persuasión no bastan para aceptarlo.

Colaborador y mantenedor son responsables de entender el trabajo, verificar precisión técnica, fuentes y enlaces, revisar traducciones, ejecutar ejemplos/pruebas relevantes, identificar información sin soporte o inventada, proteger información privada/propietaria y confirmar cumplimiento de licencia y políticas.

Usa IA para apoyar el pensamiento, no evitarlo. Al enseñar, prefiere pistas, preguntas, comparaciones y explicaciones graduales cuando ayuden a comprender. Declara incertidumbre y verifica; no inventes hechos, pruebas, citas, archivos ni comportamiento.

## Lista de finalización

Confirmar propósito único; afirmaciones técnicas precisas con fuentes adecuadas; ejemplos originales, genéricos y sin información confidencial; ejemplos ejecutables funcionan o falta de prueba declarada; documentación pública con tres versiones conceptualmente alineadas; terminología y enlaces coherentes; ningún archivo ajeno cambiado; conversaciones de revisión tratadas; resultado enseña en vez de solo proporcionar respuesta.

## Phase II: desarrollo orientado a especificaciones

Antes de implementar, consultar [constitución](../specs/constitution.es.md), [especificación](../specs/learning-hub-foundation/specification.es.md), [plan](../specs/learning-hub-foundation/implementation-plan.es.md), [tareas](../specs/learning-hub-foundation/tasks.es.md), [criterios](../specs/learning-hub-foundation/acceptance-criteria.es.md), [contrato](../specs/learning-hub-foundation/integration-contract.es.md) y [ADR](../adr/README.es.md).

Mantener especificaciones públicas y contenido educativo en los tres idiomas. Preservar rutas curriculares; separar numeración de sprints de orden educativo. No implementar Learning Hub externo aquí, contratar servicios de pago ni introducir corrección por IA. El repositorio es la fuente oficial.

Usar ramas y PR enfocados, solicitar Codex Review, resolver hallazgos relevantes, declarar controles no ejecutados y obtener aprobación explícita antes de fusionar. Actualizar especificaciones y tareas con evidencias cuando cambien alcance/contratos. Las propuestas no autorizan implementación antes de aprobación.

## Auditoría final previa a la fusión (Final Pre-Merge Audit)

Después de que GitHub Actions aplicable y Codex Review aprueben el head exacto actual del PR, realiza una auditoría técnica distinta antes de solicitar aprobación explícita del mantenedor para squash merge. Es una nueva ronda de revisión, no afirmación de revisor independiente si la realiza el mismo colaborador. Verifica alcance y criterios de aceptación, código y ejemplos modificados, discriminación de pruebas y casos límite, requisitos de enseñanza, alineación semántica en los tres idiomas, navegación, regresiones, privacidad y restricciones de seguridad. Para riesgos no verificables, registra limitación e impacto; no marques como aprobado. Registra en PR SHA auditado, ejecución de CI, evidencia de Codex Review, controles realizados, hallazgos y bloqueos pendientes. Si una corrección cambia head, vuelve a ejecutar CI aplicable y Codex Review, después repite auditoría final en ese head. Sin aprobación ni fusión basada en auditoría desactualizada; reconfirma head y controles inmediatamente antes de squash merge. El mantenedor conserva aprobación final; auditoría no sustituye juicio humano.
