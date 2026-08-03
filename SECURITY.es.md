<div align="center">

# Política de Seguridad

[🇺🇸 English](SECURITY.md) · [🇧🇷 Português](SECURITY.pt-BR.md) · [🇪🇸 Español](SECURITY.es.md)

</div>

## Contenido con soporte

Python Study Guide es un repositorio educativo, no un servicio desplegado. Las correcciones de seguridad se aplican a la rama `main` actual y, cuando existan versiones publicadas, a la versión mantenida más reciente siempre que sea viable.

Los commits históricos, las ramas eliminadas, los forks, los materiales copiados y las herramientas externas sin soporte no son mantenidos por este proyecto.

## Informa las vulnerabilidades de forma privada

No abras una issue pública para una vulnerabilidad que pueda exponer usuarios, credenciales, información privada, permisos del repositorio o la integridad de la cadena de suministro.

Cuando la pestaña **Security** del repositorio muestre la opción **Report a vulnerability**, utilízala para enviar el informe de forma privada mediante GitHub.

Si el reporte privado de vulnerabilidades no está disponible, abre una issue pública con el título:

```text
[SECURITY CONTACT REQUEST]
```

Solicita a la persona responsable del mantenimiento un canal privado, pero **no** incluyas en esa issue detalles de la vulnerabilidad, secretos afectados, pasos de explotación, nombres, capturas de pantalla ni otra información sensible.

Incluye únicamente en el informe privado final la información necesaria para comprender el problema:

- archivo, workflow, recomendación de dependencia o función del repositorio afectada;
- impacto potencial;
- pasos seguros de reproducción o una prueba de concepto mínima;
- versiones, commits o entornos afectados;
- mitigación sugerida, cuando esté disponible;
- información sobre cualquier divulgación pública ya realizada.

No incluyas credenciales reales, tokens, URLs privadas, datos personales, datos de empleadores, código propietario ni información obtenida sin autorización.

## Qué pertenece a un informe de seguridad

Algunos ejemplos:

- un workflow o una configuración que pueda permitir ejecución de código no autorizada o uso indebido de privilegios;
- instrucciones que expongan credenciales o fomenten un manejo inseguro de secretos;
- archivos maliciosos o comprometidos presentados como contenido confiable del proyecto;
- una recomendación de dependencia con impacto de seguridad conocido, relevante y reproducible;
- una vulnerabilidad en código mantenido por el proyecto que produzca un riesgo de seguridad realista.

## Qué no es una vulnerabilidad de seguridad

Utiliza las plantillas normales de issues para:

- explicaciones o traducciones incorrectas;
- enlaces rotos o problemas de formato;
- errores comunes de Python sin impacto de seguridad;
- preguntas sobre el material de aprendizaje;
- vulnerabilidades en productos externos o proyectos personales no relacionados;
- preocupaciones hipotéticas sin una ruta de ataque plausible o un componente afectado del proyecto.

## Proceso de respuesta

Este proyecto se mantiene con el mejor esfuerzo posible y no ofrece un acuerdo garantizado de nivel de servicio.

La persona responsable del mantenimiento procura:

1. confirmar la recepción de un informe válido en un plazo de siete días naturales;
2. verificar el alcance y la gravedad;
3. coordinar una corrección y un plan de divulgación cuando sea necesario;
4. reconocer a quien informó, cuando se solicite y sea seguro;
5. publicar información relevante de remediación después de que las personas afectadas puedan protegerse.

Concede un plazo razonable para la investigación antes de realizar una divulgación pública. La persona responsable podrá contactar a GitHub, mantenedores de paquetes u otras partes responsables cuando se requiera coordinación.

## Expectativas para una investigación segura

La investigación de seguridad debe realizarse de buena fe y en entornos autorizados. No:

- accedas, modifiques ni conserves datos que no te pertenezcan;
- interrumpas servicios ni perjudiques a otras personas;
- utilices ingeniería social, robo de credenciales o pruebas destructivas;
- explotes un hallazgo más allá de lo necesario para demostrar el impacto;
- exijas pagos, empleo o favores como condición para no realizar una divulgación perjudicial.

Este proyecto no mantiene actualmente un programa de recompensas por vulnerabilidades ni promete compensación económica.
