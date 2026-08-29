<div align="center">

# Consumindo APIs HTTP com `requests`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Bibliotecas Externas](../README.pt-BR.md) · [← Anterior: `openpyxl`](../02-openpyxl/README.pt-BR.md)

Arquivos locais são apenas um tipo de fronteira. Programas Python modernos também trocam dados com serviços web, APIs internas, plataformas SaaS, servidores de autenticação, endpoints de armazenamento e outros sistemas por HTTP. O pacote `requests` oferece ao Python um cliente HTTP compacto e legível, mantendo visíveis os conceitos de protocolo necessários para integrações confiáveis.

Este capítulo mira a série **Requests 2.34.x** e foi pesquisado com base na documentação e nos metadados atuais do **Requests 2.34.2**. Requests 2.34.2 exige Python 3.10 ou superior; este repositório valida os exemplos em Python 3.13.

**Tempo estimado de estudo:** 270–360 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o modelo HTTP de requisição/resposta sem tratar uma chamada de API como uma função mágica;
- executar GET, POST, PUT, PATCH e DELETE de forma intencional;
- enviar parâmetros de query, headers, dados de formulário, corpos JSON, arquivos e dados de autenticação;
- distinguir sucesso de transporte, sucesso HTTP e validade do payload;
- configurar timeouts de conexão/leitura e entender o que eles não garantem;
- tratar exceções do Requests sem esconder contexto útil;
- usar `Session` para reutilização de conexões, cookies e padrões compartilhados;
- entender redirects, verificação TLS, bundles de CA, proxies e configurações de ambiente;
- processar respostas grandes por streaming e fechar recursos deterministicamente;
- adicionar retries apenas quando a operação puder ser repetida com segurança;
- proteger credenciais e evitar registrar segredos;
- validar contratos de resposta em vez de confiar em JSON arbitrário;
- construir testes HTTP determinísticos sem depender de um serviço público na internet.

## 1. Por que `requests` existe

A biblioteca padrão do Python consegue falar HTTP, mas `requests` oferece uma interface de nível mais alto para trabalho comum de cliente: URLs, parâmetros de query, headers, cookies, autenticação, corpos de requisição, verificação TLS, Sessions, streaming e exceções.

A conveniência é valiosa, mas a rede continua sendo uma fronteira de sistema distribuído. Uma API legível não elimina latência, falhas parciais, regras de autenticação, erros de servidor, retries ou decisões de segurança.

## 2. Pense em requisições e respostas

Um cliente envia uma requisição HTTP contendo alguma combinação de:

```text
method + URL + headers + optional body
```

O servidor retorna uma resposta HTTP contendo:

```text
status code + headers + body
```

Seu código Python precisa raciocinar sobre as duas metades.

## 3. Bibliotecas externas precisam de um contrato de versão

Este repositório declara as dependências da Fase 9 em `requirements-external.txt`.

Para este capítulo, o contrato é:

```text
requests >= 2.34 and < 2.35
```

A série 2.34 também introduziu tipagem inline no próprio Requests, permitindo que type checkers atuais consumam os tipos da API pública sem depender de um pacote separado de stubs.

## 4. Instale o conjunto de dependências do repositório

Crie e ative um ambiente virtual e então instale:

```bash
python -m pip install -r requirements-external.txt
```

Para experimentação isolada, `python -m pip install requests` é válido, mas um projeto deve registrar o intervalo de dependências suportado.

## 5. Importe o pacote

O import convencional é:

```python
import requests
```

O módulo de nível superior expõe funções convenientes como `get()`, `post()` e `delete()`, além de classes como `Session` e tipos de exceção em `requests.exceptions`.

## 6. Uma URL faz parte do contrato de entrada

Uma URL HTTP normalmente contém:

```text
scheme://host:port/path?query#fragment
```

Para um cliente HTTP, scheme, host, port, path e parâmetros de query afetam a requisição real. Fragments normalmente são interpretados no lado cliente e não são enviados como alvo da requisição HTTP.

Não concatene fragmentos de URL não confiáveis de forma descuidada.

## 7. Comece com uma requisição GET

Um GET básico se parece com isto:

```python
import requests


response = requests.get("https://example.com/api/items", timeout=(3, 10))
print(response.status_code)
```

Este snippet é ilustrativo porque depende de um endpoint externo. Os exemplos executáveis publicados mais adiante usam um servidor local de teste.

## 8. Status codes comunicam resultados HTTP

Classes comuns são:

```text
1xx -> informational
2xx -> successful response
3xx -> redirection
4xx -> client-side request problem
5xx -> server-side failure
```

`200` não é o único sucesso. Um POST pode corretamente retornar `201 Created`, e um DELETE pode retornar `204 No Content`.

## 9. Use `raise_for_status()` quando códigos HTTP sem sucesso forem falhas

```python
response = requests.get(url, timeout=(3, 10))
response.raise_for_status()
```

Para status HTTP sem sucesso, `raise_for_status()` levanta `requests.HTTPError` e mantém a resposta ligada à exceção.

Não descarte esse contexto ao relatar uma falha.

## 10. Sucesso de transporte não é sucesso da aplicação

Uma troca HTTP pode funcionar na camada de rede enquanto o servidor retorna `404`, `429` ou `500`.

Da mesma forma, uma resposta `200` pode conter dados que violam o seu contrato de negócio.

Um cliente robusto verifica mais do que “`requests.get()` retornou?”.

## 11. `response.text` é texto decodificado

```python
text = response.text
```

Requests decodifica os bytes da resposta de acordo com informações de encoding e suas regras de detecção.

Use texto quando o corpo for realmente textual e você quiser uma `str`.

## 12. `response.content` fornece bytes brutos

```python
payload = response.content
```

Use bytes para arquivos binários, checksums, imagens, artefatos comprimidos ou qualquer formato em que converter para texto seria incorreto.

## 13. Decodifique JSON com `response.json()`

```python
response = requests.get(url, timeout=(3, 10))
response.raise_for_status()
data = response.json()
```

`response.json()` faz o parse do corpo. Ele não prova que o status HTTP foi bem-sucedido.

## 14. JSON inválido tem um modo de falha próprio

Requests expõe `requests.exceptions.JSONDecodeError` para falhas de decodificação JSON.

```python
try:
    data = response.json()
except requests.exceptions.JSONDecodeError as exc:
    raise RuntimeError("API returned invalid JSON") from exc
```

Uma resposta `204 No Content`, uma página HTML de erro ou JSON malformado podem fazer a decodificação falhar.

## 15. O formato do JSON ainda precisa ser validado

Mesmo JSON válido pode estar errado para o programa:

```python
if not isinstance(data, dict) or "items" not in data:
    raise ValueError("Unexpected API response shape")
```

O parse responde “isto é JSON?”. A validação de contrato responde “este é o JSON esperado pela aplicação?”.

## 16. Envie parâmetros de query com `params`

Não monte query strings manualmente quando Requests pode codificá-las:

```python
response = requests.get(
    url,
    params={"status": "open", "limit": 20},
    timeout=(3, 10),
)
```

Requests cuida do encoding da query e expõe a URL final em `response.url`.

## 17. Parâmetros repetidos podem usar sequências

Algumas APIs esperam chaves repetidas. Requests aceita valores em sequência ou uma lista de tuplas de dois itens.

```python
params = [("tag", "python"), ("tag", "http")]
response = requests.get(url, params=params, timeout=(3, 10))
```

Siga o contrato documentado da API-alvo.

## 18. Headers da requisição são metadados

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "study-client/1.0",
}
response = requests.get(url, headers=headers, timeout=(3, 10))
```

Headers podem comunicar preferências de representação, autenticação, requisições condicionais, tracing e outros metadados de protocolo.

## 19. Não confunda headers de requisição e resposta

Headers de requisição são enviados pelo cliente. Headers de resposta são devolvidos pelo servidor.

```python
content_type = response.headers.get("Content-Type")
```

Os headers de resposta do Requests se comportam como um mapping case-insensitive.

## 20. Use um `User-Agent` descritivo quando fizer sentido

Muitas APIs valorizam um identificador de cliente para operação e diagnóstico de suporte.

Evite fingir ser um navegador não relacionado, a menos que o contrato da integração exija isso explicitamente.

## 21. Envie dados de formulário com `data=`

Para dados no estilo de formulário:

```python
response = requests.post(
    url,
    data={"username": "demo", "mode": "compact"},
    timeout=(3, 10),
)
```

Requests codifica um mapping passado por `data=` como dados de formulário.

## 22. Envie JSON com `json=`

Para APIs JSON, prefira o parâmetro dedicado:

```python
payload = {"name": "Nova", "active": True}
response = requests.post(url, json=payload, timeout=(3, 10))
response.raise_for_status()
```

`json=` serializa o valor e define um content type JSON apropriado.

## 23. Não serialize JSON manualmente sem motivo

Isto costuma ser menos claro:

```python
import json

body = json.dumps(payload)
response = requests.post(
    url,
    data=body,
    headers={"Content-Type": "application/json"},
    timeout=(3, 10),
)
```

Use `json=` a menos que precise controlar precisamente os bytes serializados.

## 24. PUT e PATCH expressam contratos de atualização diferentes

A especificação HTTP e a documentação de cada API determinam a semântica. Em geral:

```text
PUT   -> replace or set a representation at a target
PATCH -> partially modify a representation
```

Não deduza o comportamento do servidor apenas pelo nome do método. Leia o contrato da API.

## 25. DELETE pode ter sucesso sem corpo

```python
response = requests.delete(url, timeout=(3, 10))
response.raise_for_status()
```

Um `204 No Content` bem-sucedido não deve ser seguido por `response.json()` incondicional.

## 26. Idempotência importa antes de retries

Uma operação é idempotente quando repetir a mesma requisição pretendida produz o mesmo efeito pretendido que executá-la uma vez.

GET, HEAD, PUT e DELETE têm semântica idempotente no nível do método HTTP; POST em geral não tem. O comportamento da aplicação e chaves de idempotência podem adicionar garantias extras.

## 27. Quase toda requisição de produção precisa de timeout

Requests **não** aplica timeout por padrão.

```python
response = requests.get(url, timeout=10)
```

Sem um timeout explícito, um programa pode esperar indefinidamente por atividade de rede.

## 28. Separe timeouts de conexão e leitura quando útil

Requests aceita uma tupla:

```python
response = requests.get(url, timeout=(3, 15))
```

O primeiro valor é o connect timeout. O segundo é o read timeout.

Isso costuma ser mais claro em integrações em que estabelecer conexão e aguardar bytes de resposta têm expectativas diferentes.

## 29. Timeout do Requests não é um deadline total de relógio

O comportamento documentado de timeout se baseia em inatividade do socket, não em uma duração máxima garantida para o download completo.

Uma resposta lenta que continua entregando bytes pode durar mais que o valor nominal do read timeout.

Se o fluxo precisa de um deadline geral rígido, projete-o separadamente.

## 30. Requests possui uma hierarquia útil de exceções

Exceções específicas do Requests herdam de `requests.exceptions.RequestException`.

Subclasses importantes incluem:

```text
HTTPError
ConnectionError
Timeout
TooManyRedirects
JSONDecodeError
SSLError
```

Capture de forma específica quando houver recuperação diferente.

## 31. `Timeout` merece tratamento explícito

```python
try:
    response = requests.get(url, timeout=(3, 10))
except requests.Timeout as exc:
    raise RuntimeError("Remote service timed out") from exc
```

Um timeout é diferente de um HTTP `500`: o cliente pode não saber se o servidor processou a requisição.

Essa incerteza é crucial antes de repetir uma operação de escrita.

## 32. `ConnectionError` cobre falhas de conexão de rede

Falhas de DNS, conexão recusada e problemas de transporte relacionados podem surgir como `requests.ConnectionError`.

Não converta isso em um resultado vazio e bem-sucedido. Preserve o sinal de falha ou aplique uma política de recuperação explícita.

## 33. `HTTPError` fornece acesso à resposta

```python
try:
    response.raise_for_status()
except requests.HTTPError as exc:
    status = exc.response.status_code
    raise RuntimeError(f"API returned HTTP {status}") from exc
```

Evite incluir corpos arbitrários de resposta nos logs porque podem conter segredos ou dados pessoais.

## 34. Um limite de `RequestException` pode adicionar contexto

Na fronteira da aplicação, um wrapper pode acrescentar o nome da operação do serviço:

```python
try:
    response = requests.get(url, timeout=(3, 10))
    response.raise_for_status()
except requests.RequestException as exc:
    raise RuntimeError("Could not load catalog") from exc
```

Não capture `Exception` apenas para fazer uma falha de rede desaparecer.

## 35. Redirects têm histórico

Requests segue redirects em requisições GET comuns e expõe respostas anteriores por:

```python
for previous in response.history:
    print(previous.status_code, previous.url)
```

A URL final fica disponível em `response.url`.

## 36. Limite ou desative redirects quando o contrato exigir

```python
response = requests.get(
    url,
    allow_redirects=False,
    timeout=(3, 10),
)
```

Redirects podem importar para autenticação, auditoria, defesas contra SSRF e URLs assinadas.

## 37. Autenticação Basic possui helper dedicado

```python
from requests.auth import HTTPBasicAuth


response = requests.get(
    url,
    auth=HTTPBasicAuth("demo-user", "demo-password"),
    timeout=(3, 10),
)
```

Nunca grave credenciais reais em código-fonte, exemplos, commits ou logs.

## 38. Bearer tokens normalmente são headers

```python
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers, timeout=(3, 10))
```

O token deve vir de uma fonte segura de runtime, como secret manager ou variável de ambiente protegida, não de um arquivo do repositório.

## 39. Redija segredos na observabilidade

Não registre valores completos de:

```text
Authorization
Proxy-Authorization
Cookie
Set-Cookie
API keys
signed URLs
client certificates or private keys
```

Logs úteis podem conter método HTTP, host/path sanitizado, status code, tempo decorrido, contador de retry e identificadores de correlação.

## 40. `Session` mantém estado entre requisições

```python
import requests


with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})
    response = session.get(url, timeout=(3, 10))
```

Uma Session pode persistir padrões e cookies entre chamadas.

## 41. Sessions também reutilizam conexões

Requests Sessions usam connection pooling do urllib3. Várias chamadas ao mesmo host podem reutilizar conexões subjacentes em vez de abrir uma nova conexão TCP/TLS a cada vez.

Isso pode reduzir significativamente o overhead em fluxos repetidos de API.

## 42. Padrões da Session podem ser sobrescritos por requisição

Headers, autenticação, cookies, proxies e outros parâmetros em nível de Session são defaults convenientes, não globais imutáveis.

Mantenha a configuração compartilhada intencional para não herdar credenciais de outro serviço acidentalmente.

## 43. Feche Sessions deterministicamente

Use context manager ou `close()`:

```python
with requests.Session() as session:
    response = session.get(url, timeout=(3, 10))
    response.raise_for_status()
```

A propriedade dos recursos deve ser visível em processos de longa duração.

## 44. Cookies podem persistir em uma Session

Um servidor pode definir cookies em uma resposta e esperá-los em requisições seguintes. Uma Session mantém um cookie jar entre chamadas.

Para clientes de API, autenticação explícita por token costuma ser mais fácil de raciocinar, mas fluxos baseados em cookies ainda existem.

## 45. Prepared requests expõem a requisição de saída exata

Requests consegue montar um `PreparedRequest` antes de enviá-lo:

```python
from requests import Request, Session


with Session() as session:
    request = Request("GET", url, headers={"X-Trace": "demo"})
    prepared = session.prepare_request(request)
    print(prepared.method, prepared.url)
```

Isso é útil para assinatura avançada, inspeção ou mutação controlada da requisição.

## 46. Prefira `Session.prepare_request()` quando o estado da Session importa

Chamar `Request.prepare()` diretamente não aplica automaticamente todo o estado da Session.

Se cookies, headers padrão ou autenticação da Session fazem parte do contrato, prepare a requisição por essa Session.

## 47. Fluxos com prepared request precisam considerar o ambiente

A documentação avançada do Requests observa que enviar manualmente uma prepared request pode ignorar configurações derivadas do ambiente se elas não forem mescladas explicitamente.

Isso importa para configurações como bundles de CA e proxies.

Preparação avançada de requisições deve ser intencional, não o padrão para chamadas comuns.

## 48. Verificação de certificado HTTPS é habilitada por padrão

Requests verifica certificados TLS do servidor em conexões HTTPS.

```python
response = requests.get("https://example.com", timeout=(3, 10))
```

Se a verificação falhar, Requests levanta `SSLError` em vez de confiar silenciosamente no peer.

## 49. `verify=False` desabilita uma garantia importante de segurança

```python
response = requests.get(url, verify=False, timeout=(3, 10))
```

Isso aceita certificados possivelmente expirados, autoassinados ou para hostname incorreto e pode permitir ataques man-in-the-middle.

Não resolva um problema de certificado em produção desabilitando globalmente a verificação.

## 50. PKI privada deve usar um bundle de CA explícito

Requests permite que `verify` aponte para um bundle de CA confiável:

```python
response = requests.get(
    url,
    verify="/path/to/company-ca-bundle.pem",
    timeout=(3, 10),
)
```

Requests também reconhece `REQUESTS_CA_BUNDLE`, com `CURL_CA_BUNDLE` como fallback em seu comportamento documentado de ambiente.

## 51. Certificados de cliente suportam fluxos de mTLS

O parâmetro `cert` pode apontar para um certificado de cliente ou para um par certificado/chave:

```python
response = requests.get(
    url,
    cert=("client.crt", "client.key"),
    timeout=(3, 10),
)
```

Arquivos de chave privada são segredos. Proteja-os como credenciais.

## 52. Proxies podem vir de argumentos ou do ambiente

Requests suporta configuração de proxy por requisição e settings derivados do ambiente.

```python
proxies = {"https": "http://proxy.example:8080"}
response = requests.get(url, proxies=proxies, timeout=(3, 10))
```

Não coloque credenciais reais de proxy no código-fonte.

## 53. `Session.trust_env` controla a integração com o ambiente

Sessions confiam por padrão em configurações relevantes do ambiente, como proxies e fontes de autenticação.

Se um cliente precisa operar independentemente da configuração ambiente do processo, avalie `session.trust_env` explicitamente e documente as consequências.

## 54. Streaming evita carregar o corpo inteiro imediatamente

```python
with requests.get(url, stream=True, timeout=(3, 30)) as response:
    response.raise_for_status()
    for chunk in response.iter_content(chunk_size=64 * 1024):
        if chunk:
            process(chunk)
```

Streaming é útil para downloads grandes e processamento incremental.

## 55. Respostas em streaming devem ser consumidas ou fechadas

A reutilização de conexão depende da liberação da conexão subjacente.

Usar a resposta como context manager torna a fronteira de propriedade explícita mesmo se o processamento gerar exceção.

## 56. `iter_content()` geralmente é melhor que ler `raw` diretamente

`iter_content()` coopera com o comportamento de decodificação do Requests e com iteração por chunks.

Escolha o tamanho do chunk conforme o caso de uso e não assuma que cada chunk corresponde a uma mensagem lógica do servidor.

## 57. Streaming por linhas é útil para protocolos orientados a linha

`response.iter_lines()` pode processar uma resposta de streaming linha por linha.

Tenha cuidado com linhas vazias de keep-alive, registros parciais e semântica de reconexão definida pela API específica.

## 58. Grave downloads grandes com segurança

Para um artefato importante, um padrão mais seguro é:

```text
download to temporary path
-> verify status / size / checksum if available
-> flush and close
-> atomically move into final location
```

Isso evita que um download parcial pareça um arquivo concluído.

## 59. Uploads multipart usam `files=`

```python
with open("report.txt", "rb") as file_handle:
    response = requests.post(
        url,
        files={"file": ("report.txt", file_handle, "text/plain")},
        timeout=(3, 30),
    )
```

O arquivo deve ser aberto em modo binário para tratamento previsível de bytes.

## 60. Requests não repete conexões com falha por padrão

O `HTTPAdapter` embutido usa zero retries de conexão por padrão.

Retries são uma política da aplicação, não algo que você deve presumir que ocorreu automaticamente.

## 61. `HTTPAdapter` pode adicionar uma política de retry

Para comportamento granular, a documentação do Requests usa a classe `Retry` do urllib3:

```python
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


retry_policy = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[429, 502, 503, 504],
    allowed_methods={"GET", "HEAD"},
)

with Session() as session:
    session.mount("https://", HTTPAdapter(max_retries=retry_policy))
    response = session.get(url, timeout=(3, 10))
```

A política deve ser projetada junto com o contrato da API, não copiada cegamente.

## 62. Nunca repita uma escrita apenas porque ela falhou

Um timeout após enviar um POST pode significar:

```text
client does not know whether server committed the operation
```

Repeti-lo cegamente pode criar duplicidades.

Use chaves de idempotência, identificadores de operação, métodos seguros ou lógica de reconciliação quando o serviço oferecer essas garantias.

## 63. Respeite `Retry-After` e contratos de rate limit

Uma resposta `429 Too Many Requests` normalmente indica que o cliente deve desacelerar.

Os headers exatos e o comportamento de retry são específicos da API. Leia o contrato do serviço e evite loops apertados que ampliem uma indisponibilidade.

## 64. Backoff reduz tempestades de retry

Retries normalmente devem aguardar entre tentativas. Backoff exponencial e jitter ajudam muitos clientes a não sincronizarem tentativas contra o mesmo serviço em recuperação.

A política exata pertence ao desenho de confiabilidade do sistema.

## 65. Response hooks podem adicionar comportamento transversal

Requests suporta hooks de `response`:

```python
def record_status(response: requests.Response, *args: object, **kwargs: object) -> None:
    print(response.status_code)


response = requests.get(
    url,
    hooks={"response": record_status},
    timeout=(3, 10),
)
```

Hooks devem permanecer pequenos e tratar suas próprias premissas e falhas.

## 66. Paginação é contrato da API, não recurso do Requests

APIs podem paginar com:

```text
page/limit query parameters
cursor tokens
Link headers
next URLs in JSON
```

O cliente deve parar na condição terminal documentada pelo serviço e se proteger contra loops infinitos acidentais.

## 67. Link headers já são parseados

Quando a resposta contém headers padrão de Web Linking, Requests expõe links parseados por:

```python
next_link = response.links.get("next")
```

Não presuma que toda API usa Link headers para paginação.

## 68. Valide o media type da resposta quando importar

Se o endpoint promete JSON, inspecione o contrato conforme necessário:

```python
content_type = response.headers.get("Content-Type", "")
if "application/json" not in content_type.lower():
    raise ValueError("Expected a JSON response")
```

Seja preciso o suficiente para a API integrada; media types podem conter parâmetros ou formatos vendor-specific `+json`.

## 69. Logs HTTP exigem redação de dados sensíveis

Um registro estruturado útil pode conter:

```text
service name
operation
HTTP method
sanitized route
status code
elapsed time
retry attempt
correlation ID
```

Evite registrar URLs completas quando parâmetros de query puderem conter segredos ou dados pessoais.

## 70. Testes determinísticos não devem depender da internet pública

Um endpoint público pode ficar lento, indisponível, limitado por rate limit, bloqueado geograficamente ou alterado sem relação com seu repositório.

Os exemplos executáveis deste capítulo iniciam um `ThreadingHTTPServer` local em `127.0.0.1`, exercitam Requests contra ele e então encerram o servidor. Assim testamos HTTP real sem dependência externa de rede.

## 71. Exemplo prático: GET com parâmetros de query

[`examples/get_with_query.py`](examples/get_with_query.py) envia um GET HTTP local real, deixa Requests codificar parâmetros de query, verifica o status, decodifica JSON e imprime o contrato de query parseado.

Saída esperada:

```text
status: 200
path: /items
query: {'status': ['open'], 'limit': ['2']}
```

## 72. Exemplo prático: POST JSON

[`examples/post_json.py`](examples/post_json.py) verifica que `json=` envia um payload JSON com o content type esperado.

Saída esperada:

```text
status: 201
created: {'name': 'Nova', 'active': True}
content-type: application/json
```

## 73. Exemplo prático: padrões de Session

[`examples/session_defaults.py`](examples/session_defaults.py) usa uma Session para aplicar headers compartilhados e confirma que o servidor local os recebeu.

Saída esperada:

```text
client: python-study-guide
auth-scheme: Bearer
```

O token é fictício e existe apenas dentro do processo local do exemplo.

## 74. Exemplo prático: erros HTTP visíveis

[`examples/http_error_handling.py`](examples/http_error_handling.py) recebe `404` intencionalmente e demonstra `raise_for_status()` preservando a resposta em `HTTPError`.

Saída esperada:

```text
caught: HTTPError
status: 404
```

## 75. Exemplo prático: download por streaming

[`examples/stream_download.py`](examples/stream_download.py) transmite bytes locais determinísticos com `iter_content()` e fecha a resposta por context manager.

Saída esperada:

```text
bytes: 12
content: chunked-data
```

## 76. Erros comuns

Evite estes padrões:

| Erro | Por que é arriscado | Melhor abordagem |
|---|---|---|
| omitir `timeout` | requisição pode esperar indefinidamente | definir expectativas de conexão/leitura |
| chamar `json()` e presumir sucesso | respostas de erro podem conter JSON válido | verificar status HTTP e contrato do payload |
| usar `verify=False` em produção | desabilita verificação de identidade TLS | corrigir cadeia de confiança ou fornecer CA bundle |
| repetir toda exceção | pode duplicar escritas ou piorar indisponibilidade | repetir apenas falhas seguras e classificadas |
| criar nova Session para toda chamada | perde reutilização de conexão | possuir Session durante a vida lógica do cliente |
| registrar Authorization | vaza credenciais | redigir segredos |
| confiar em qualquer formato JSON | drift de schema vira bug oculto | validar campos/tipos necessários |
| testar contra API pública de demonstração | CI fica externamente frágil | usar servidor local ou test double controlado |

## 77. Tabela de decisão

| Necessidade | Prefira |
|---|---|
| uma requisição simples | `requests.get/post/...` no módulo |
| chamadas repetidas para um serviço | `requests.Session()` |
| corpo JSON | `json=` |
| corpo de formulário | `data=` |
| parâmetros de query | `params=` |
| resposta grande | `stream=True` + `iter_content()` |
| falha HTTP deve interromper fluxo | `raise_for_status()` |
| retries customizados | `HTTPAdapter` + política explícita de `Retry` |
| CA privada | `verify=<caminho do CA bundle>` |
| teste determinístico em CI | servidor HTTP local / test double controlado |

## 78. Referência rápida

```python
import requests


with requests.Session() as session:
    response = session.get(
        "https://example.com/api/items",
        params={"limit": 20},
        headers={"Accept": "application/json"},
        timeout=(3, 10),
    )
    response.raise_for_status()
    data = response.json()
```

Antes da produção, acrescente regras específicas de autenticação, validação de schema, observabilidade, paginação, retry e segurança do serviço.

## 79. Checklist de projeto de cliente HTTP

Antes de publicar uma integração, responda:

1. Quais métodos HTTP e rotas são permitidos?
2. De onde vêm as base URLs?
3. Todas as URLs externas são confiáveis ou validadas?
4. Quais são os connect e read timeouts?
5. Quais status codes são esperados?
6. Quais media types e campos de resposta são obrigatórios?
7. Como credenciais são obtidas, rotacionadas e redigidas?
8. A verificação TLS está habilitada e a PKI privada está configurada corretamente?
9. O cliente reutiliza uma Session?
10. Quais falhas são retryable?
11. Escritas repetidas são idempotentes ou protegidas por idempotency keys?
12. Como paginação e rate limits são tratados?
13. Respostas em streaming sempre são fechadas?
14. Qual telemetria é segura para registrar?
15. Os testes executam sem dependência de rede pública?

## 80. Exercício integrado

Construa um **cliente fictício de API de estoque** contra um servidor HTTP local de teste.

Requisitos:

1. Crie uma classe reutilizável `InventoryClient` que possua uma `requests.Session`.
2. Aceite uma base URL no construtor.
3. Aplique `Accept: application/json` em nível de Session.
4. Adicione um método que liste itens com query params `status` e `limit`.
5. Adicione um método que crie um item com corpo JSON.
6. Use timeouts explícitos de conexão/leitura.
7. Chame `raise_for_status()` antes de decodificar um payload de sucesso.
8. Valide que objetos de item contêm `id` inteiro e `name` string.
9. Traduza exceções do Requests para uma exceção própria da aplicação, preservando a original com `raise ... from`.
10. Nunca registre o valor de Authorization.
11. Adicione servidor local que retorne casos 200, 201, 404, 429 e JSON malformado.
12. Teste que uma resposta `204` não é decodificada como JSON.
13. Adicione paginação com condição terminal documentada.
14. Explique quais operações você repetiria e por quê.
15. Acrescente um desafio com idempotency key para uma escrita.

Desafios de extensão:

- transmitir um export gerado para arquivo temporário e renomeá-lo atomicamente;
- configurar retry seguro para GET com backoff;
- adicionar logs de tempo de resposta com correlation ID;
- usar prepared request para inspecionar headers exatos antes do envio;
- definir um pequeno modelo tipado depois de validar o contrato JSON.

## 81. Conexões com conceitos anteriores

`requests` se conecta diretamente ao material anterior:

- **dicionários:** headers, query params, cookies e objetos JSON;
- **funções/classes:** clientes reutilizáveis e fronteiras explícitas;
- **exceções:** falhas de transporte, HTTP e decodificação;
- **JSON:** serialização e parse de payloads;
- **`pathlib`:** destinos seguros de download e caminhos de CA/certificado;
- **logging:** chamadas observáveis com redação de segredos;
- **`datetime`:** timestamps, validators de cache e campos de data de APIs;
- **`os`:** variáveis de ambiente para configuração em runtime;
- **`pandas`:** transformar dados tabulares recebidos de uma API;
- **`openpyxl`:** transformar dados de API em workbooks Excel controlados.

## 82. Referências primárias

- [Documentação do Requests](https://requests.readthedocs.io/en/latest/)
- [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Requests Advanced Usage](https://requests.readthedocs.io/en/latest/user/advanced/)
- [Requests Developer Interface](https://requests.readthedocs.io/en/latest/api/)
- [Requests no PyPI](https://pypi.org/project/requests/)
- [Histórico de releases do Requests](https://github.com/psf/requests/releases)

Quando este capítulo foi preparado, Requests 2.34.2 era a versão estável mais recente. O currículo mira a série 2.34.x em vez de depender de uma versão futura sem limite.

## 83. Próximo capítulo

A Fase 9 agora conecta três fronteiras práticas:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
requests -> exchange data with HTTP services and APIs
```

A próxima biblioteca planejada é **`pytest`**, quando o foco passa de usar bibliotecas externas para provar sistematicamente que o comportamento Python continua correto.

Antes de avançar, construa pelo menos um cliente contra um servidor HTTP local. Código confiável de API começa quando o comportamento da rede se torna algo que você consegue reproduzir, inspecionar e testar.
