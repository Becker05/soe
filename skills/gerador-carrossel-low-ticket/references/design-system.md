# Design System — Métricas Reais

Documentação operacional da identidade visual dos carrosséis. O contrato visual canônico está em `layout-metricas-reais.md` e **prevalece em qualquer conflito visual**.

> **Pendência de implementação:** o renderer atual ainda aceita os tipos legados `capa`, `gancho2`, `ponto`, `lista`, `vs`, `quote`, `prova` e `cta`. Os sete tipos canônicos e o schema novo descritos abaixo ainda não foram implementados em `scripts/gera_carrossel.py`. Não enviar o JSON canônico ao renderer legado como se fosse compatível.

## Base visual

- Canvas: `1080 × 1350 px` (4:5)
- Fundo: preto puro `#000000`
- Tipografia: `Inter`
- Safe area: 88 px nas laterais, 86 px no topo e 82 px na base
- Sem degradê, textura, fotografia, gráfico, card, mockup, ícone grande ou duas colunas
- Legibilidade mobile acima de variedade visual
- Nunca reduzir o título abaixo de 60 px para fazer a copy caber; a copy volta para edição

## Paleta e semântica

| Papel | Cor | Uso |
|---|---|---|
| Fundo | `#000000` | base de todos os slides |
| Verde | `#22E58F` | reconciliação, métrica confiável, decisão segura |
| Vermelho | `#FF5A5F` | leitura no escuro, contradição entre fontes, risco de decisão |
| Texto | `#FFFFFF` | conteúdo principal |
| Apoio | `#AEB4BE` | subtítulos e apoio |
| Chrome | `#8E949E` | rótulos, índice e @ |
| Filete | `#17181B` | separação de itens |

Cada slide usa **no máximo uma cor de destaque**. Nunca usar vermelho e verde no mesmo slide. A plataforma nunca é o inimigo: o vermelho marca a leitura sem estrutura ou a contradição, não Meta, Google, TikTok, GA4 ou qualquer ferramenta.

## Tipografia e chrome

- Título: Inter 700, 74 px, mínimo 60 px, entrelinha 1.14, até 12 palavras e 5 linhas
- Apoio: Inter 400, 36 px, entrelinha 1.50, até 25 palavras e 5 linhas
- Rótulo: Inter 600, 22 px, caixa alta, letter spacing 0.14em
- Índice no topo esquerdo: atual em accent + `/ total` em cinza
- `@souarturbecker` no topo direito, 20 px, cinza
- Nenhum outro elemento fixo

## Sete tipos canônicos

| Tipo | Função | Estrutura fixa |
|---|---|---|
| `capa` | abrir com o hook | título, apoio opcional e `arraste →`; conteúdo centralizado |
| `gancho` | abrir o loop do slide 2 | título + apoio; centralizado; não explica a capa |
| `nota` | desenvolver uma ideia | rótulo opcional + título + apoio; alinhado ao topo |
| `lista_progressiva` | pagar uma lista item a item | mesma lista em 3+ slides, um item ativo, passados em cinza, payload futuro mascarado |
| `espelho` | comparar leituras em sequência | mesmo layout em 2+ slides, rótulo fixo e um elemento variável; nunca lado a lado |
| `decisao` | transformar leitura em ação | rótulo `A DECISÃO`, frase principal e uma única ação verde |
| `cta` | apresentar a oferta | rótulo `CARTILHA DAS MÉTRICAS REAIS`, título, apoio e pílula `Link na bio →` |

Tipos fora desse conjunto não pertencem ao contrato canônico.

## Destaque

O schema canônico usa `accent` e `destaque` para declarar uma única cor e um único trecho destacado por slide. Vermelho significa leitura no escuro/contradição. Verde significa reconciliação/decisão segura.

O renderer legado ainda usa markup textual (`*verde*` e `~vermelho~`); essa compatibilidade é temporária até o rewrite.

## Estrutura recomendada

Um carrossel usa 8–10 slides e escolhe somente os tipos necessários ao fio condutor. O slide 1 concentra o hook; o slide 2 abre o loop; o miolo repete uma estrutura narrativa; o penúltimo fecha a decisão; o último apresenta a Cartilha das Métricas Reais sem promessa de prazo.

## Specs finais

JPG com qualidade adequada para feed · 1080 × 1350 · legenda com primeira linha-gancho e 3–5 hashtags específicas.

## Saída no padrão N8N

Uma subpasta nova por post dentro da pasta base: `post-AAAA-MM-DD-<slug>/`, contendo `img-01.jpg`, `img-02.jpg`... na ordem do carrossel e `legenda.txt` em texto puro. O destino do Artur no Drive é `G:\Meu Drive\Trafego\Claude\Criativos`.
