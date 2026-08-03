<div align="center">

# Desarrollo Asistido por IA

[🇺🇸 English](README.en.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

La inteligencia artificial puede acelerar la investigación, la organización, las explicaciones, las traducciones, la programación y las revisiones. También puede producir información incorrecta, incompleta, desactualizada o inventada usando un lenguaje convincente.

Por eso, este proyecto utiliza la IA como herramienta de apoyo, no como autoridad final.

El principio orientador es sencillo:

> Usa la IA para ampliar tu capacidad de pensar, construir, verificar y aprender. No la utilices para abandonar la responsabilidad sobre el resultado.

## Objetivo de este documento

Esta página explica:

- cómo la IA apoya Python Study Guide;
- cómo una persona principiante puede conversar con un asistente de IA;
- cómo proporcionar un contexto útil;
- cómo escribir y refinar prompts;
- cómo pedir enseñanza y no solamente respuestas;
- cómo transformar una conversación en un brief de implementación;
- cómo enviar un brief revisado a Codex;
- cómo validar un trabajo asistido por IA;
- cómo proteger información privada y confidencial.

No se requiere experiencia previa con herramientas de IA.

## Cómo apoya la IA a este proyecto

ChatGPT y Codex pueden ayudar en actividades como:

- planificar la estructura del repositorio;
- explicar conceptos de Python;
- investigar y verificar información técnica;
- redactar y revisar contenido educativo;
- alinear la documentación en inglés, portugués de Brasil y español;
- crear ejemplos y ejercicios originales;
- identificar inconsistencias;
- revisar pull requests;
- editar archivos y mantener el repositorio.

Sus funciones están relacionadas, pero no son idénticas.

### ChatGPT

ChatGPT es útil para conversar, explicar, estudiar, generar ideas, comparar alternativas, redactar, traducir y transformar una idea poco definida en un plan estructurado.

### Codex

Codex es un agente de programación con IA que puede trabajar a partir de un prompt o una especificación para inspeccionar un repositorio, editar archivos, ejecutar comandos y pruebas, revisar código y preparar cambios para revisión humana.

Las interfaces y las funciones disponibles pueden cambiar. El flujo duradero es más importante que cualquier botón específico:

```text
Comprender el problema
        ↓
Conversar y aprender
        ↓
Definir los requisitos
        ↓
Crear un brief de implementación
        ↓
Pedir a Codex que lo implemente
        ↓
Revisar archivos, pruebas y explicaciones
        ↓
Abrir y revisar un pull request
        ↓
Hacer merge solamente después de validar
```

## Responsabilidad humana

La IA no elimina la responsabilidad humana.

Una respuesta clara o persuasiva no es automáticamente correcta. La persona responsable del proyecto y quien contribuye siguen siendo responsables de:

- comprender lo que se envía;
- verificar afirmaciones técnicas;
- confirmar información importante en fuentes confiables;
- probar ejemplos ejecutables;
- revisar traducciones;
- identificar suposiciones sin fundamento;
- proteger información privada;
- decidir si un cambio está listo para el merge.

No envíes contenido que no puedas explicar, revisar o defender.

## Piensa antes de escribir el prompt

Un prompt útil suele comenzar antes de escribir el mensaje.

Intenta responder estas preguntas con tus propias palabras:

1. ¿Qué estoy intentando lograr?
2. ¿Qué sé actualmente?
3. ¿Dónde tengo dificultades?
4. ¿Qué restricciones deben respetarse?
5. ¿Qué resultado sería útil?
6. ¿Cómo sabré si el resultado es correcto?

Las respuestas no necesitan ser perfectas. El objetivo es dar dirección a la conversación.

## Anatomía de un prompt útil

Un prompt puede organizarse con seis elementos sencillos:

| Elemento | Pregunta que responde |
|---|---|
| Contexto | ¿En qué situación estamos trabajando? |
| Objetivo | ¿Qué quiero conseguir? |
| Estado actual | ¿Qué tengo o comprendo actualmente? |
| Restricciones | ¿Qué reglas o límites deben seguirse? |
| Resultado esperado | ¿En qué formato debe presentarse la respuesta? |
| Validación | ¿Cómo debe comprobarse el resultado? |

Esto es una guía, no una fórmula obligatoria. Una pregunta pequeña puede necesitar una sola frase. Un cambio en un repositorio puede requerir una especificación detallada.

### Prompt débil

```text
Haz un programa en Python.
```

La solicitud es demasiado amplia. La IA debe adivinar el público, el propósito, las entradas, la salida, las restricciones y el estilo de enseñanza deseado.

### Mejor prompt de aprendizaje

```text
Estoy comenzando a estudiar Python y todavía no he aprendido funciones.

Quiero crear un programa pequeño que reciba tres calificaciones y calcule
un promedio.

Primero, explica qué conceptos básicos necesito conocer. Después, muestra
un ejemplo sencillo y explícalo línea por línea.

No entregues un proyecto completo inmediatamente. Al final, propón un
ejercicio parecido para que lo resuelva por mi cuenta y muestra la respuesta
solamente después de mi intento.
```

Este prompt proporciona contexto, un objetivo, el nivel actual de la persona, una restricción pedagógica y el resultado esperado.

## Pide a la IA que te ayude a pensar

La IA puede actuar como tutora y no como una máquina de entregar respuestas terminadas.

Algunas instrucciones útiles son:

```text
No proporciones todavía la respuesta completa. Dame una pista cada vez.
```

```text
Explica por qué falla mi solución, pero permíteme intentar corregirla.
```

```text
Hazme preguntas para comprobar si comprendí el concepto.
```

```text
Compara mi solución con otro enfoque y explica sus ventajas y limitaciones.
```

```text
Indica qué partes de mi razonamiento son correctas antes de explicar el error.
```

```text
Después de la explicación, pídeme que resuma el concepto con mis propias palabras.
```

El objetivo no es volver el aprendizaje innecesariamente difícil. Es mantener a la persona mentalmente involucrada.

## Refina la conversación

Un buen prompt no necesita ser perfecto en el primer intento.

Un ciclo productivo es:

```text
Preguntar
  ↓
Leer críticamente
  ↓
Identificar lo que falta o no está claro
  ↓
Añadir contexto o restricciones
  ↓
Pedir una revisión
  ↓
Verificar el resultado
```

Ejemplos de mensajes de seguimiento útiles:

```text
Usa un vocabulario más sencillo y define cada término técnico.
```

```text
Tu ejemplo introdujo listas, pero todavía no he estudiado ese tema.
Reescríbelo usando solamente variables, input, conversión, operaciones
aritméticas y print.
```

```text
Muestra la fuente de la afirmación técnica sobre el comportamiento de Python.
```

```text
Crea dos casos de prueba, incluido uno que pueda revelar un error frecuente.
```

Refinar no significa fracasar. Es parte de comunicar requisitos.

## De ChatGPT a Codex

ChatGPT puede ayudar a transformar una idea en un brief de implementación revisado. Codex puede trabajar después con ese brief dentro de un repositorio.

Antes de enviar la tarea a Codex, confirma que el brief describa:

- el contexto del repositorio;
- la tarea;
- los archivos o el área que pueden modificarse;
- los requisitos;
- lo que no debe hacerse;
- los criterios de aceptación;
- los pasos de validación;
- las reglas de idioma y documentación.

### Ejemplo de brief de implementación para Codex

```text
Contexto del repositorio

Este es un repositorio educativo multilingüe de Python para principiantes.
Los nombres de directorios, archivos, identificadores, comentarios del código,
branches y mensajes de commit deben permanecer en inglés.
La documentación se mantiene en inglés, portugués de Brasil y español.

Tarea

Crea un ejemplo para principiantes que calcule el promedio de tres calificaciones.

Requisitos

- Utiliza solamente funcionalidades integradas de Python.
- Mantén el ejemplo pequeño y ejecutable.
- Utiliza nombres de variables descriptivos en inglés.
- Explica los conceptos necesarios antes del ejemplo.
- Crea documentación conceptualmente alineada en los tres idiomas admitidos.
- Utiliza solamente datos originales, ficticios y no confidenciales.
- No modifiques archivos que no estén relacionados con la tarea.

Criterios de aceptación

- El ejemplo se ejecuta sin errores.
- El promedio se calcula correctamente.
- La explicación es adecuada para alguien que todavía no ha estudiado funciones.
- Las tres versiones conservan el mismo significado y objetivo de aprendizaje.
- Los enlaces y las rutas relativas funcionan.

Validación

- Ejecuta el ejemplo con al menos dos casos de prueba.
- Revisa todos los archivos modificados.
- Informa qué se probó y declara cualquier elemento que no haya podido verificarse.
- Envía el trabajo mediante una branch y un pull request específicos.
```

Un prompt detallado mejora la dirección. No garantiza que el resultado sea correcto.

## Revisa el trabajo generado por IA

Revisa el resultado como si lo hubiera entregado una persona colaboradora competente, pero capaz de cometer errores.

### Revisión de la documentación

Confirma que:

- la explicación sea técnicamente correcta;
- las afirmaciones importantes cuenten con fuentes adecuadas;
- el texto corresponda al nivel de aprendizaje previsto;
- los ejemplos sean originales;
- los tres idiomas permanezcan conceptualmente alineados;
- los enlaces funcionen;
- las incertidumbres se indiquen en lugar de ocultarse.

### Revisión del código

Confirma que:

- el código se ejecute como se describe;
- se hayan considerado los casos esperados y los casos límite;
- los nombres sean claros;
- el ejemplo no introduzca conceptos innecesarios;
- los comentarios expliquen motivos y no operaciones evidentes;
- las dependencias estén justificadas;
- no haya secretos ni datos privados.

### Revisión del repositorio

Confirma que:

- solamente se hayan modificado archivos relevantes;
- la branch se haya creado desde la versión actual de `main`;
- el pull request tenga un único propósito claro;
- se hayan considerado los comentarios de revisiones automáticas;
- las conversaciones se hayan resuelto solamente después de corregir el problema correspondiente.

## Privacidad e información confidencial

Nunca proporciones a un sistema de IA información que no estés autorizado a compartir con otra persona o servicio externo.

Elimina o evita:

- nombres reales cuando no sean necesarios;
- direcciones de correo electrónico y números de teléfono;
- contraseñas, claves de API, tokens, cookies y credenciales;
- datos financieros, médicos, laborales o de clientes;
- URL privadas, nombres de hosts, rutas y detalles de infraestructura;
- documentos internos y código fuente privado;
- reglas de negocio y flujos confidenciales;
- detalles identificables de proyectos personales, familiares, profesionales o de clientes.

Una anonimización superficial puede no ser suficiente. La combinación de fechas, cargos, nombres de sistemas, estructuras de cuentas, reglas poco comunes y detalles del flujo todavía puede revelar el origen.

Para material educativo, crea un escenario ficticio nuevo desde el principio.

## Controles de datos y mejora de modelos

La elección del plan, los controles de datos y la mejora de los modelos son temas diferentes.

OpenAI ofrece Controles de Datos que permiten a las personas decidir si las conversaciones elegibles de ChatGPT pueden ayudar a mejorar sus modelos. Las configuraciones y políticas disponibles pueden variar según el producto, el tipo de cuenta y el momento.

Independientemente de la configuración seleccionada, no envíes información confidencial o no autorizada.

Consulta la documentación oficial actual antes de tomar decisiones sobre privacidad o uso de datos.

## Planes, disponibilidad y límites

OpenAI ofrece planes gratuitos y de pago de ChatGPT. La disponibilidad de Codex, las interfaces compatibles, las funciones, los límites de uso y las opciones de créditos pueden variar según el plan y cambiar con el tiempo.

Un plan de pago puede ser útil cuando sus funciones y límites actuales coinciden con las necesidades de estudio o desarrollo de una persona. El pago no sustituye la comprensión, la verificación, las pruebas ni el uso responsable.

Este repositorio no publica precios ni límites fijos de planes. Consulta la documentación oficial actual de OpenAI antes de elegir un plan.

## Contribuciones asistidas por IA

Las contribuciones asistidas por IA son bienvenidas cuando quien contribuye sigue siendo responsable del resultado.

La persona colaboradora debe:

- comprender el contenido enviado;
- revisar y verificar el material;
- ejecutar los ejemplos y pruebas relevantes;
- revisar todas las versiones de idioma afectadas;
- informar las incertidumbres;
- eliminar material privado o propietario;
- cumplir las licencias y políticas del repositorio.

No envíes contenido generado automáticamente sin una revisión humana significativa.

## Independencia y marcas

ChatGPT, Codex y OpenAI son marcas de OpenAI.

Python Study Guide es un proyecto educativo independiente. No está afiliado, patrocinado ni respaldado por OpenAI.

Las referencias a productos de OpenAI son descriptivas. La identidad propia del proyecto debe seguir siendo el elemento principal.

## Recursos oficiales

Como las capacidades y políticas de los productos pueden cambiar, consulta siempre las páginas oficiales actuales:

- [ChatGPT capabilities overview](https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview)
- [Prompt engineering best practices for ChatGPT](https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt)
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq)
- [OpenAI brand guidelines](https://openai.com/brand/)

## Principio final

Un flujo útil con IA no termina cuando aparece una respuesta. Termina cuando la persona comprende el resultado, lo verifica, lo mejora y puede asumir la responsabilidad por él.
