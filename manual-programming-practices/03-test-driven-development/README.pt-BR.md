# Desenvolvimento orientado por testes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-specification-driven-development/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../04-professional-workflow/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Tempo estimado:** 45–60 minutos. Siga os requisitos da [aula de especificação](../02-specification-driven-development/README.pt-BR.md). TDD significa escrever um teste que falha para comportamento pequeno, implementar o suficiente para passar e melhorar o código sem alterar comportamento. É um ciclo de feedback, não substituto dos requisitos. Usamos unittest da biblioteca padrão; veja [pytest](../../external-libraries/04-pytest/README.pt-BR.md) para a alternativa já ensinada.

## 1. Red: escreva um teste primeiro

Em nova pasta de prática, crie reading_progress.py com implementação provisória intencional:

```python
def remaining_pages(total_pages, pages_read):
    raise NotImplementedError
```

Crie test_reading_progress.py ao lado:

```python
import unittest
from reading_progress import remaining_pages


class ReadingProgressTests(unittest.TestCase):
    def test_remaining_pages(self):
        self.assertEqual(remaining_pages(20, 7), 13)
```

Na pasta execute:

```shell
python -m unittest discover -s . -p 'test_*.py' -v
```

Em shell compatível, isso descobre o teste; use aspas duplas no padrão se necessário. Use seu Python de ambiente verificado. Espere um teste com erro (NotImplementedError): falta o comportamento. Teste que não importa o módulo por motivo alheio não comprova o red desejado; corrija o ambiente primeiro.

## 2. Green: implemente apenas o primeiro comportamento

Substitua o provisório por `return total_pages - pages_read`. Execute novamente. Deve passar. Adicione testes de AC2, depois AC3 e AC4 em incrementos pequenos. Use `self.assertRaises(ValueError)` ou `self.assertRaises(TypeError)` como gerenciadores de contexto. Execute cada teste novo antes de implementar o comportamento faltante; a subtração sozinha falhará nos testes de intervalos inválidos. Valide os tipos exatos antes dos intervalos com type(value) is int; isso exclui deliberadamente bool (subclasse de int) e outras subclasses de int. Adicione teste de ausência de saída (AC5) com stdout/stderr redirecionados, depois verifique precedência de erro de tipo e rejeição de subclasse de int. Não enfraqueça teste com falha para passar.

## 3. Refactor: melhore e verifique

Melhore nomes ou remova repetição somente mantendo testes verdes. Por exemplo, agrupe casos de limite equivalentes com subTest. Refatoração altera estrutura, não comportamento especificado. Execute suíte completa após cada alteração.

Tente sozinho antes de abrir a [implementação de referência](examples/reading_progress.py) e os [testes de referência](examples/test_reading_progress.py). O código final é compartilhado entre idiomas. A referência tem sete métodos de teste, incluindo grupos de limites; um método pode verificar vários casos. Na raiz do repositório execute:

```shell
python -m unittest discover -s manual-programming-practices/03-test-driven-development/examples -p 'test_*.py' -v
python manual-programming-practices/03-test-driven-development/examples/reading_progress.py
```

Saída esperada do demo: 13. A suíte final deve passar; o provisório vermelho está apenas na aula, não em código executável versionado. O CI executa a suíte dedicada e o demo aprovado.

## 4. Prática independente

Sem ler a referência, implemente contrato, escreva testes e registre observações red/green/refactor. Troque temporariamente subtração por adição ou remova uma validação na sua cópia. Confira que um teste relevante falha; restaure implementação correta e execute novamente. Explique por que aprovação não comprova todos os casos possíveis ou qualidade do código. Para funcionalidade nova, atualize primeiro a especificação quando mudar comportamento.

**Referência rápida:** definir comportamento → teste falhando → menor implementação correta → teste passando → refatorar → repetir. Consulte [unittest](https://docs.python.org/3.13/library/unittest.html) para asserções e descoberta.

<!-- chapter-navigation:bottom -->
[← Anterior](../02-specification-driven-development/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../04-professional-workflow/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
