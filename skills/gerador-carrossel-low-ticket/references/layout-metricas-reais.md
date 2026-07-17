# Addendum da Skill — Layout da marca Métricas Reais

Use este bloco como regra canônica de geração visual da skill `gerador-carrossel-low-ticket`.
Ele substitui qualquer lógica antiga de layout que permita cards, ícones, fundos coloridos,
gráficos decorativos ou variações visuais sem função narrativa.

---

## 1. Princípio visual

A arte não interpreta livremente a copy.

Ela deve renderizar a copy dentro de um sistema fixo, reconhecível e repetível.

**Identidade:** bloco de notas do iPhone.
**Objetivo:** fazer o seguidor reconhecer a marca antes mesmo de ler o @.
**Prioridade:** legibilidade mobile > estética > variedade.

---

## 2. Canvas e safe area

- Tamanho: `1080 × 1350 px`
- Fundo: `#000000`
- Sem degradê, textura, grão, vinheta ou fotografia
- Margem horizontal mínima: `88 px`
- Margem superior mínima: `86 px`
- Margem inferior mínima: `82 px`
- Área útil: `904 × 1182 px`
- Nada pode sair da safe area
- Não reduzir fonte para “fazer caber”; se não couber, a copy volta para edição

---

## 3. Tipografia

Usar apenas uma família neutra: `Inter` ou `SF Pro`.

### Título

- Peso: `700`
- Cor: `#FFFFFF`
- Tamanho desktop do arquivo: `74 px`
- Mínimo permitido: `60 px`
- Entrelinha: `1.14`
- Alinhamento: esquerda
- Máximo: `12 palavras`
- Máximo: `5 linhas`

### Apoio

- Peso: `400`
- Cor: `#AEB4BE`
- Tamanho: `36 px`
- Entrelinha: `1.50`
- Máximo: `25 palavras`
- Máximo: `5 linhas`

### Rótulo

- Peso: `600`
- Caixa alta
- Cor: `#8E949E`
- Tamanho: `22 px`
- Letter spacing: `0.14em`

### Chrome

- Índice no topo esquerdo: número atual na cor de destaque + `/ total` em `#8E949E`
- @ no topo direito: `@souarturbecker`, `20 px`, `#8E949E`
- Nenhum outro elemento fixo

---

## 4. Cores semânticas

- Vermelho `#FF5A5F`: leitura sem estrutura, número conflitante, risco de decisão
- Verde `#22E58F`: reconciliação, métrica confiável, decisão segura
- Branco `#FFFFFF`: conteúdo principal
- Cinza claro `#AEB4BE`: apoio
- Cinza médio `#8E949E`: rótulos e chrome
- Filete `#17181B`: separação de itens

### Regra bloqueante

Cada slide usa no máximo **uma** cor de destaque.

Nunca usar vermelho e verde no mesmo slide.

A plataforma nunca recebe vermelho por ser “inimiga”.
A cor marca a leitura, não a ferramenta.

---

## 5. Tipos visuais permitidos

A skill só pode usar estes tipos:

### `capa`

- Centralização vertical
- Título principal
- Apoio opcional
- `arraste →` no rodapé esquerdo
- Sem lista
- Sem card
- Sem botão

### `gancho`

- Centralização vertical
- Título + apoio
- Abre loop
- Sem explicar o slide anterior

### `nota`

- Conteúdo alinhado ao topo
- Rótulo opcional
- Título
- Apoio
- Sem ornamentação

### `lista_progressiva`

- Rótulo acima da lista
- Mesma lista em 3 ou mais slides consecutivos
- Um item ativo por slide
- Itens passados em cinza
- Itens futuros mascarados quando forem payload
- Filete `#17181B` entre itens

### `espelho`

- Mesmo layout em 2 ou mais slides consecutivos
- Um rótulo fixo
- Um elemento variável
- Serve para Meta x GA4, antes x depois, canal A x canal B
- Não usar duas colunas; o espelho é narrativo, não lado a lado

### `decisao`

- Rótulo `A DECISÃO`
- Frase principal em branco
- Uma única ação destacada em verde
- Centralização vertical quando ocupar menos de 50% da altura

### `cta`

- Rótulo `CARTILHA DAS MÉTRICAS REAIS`
- Título curto
- Apoio curto
- Pílula verde permitida somente aqui
- Texto da pílula: `Link na bio →`
- Não inventar selos, mockups ou ícones

Tipos proibidos: `card`, `grafico`, `dashboard`, `foto`, `quote-card`, `duas-colunas`,
`mockup`, `icone-grande`, `barra-progresso`.

---

## 6. Regra de densidade

Antes de renderizar, contar palavras por slide.

- Título: até 12 palavras
- Apoio: até 25 palavras
- Total recomendado: até 32 palavras
- Total máximo absoluto: 40 palavras

Se exceder:

1. resumir;
2. dividir em dois slides;
3. reprovar a copy.

Nunca resolver reduzindo a fonte abaixo do mínimo.

---

## 7. Alinhamento vertical

- Conteúdo abaixo de 50% da altura útil: centralizar verticalmente
- Conteúdo acima de 50%: alinhar no topo
- O título nunca começa antes de `y = 190`
- O CTA nunca termina depois de `y = 1220`

---

## 8. Contrato JSON

```json
{
  "meta": {
    "slug": "atribuicao-contagem-meta-ga4",
    "width": 1080,
    "height": 1350,
    "total_slides": 10,
    "handle": "@souarturbecker"
  },
  "slides": [
    {
      "numero": 1,
      "tipo": "capa",
      "accent": "red",
      "rotulo": null,
      "titulo": "Dois relatórios mostram leituras diferentes.",
      "apoio": "A diferença está no método de cada fonte.",
      "destaque": {
        "texto": "leituras diferentes",
        "cor": "red"
      },
      "alinhamento_vertical": "center",
      "rodape": "arraste →"
    }
  ]
}
```
