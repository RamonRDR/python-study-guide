<div align="center">

# Dicionários: Chaves e Valores

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Tuplas e imutabilidade](../03-tuples-and-immutability/README.pt-BR.md) · [Voltar ao índice de Coleções](../README.pt-BR.md) · [Próximo capítulo: Conjuntos e valores únicos →](../05-sets-and-unique-values/README.pt-BR.md)

Listas e tuplas organizam valores por **posição**. Dicionários apresentam um modelo diferente: cada valor armazenado é associado a uma **chave**.

Essa mudança é poderosa porque uma chave pode descrever o que um valor significa. Em vez de lembrar que um nome está na posição `0`, você pode pedir o valor armazenado sob a chave `"name"`.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 a 03 de Coleções |
| Tempo estimado de estudo | 120 a 150 minutos |
| Conceitos principais | mapeamentos, chaves, valores, literais de dicionário, busca, `get()`, mutação, `update()`, remoção, pertencimento, ordem de inserção, chaves hashable, views de dicionário, `copy()` |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar como um dicionário difere de uma sequência posicional;
- criar dicionários vazios e preenchidos;
- identificar chaves e seus valores associados;
- ler um valor com `dictionary[key]`;
- explicar por que uma busca direta por uma chave ausente gera `KeyError`;
- usar `get()` quando uma chave ausente deve retornar um valor alternativo em vez de gerar `KeyError`;
- adicionar um novo par chave-valor por atribuição;
- atualizar o valor associado a uma chave existente;
- combinar entradas com `update()`;
- remover entradas com `del`, `pop()` e `clear()`;
- testar pertencimento de chaves com `in` e `not in`;
- explicar que as chaves de um dicionário são únicas;
- reconhecer tipos de chave comuns e seguros para iniciantes e compreender o significado prático de *hashable*;
- inspecionar `keys()`, `values()` e `items()`;
- explicar ordem de inserção sem tratar um dicionário como uma sequência posicional;
- distinguir outra referência ao mesmo dicionário de uma cópia rasa;
- escolher um dicionário quando valores são naturalmente identificados por chaves significativas.

## 1. De posições para chaves

Considere uma tupla que representa uma pessoa fictícia estudando:

```python
learner = ("Ana", "Python", "beginner")

print(learner[0])
print(learner[1])
```

```text
Ana
Python
```

Isso funciona, mas o significado das posições `0` e `1` precisa ser lembrado separadamente.

Um dicionário torna essas relações explícitas:

```python
learner = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print(learner["name"])
print(learner["track"])
```

```text
Ana
Python
```

As chaves `"name"` e `"track"` descrevem os valores que identificam.

Essa é a ideia central de um dicionário:

**chave → valor**

## 2. O que é um dicionário

O tipo de dicionário embutido do Python é `dict`.

Um dicionário é um **mapeamento**. Um mapeamento associa chaves a valores em vez de atribuir valores a posições numeradas.

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
    "available": True,
}

print(type(course))
```

```text
<class 'dict'>
```

O dicionário contém três entradas. Cada entrada possui uma chave e um valor associado.

## 3. Sintaxe de literal de dicionário

Um literal de dicionário usa chaves com pares `key: value` separados por vírgulas:

```python
profile = {
    "name": "Mina",
    "city": "Lisbon",
    "active": True,
}
```

Leia cada par da esquerda para a direita:

- `"name"` mapeia para `"Mina"`;
- `"city"` mapeia para `"Lisbon"`;
- `"active"` mapeia para `True`.

Em dicionários com várias linhas, uma vírgula final após a última entrada é um estilo comum e legível.

## 4. Criando um dicionário vazio

Use chaves vazias para criar um dicionário vazio:

```python
settings = {}

print(settings)
print(type(settings))
print(len(settings))
```

```text
{}
<class 'dict'>
0
```

Isso será importante novamente no próximo capítulo: `{}` cria um **dicionário** vazio, não um conjunto vazio.

## 5. Chaves e valores têm papéis diferentes

Uma chave identifica uma entrada. Um valor é a informação associada àquela chave.

```python
book = {
    "title": "A Small Python Book",
    "pages": 180,
    "finished": False,
}
```

Aqui:

- as chaves são `"title"`, `"pages"` e `"finished"`;
- os valores são `"A Small Python Book"`, `180` e `False`.

Os valores não precisam ter o mesmo tipo.

## 6. Lendo um valor com colchetes

Use uma chave entre colchetes para recuperar seu valor:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

print(profile["name"])
print(profile["level"])
```

```text
Ana
beginner
```

Os colchetes podem parecer familiares por causa de listas e tuplas, mas o modelo de busca é diferente.

Em uma lista, a expressão entre colchetes normalmente é uma posição inteira. Em um dicionário, ela é uma chave.

## 7. Um dicionário não é indexado por posição

A ordem de inserção não transforma um dicionário em uma lista.

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

print(profile[0])
```

O dicionário acima não possui a chave `0`, portanto essa busca gera `KeyError`.

Se um dicionário realmente possui uma chave inteira, esse inteiro funciona porque é uma chave, não porque é uma posição:

```python
labels = {
    0: "zero",
    10: "ten",
}

print(labels[10])
```

```text
ten
```

Mantenha os dois modelos separados:

- sequência: **posição → valor**;
- dicionário: **chave → valor**.

## 8. Chaves ausentes e `KeyError`

Uma busca direta exige que a chave exista:

```python
profile = {
    "name": "Ana",
}

print(profile["city"])
```

Como `"city"` está ausente, o Python gera `KeyError`.

Isso é útil quando uma chave ausente representa um erro de programação ou uma suposição inválida. Mais adiante, os capítulos sobre tratamento de erros mostrarão como exceções podem ser tratadas de forma deliberada.

## 9. Lendo com segurança usando `get()`

`get()` lê uma chave sem gerar `KeyError` quando ela está ausente:

```python
profile = {
    "name": "Ana",
}

print(profile.get("name"))
print(profile.get("city"))
```

```text
Ana
None
```

Sem um valor alternativo explícito, `get()` retorna `None` para uma chave ausente.

## 10. Fornecendo um valor alternativo para `get()`

Passe um segundo argumento quando outro valor alternativo comunicar a situação com mais clareza:

```python
profile = {
    "name": "Ana",
}

print(profile.get("city", "not provided"))
print(profile.get("level", "unknown"))
```

```text
not provided
unknown
```

O valor alternativo é retornado somente quando a chave solicitada está ausente. `get()` não adiciona essa chave ao dicionário.

## 11. Um `None` armazenado e uma chave ausente podem parecer iguais

Essa diferença importa:

```python
profile = {
    "nickname": None,
}

print(profile.get("nickname"))
print(profile.get("city"))
```

```text
None
None
```

O primeiro `None` está armazenado no dicionário. O segundo `None` é o resultado padrão para uma chave ausente.

Quando seu programa precisar diferenciar esses casos, o pertencimento da chave se torna importante.

## 12. Contando entradas com `len()`

`len()` retorna a quantidade de entradas chave-valor:

```python
profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print(len(profile))
```

```text
3
```

Uma chave e seu valor associado contam juntos como uma entrada do dicionário.

## 13. Pertencimento verifica chaves por padrão

Os operadores `in` e `not in` testam as **chaves** do dicionário:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("name" in profile)
print("Python" in profile)
print("city" not in profile)
```

```text
True
False
True
```

`"Python"` é um valor, não uma chave, então `"Python" in profile` é `False`.

Para testar explicitamente os valores atuais, use a view de valores:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("Python" in profile.values())
```

```text
True
```

## 14. Adicionando uma nova entrada por atribuição

Atribua a uma chave que ainda não existe:

```python
profile = {
    "name": "Ana",
}

profile["track"] = "Python"
profile["active"] = True

print(profile)
```

```text
{'name': 'Ana', 'track': 'Python', 'active': True}
```

Diferente da atribuição direta a um item de lista, a atribuição em dicionários não exige que uma posição numérica já exista. Uma nova chave cria uma nova entrada.

## 15. Atualizando um valor existente

Atribua a uma chave que já existe para substituir seu valor associado:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

profile["level"] = "intermediate"

print(profile)
```

```text
{'name': 'Ana', 'level': 'intermediate'}
```

A chave permanece a mesma. Seu valor muda.

Isso é mutação de dicionário: dicionários são objetos mutáveis.

## 16. As chaves de um dicionário são únicas

Um dicionário não pode conter duas entradas separadas com chaves iguais ao mesmo tempo.

Se a mesma chave aparecer mais de uma vez durante a construção de um dicionário, o valor posterior passa a ser o valor associado àquela chave:

```python
profile = {
    "name": "Ana",
    "name": "Mina",
}

print(profile)
```

```text
{'name': 'Mina'}
```

Embora o Python defina esse comportamento, repetir uma chave literal normalmente prejudica a legibilidade. Prefira uma entrada clara por chave.

Os valores, por outro lado, podem se repetir:

```python
scores = {
    "first": 10,
    "second": 10,
}

print(scores)
```

```text
{'first': 10, 'second': 10}
```

## 17. Atualizando várias entradas com `update()`

`update()` aplica entradas de outro mapeamento ou fonte compatível ao dicionário existente:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

profile.update({
    "level": "intermediate",
    "active": True,
})

print(profile)
```

```text
{'name': 'Ana', 'level': 'intermediate', 'active': True}
```

O valor existente de `"level"` foi substituído, enquanto `"active"` foi adicionado.

Assim como vários métodos de mutação in-place vistos em listas, `dict.update()` retorna `None`.

## 18. Removendo uma entrada com `del`

Use `del` quando você conhece a chave e não precisa do valor removido:

```python
profile = {
    "name": "Ana",
    "temporary": True,
}

del profile["temporary"]

print(profile)
```

```text
{'name': 'Ana'}
```

Se a chave estiver ausente, `del dictionary[key]` gera `KeyError`.

## 19. Removendo e retornando com `pop()`

`pop(key)` remove uma entrada e retorna seu valor:

```python
settings = {
    "theme": "dark",
    "language": "en",
}

removed_language = settings.pop("language")

print("Removed:", removed_language)
print("Settings:", settings)
```

```text
Removed: en
Settings: {'theme': 'dark'}
```

Isso repete uma ideia útil das listas: `pop()` altera a coleção e também fornece o valor removido.

Você também pode fornecer um valor alternativo para uma chave ausente:

```python
settings = {
    "theme": "dark",
}

removed = settings.pop("language", "not set")

print(removed)
print(settings)
```

```text
not set
{'theme': 'dark'}
```

Com um valor alternativo, a chave ausente não gera `KeyError`.

## 20. Removendo todas as entradas com `clear()`

`clear()` mantém o objeto dicionário, mas remove todas as suas entradas:

```python
settings = {
    "theme": "dark",
    "language": "en",
}

settings.clear()

print(settings)
print(len(settings))
```

```text
{}
0
```

`clear()` altera o dicionário in-place e retorna `None`.

## 21. Dicionários preservam a ordem de inserção

A partir do Python 3.7, preservar a ordem de inserção dos dicionários é uma garantia da especificação da linguagem Python. O CPython 3.6 também preservava a ordem de inserção, mas apenas como detalhe de implementação, portanto código destinado ao Python 3.6 não deve tratar esse comportamento como garantia da linguagem em todas as implementações.

Isso significa que, no Python 3.7 e posteriores, as entradas são observadas na ordem em que suas chaves foram inseridas:

```python
profile = {}

profile["name"] = "Ana"
profile["track"] = "Python"
profile["level"] = "beginner"

print(profile)
```

```text
{'name': 'Ana', 'track': 'Python', 'level': 'beginner'}
```

Atualizar o valor de uma chave existente não move essa chave para uma nova posição:

```python
profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

profile["track"] = "Data"

print(profile)
```

```text
{'name': 'Ana', 'track': 'Data', 'level': 'beginner'}
```

A ordem é útil para observação previsível, mas a busca em dicionários continua baseada em chaves, não em posições numeradas.

## 22. Que tipos de valores podem ser chaves?

As chaves de um dicionário precisam ser **hashable**.

Para uma pessoa iniciante, o modelo prático é:

- strings são usadas com frequência como chaves;
- inteiros podem ser chaves;
- Booleanos podem ser chaves, embora chaves de string descritivas muitas vezes sejam mais claras para registros;
- tuplas podem ser chaves quando todo o seu conteúdo é hashable;
- listas, dicionários e conjuntos não podem ser chaves de dicionário.

Uma chave hashable possui um valor de hash estável adequado para busca em dicionários e segue as regras de igualdade/hash do Python. Você não precisa implementar hashing por conta própria para usar dicionários comuns.

Isto funciona:

```python
coordinates = {
    (10, 20): "checkpoint",
}

print(coordinates[(10, 20)])
```

```text
checkpoint
```

Isto não funciona porque uma lista é mutável e unhashable:

```python
invalid = {
    [10, 20]: "checkpoint",
}
```

O Python gera `TypeError` ao tentar usar a lista como chave.

## 23. Valores de dicionário são flexíveis

Valores não possuem a mesma restrição das chaves. Um valor pode ser uma string, número, Booleano, lista, tupla, outro dicionário ou muitos outros objetos Python.

```python
profile = {
    "name": "Ana",
    "topics": ["strings", "lists"],
    "progress": (3, 6),
}

print(profile["topics"])
print(profile["progress"])
```

```text
['strings', 'lists']
(3, 6)
```

Um valor mutável dentro de um dicionário ainda pode ser alterado:

```python
profile = {
    "name": "Ana",
    "topics": ["strings"],
}

profile["topics"].append("lists")

print(profile)
```

```text
{'name': 'Ana', 'topics': ['strings', 'lists']}
```

O dicionário mapeia `"topics"` para uma lista, e essa lista possui seu próprio comportamento de mutabilidade.

## 24. Inspecionando chaves com `keys()`

`keys()` retorna uma view de dicionário contendo as chaves atuais:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.keys())
print(list(course.keys()))
```

```text
dict_keys(['title', 'phase', 'chapter'])
['title', 'phase', 'chapter']
```

Converter a view com `list()` é útil quando você precisa especificamente de uma lista separada das chaves atuais.

## 25. Inspecionando valores com `values()`

`values()` retorna uma view dos valores atuais:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.values())
print(list(course.values()))
```

```text
dict_values(['Python', 3, 4])
['Python', 3, 4]
```

Lembre que os valores não precisam ser únicos.

## 26. Inspecionando pares com `items()`

`items()` retorna uma view de pares chave-valor:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.items())
print(list(course.items()))
```

```text
dict_items([('title', 'Python'), ('phase', 3), ('chapter', 4)])
[('title', 'Python'), ('phase', 3), ('chapter', 4)]
```

Cada par se comporta como uma tupla de dois itens contendo a chave e seu valor.

Na Fase 4, loops tornarão `items()` especialmente útil porque você poderá processar esses pares um de cada vez.

## 27. Views de dicionário refletem alterações posteriores

Os objetos retornados por `keys()`, `values()` e `items()` são **views**, não snapshots congelados.

```python
profile = {
    "name": "Ana",
}

keys_view = profile.keys()
profile["level"] = "beginner"

print(list(keys_view))
```

```text
['name', 'level']
```

A view reflete o dicionário atual.

Se você precisar de um snapshot separado em código iniciante, converter a view para uma lista cria uma lista separada naquele momento.

## 28. Criando dicionários com `dict()`

O construtor `dict()` também pode criar dicionários.

A construção no estilo de argumentos nomeados é concisa quando as chaves de string desejadas são identificadores Python válidos e não são palavras reservadas:

```python
profile = dict(name="Ana", level="beginner")

print(profile)
```

```text
{'name': 'Ana', 'level': 'beginner'}
```

Como você já conhece tuplas e listas, também pode compreender uma sequência de pares chave-valor:

```python
pairs = [
    ("name", "Ana"),
    ("level", "beginner"),
]

profile = dict(pairs)

print(profile)
```

```text
{'name': 'Ana', 'level': 'beginner'}
```

Literais de dicionário muitas vezes são a escolha mais clara para registros fixos escritos diretamente no código, mas `dict()` é útil quando seus dados já existem em outra forma compatível.

## 29. Outro nome não é uma cópia

Dicionários são mutáveis, então a lição de compartilhamento de referência das listas se aplica novamente:

```python
original = {
    "theme": "light",
}

alias = original
alias["theme"] = "dark"

print("Original:", original)
print("Alias:", alias)
```

```text
Original: {'theme': 'dark'}
Alias: {'theme': 'dark'}
```

As duas variáveis se referem ao mesmo dicionário.

## 30. Criando uma cópia rasa com `copy()`

`copy()` cria um dicionário externo separado:

```python
original = {
    "theme": "light",
    "language": "en",
}

copied = original.copy()
copied["theme"] = "dark"

print("Original:", original)
print("Copied:", copied)
```

```text
Original: {'theme': 'light', 'language': 'en'}
Copied: {'theme': 'dark', 'language': 'en'}
```

Assim como `list.copy()`, `dict.copy()` é **rasa**. Objetos mutáveis aninhados continuam compartilhados, a menos que sejam copiados separadamente.

Esse tema de cópia profunda pertence a uma etapa posterior. Por enquanto, lembre que `copy()` separa o próprio dicionário externo.

## 31. Quando um dicionário é uma boa escolha

Um dicionário costuma ser uma boa escolha quando:

- cada valor possui um rótulo ou identificador significativo;
- você quer recuperar informações por esse rótulo;
- a relação entre campos importa mais do que posições numeradas;
- você precisa adicionar ou atualizar campos por chave.

Por exemplo:

```python
student = {
    "name": "Mina",
    "track": "Python",
    "completed_chapters": 3,
}
```

As chaves tornam o registro autoexplicativo.

Uma lista normalmente é mais clara quando a ideia principal é uma série ordenada de itens semelhantes. Uma tupla é útil quando a forma ordenada é intencionalmente fixa. O capítulo final de Coleções comparará diretamente os quatro tipos de coleção.

## 32. Exemplo prático: atualizar um perfil de estudos

```python
study_profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

study_profile["level"] = "intermediate"
study_profile["active"] = True
study_profile["topics"] = ["lists", "tuples", "dictionaries"]
removed_active = study_profile.pop("active")

print("Name:", study_profile["name"])
print("Level:", study_profile.get("level"))
print("Removed active:", removed_active)
print("Keys:", list(study_profile.keys()))
print("Profile:", study_profile)
```

```text
Name: Ana
Level: intermediate
Removed active: True
Keys: ['name', 'track', 'level', 'topics']
Profile: {'name': 'Ana', 'track': 'Python', 'level': 'intermediate', 'topics': ['lists', 'tuples', 'dictionaries']}
```

Este exemplo combina busca, atualização, adição, remoção e inspeção de chaves sem precisar de loops ou condicionais.

## 33. Erros comuns

### Tratar um dicionário como uma lista

`dictionary[0]` não significa “a primeira entrada”, a menos que `0` seja literalmente uma chave.

### Assumir que `in` procura valores

`value in dictionary` testa chaves. Use `value in dictionary.values()` quando você precisar intencionalmente testar pertencimento entre valores.

### Usar busca direta para uma chave opcional

`dictionary[key]` gera `KeyError` quando a chave está ausente. `get()` pode retornar um valor alternativo quando a ausência é esperada.

### Esquecer que `get()` não adiciona a chave

Ler `dictionary.get("city", "unknown")` retorna o valor alternativo, mas deixa o dicionário inalterado.

### Assumir que todo `None` vindo de `get()` significa “ausente”

Uma chave pode armazenar `None` legitimamente. Use informação de pertencimento quando seu programa precisar diferenciar esses casos.

### Esperar que chaves duplicadas criem entradas duplicadas

As chaves são únicas dentro de um dicionário. Atribuir ou construir a mesma chave novamente substitui o valor associado.

### Usar uma lista como chave de dicionário

Listas são unhashable e não podem ser chaves. Use um valor hashable adequado.

### Esquecer que dicionários são mutáveis

Outra variável pode se referir ao mesmo dicionário. Uma simples atribuição não o copia.

### Assumir que `copy()` duplica valores mutáveis aninhados

`dict.copy()` é rasa. Ela separa o dicionário externo, não todos os objetos armazenados dentro dele.

### Confundir ordem de inserção com busca posicional

A ordem do dicionário é preservada, mas a busca continua baseada em chaves.

## 34. Legibilidade e desenho de chaves

Boas chaves de dicionário tornam os dados mais fáceis de compreender.

Prefira chaves que descrevam claramente o significado de seus valores:

```python
profile = {
    "name": "Ana",
    "completed_chapters": 4,
    "is_active": True,
}
```

Compare isso com chaves vagas como `"a"`, `"b"` e `"c"`. A versão mais curta pode economizar caracteres, mas força quem lê a memorizar significados escondidos.

O mesmo princípio de nomes usado em variáveis vale para chaves de dicionário: escolha nomes que tornem a relação visível.

## 35. Conexões com conceitos anteriores e posteriores

Este capítulo reutiliza ideias que você já conhece:

- colchetes foram apresentados com sequências, mas agora contêm chaves em vez de posições;
- dicionários são mutáveis como listas;
- `copy()` de dicionário repete a ideia de cópia rasa das listas;
- tuplas podem servir como chaves de dicionário quando seu conteúdo é hashable;
- listas podem aparecer como valores de dicionário e manter seu próprio comportamento de mutabilidade;
- `len()` e operadores de pertencimento funcionam com um novo modelo de coleção.

Ele também prepara conceitos posteriores:

- conjuntos reutilizarão a ideia de valores hashable e colocarão unicidade no centro;
- loops da Fase 4 percorrerão chaves, valores e pares chave-valor repetidamente;
- funções frequentemente receberão ou retornarão dicionários que representam dados estruturados;
- o trabalho com JSON mais adiante no guia parecerá familiar porque objetos JSON se parecem com mapeamentos de chaves de string, embora JSON e dicionários Python não sejam conceitos idênticos.

## 36. Exercício: construir e manter um registro de aprendizagem

Crie `learning_record.py` com este dicionário inicial:

```python
record = {
    "name": "Mina",
    "track": "Python",
    "level": "beginner",
}
```

Sem usar loops ou condicionais:

1. imprima o valor associado a `"name"` usando busca com colchetes;
2. imprima `"city"` com `get()` e o valor alternativo `"not provided"`;
3. altere `"level"` para `"intermediate"`;
4. adicione a chave `"active"` com valor `True`;
5. adicione `"topics"` com a lista `["lists", "tuples"]`;
6. acrescente `"dictionaries"` à lista armazenada em `"topics"`;
7. imprima a quantidade de entradas com `len()`;
8. imprima se `"track"` é uma chave;
9. remova `"active"` com `pop()` e armazene seu valor em `removed_active`;
10. imprima `removed_active`;
11. imprima as chaves como uma lista;
12. imprima os valores como uma lista;
13. crie uma cópia rasa chamada `record_copy`;
14. altere somente `record_copy["level"]` para `"advanced"`;
15. imprima os dois dicionários e confirme que a entrada externa `"level"` mudou somente na cópia.

Um possível formato de saída final é:

```text
Name: Mina
City: not provided
Entries: 5
Has track: True
Removed active: True
Keys: ['name', 'track', 'level', 'topics']
Values: ['Mina', 'Python', 'intermediate', ['lists', 'tuples', 'dictionaries']]
Original: {'name': 'Mina', 'track': 'Python', 'level': 'intermediate', 'topics': ['lists', 'tuples', 'dictionaries']}
Copy: {'name': 'Mina', 'track': 'Python', 'level': 'advanced', 'topics': ['lists', 'tuples', 'dictionaries']}
```

Tente prever o dicionário após cada mutação antes de executar o programa.

## 37. Autoavaliação

Antes de avançar, confirme se consegue responder estas perguntas:

1. Qual é a principal diferença de busca entre uma sequência e um dicionário?
2. O que `dictionary[key]` faz quando a chave está ausente?
3. O que `get()` retorna para uma chave ausente quando nenhum valor alternativo é fornecido?
4. `get()` adiciona uma chave ausente?
5. O que `in` testa em um dicionário por padrão?
6. O que acontece quando você atribui a uma nova chave?
7. O que acontece quando você atribui a uma chave existente?
8. Um dicionário pode conter duas chaves iguais separadas ao mesmo tempo?
9. Por que uma string normalmente pode ser uma chave enquanto uma lista não pode?
10. O que `keys()`, `values()` e `items()` expõem?
11. A ordem de inserção torna posições inteiras índices válidos de um dicionário?
12. O que `pop(key)` retorna?
13. Por que mutações feitas por um alias podem afetar o dicionário original?
14. O que `copy()` separa e sobre o que a palavra *rasa* alerta?

Se alguma resposta parecer incerta, volte à seção correspondente e altere um dos exemplos por conta própria.

## 38. Referência rápida

- Criar um dicionário vazio: `data = {}`
- Criar entradas: `data = {"key": "value"}`
- Ler uma chave existente: `value = data["key"]`
- Ler com valor alternativo: `value = data.get("key", fallback)`
- Contar entradas: `len(data)`
- Testar uma chave: `"key" in data`
- Testar um valor explicitamente: `value in data.values()`
- Adicionar ou substituir: `data["key"] = value`
- Aplicar várias entradas: `data.update(other)`
- Excluir por chave: `del data["key"]`
- Remover e retornar: `removed = data.pop("key")`
- Esvaziar o dicionário: `data.clear()`
- Inspecionar chaves: `data.keys()`
- Inspecionar valores: `data.values()`
- Inspecionar pares chave-valor: `data.items()`
- Criar uma cópia rasa externa: `other = data.copy()`

Lembre do modelo:

- chaves identificam entradas;
- chaves são únicas e precisam ser hashable;
- valores podem se repetir e podem ser mutáveis;
- dicionários são mutáveis;
- dicionários preservam ordem de inserção;
- ordem preservada não cria indexação posicional.

## 39. Para onde ir agora

Agora você conhece três modelos diferentes de coleção:

1. **Lista:** posições ordenadas que podem ser alteradas.
2. **Tupla:** posições ordenadas cuja estrutura da tupla não pode ser alterada.
3. **Dicionário:** chaves significativas mapeadas para valores.

O próximo capítulo de Coleções apresenta **conjuntos e valores únicos**. Conjuntos removerão completamente os pares chave-valor e a busca posicional, colocando unicidade e pertencimento no centro do modelo.

---

Referências oficiais usadas para verificação técnica:

- [Tutorial do Python: Dicionários](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Tipos embutidos do Python: Tipo mapeamento — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Glossário do Python: hashable](https://docs.python.org/3/glossary.html#term-hashable)
