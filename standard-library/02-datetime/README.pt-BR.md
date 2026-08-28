# Trabalhando com Datas e Cálculos de Tempo Usando `datetime`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

O módulo `datetime` do Python fornece objetos explícitos para datas, horários, valores combinados de data e hora, durações, deslocamentos fixos de UTC, parsing, formatação, comparação e aritmética.

Strings como `"2026-08-27"` são úteis para armazenamento e comunicação, mas não sabem automaticamente quantos dias separam duas datas, se um ano é bissexto ou como somar uma duração corretamente. O módulo `datetime` dá tipos e regras próprios a esses conceitos.

Para a maior parte do trabalho iniciante e intermediário, os imports centrais são:

```python
from datetime import date, datetime, time, timedelta, timezone
```

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- distinguir `date`, `time`, `datetime` e `timedelta`;
- construir objetos de data e hora explicitamente;
- inspecionar componentes de ano, mês, dia, hora, minuto e segundo;
- usar `date.today()` e `datetime.now()` de forma consciente;
- fazer aritmética com `timedelta`;
- entender a diferença entre `timedelta.seconds` e `timedelta.total_seconds()`;
- fazer parsing com `strptime()` e formatação com `strftime()`;
- usar helpers ISO como `fromisoformat()` e `isoformat()`;
- distinguir objetos `datetime` naive e timezone-aware;
- representar UTC e offsets fixos com `timezone`;
- converter datetimes aware com `astimezone()`;
- entender por que atribuir `tzinfo` não é o mesmo que converter um horário;
- evitar tratar durações fixas como regras de meses do calendário;
- reconhecer quando fusos reais exigem o módulo complementar `zoneinfo`.

## 1. Por que usar tipos próprios para data e hora?

Considere duas strings:

```python
start = "2026-08-27"
end = "2026-09-03"
```

Uma pessoa percebe que parecem datas, mas o Python ainda vê strings comuns.

Com `date`, o significado fica explícito:

```python
from datetime import date

start = date(2026, 8, 27)
end = date(2026, 9, 3)

print(end - start)
```

A subtração produz um `timedelta`, pois o Python agora sabe que os valores representam datas de calendário.

A ideia de design é:

```text
texto para representação
        !=
objetos para comportamento de data/hora
```

## 2. As classes centrais

As classes mais usadas são:

| Classe | Representa |
|---|---|
| `date` | data de calendário: ano, mês e dia |
| `time` | horário sem uma data de calendário |
| `datetime` | data e horário juntos |
| `timedelta` | duração entre pontos no tempo |
| `timezone` | offset fixo em relação ao UTC |

Elas resolvem problemas relacionados, mas não são intercambiáveis.

## 3. Criando um `date`

Construa uma data com ano, mês e dia:

```python
from datetime import date

release_date = date(2026, 8, 27)

print(release_date.year)
print(release_date.month)
print(release_date.day)
```

Valores impossíveis falham imediatamente:

```python
from datetime import date

try:
    impossible = date(2026, 2, 30)
except ValueError:
    print("Invalid calendar date")
```

Essa validação é uma vantagem de usar um tipo de data em vez de transportar texto não validado pelo programa.

## 4. Criando um `time`

Um `time` representa um horário:

```python
from datetime import time

meeting_time = time(14, 30, 15)

print(meeting_time.hour)
print(meeting_time.minute)
print(meeting_time.second)
```

Um objeto `time` não contém ano, mês ou dia. Ele é útil quando o horário importa independentemente da data.

Não espere somar um `timedelta` diretamente a um `time` simples. A aritmética de horário normalmente precisa de um `datetime` ou de regras da aplicação sobre qual data deve ser usada.

## 5. Criando um `datetime`

Um `datetime` combina os dois conceitos:

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 14, 30, 15)

print(moment.date())
print(moment.time())
print(moment.year)
print(moment.hour)
```

Isso é útil para eventos, timestamps, prazos, logs, compromissos e outros valores em que data e horário importam.

## 6. Data e horário atuais

`date.today()` retorna a data local atual:

```python
from datetime import date

today = date.today()
print(today)
```

`datetime.now()` retorna a data e hora locais atuais como `datetime` naive por padrão:

```python
from datetime import datetime

now = datetime.now()
print(now)
```

Para um `datetime` UTC aware, prefira:

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)
```

Evite chamadas ao relógio real quando um teste ou exemplo determinístico puder usar um valor fixo.

### Evite `datetime.utcnow()` em código novo

`datetime.utcnow()` retorna um objeto naive mesmo representando UTC e está deprecated no Python moderno. Prefira `datetime.now(timezone.utc)` para que a relação com UTC fique explícita no próprio objeto.

## 7. O que é um `timedelta`?

Um `timedelta` representa uma duração.

```python
from datetime import timedelta

review_window = timedelta(days=7, hours=3)
print(review_window)
```

Ele pode ser somado ou subtraído de datas e datetimes:

```python
from datetime import date, timedelta

start = date(2026, 8, 27)
end = start + timedelta(days=10)

print(end)
```

Subtrair datas ou datetimes compatíveis produz um `timedelta`:

```python
from datetime import date

start = date(2026, 8, 27)
end = date(2026, 9, 3)

difference = end - start
print(difference.days)
```

## 8. `timedelta.seconds` não são os segundos totais

Este é um erro clássico.

```python
from datetime import timedelta

duration = timedelta(days=1, seconds=90)

print(duration.days)
print(duration.seconds)
print(duration.total_seconds())
```

`duration.seconds` é apenas a parte normalizada de segundos dentro do dia. Ela não inclui dias inteiros.

Use `total_seconds()` quando precisar da duração completa expressa em segundos.

No exemplo acima:

```text
componente de segundos = 90
duração total = 86490 segundos
```

## 9. Durações não são meses do calendário

Um `timedelta` modela durações fixas em dias, segundos e microssegundos. Ele não possui o conceito embutido de "um mês de calendário".

Isto:

```python
from datetime import date, timedelta

start = date(2026, 1, 31)
approximate = start + timedelta(days=30)

print(approximate)
```

significa exatamente "somar 30 dias". Não significa "ir para o mesmo dia do mês seguinte".

Regras de fechamento de mês, feriados, calendários comerciais e vencimentos são políticas da aplicação e precisam ser modeladas explicitamente.

## 10. Comparando datas e datetimes

Objetos compatíveis do mesmo tipo podem ser comparados:

```python
from datetime import date

deadline = date(2026, 9, 10)
today = date(2026, 9, 3)

if today <= deadline:
    print("Still on time")
```

Não compare strings formatadas só porque parecem datas. Alguns formatos ordenam cronologicamente, outros não, e comparação de strings não fornece semântica de calendário.

## 11. Fazendo parsing com `strptime()`

Dados externos frequentemente chegam como texto.

Use `datetime.strptime()` quando a entrada seguir um formato conhecido:

```python
from datetime import datetime

text = "27/08/2026 18:45"
moment = datetime.strptime(text, "%d/%m/%Y %H:%M")

print(moment)
```

A string de formato é um contrato entre seu código e a entrada.

Diretivas comuns:

| Diretiva | Significado |
|---|---|
| `%Y` | ano com quatro dígitos |
| `%m` | número do mês |
| `%d` | dia do mês |
| `%H` | hora de 00 a 23 |
| `%M` | minuto |
| `%S` | segundo |
| `%f` | microssegundos |
| `%z` | offset UTC |

Se o texto não corresponder ao formato esperado, o parsing gera `ValueError`.

```python
from datetime import datetime

try:
    moment = datetime.strptime("2026/08/27", "%Y-%m-%d")
except ValueError:
    print("Unexpected date format")
```

## 12. Formatando com `strftime()`

`strftime()` faz o caminho inverso: objeto para texto.

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 18, 45)

print(moment.strftime("%Y-%m-%d"))
print(moment.strftime("%d/%m/%Y %H:%M"))
```

Mantenha a distinção clara:

```text
strptime: texto -> datetime
strftime: datetime/date/time -> texto
```

## 13. Helpers orientados a ISO

Para representações em estilo ISO, métodos dedicados costumam ser mais claros que formatos customizados.

```python
from datetime import date, datetime

calendar_date = date.fromisoformat("2026-08-27")
moment = datetime.fromisoformat("2026-08-27T18:45:00+00:00")

print(calendar_date.isoformat())
print(moment.isoformat())
```

`fromisoformat()` e `isoformat()` são convenientes quando o contrato corresponde às formas suportadas pelo parser e formatador orientados a ISO do Python.

Não assuma que toda string chamada informalmente de "ISO 8601" será aceita por qualquer parser. O formato exato aceito faz parte do contrato da interface.

## 14. Controlando a precisão da saída ISO

`datetime.isoformat()` pode controlar a precisão exibida:

```python
from datetime import datetime

moment = datetime(2026, 8, 27, 18, 45, 12, 345678)

print(moment.isoformat(timespec="minutes"))
print(moment.isoformat(timespec="seconds"))
print(moment.isoformat(timespec="microseconds"))
```

Isso é útil quando um formato externo exige precisão específica.

## 15. Datetimes naive e aware

Um `datetime` pode ser **naive** ou **aware**.

Um datetime naive não contém informações suficientes de timezone para se posicionar de forma inequívoca em relação a outros instantes no mundo.

```python
from datetime import datetime

naive = datetime(2026, 8, 27, 18, 30)
print(naive.tzinfo)
```

Um datetime aware possui informação de timezone capaz de fornecer offset em relação ao UTC:

```python
from datetime import datetime, timezone

aware = datetime(2026, 8, 27, 18, 30, tzinfo=timezone.utc)
print(aware.tzinfo)
print(aware.utcoffset())
```

Essa diferença é importante em APIs, logs, sistemas distribuídos e agendamentos que atravessam fusos.

## 16. Representando UTC

Use `timezone.utc` para UTC:

```python
from datetime import datetime, timezone

moment = datetime(2026, 8, 27, 21, 30, tzinfo=timezone.utc)

print(moment.isoformat())
```

O resultado inclui o offset UTC:

```text
2026-08-27T21:30:00+00:00
```

## 17. Offsets UTC fixos

`timezone` pode representar offsets fixos:

```python
from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
moment = datetime(2026, 8, 27, 18, 30, tzinfo=brt)

print(moment.isoformat())
```

Um offset fixo como `-03:00` não é o mesmo que um fuso geográfico real. Fusos geográficos podem mudar de offset por regras históricas, horário de verão e mudanças legais.

## 18. Convertendo com `astimezone()`

Para um datetime aware, use `astimezone()` para representar o mesmo instante em outro timezone:

```python
from datetime import datetime, timedelta, timezone

brt = timezone(timedelta(hours=-3))
local = datetime(2026, 8, 27, 18, 30, tzinfo=brt)
utc = local.astimezone(timezone.utc)

print(local.isoformat())
print(utc.isoformat())
```

O horário exibido muda, mas os dois objetos representam o mesmo instante.

## 19. Atribuir `tzinfo` não é converter timezone

Este código altera metadados sem converter o valor do relógio:

```python
from datetime import datetime, timezone

naive = datetime(2026, 8, 27, 18, 30)
labeled = naive.replace(tzinfo=timezone.utc)

print(labeled.isoformat())
```

`replace(tzinfo=...)` não pergunta "que horas são 18:30 em outro fuso?". Ele cria um novo objeto com campos substituídos.

Use isso apenas quando você já souber qual timezone aquele horário naive deveria representar e anexar essa informação for a operação pretendida.

Para converter um datetime já aware entre fusos, use `astimezone()`.

## 20. Não misture aritmética naive e aware casualmente

Subtrair um datetime aware de um naive não possui significado sem uma relação explícita de timezone.

```python
from datetime import datetime, timezone

naive = datetime(2026, 8, 27, 18, 30)
aware = datetime(2026, 8, 27, 18, 30, tzinfo=timezone.utc)

try:
    difference = aware - naive
except TypeError:
    print("Cannot mix naive and aware datetimes")
```

Escolha e documente uma política de timezone nas fronteiras do sistema.

## 21. Fusos geográficos reais e `zoneinfo`

A biblioteca padrão inclui o módulo complementar `zoneinfo` para regras IANA como `America/Sao_Paulo` ou `Europe/London`.

Conceitualmente:

```python
from datetime import datetime
from zoneinfo import ZoneInfo

moment = datetime(2026, 8, 27, 18, 30, tzinfo=ZoneInfo("America/Sao_Paulo"))
print(moment.isoformat())
```

Diferentemente de `timezone(timedelta(...))`, `ZoneInfo` pode modelar regras históricas e futuras fornecidas pelo banco de dados de timezones disponível.

A disponibilidade desse banco depende do ambiente. Alguns sistemas o fornecem diretamente; outros podem precisar do pacote `tzdata`. Por isso, os exemplos executáveis deste capítulo usam offsets fixos.

## 22. Unix timestamps

Um Unix timestamp representa segundos decorridos a partir da convenção de epoch Unix da plataforma.

Crie um datetime UTC aware fornecendo timezone:

```python
from datetime import datetime, timezone

moment = datetime.fromtimestamp(0, tz=timezone.utc)
print(moment.isoformat())
```

Converta um datetime aware de volta com `.timestamp()`:

```python
from datetime import datetime, timezone

moment = datetime(1970, 1, 1, tzinfo=timezone.utc)
print(moment.timestamp())
```

Timestamps são úteis como valores de intercâmbio, mas legibilidade, faixa suportada, precisão e comportamento de plataforma ainda importam. Não os use como substitutos para compreender e definir uma política de timezone.

## 23. Substituindo campos

`replace()` retorna um novo objeto com campos selecionados alterados:

```python
from datetime import datetime

original = datetime(2026, 8, 27, 18, 30)
updated = original.replace(hour=9, minute=0)

print(original)
print(updated)
```

Ele não modifica o objeto original.

Isso é substituição de campos, não aritmética de calendário comercial. Alterar `month=2` em uma data cujo dia não existe em fevereiro pode gerar `ValueError`.

## 24. Combinando data e horário

`datetime.combine()` é útil quando valores separados precisam se tornar um único datetime:

```python
from datetime import date, datetime, time

calendar_date = date(2026, 8, 27)
clock_time = time(18, 30)
moment = datetime.combine(calendar_date, clock_time)

print(moment)
```

O resultado é naive, a menos que informação de timezone seja fornecida por um design explícito.

## 25. Erros comuns

### Erro 1: armazenar tudo como string

Strings são apropriadas nas fronteiras, mas cálculos devem normalmente usar objetos de data/hora.

### Erro 2: tratar `timedelta.seconds` como duração inteira

Use `total_seconds()` quando precisar incluir os dias.

### Erro 3: usar `timedelta(days=30)` como "um mês"

Isso significa 30 dias, não um mês de calendário.

### Erro 4: fazer parsing sem contrato explícito

Se a entrada tem formato definido, codifique esse formato deliberadamente e trate `ValueError` quando a entrada puder ser inválida.

### Erro 5: misturar datetimes naive e aware

Defina se o sistema usa horário local, UTC ou fusos explícitos em cada fronteira.

### Erro 6: usar `replace(tzinfo=...)` como conversão

Substituição de campo e conversão de timezone são operações diferentes.

### Erro 7: usar offset fixo como se fosse fuso geográfico

Regras reais podem mudar. Use `zoneinfo` quando regras geográficas importarem.

### Erro 8: usar o relógio real em testes determinísticos

Injete ou construa datetimes fixos quando a reprodutibilidade for importante.

## 26. Exemplo prático

Imagine um relatório que recebe um timestamp UTC em texto, faz parsing, aplica um offset local fixo para apresentação e calcula um prazo de revisão.

```python
from datetime import datetime, timedelta, timezone

source = "2026-08-27T21:30:00+00:00"
created_utc = datetime.fromisoformat(source)

local_zone = timezone(timedelta(hours=-3))
created_local = created_utc.astimezone(local_zone)
deadline = created_local + timedelta(days=5)

print(created_local.isoformat())
print(deadline.isoformat())
```

O fluxo fica explícito:

```text
contrato de texto
    ↓
datetime aware
    ↓
conversão de timezone
    ↓
aritmética de duração
    ↓
saída formatada
```

## 27. Exercício

Crie um programa que:

1. faça parsing de `"2026-10-15 09:30"` usando `strptime()`;
2. trate esse valor como horário de parede com offset fixo `-03:00`;
3. some 2 dias e 4 horas com `timedelta`;
4. converta o resultado para UTC com `astimezone()`;
5. imprima os valores local e UTC com `isoformat()`;
6. imprima a duração completa em segundos;
7. formate o resultado UTC como `YYYY-MM-DD HH:MM`.

Depois responda:

- Quais objetos são naive e quais são aware?
- Por que `replace(tzinfo=...)` é aceitável para anexar o offset conhecido da origem aqui, mas não para converter entre fusos?
- Por que `total_seconds()` deve ser usado em vez de `.seconds` para a duração completa?
- Por que um offset fixo `-03:00` não equivale automaticamente a todas as regras históricas ou futuras de `America/Sao_Paulo`?

## 28. Checklist de revisão

Antes de avançar, confirme que você consegue explicar:

- `date`, `time`, `datetime`, `timedelta` e `timezone`;
- construção e validação de valores de calendário;
- `date.today()` e `datetime.now()`;
- por que UTC aware deve usar `datetime.now(timezone.utc)`;
- aritmética de datas e datetimes;
- `.days`, `.seconds` e `.total_seconds()`;
- por que durações fixas não são meses de calendário;
- `strptime()` versus `strftime()`;
- `fromisoformat()` e `isoformat()`;
- datetimes naive versus aware;
- UTC e offsets fixos;
- `astimezone()` versus `replace(tzinfo=...)`;
- por que regras de fusos geográficos pertencem ao `zoneinfo`;
- timestamps como valores de intercâmbio;
- como manter testes determinísticos.

## Referência rápida

```python
from datetime import date, datetime, time, timedelta, timezone

calendar_date = date(2026, 8, 27)
clock_time = time(18, 30)
moment = datetime(2026, 8, 27, 18, 30)
duration = timedelta(days=2, hours=4)

calendar_date + timedelta(days=1)
moment + duration

datetime.strptime("2026-08-27 18:30", "%Y-%m-%d %H:%M")
moment.strftime("%d/%m/%Y %H:%M")

date.fromisoformat("2026-08-27")
datetime.fromisoformat("2026-08-27T18:30:00+00:00")
moment.isoformat()

aware_utc = datetime(2026, 8, 27, 21, 30, tzinfo=timezone.utc)
fixed_offset = timezone(timedelta(hours=-3))
aware_utc.astimezone(fixed_offset)

duration.total_seconds()
```

## Exemplos executáveis

- [`examples/date_arithmetic.py`](examples/date_arithmetic.py)
- [`examples/parse_and_format.py`](examples/parse_and_format.py)
- [`examples/utc_conversion.py`](examples/utc_conversion.py)
- [`examples/duration_seconds.py`](examples/duration_seconds.py)

Os exemplos são determinísticos e não dependem do relógio atual nem de um banco externo de timezones.

## Próximo capítulo

Continue com **Capítulo 03: `json` Além da Persistência Básica**, onde a biblioteca padrão revisita serialização JSON com controle mais profundo de encoders, decoders, formatação, hooks numéricos e contratos rigorosos de interoperabilidade.

## Referências oficiais

- [Python 3.14 `datetime` - tipos básicos de data e hora](https://docs.python.org/3.14/library/datetime.html)
- [Python 3.14 códigos de formato de `strftime()` e `strptime()`](https://docs.python.org/3.14/library/datetime.html#strftime-and-strptime-format-codes)
- [Python 3.14 `zoneinfo` - suporte a fusos IANA](https://docs.python.org/3.14/library/zoneinfo.html)
