# Retos de cadenas y números

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../07-problem-solving-patterns/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../09-collections/README.es.md)
<!-- /chapter-navigation:top -->

Repasa pertenencia literal de caracteres, índices, división entera y resto. En el palíndromo medio, reutiliza dos punteros comparando posiciones simétricas en lugar de suma de par.

Lee contrato y lecciones de requisitos previos enlazadas, predice resultados, intenta el inicial en archivo personal y comprueba límites. Abre pistas progresivamente; compara referencia solo tras intentar. No hay ejecutor en navegador.

### Ventana variable con últimas posiciones

Una ventana fija mantiene longitud; una variable puede reducirse o crecer según restricción. Para caracteres únicos, mantén frontera izquierda inclusiva y recorre derecha carácter a carácter. Diccionario guarda último índice de cada carácter. Si índice es al menos left, la aparición antigua debe salir: mueve left a índice más uno. Si no, deja left. Longitud válida right - left + 1. Guarda la mejor. En "abba", tras segundo b la ventana comienza en índice 2; en a final, índice anterior 0 queda fuera, así que no muevas left hacia atrás. Máximo 2. Bajo hashing habitual, tiempo lineal esperado y espacio proporcional a caracteres distintos. Regla específica de unicidad, no universal para ventanas variables.

## Retos disponibles

- [Contador de vocales](../../exercises/problem-solving/vowel-counter/README.es.md) · Fácil · 10 min
- [Contador de dígitos ASCII](../../exercises/problem-solving/ascii-digit-counter/README.es.md) · Fácil · 10 min
- [Suma de dígitos](../../exercises/problem-solving/sum-digits/README.es.md) · Fácil · 12 min
- [Palíndromo literal](../../exercises/problem-solving/literal-palindrome/README.es.md) · Media · 18 min

- [Mayor subcadena sin repetición](../../exercises/problem-solving/longest-distinct-substring/README.es.md) · Difícil · 35 min

<!-- chapter-navigation:bottom -->
[← Anterior](../07-problem-solving-patterns/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../09-collections/README.es.md)
<!-- /chapter-navigation:bottom -->
