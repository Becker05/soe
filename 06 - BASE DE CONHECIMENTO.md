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
| _demais temas da fila_ | INEXISTENTE — acionar gate (doc 08) |

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
- **Prova exibível** (sim / não / anonimizada / autorização pendente — se a prova pode aparecer em tela; um caso que só existe como texto não sustenta o framework Vídeo curto do 04B)
- **Provas já publicadas** (prova · formato · data · contas alcançadas)
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
- **Prova exibível:** P-03 sim. Caso 522 vs 250 com autorização de uso pendente.
- **Provas já publicadas:** 567 vs 317 · carrossel · 6 contas alcançadas. ⚠ Número publicado sem origem no Banco de Provas. Verificar procedência ou retirar de circulação.
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
## Verbete: JANELA DE ATRIBUIÇÃO
Conceito: Janela de atribuição
Definição: É o prazo que cada ambiente usa para decidir se uma compra ainda pode ser creditada a um clique ou a uma visualização que aconteceram antes dela.
Pergunta de negócio respondida: "O prazo de crédito explica a diferença entre os dois números que estou comparando?"
Impacto no negócio: A janela define quantas compras entram na conta de cada campanha dentro de um relatório. Prazos diferentes produzem contagens diferentes para a mesma operação, sem que uma única venda tenha mudado. Quem compara dois relatórios sem saber o prazo de cada um está comparando contagens feitas com réguas distintas, e decide verba em cima dessa comparação.
Erro comum: Alterar o prazo de crédito e ler a variação como queda ou alta de vendas. O segundo erro, mais frequente: comparar o número do gerenciador com o de um relatório do GA4 sem verificar qual prazo cada ambiente aplicou naquele recorte.
Analogia canônica: O prazo combinado de uma comissão de indicação. A loja paga quem indica se a compra acontecer em até sete dias. Se o combinado passa para um dia, parte das comissões deixa de ser paga. As vendas continuam exatamente as mesmas. Mudou quem recebe o crédito, e só isso. (Evitar analogias de relógio adiantado, prazo vencido ou validade estragada. Todas sugerem que existe um prazo correto e os outros estão errados.)
Decisão que influencia: Escalar, manter ou pausar campanha. Comparar dois períodos da mesma conta. Comparar canais com ciclos de compra diferentes. Definir meta de ROAS ou de CPA por canal — uma meta só se sustenta com o prazo declarado ao lado.
Objeção frequente + resposta: "Mudei a janela e as vendas caíram pela metade. Então o número anterior estava inflado?" → Os dois números contaram segundo o prazo que receberam. A pergunta útil vem antes: qual prazo corresponde ao ciclo de compra da sua loja e à decisão que você precisa tomar agora. Trocar a janela sem cruzar com pedidos aprovados e receita da loja troca o retrato, não a informação.
Limitações e exceções: Clique e visualização têm prazos separados e podem ser configurados de forma independente. A janela é um componente do crédito, ao lado do modelo, do escopo, do fuso horário, da deduplicação e da qualidade da implementação — isolar o efeito dela exige manter todo o resto constante. Mudança de configuração costuma valer daqui para frente e não recalcular o histórico do relatório, o que precisa ser validado no ambiente antes de qualquer comparação de período. ⚠ Valores padrão e opções disponíveis mudam ao longo do tempo em qualquer plataforma: nunca afirmar um número de dias sem consultar a documentação oficial na data da publicação.
Afirmações permitidas:
"Cada ambiente credita dentro do prazo configurado nele."
"Uma diferença entre relatórios pode vir do prazo de crédito, e o prazo sozinho não prova erro."
"Comparar dois números sem saber a janela de cada um é comparar contagens feitas com regras diferentes."
"Mudar o prazo muda a contagem do relatório. As vendas da loja seguem as mesmas."
Afirmações proibidas:
"A janela de X dias é a correta." (não existe prazo verdadeiro)
"Janela maior infla as vendas." (inflar sugere intenção — viola a regra do vilão)
"Reduza a janela para ver suas vendas reais."
"A Meta usa uma janela larga para parecer melhor."
Qualquer número de dias apresentado como padrão de plataforma sem fonte oficial datada.
Caso / prova: P-03. Mesma campanha, mesmo período, duas regras de crédito: 82 compras e R$31 mil no gerenciador, 29 compras e R$11 mil no relatório de critério único. O custo apurado foi praticamente idêntico nos dois ambientes, R$4.879 e R$4.881, o que elimina divergência de período, de conta e de recorte. Ressalva de leitura, obrigatória neste verbete: o P-03 não isola a janela. Ele mostra o efeito combinado das regras de crédito, janela e modelo juntos. Aqui ele prova o mecanismo, não o peso específico do prazo. Enquanto não existir um recorte da mesma conta com duas janelas e todo o resto constante, a peça não pode atribuir a diferença de 82 para 29 ao prazo sozinho.
Fontes ou evidências: Banco de Provas, P-03. (A indexação da aula conflita entre o doc 05 e o patch de casos — pendência 4 do patch, não resolvida aqui.) Documentação oficial da Meta sobre configuração de janela: pendente, ver abaixo.
Prova exibível: P-03 sim.
Provas já publicadas: nenhuma.
Estado: EM REVISÃO — não gera conteúdo até Artur validar. Ver as duas pendências.
Última revisão: 22/07/2026 (redação inicial)
Ganchos e ângulos já usados: vazio.
Pendências que separam este verbete do estado VALIDADO

1. Valores de janela na plataforma. Comportamento atual de plataforma é conhecimento temporário pelo doc 07 e não pode sair do conhecimento interno do modelo. Duas saídas:

(a) Validar o verbete sem os valores. O verbete explica o mecanismo, o erro de leitura e a decisão, e nenhuma afirmação depende de um número de dias. Basta manter a proibição do último item das afirmações proibidas.
(b) Você autoriza a consulta à documentação oficial da Meta, o campo entra com data de consulta, e o verbete passa a permitir citar configuração específica. Nesse caso vale registrar a data no próprio campo, porque o valor expira.

A rota (a) libera a produção agora. A rota (b) atrasa e entrega um verbete mais completo.

2. Caso que isole a janela. Um recorte da mesma conta, mesmo período, mesma campanha, variando só o prazo de clique. Sem isso, o verbete usa o P-03 com a ressalva registrada acima. Entra como pendência do Banco de Provas, não bloqueia a produção.

Ganchos do banco que passam a ter verbete amarrado

Nenhum gancho da lista EM FILA cita janela. Três LIBERADOS hoje amarrados a Atribuição podem migrar ou duplicar amarração quando este verbete for validado:

"O melhor criativo da jornada pode parecer o pior no último clique." (modelo, não janela — não migrar)
"Mais dados não consertam uma pergunta mal feita." (serve aos dois)
"Quatro números que eu reconcilio antes de mexer na verba." (serve aos dois)

Nenhum gancho novo foi criado aqui. Gancho novo entra pelo banco-de-ganchos com estado e verbete amarrado.
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
- **Prova exibível:** P-04 sim.
- **Provas já publicadas:** "A Meta disse ROAS 4,1. O GA4 disse 1,9" · carrossel · 9 contas alcançadas.
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
- **Prova exibível:** P-02 anonimizada. P-07 sim.
- **Provas já publicadas:** "Todo mundo trata UTM como detalhe técnico" · carrossel · 4 contas alcançadas.
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
- **Prova exibível:** P-01 parcial, ver ressalva de leitura no patch de casos.
- **Provas já publicadas:** nenhuma.
- **Estado:** VALIDADO
- **Última revisão:** _(preencher)_
- **Ganchos e ângulos já usados:** _(vazio)_

---

## Fila de verbetes

Ordem por demanda editorial cruzada com existência de prova. Cada novo verbete segue exatamente o schema acima. Conhecimento temporário não entra como verbete permanente sem passar por Artur — ver doc 07.

### T1 — construir primeiro (tem prova ou é extensão de verbete validado)

| Verbete | Base disponível |
|---|---|
| Direct | P-01, P-07 |
| Janela de atribuição | extensão de Atribuição |
| Deduplicação | adjacente a P-03 |
| Server-side | conhecimento estável, sem prova própria ainda |

### T2 — demanda alta, sem prova própria (exige auditoria ou caso antes)

Cross-domain · pedidos sem sessão · transaction_id · eventos de funil · parâmetros de item · data layer · tráfego interno · reembolso · novo x recorrente · CAC · CPA · LTV · MER · last-click · modelagem · data-driven · Enhanced Conversions · API de Conversões · organic · referral · checkout · revenue · purchase · pixel · eventos · conversões · mensuração · rastreamento.

### T3 — temporário pelo doc 07, não vira verbete permanente sem aprovação

Consent Mode · Source Group · tráfego de IA · mudanças de plataforma em geral.

### Plataformas e ferramentas

GA4 · GTM · Meta Ads · Google Ads · Pinterest · TikTok · BigQuery · Looker Studio · Nuvemshop · WooCommerce · Shopify · Loja Integrada. Entram como contexto dentro de verbetes conceituais, não como verbete próprio — o Manifesto proíbe a ferramenta como protagonista.
