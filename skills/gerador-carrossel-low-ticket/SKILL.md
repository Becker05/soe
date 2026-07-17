---
name: gerador-carrossel-low-ticket
description: >
  Gera carrosséis de feed PRONTOS (JPGs 1080x1350 renderizados com layout, fontes e identidade
  visual da Cartilha das Métricas Reais) e salva a copy no Notion na base "Conteúdo Low Ticket".
  Saída padrão N8N: pasta nova por post com img-01.jpg... + legenda.txt.
  Use SEMPRE que o usuário pedir "gera o carrossel", "monta os slides", "cria/faz a arte do
  carrossel", "carrossel pronto pra postar", "produz o carrossel de topo/meio/fundo", colar um
  link do Notion com a pauta/conteúdo da semana pedindo pra virar carrossel, ou quando a
  conteudo-low-ticket tiver definido a copy e o próximo passo for produzir as imagens — mesmo
  sem dizer "skill". No início, pergunta a fonte: ideia do usuário, link do Notion, ou próximo
  item planejado. A copy segue os frameworks da conteudo-low-ticket (gancho no slide 1, segundo
  gancho no slide 2, 8–10 slides, CTA final); esta skill produz o ARQUIVO final, não só o
  roteiro. NÃO use para Reels/Stories/vídeo (use conteudo-low-ticket) nem conteúdo de
  autoridade do perfil (use tech-creator-ga4).
---

# Gerador de Carrossel Low Ticket — do roteiro ao PNG postável

## ⛔ REGRA DE POSICIONAMENTO — checar ANTES de renderizar

> **Posicionamento derivado do Manifesto** (repo `soe` → `01 - MANIFESTO EDITORIAL.md` + vilão do `05 - AGENTE MESTRE.md`) — versão de 16/07/2026. Cópia de trabalho da Constituição. **Se o Manifesto mudar, ressincronizar.** Não editar de forma independente.

**Vale mesmo quando a copy vem pronta do Notion.** Copy verbatim continua sendo verbatim — mas *verbatim* não significa *sem revisão de posicionamento*. Se o Notion estiver errado, **o Notion é que se corrige**, não o slide.

> **O vilão é decidir no escuro, sem estrutura de mensuração confiável. O herói é a métrica confiável que reconcilia as fontes.**

A plataforma **nunca** é a vilã: nunca atacar Meta/Google/TikTok, nunca dizer que uma plataforma mente. O gerenciador é parte interessada (mede o próprio trabalho) — isso é conflito de interesse, não mentira. Nenhuma fonte é a verdade absoluta, nem o GA4: o herói é a reconciliação, não uma ferramenta.

### PARE e não renderize se algum slide disser:

- ❌ "A Meta mente / o Google engana" → ✅ "A Meta atribui pelo método dela — não é mentira, é o modelo dela"
- ❌ "Todo mundo mente / os dois estão errados" → ✅ "Cada fonte responde uma pergunta diferente; sem estrutura você decide no escuro"
- ❌ "O GA4 revela a verdade / é a única fonte sem interesse" → ✅ "O GA4 bem configurado ajuda a **reconciliar** as fontes"
- ❌ "Não confie em nenhum painel" → ✅ "Confie numa **estrutura** que reconcilia os painéis"
- ❌ CTA que não nomeia a saída → ✅ CTA que diz **com o quê** o problema se resolve: métricas confiáveis / a Cartilha

Ao encontrar violação: **aponte a contradição pro Artur, proponha a correção, e só renderize depois do OK dele.** Renderizar uma copy que queima a oferta custa mais caro que atrasar o post.

### O teste dos 3 segundos (rode em toda copy recebida)

1. Quem é o culpado? Se for "uma plataforma" (Meta/Google/GA4) → **refaça**. Tem que ser "decidir sem estrutura de mensuração".
2. Qual a saída oferecida? Se não for "métricas confiáveis / reconciliação" → o carrossel só reclama, não vende.
3. A pessoa sai achando que analytics não funciona, ou que falta estrutura na leitura dela? Tem que ser **a segunda**.

### A cor reforça o posicionamento

| Cor | Significa | Nunca use em |
|---|---|---|
| 🔴 `#FF5A5F` | leitura no escuro, número sem estrutura, contradição entre fontes | a métrica confiável / a decisão validada |
| 🟢 `#22E58F` | métrica confiável, fontes reconciliadas, a decisão segura | o número solto / a leitura sem estrutura |

O arco cromático do carrossel deve virar de vermelho para verde **exatamente no slide em que a copy apresenta a estrutura de mensuração confiável como solução**. (Nunca pintar uma plataforma de vermelho como "inimiga" — o vermelho é a *leitura no escuro*, não a Meta nem o GA4.)

---

## ⛔ REGRA DE CTA — checar ANTES de renderizar

**Nunca renderize um slide ou legenda com promessa de prazo** — "em 7 dias", "em 24 horas", "em uma semana". Faz o leitor entender que vai levar uma semana pra funcionar; a configuração leva **horas**. Prazo cria objeção de esforço onde não existe.

**O slide de CTA nomeia o produto em texto:** rótulo `CARTILHA DAS MÉTRICAS REAIS` + o nome no apoio. "Link na bio" sozinho é endereço, não CTA.

**O apoio promete capacidade, não velocidade.** ✅ "você passa a ver de onde cada venda veio" · ❌ "em 7 dias você vê".

Copy com prazo ou sem o produto nomeado → **não renderize**.

---

## ⛔ GATE DE FIO CONDUTOR — checar ANTES de renderizar

Vale para copy escrita aqui **e** para copy recebida (Notion, usuário, `conteudo-low-ticket`). Copy que não passa nas 4 checagens **não vira JPG** — corrija a sequência primeiro. Renderizar slide bonito com sequência quebrada é desperdiçar render.

### 1. Teste dos títulos
Leia só os títulos, em ordem. Formam **um parágrafo contínuo**, onde cada slide gera a pergunta que o próximo responde? Se viram uma lista de argumentos avulsos → **não renderize**.

### 2. Teste do embaralhamento
Troque a ordem dos slides do meio. Se nada quebra, não há lógica — há uma lista → **não renderize**.

### 3. Constante + variável
Pelo menos **3 slides seguidos com o mesmo tipo de slide** (mesmo layout no JSON), onde só **um elemento muda**: o item ativo da lista, o dia, o número. Se cada slide usa um tipo diferente (7 layouts em 9 slides), o leitor lê 9 informações desconectadas → **não renderize**.

**Como isso se traduz no JSON:** slides consecutivos com o **mesmo `tipo`**, mesmos itens de lista, mudando só o índice ativo / o destaque. É esse padrão que produz a sensação de arrastar pra "ver o próximo acender".

### 4. Lista aberta = lista paga
Lista prometida em um slide ("as três desculpas", "os quatro contatos") precisa ser classificada:
- **Lista-eixo** (o carrossel é sobre ela) → paga **item por item**, um slide cada, lista inteira na tela, um item acendendo. É ela que vira a constante da checagem 3.
- **Lista-apoio** (3 exemplos ilustrativos) → pode ficar num slide só, **desde que exista outra constante** no carrossel (espelho de dois slides, linha do tempo, número/termo gigante que se repete mudando de cor).

**Se o carrossel não tem nenhuma outra constante, a lista É o eixo.** Lista aberta sem pagamento e sem outra constante → **não renderize**.

### 5. Lista-payload MASCARA o que ainda não chegou

Antes de renderizar uma lista-eixo, pergunte: **os itens são andaime ou são o conteúdo?**

- **Andaime** (`Segunda`, `Quarta`, `Sexta`, `Domingo` · `DIA 0`, `DIA 3`, `DIA 8`): mostrar os próximos em cinza **não estraga nada**. É um calendário. A curiosidade é o que *acontece* naquele dia, não o rótulo.
- **Payload** (`O SAFARI APAGOU O COOKIE ANTES DA COMPRA`, `SATUROU O PÚBLICO`): o item **é** a informação. Exibi-lo em cinza no slide 03 **entrega a punchline do slide 05 na abertura**. O leitor lê os três de uma vez e não precisa mais arrastar.

**Regra:** em lista-payload, os itens ainda não alcançados aparecem **mascarados** — o leitor vê o *slot*, nunca o texto.

**Três estados, não dois:**

| Estado | Cor | Peso / caixa | Conteúdo |
|---|---|---|---|
| `visto` (i < ativa) | `#5A6068` | 400, caixa normal | o texto real |
| `ativo` (i === ativa) | `#FFFFFF` (marca no accent) | 600 | o texto real |
| `porvir` (i > ativa) | `#3A3E44` | letter-spacing 0.35em | **máscara `· · · · ·`** |

```javascript
const estado = i < ativa ? 'visto' : (i === ativa ? 'ativo' : 'porvir');
const texto  = estado === 'porvir' ? '· '.repeat(18).trim() : item.txt;
// nunca renderizar item.txt quando estado === 'porvir'
```

Isso preserva a constante (a grade de N slots está sempre na tela) **e** devolve o motivo de arrastar. Andaime pode revelar; payload mascara.

**Corpo dos itens:** 34px, caixa normal, só o ativo em peso 600. Caixa alta a 46px quebra em duas linhas por item e afoga o slide.
**Rótulo da lista vem ANTES da lista** (`order: -1`), nunca depois.

### Coerência obrigatória
- **Um narrador só** do primeiro ao último slide (não pular de "eu" → "as contas que eu abro" → "você").
- **Caso aberto na capa é fechado antes do CTA.** Número solto (ROAS, %) sem ancoragem no caso não entra.
- **Slide 2 abre o loop** — promete a sequência, não comenta o slide 1.
- **Sem dois slides dizendo a mesma coisa.** Cada slide avança ou é cortado.

> **Referência de ouro:** "Ninguém compra no primeiro clique" — linha do tempo Segunda→Domingo, a mesma lista de 4 itens em 4 slides, um dia acendendo por vez. Em dúvida, compare a sequência com esse carrossel.

---

Transforma um tema/copy em **carrossel renderizado**: JPGs 1080x1350 com a identidade visual do produto, entregues numa **pasta por post no padrão N8N** (`img-01.jpg`, `img-02.jpg`... + `legenda.txt`) prontos pro fluxo de aprovação no WhatsApp e publicação automática, + registro da copy no Notion pra revisão e controle.

> **Divisão de trabalho:** a `conteudo-low-ticket` é o motor de copy (frameworks, funil, ganchos). Esta skill é a fábrica: pega a copy, escolhe os tipos de slide certos, renderiza e salva. Se a copy ainda não existe, gere-a AQUI seguindo as regras herdadas (ver `references/regras-de-copy.md`).

---

## Fluxo de trabalho

0. **Pergunte a fonte do conteúdo.** Se o pedido já não deixar claro, pergunte antes de qualquer coisa (uma pergunta só, com as opções): **(a)** o usuário tem uma ideia/tema na cabeça, **(b)** ele vai passar o link de uma página do Notion com o conteúdo (ex.: pauta da semana), ou **(c)** puxar da base "Conteúdo Low Ticket" o próximo item planejado. Se ele mandar um link do Notion junto do pedido, NÃO pergunte — busque a página (Notion fetch), extraia tema/copy/funil dela e siga. Se a página do Notion já tiver copy pronta, use-a como base (ajustando pro formato dos slides) em vez de escrever do zero.
1. **Copy primeiro.** Leia `references/regras-de-copy.md` (regras herdadas da conteudo-low-ticket + contexto do produto). Se o usuário só deu o tema, escreva a copy completa do carrossel (8–10 slides, funil definido) **e a legenda do post** (1ª linha = gancho independente, corpo, CTA/comando, 3–5 hashtags) e mostre em texto ANTES de renderizar — mais barato iterar em texto que em imagem.
1b. **Rode o GATE DE FIO CONDUTOR (seção acima) na copy — bloqueante.** Títulos, embaralhamento, constante+variável, lista paga. Copy reprovada não vira JPG: conserte a sequência e só então siga.
2. **Monte o JSON.** Leia `references/design-system.md` para os tipos de slide e o schema. Mapeie cada slide da copy pro tipo visual certo (capa → gancho2 → pontos/lista/vs/prova → quote → cta). Use os destaques `*verde*` (métrica confiável/decisão) e `~vermelho~` (leitura no escuro/contradição — nunca uma plataforma) com parcimônia — 1 destaque por slide no máximo. **Inclua o campo `"legenda"`** (texto puro, com `\n` entre parágrafos) e, se quiser nome de pasta explícito, o campo `"pasta"` (senão vira `post-<hoje>-<slug>`).
3. **Renderize.** `python3 scripts/gera_carrossel.py carrossel.json pasta_base/`. O script cria **uma subpasta nova por post** dentro de `pasta_base/`, no padrão N8N: `post-AAAA-MM-DD-<slug>/` com `img-01.jpg`, `img-02.jpg`... (JPG, a ordem numérica = ordem dos slides no Instagram) + `legenda.txt`. As fontes já estão em `assets/fonts/` — não precisa de internet.
4. **Revise visualmente.** Abra os JPGs (view) e OLHE o resultado antes de entregar: texto cortado? destaque no lugar certo? hierarquia clara? Fundo escuro sem sujeira de compressão? Corrija o JSON e regenere se preciso (o script sufixa `-2`, `-3` se a pasta já existir — não reaproveita pasta antiga).
5. **Entregue.** Gere direto em `/mnt/user-data/outputs/` (ou zipe a subpasta do post) e apresente. A pasta já está pronta pro N8N: ele detecta a pasta nova → pega `img-01.jpg…` ordenadas + `legenda.txt` → monta a prévia → manda aprovar no WhatsApp → publica. Destino final do Artur no Drive: `G:\Meu Drive\Trafego\Claude\Criativos`. Se a capa tiver `"foto": true`, avise que a zona demarcada é onde entra o recorte PNG dele.
6. **Salve no Notion.** Crie a página na base "Conteúdo Low Ticket" (ver abaixo) com copy slide a slide, legenda e specs. Status inicial: **Rascunho**.

---

## Notion — onde e como salvar

- **Data source ID:** `ebd39656-d2b7-43c6-bb6b-b96a66e6ddfc` (base "Conteúdo Low Ticket"). O ID é a fonte canônica — se a página-mãe ainda estiver com o nome antigo "Método das Vendas Reais — Conteúdo", isso é um rename a fazer no Notion à parte; **não deixe de salvar por causa do nome**. Se o ID não for encontrado, use Notion search por "Conteúdo Low Ticket" e confirme com o usuário antes de criar outra.
- **Propriedades:** `Nome` (título do carrossel), `date:Data:start` (hoje), `Formato` = "Carrossel", `Funil` (Topo/Meio/Fundo), `Status` = "Rascunho", `Nº Slides`, `Slug` (mesmo slug dos arquivos)
- **Conteúdo da página:** seção "Slides" com a copy de cada slide numerada (tipo + texto), seção "Legenda" (o mesmo texto que foi pro `legenda.txt` — 1ª linha = gancho independente, corpo, CTA), seção "Specs" (1080x1350, nº de slides, hashtags 3–5), e uma seção "Arquivos" citando o nome da pasta do post e os `img-01.jpg…` gerados (as imagens ficam no download/Drive; o Notion guarda a copy).

---

## Regras de conduta

- **Texto na imagem é curto.** Título de slide ≤ 12 palavras; corpo ≤ 25 palavras. Se a copy não cabe, corte a copy — o script reduz a fonte, mas fonte pequena mata o carrossel no mobile.
- **1 ideia por slide, 1 destaque por slide.** Verde = métrica confiável/decisão; vermelho = leitura no escuro/contradição entre fontes. **Nunca pintar uma plataforma de vermelho como inimiga.** Nunca os dois destaques no mesmo trecho.
- **A plataforma nunca é vilã; nenhuma fonte é a verdade.** Ver a REGRA DE POSICIONAMENTO acima.
- **Slide 1 carrega 80% do peso.** Hook de 5–8 palavras, específico pro dono de e-commerce. Slide 2 precisa funcionar sozinho (o Instagram reexibe a partir dele).
- **Sempre revisar o PNG renderizado antes de entregar.** Nunca entregue sem olhar.
- **Sem overpromise.** Prometa clareza ("saber o que gerou a venda"), nunca faturamento garantido.
- **Variações:** se o usuário pedir volume, varie o gancho da capa (4–5 versões da capa é mais barato que 5 carrosséis inteiros) — o método pede teste de variações.
- Ao final, ofereça: gerar variações de capa, produzir o próximo carrossel do calendário, ou atualizar o Status no Notion quando for postado.
