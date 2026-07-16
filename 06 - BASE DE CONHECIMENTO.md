# 06 — BASE DE CONHECIMENTO

O ativo mais valioso do sistema. Antes de escrever sobre qualquer tema, o Claude **lê o verbete** correspondente. Isso garante consistência, precisão técnica e — via o registro de ângulos — evita repetir a mesma *execução* (a tese, essa sim, se repete).

## Índice (consultar primeiro)

O orquestrador abre o índice antes de abrir qualquer verbete. Só verbete `VALIDADO` gera conteúdo (ver doc 08).

| Verbete | Estado |
|---|---|
| Atribuição | VALIDADO |
| ROAS | VALIDADO |
| UTM | VALIDADO |
| (not set) | VALIDADO |
| _demais temas do roadmap_ | INEXISTENTE — acionar gate (doc 08) |

## Estados possíveis

`VALIDADO` (gera conteúdo) · `EM REVISÃO` (não gera) · `RASCUNHO` (não gera) · `OBSOLETO` (não gera). Em qualquer estado que não seja VALIDADO, o Claude interrompe e avisa o motivo.

## Schema fixo de cada verbete

- **Conceito**
- **Definição** (uma frase, sem jargão, tecnicamente precisa)
- **Pergunta de negócio respondida**
- **Impacto no negócio**
- **Erro comum**
- **Analogia canônica**
- **Decisão que influencia**
- **Objeção frequente + resposta**
- **Limitações e exceções**
- **Afirmações permitidas**
- **Afirmações proibidas**
- **Caso / prova**
- **Fontes ou evidências**
- **Estado** (VALIDADO / EM REVISÃO / RASCUNHO / OBSOLETO — só VALIDADO gera conteúdo)
- **Última revisão**
- **Ganchos e ângulos já usados** (gancho literal · tese · analogia · exemplo · formato · data)

## Regra de repetição (substitui a antiga "ganchos não se repetem")

O mesmo **gancho literal** não deve ser reutilizado em intervalo curto. A mesma **tese central pode e deve reaparecer**, desde que mude pelo menos um: novo exemplo, nova pergunta, novo nível de consciência, nova decisão, novo formato, nova analogia (quando permitido). O sistema evita conteúdo duplicado sem obrigar a marca a abandonar suas ideias-âncora.

## Regra de precisão (vale para todos os verbetes)

Quando o tema depender de contexto técnico, não transforme uma tendência em regra universal. Use "pode", "depende do relatório", "precisa ser validado", "a diferença, sozinha, não prova erro". Nenhuma fonte isolada é "a verdade": a plataforma de anúncios, o GA4, a loja, o CRM e o financeiro respondem a perguntas diferentes. A autoridade da marca está em entender o papel de cada fonte, validar a coleta, reconciliar diferenças, explicar limitações e transformar a leitura em decisão.

---

## Verbete: ATRIBUIÇÃO

- **Conceito:** Atribuição
- **Definição:** É a regra que decide a qual campanha/canal uma venda será creditada quando o cliente passou por vários pontos de contato antes de comprar.
- **Pergunta de negócio respondida:** "Posso confiar que essa campanha realmente gerou essa venda?"
- **Impacto no negócio:** Define onde o gestor acha que o dinheiro está funcionando e, portanto, onde coloca mais verba. Atribuição mal compreendida = verba no lugar errado.
- **Erro comum:** Comparar diretamente o número atribuído pela plataforma de anúncios com o número de um relatório do GA4 e concluir que uma delas está errada. Cada ambiente pode usar janelas, modelos, escopos e regras diferentes.
- **Analogia canônica:** Câmeras posicionadas em pontos diferentes do mesmo jogo. Cada uma registra uma parte real da jogada, mas nenhuma câmera isolada mostra o campo inteiro. (Evitar a analogia de "dois árbitros", que sugere que um deles define a verdade.)
- **Decisão que influencia:** Quanto investir em cada canal; se um canal "caro" no último clique na verdade abre a jornada.
- **Objeção frequente + resposta:** "Então em qual número eu acredito?" → Antes de escolher um número, entenda qual pergunta cada relatório responde. A plataforma mostra as conversões que atribuiu aos anúncios segundo suas próprias regras. O GA4 organiza jornada e conversões segundo a coleta, o escopo e o modelo do relatório consultado. A decisão vem da reconciliação dessas leituras com pedidos, receita e contexto da operação.
- **Limitações e exceções:** A Meta não mostra apenas "influência"; ela credita conforme janela, eventos observados ou modelados, interação com anúncios, configuração da conta e modelo. O GA4 não é genericamente "last-click"; tem relatórios, escopos e modelos distintos, e a leitura muda conforme o relatório.
- **Afirmações permitidas:** "Cada ambiente atribui segundo janelas, modelos e regras próprias." · "A diferença entre plataformas, sozinha, não prova erro."
- **Afirmações proibidas:** "A Meta mostra influência e o GA4 mostra o fechamento." · "Uma das plataformas está mentindo."
- **Caso / prova:** Em uma operação analisada, a Meta apresentou 522 compras atribuídas enquanto um relatório do GA4 apresentou 250 compras para o mesmo período. A diferença não prova, por si só, que uma plataforma esteja errada — exige verificar janela, modelo, escopo, período, implementação, deduplicação e dados da loja antes de orientar a decisão. (Registro interno abaixo.)
- **Fontes ou evidências:** Print/relatório da operação âncora — ver bloco de registro interno.
- **Estado:** VALIDADO — ressalva: a conclusão "nenhuma está errada" só vale após auditoria da implementação.
- **Última revisão:** _(preencher na entrada no repo)_
- **Ganchos e ângulos já usados:** _(vazio)_

### Registro interno do caso 522 vs 250 (preencher antes de usar como prova forte)
```md
- Período analisado:
- Receita da loja:
- Pedidos aprovados:
- Pedidos cancelados:
- Investimento:
- Janela da Meta:
- Modelo/relatório do GA4:
- Fuso horário:
- Consentimento:
- Implementação validada:
- Fonte do print:
- Autorização para uso:
```

---

## Verbete: ROAS

- **Conceito:** ROAS (retorno sobre o investimento em anúncios)
- **Definição:** Relação entre a receita atribuída aos anúncios e o valor investido em mídia, dentro de um período e de uma regra de atribuição.
- **Pergunta de negócio respondida:** "Esse canal/campanha merece mais investimento?"
- **Impacto no negócio:** É usado para escalar, manter ou reduzir investimento. Como a receita atribuída varia entre plataformas e modelos, diferentes relatórios podem apresentar ROAS distintos para a mesma operação.
- **Erro comum:** Tratar o ROAS exibido por uma plataforma como se ele representasse sozinho o retorno financeiro completo do negócio.
- **Analogia canônica:** É como avaliar um investimento olhando só o extrato de uma corretora, sem cruzar com o que caiu na conta. O número está certo — mas não é a foto inteira.
- **Decisão que influencia:** Escalar, manter ou desligar campanha; definir meta de ROAS por canal.
- **Objeção frequente + resposta:** "Meu ROAS na Meta é 4. Então está ótimo, não é?" → Pode ser um bom sinal dentro do modelo da Meta, mas esse número precisa ser analisado junto com pedidos, receita da loja, margem, novos clientes, outros canais e o papel da campanha na jornada. A pergunta não é apenas se o ROAS é alto, mas se a leitura sustenta uma decisão segura de investimento.
- **Limitações e exceções:** ROAS depende de receita atribuída, investimento, período, modelo, canal e janela. A relação entre receita total da loja e investimento total pode se aproximar do MER, mas não deve ser chamada automaticamente de "ROAS real".
- **Afirmações permitidas:** "O ROAS muda conforme a receita atribuída e o modelo analisado."
- **Afirmações proibidas:** "O ROAS do caixa é o ROAS verdadeiro." · "Existe um único ROAS real."
- **Caso / prova:** No caso âncora, ROAS de 4,10 (Meta) e 1,91 (relatório GA4 de último clique) na mesma operação — leituras diferentes que só sustentam decisão quando reconciliadas.
- **Fontes ou evidências:** Mesma operação âncora.
- **Estado:** VALIDADO
- **Última revisão:** _(preencher)_
- **Ganchos e ângulos já usados:** _(vazio)_

---

## Verbete: UTM

- **Conceito:** UTM
- **Definição:** São etiquetas presas ao link do anúncio para o analytics identificar de onde veio cada visita e cada venda.
- **Pergunta de negócio respondida:** "De onde realmente vieram minhas vendas?"
- **Impacto no negócio:** Sem um padrão de UTMs, a origem das visitas e vendas fica fragmentada. O gestor pode interpretar a mesma campanha como várias iniciativas diferentes ou comparar canais com critérios inconsistentes.
- **Erro comum:** Usar maiúsculas/minúsculas diferentes, nomes inconsistentes, parâmetros incompletos ou padrões distintos para o mesmo canal. Isso fragmenta os relatórios e pode fazer a mesma campanha aparecer em várias linhas ou em agrupamentos inesperados.
- **Analogia canônica:** É a etiqueta na bagagem no aeroporto. Se cada balcão escrever o destino de um jeito, a mala se perde — não porque o sistema falhou, mas porque a etiqueta estava bagunçada.
- **Decisão que influencia:** Confiança em qualquer relatório de origem de venda; toda decisão de canal depende disso estar limpo.
- **Objeção frequente + resposta:** "UTM é detalhe técnico, não muda meu faturamento." → Não muda o faturamento, muda a sua capacidade de saber o que gerou o faturamento — e é isso que decide onde você investe amanhã.
- **Limitações e exceções:** UTMs inconsistentes normalmente provocam fragmentação de origem/mídia/campanha, agrupamentos errados, linhas semanticamente duplicadas e tráfego classificado como *unassigned* ou em categorias inesperadas. Não necessariamente aumentam o `(not set)`.
- **Afirmações permitidas:** "UTMs inconsistentes fragmentam e prejudicam a leitura de origem, mídia e campanha."
- **Afirmações proibidas:** "UTM malformada sempre gera not set."
- **Caso / prova:** Auditorias reais em que UTMs malformadas eram causa secundária de confusão nos relatórios de origem.
- **Fontes ou evidências:** _(referenciar auditoria específica ao publicar)_
- **Estado:** VALIDADO
- **Última revisão:** _(preencher)_
- **Ganchos e ângulos já usados:** _(vazio)_

---

## Verbete: (not set)

- **Conceito:** `(not set)` / valor ausente em uma dimensão
- **Definição:** É o valor exibido quando o GA4 não possui informação suficiente para preencher determinada dimensão naquele relatório.
- **Pergunta de negócio respondida:** "Posso confiar nessa análise ou tem informação faltando?"
- **Impacto no negócio:** Um volume relevante de `(not set)` pode limitar a confiança em uma análise. Mas seu significado precisa ser investigado dentro do relatório em que apareceu — não tratado como um problema único e universal.
- **Erro comum:** Interpretar todo `(not set)` como perda de origem de tráfego ou como falha automática do GA4.
- **Analogia canônica:** É um campo em branco em um formulário. O formulário não explica sozinho por que ficou vazio: a informação pode não ter sido enviada, pode não se aplicar àquela linha, ou pode ter sido consultada no contexto errado.
- **Decisão que influencia:** O quanto você pode confiar em um relatório antes de decidir verba.
- **Objeção frequente + resposta:** "Sempre vai existir um pouco de `(not set)`, certo?" → Pode existir, mas a aceitabilidade depende da dimensão, do relatório e do volume. Antes de corrigir, é preciso identificar exatamente qual informação está faltando e por que não foi preenchida.
- **Limitações e exceções:** A causa depende da combinação entre dimensão, métrica, escopo, evento, implementação, processamento e integração. `(not set)` não significa sempre "origem desconhecida".
- **Afirmações permitidas:** "`(not set)` é um valor ausente naquele relatório; a causa precisa ser investigada no contexto."
- **Afirmações proibidas:** "Not set = origem não identificada." · "Todo not set é falha do GA4."
- **Caso / prova:** _(preencher com caso próprio de redução de not set após correção de tracking)_
- **Fontes ou evidências:** _(preencher)_
- **Estado:** VALIDADO
- **Última revisão:** _(preencher)_
- **Ganchos e ângulos já usados:** _(vazio)_

---

## Roadmap de verbetes (a construir, mesmo schema)

Fila prioritária de conhecimento permanente a documentar: mensuração · rastreamento · GA4 · GTM · server-side · Meta Ads · Google Ads · Pinterest · TikTok · Consent Mode · BigQuery · Looker Studio · pixel · eventos · conversões · direct · organic · referral · cross domain · checkout · revenue · purchase · CAC · CPA · LTV · MER · data-driven · last-click · modelagem · deduplicação · Enhanced Conversions · API de Conversões · Nuvemshop · WooCommerce · Shopify · Loja Integrada.

Cada novo verbete segue exatamente o schema acima. Conhecimento temporário (mudanças de plataforma) não entra como verbete permanente sem passar por Artur — ver doc 07.
