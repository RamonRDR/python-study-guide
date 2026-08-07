<div align="center">

# `type()` e `isinstance()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Tipos de dados embutidos](../04-built-in-data-types/README.pt-BR.md)

O Capítulo 04 ensinou a reconhecer tipos comuns de valores a partir da notação do código-fonte. Este capítulo acrescenta a inspeção direta. O Python fornece `type()` para revelar o tipo exato de um valor e `isinstance()` para perguntar se um valor pertence a um tipo ou a uma família de tipos compatível.

Essa diferença importa. Identidade exata de tipo e compatibilidade de tipo respondem a perguntas diferentes, especialmente quando há herança envolvida.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 a 04 |
| Tempo estimado de estudo | 55 a 75 minutos |
| Conceitos principais | `type()`, `isinstance()`, tipo exato, tipo compatível, objeto de tipo, tupla de tipos |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- inspecionar um valor com `type()`;
- ler resultados comuns de `type()`;
- explicar que `type()` retorna um objeto de tipo, e não texto;
- verificar um valor com `isinstance()`;
- passar um tipo ou uma tupla de tipos para `isinstance()`;
- explicar a diferença entre inspeção do tipo exato e verificação de compatibilidade;
- entender por que `isinstance(True, int)` é `True`;
- evitar comparar resultados de `type()` com strings;
- escolher entre `type()` e `isinstance()` em tarefas simples para iniciantes.

## 1. Reconhecer um tipo nem sempre é suficiente

Muitas vezes é possível prever o tipo de um valor lendo o código-fonte:

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

Porém, programas nem sempre recebem valores na forma de literais óbvios. Valores podem vir de chamadas de funções, arquivos, bibliotecas, cálculos ou entrada da pessoa usuária.

A inspeção direta responde a perguntas que uma simples análise visual nem sempre consegue responder com segurança.

## 2. `type()` revela o tipo exato

Chame `type()` com um valor:

```python
course_name = "Python Study Guide"

print(type(course_name))
```

Saída esperada:

```text
<class 'str'>
```

O resultado informa que `course_name` atualmente referencia uma instância de `str`.

## 3. Inspecione os tipos comuns do Capítulo 04

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None

print(type(course_name))
print(type(chapter_number))
print(type(estimated_minutes))
print(type(is_available))
print(type(next_chapter))
```

Saída esperada:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

A representação entre sinais de menor e maior é a forma como o Python exibe objetos de tipo de maneira legível.

## 4. `type()` retorna um objeto, não uma string de rótulo

Esta distinção é importante:

```python
chapter_number = 5
chapter_type = type(chapter_number)

print(chapter_type)
```

`chapter_type` referencia o objeto de tipo `int`. Ele não contém o texto `"int"`.

Portanto, esta ideia está incorreta:

```text
type(chapter_number) == "int"
```

O lado esquerdo é um objeto de tipo. O lado direito é uma string.

## 5. Nomes de tipos como `str` e `int` também são objetos

Nomes como `str`, `int`, `float` e `bool` referenciam objetos de tipo embutidos.

Por isso, é possível comparar um resultado exato de `type()` com um objeto de tipo:

```python
chapter_number = 5

print(type(chapter_number) is int)
print(type(chapter_number) is str)
```

Saída esperada:

```text
True
False
```

Aqui, `is` pergunta se as duas referências apontam para o mesmo objeto. Comparações de identidade em detalhes pertencem a um tópico posterior de fluxo do programa; por enquanto, leia esse padrão como uma verificação de tipo exato.

## 6. Verificações de tipo exato são propositalmente rígidas

```python
is_available = True

print(type(is_available) is bool)
print(type(is_available) is int)
```

Saída esperada:

```text
True
False
```

`type()` informa o tipo exato do valor em tempo de execução. Para `True`, esse tipo exato é `bool`.

Essa rigidez pode ser útil, mas nem sempre é a melhor forma de perguntar se um valor é aceitável para uma categoria mais ampla.

## 7. `isinstance()` faz uma pergunta de compatibilidade

`isinstance()` recebe um valor e um tipo:

```python
chapter_number = 5

print(isinstance(chapter_number, int))
print(isinstance(chapter_number, str))
```

Saída esperada:

```text
True
False
```

Leia a primeira chamada como:

> `chapter_number` é uma instância de `int` ou de um tipo derivado de `int`?

Essa parte final é a principal diferença em relação a uma verificação exata com `type()`.

## 8. `isinstance()` retorna um booleano

O resultado de `isinstance()` é sempre `True` ou `False`:

```python
course_name = "Python Study Guide"
is_text = isinstance(course_name, str)

print(is_text)
```

Saída esperada:

```text
True
```

Você pode armazenar o resultado em uma variável booleana com nome claro e reutilizá-lo depois.

## 9. Verifique mais de um tipo aceito

O segundo argumento de `isinstance()` pode ser uma tupla de tipos:

```python
whole_number = 5
decimal_number = 5.0
text_number = "5"

print(isinstance(whole_number, (int, float)))
print(isinstance(decimal_number, (int, float)))
print(isinstance(text_number, (int, float)))
```

Saída esperada:

```text
True
True
False
```

Isso pergunta se o valor é compatível com qualquer tipo presente na tupla.

## 10. Não escreva `int or float` como argumento de tipo

Esta não é a mesma verificação:

```text
isinstance(value, int or float)
```

A expressão `int or float` é avaliada antes de `isinstance()` recebê-la, então ela não significa “`int` ou `float`” nesse contexto.

Use uma tupla:

```python
value = 5.0

print(isinstance(value, (int, float)))
```

## 11. A relação entre `bool` e `int`

O Python define `bool` como uma subclasse de `int`. Isso produz um resultado que surpreende muitas pessoas iniciantes:

```python
is_available = True

print(type(is_available) is bool)
print(type(is_available) is int)
print(isinstance(is_available, bool))
print(isinstance(is_available, int))
```

Saída esperada:

```text
True
False
True
True
```

O tipo exato é `bool`, mas um booleano também é considerado uma instância de `int` em verificações baseadas em herança.

## 12. Por que o detalhe de `bool` importa

Imagine um programa que aceita quantidades inteiras:

```python
quantity = True

print(isinstance(quantity, int))
```

Isso imprime `True`, embora `True` possa ser uma escolha semanticamente ruim para uma quantidade.

Compatibilidade de tipo não substitui o significado do domínio. O programa ainda precisa decidir se o valor faz sentido para sua finalidade.

## 13. `type()` versus `isinstance()`

Uma regra útil para iniciantes é:

| Pergunta | Prefira |
|---|---|
| Qual é o tipo exato deste valor? | `type(value)` |
| Este valor é compatível com este tipo? | `isinstance(value, SomeType)` |
| Ele é compatível com qualquer um de vários tipos? | `isinstance(value, (TypeA, TypeB))` |
| Preciso considerar subclasses? | Normalmente `isinstance()` |

Use verificações exatas quando a exatidão for realmente o requisito. Use `isinstance()` quando subclasses compatíveis também devam contar.

## 14. `input()` é um bom exemplo para inspeção

O Capítulo 04 afirmou que `input()` retorna texto. Agora você pode verificar isso diretamente:

```python
response = input("Practice minutes: ")

print(type(response))
```

Se a pessoa digitar `45`, a linha final ainda exibirá:

```text
<class 'str'>
```

Os caracteres podem parecer numéricos, mas o valor retornado é uma string.

## 15. `None` também pode ser inspecionado

```python
review_note = None

print(type(review_note))
print(isinstance(review_note, type(None)))
```

Saída esperada:

```text
<class 'NoneType'>
True
```

No Python cotidiano, a ausência normalmente é verificada com `is None`, e não por inspeção de `NoneType`. Este exemplo existe para conectar `None` ao sistema de tipos, não para recomendar uma verificação de ausência mais longa.

## 16. A inspeção de tipos é uma ferramenta de diagnóstico

`type()` é especialmente útil durante o aprendizado, depuração, exploração de valores desconhecidos e verificação de suposições.

Por exemplo:

```python
value = "42"

print("Value:", value)
print("Type:", type(value))
```

A saída visível e a inspeção do tipo, juntas, fornecem mais informação do que qualquer uma delas isoladamente.

## 17. Evite espalhar verificações de tipo por toda parte

Um programa não se torna mais seguro apenas porque recebe `type()` ou `isinstance()` ao redor de cada valor.

Verificações em excesso podem:

- duplicar garantias já fornecidas em outra parte;
- deixar código simples barulhento;
- esconder um problema de desenho;
- rejeitar objetos úteis e compatíveis quando verificações exatas são rígidas demais.

Use inspeção quando a pergunta sobre o tipo for relevante para o programa.

## 18. Prefira comportamento quando o comportamento for o requisito real

Às vezes, um programa não precisa conhecer o tipo exato. Ele só precisa de um objeto que suporte determinada operação.

Essa ideia mais ampla costuma estar associada ao estilo de “duck typing” do Python. Ela se torna mais útil depois, quando você conhecer funções, exceções, protocolos e classes personalizadas.

Por enquanto, lembre-se: uma verificação de tipo deve responder a um requisito real, e não apenas satisfazer curiosidade dentro da lógica de produção.

## 19. Exemplos do repositório

| Arquivo | Finalidade | Execução automática |
|---|---|---|
| [`inspect_types.py`](examples/inspect_types.py) | Exibe os tipos exatos do conjunto de valores do Capítulo 04 | Sim |
| [`check_type_families.py`](examples/check_type_families.py) | Compara verificações exatas, `isinstance()`, tuplas de tipos e a relação `bool`/`int` | Sim |

Os dois exemplos são determinísticos, não interativos e adequados para verificações sem supervisão.

## 20. Exemplo prático: inspecione um pequeno catálogo de valores

Crie `inspect_types.py`:

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None

print("course_name:", type(course_name))
print("chapter_number:", type(chapter_number))
print("estimated_minutes:", type(estimated_minutes))
print("is_available:", type(is_available))
print("next_chapter:", type(next_chapter))
```

Saída esperada:

```text
course_name: <class 'str'>
chapter_number: <class 'int'>
estimated_minutes: <class 'float'>
is_available: <class 'bool'>
next_chapter: <class 'NoneType'>
```

## 21. Exemplo prático: tipo exato e tipo compatível

Crie `check_type_families.py`:

```python
whole_number = 5
decimal_number = 5.0
is_available = True

print("Exact int:", type(whole_number) is int)
print("Number family:", isinstance(whole_number, (int, float)))
print("Float in number family:", isinstance(decimal_number, (int, float)))
print("Exact bool:", type(is_available) is bool)
print("Bool is int-compatible:", isinstance(is_available, int))
```

Saída esperada:

```text
Exact int: True
Number family: True
Float in number family: True
Exact bool: True
Bool is int-compatible: True
```

## 22. Exercício

Crie `value_inspector.py` com estes nomes exatos:

```python
guide_name
chapter_number
completion_rate
is_published
review_note
```

Atribua um valor de cada tipo apresentado no Capítulo 04.

Depois:

1. imprima cada valor;
2. imprima o resultado de `type()` para cada valor;
3. use `isinstance()` para confirmar que `guide_name` é uma `str`;
4. use `isinstance()` para confirmar que `chapter_number` pertence a `(int, float)`;
5. teste se `completion_rate` pertence a `(int, float)`;
6. inspecione `is_published` com `type()` e também com `isinstance(..., int)`;
7. explique por que os resultados finais relacionados a booleanos não são contraditórios.

## 23. Erros comuns

### Comparar um objeto de tipo com texto

```text
type(value) == "str"
```

Use o objeto de tipo `str`, não a string `"str"`.

### Passar uma string para `isinstance()`

```text
isinstance(value, "str")
```

O argumento de tipo deve ser um objeto de tipo ou uma tupla aceita de objetos de tipo.

### Usar `int or float`

```text
isinstance(value, int or float)
```

Use:

```python
isinstance(value, (int, float))
```

### Presumir que `isinstance(True, int)` é falso

O resultado é `True` porque `bool` é uma subclasse de `int`.

### Usar verificações exatas quando subclasses devem contar

```python
type(value) is int
```

Isso rejeita valores cujo tipo deriva de `int`. Use `isinstance(value, int)` quando subclasses compatíveis também devam contar.

### Usar verificações de tipo em vez de entender os dados

Saber que um valor é `int` não informa se ele representa uma idade, quantidade, porcentagem ou identificador válido. Tipo e significado são preocupações relacionadas, mas diferentes.

## 24. Autoverificação

Você está pronto para o próximo capítulo quando conseguir responder:

- O que `type()` retorna?
- Por que `<class 'str'>` não é a mesma coisa que o texto `"str"`?
- Qual pergunta `isinstance()` responde?
- Como verificar se um valor é `int` ou `float`?
- Por que `isinstance(True, int)` é verdadeiro?
- Qual é o tipo exato de `True`?
- Quando uma verificação exata com `type()` é mais rígida que `isinstance()`?
- Por que verificações de tipo não devem ser adicionadas automaticamente em todo lugar?
- Qual tipo `input()` retorna?
- Qual problema a conversão de tipos resolverá no próximo capítulo?

## 25. Resumo para consulta rápida

| Objetivo | Exemplo |
|---|---|
| Inspecionar o tipo exato | `type(value)` |
| Verificar um tipo embutido exato | `type(value) is int` |
| Verificar um tipo compatível | `isinstance(value, int)` |
| Aceitar vários tipos | `isinstance(value, (int, float))` |
| Inspecionar o resultado de entrada | `type(response)` |
| Tipo booleano exato | `type(flag) is bool` |
| Booleano compatível com `int` | `isinstance(flag, int)` |
| Evitar comparação com string | Use `str`, não `"str"` |

## 26. Execute os exemplos do repositório

A partir da raiz do repositório:

```bash
python fundamentals/05-type-and-isinstance/examples/inspect_types.py
python fundamentals/05-type-and-isinstance/examples/check_type_families.py
```

## 27. Execute as verificações do repositório

A partir da raiz do repositório:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

Os dois exemplos deste capítulo estão aprovados para execução sem supervisão.

## Referências oficiais

- [Função embutida do Python — `type()`](https://docs.python.org/3/library/functions.html#type)
- [Função embutida do Python — `isinstance()`](https://docs.python.org/3/library/functions.html#isinstance)
- [Tipos embutidos do Python — valores booleanos](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
- [Modelo de dados do Python — objetos, valores e tipos](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Tipos de dados embutidos](../04-built-in-data-types/README.pt-BR.md)
