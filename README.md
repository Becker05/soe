# Sistema Operacional Editorial (SOE)
### Constituição editorial da marca Artur Becker

> **Escopo:** o SOE governa a **marca Artur Becker** — não um único produto. A **Cartilha das Métricas Reais** é o primeiro produto da marca, não o centro do sistema. Produtos futuros (auditoria, dashboard, mentoria, comunidade) herdam esta mesma Constituição.
>
> **Regra de nível:** documentos 00–03 são de **marca** (product-agnostic) e nunca devem depender de um produto específico. Menções à Cartilha aparecem só como *ativo comercial atual*, substituível quando surgir o próximo produto.

## Princípio Fundamental

O objetivo do SOE não é produzir conteúdo. É construir uma marca. Todo conteúdo é apenas uma consequência dessa construção. Por isso o sistema serve a posts, mas também a landing pages, anúncios, e-mails, páginas da Hotmart, roteiros, apresentações, propostas e produtos futuros.

## Estrutura

```
/EDITORIAL
├── 00 - NORTE ESTRATÉGICO.md          ← o coração. 1ª validação de toda peça.
├── 01 - MANIFESTO EDITORIAL.md        ← o cérebro. Em conflito, vence.
├── 02 - POSICIONAMENTO.md
├── 03 - LINGUAGEM E COMUNICAÇÃO.md    ← (ex-Tom de Voz) consultado por quase todos os modos
├── 04A - FRAMEWORKS ESTRATÉGICOS.md   ← quando usar
├── 04B - FRAMEWORKS DE ESCRITA.md     ← como executar
├── 05 - AGENTE MESTRE.md              ← instruções do Project
├── 06 - BASE DE CONHECIMENTO.md       ← ativo de longo prazo; ler ANTES de escrever
├── 07 - BASE DE REFERÊNCIAS.md        ← de onde o conhecimento pode vir e em que ordem
├── 08 - REGRAS DE EXECUÇÃO.md         ← pipeline canônico; entrada única + gates
├── 09 - BASE DE DESEMPENHO EDITORIAL.md ← o que a marca aprende sobre o próprio canal
├── /execucao
│   └── banco-de-ganchos.md            ← insumo de produção; não gera conteúdo sozinho
└── README.md
```

## As duas bases

O sistema tem duas bases e elas não se confundem.

**Doc 06 — Conhecimento.** O que é verdade sobre mensuração. Muda pouco. Gera conteúdo.

**Doc 09 — Desempenho.** O que é verdade sobre como o conteúdo da marca se comporta na distribuição. Muda sempre. Não gera conteúdo: informa como a execução acontece.

Uma leitura de desempenho nunca vence o Manifesto. Ela mede se a execução dele está funcionando.

## O fluxo oficial

Ideia → Base de Conhecimento → Estratégia → Framework → Formato e veículo → Copy → Revisão → Arte → Publicação → Atualização da Base

## Ordem de prioridade (em caso de conflito)

1. Norte Estratégico
2. Manifesto
3. Base de Conhecimento
4. Linguagem e Comunicação
5. Posicionamento
6. Frameworks
7. Base de Desempenho Editorial
8. Agente

## Onde cada coisa mora

- **Git (aqui):** fonte da verdade versionada. Editar posicionamento = editar aqui.
- **Claude Project:** instruções = doc 05; conhecimento = docs 00–04B + 06 + 09 + banco de ganchos. Peça avulsa do dia a dia.
- **Skills:** produção determinística (render, Notion, N8N). Devem **referenciar** o Manifesto para vilão/tom, não redeclarar.
- **Cowork:** esteira completa da semana.
- **Claude Code:** manutenção dos .md e, no futuro, subagentes reais.

## Ordem de implantação

Git → Claude Code → Project → Skills → Cowork → N8N.

## Estrutura de pastas recomendada (à medida que crescer — não criar vazia)

`/constituicao` (00–03) · `/conhecimento` (base, cases, estudos) · `/execucao` (04A, 04B, banco de ganchos, templates, prompts) · `/skills` · `/agents` · `/automacao` (n8n, notion, git) · `/outputs` · `/assets`.

## Regra de manutenção da Base

Todo ângulo publicado entra em "ganchos e ângulos já usados" do verbete. Toda prova publicada entra em "provas já publicadas", com formato e alcance. O gancho literal não se repete em intervalo curto; a tese se repete sempre, por novos ângulos.

Leitura de desempenho com número entra no doc 09. Sem número, não entra.
