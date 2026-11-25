# Retos de funciones y recursividad

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../09-collections/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../11-searching-and-sorting/README.es.md)
<!-- /chapter-navigation:top -->

Repasa parámetros, retornos y casos base recursivos. Factorial multiplica enteros positivos hasta n; potencia entera multiplica repetidamente la misma base. Cero tiene resultado base definido como uno en ambas tareas.

Lee contrato y lecciones de requisitos previos enlazadas, predice resultados, intenta el inicial en archivo personal y comprueba límites. Abre pistas progresivamente; compara referencia solo tras intentar. No hay ejecutor en navegador.

### Recorrido recursivo de listas anidadas

Una lista anidada es jerarquía finita: elemento es entero hoja u otra lista. En auxiliar recursiva, recorre elementos; añade entero a resultado compartido o visita lista recursivamente antes del siguiente elemento. Lista vacía retorna tras cero iteraciones. Usa isinstance(item, list) para distinguir nodos de lista; pasa el mismo acumulador a auxiliar o defínela dentro de función para añadir a lista. En [1, [2, [3]], 4], visita 1, desciende a [2, [3]], añade 2 y 3, vuelve y añade 4. No añadas lista entera ni concatenes copias en cada nivel. Supón entrada finita sin ciclos y anidamiento limitado. Pila crece con profundidad, no cantidad de hojas.

## Retos disponibles

- [Limitar un valor](../../exercises/problem-solving/clamp-value/README.es.md) · Fácil · 10 min
- [Factorial recursivo](../../exercises/problem-solving/recursive-factorial/README.es.md) · Media · 18 min
- [Potencia entera recursiva](../../exercises/problem-solving/recursive-power/README.es.md) · Media · 20 min

- [Aplanar listas anidadas](../../exercises/problem-solving/recursive-flatten/README.es.md) · Difícil · 35 min

<!-- chapter-navigation:bottom -->
[← Anterior](../09-collections/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../11-searching-and-sorting/README.es.md)
<!-- /chapter-navigation:bottom -->
