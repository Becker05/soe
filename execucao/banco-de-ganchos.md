# Banco de Ganchos

Insumo, não fonte. Um gancho aqui não autoriza produção. Ele entra no pipeline pelo passo 9 do doc 08, depois que o verbete já foi validado.

## Condições para um gancho sair daqui

1. Passou pelo filtro de acusação (tabela de ganchos, doc 03).
2. Está amarrado a um verbete `VALIDADO` no doc 06.
3. Nenhum número nele está fora do Banco de Provas.
4. Não esconde a resposta para gerar curiosidade artificial (doc 03).

## Estados

`LIBERADO` — cumpre as quatro condições, pode ir ao cartão de decisão.
`EM FILA` — bom gancho, verbete inexistente. Destrava quando o verbete for escrito.
`BLOQUEADO` — depende de tema temporário (T3, doc 06). Exige aprovação de Artur.
`REPROVADO` — viola regra de marca ou de evidência. Não entra mesmo com verbete pronto.

---

## Origem: planilha `sistema-instagram-ga4-ecommerce`, aba 3 GANCHOS, 07/2026

50 ganchos triados. Resultado: 22 liberados, 19 em fila, 2 bloqueados, 7 reprovados.

**Nota sobre as categorias de origem.** A planilha agrupa cinco ganchos sob a categoria "Segredo". A palavra está na lista de evitar do Manifesto. A categoria foi renomeada para "Método" abaixo; os ganchos foram avaliados individualmente.

---

### LIBERADOS

| Gancho | Verbete | Observação |
|---|---|---|
| O mesmo pedido apareceu em três relatórios — e cada número pode estar correto. | Atribuição | Núcleo da tese da marca |
| Este "(not set)" pode estar contando uma história que você ignorou. | (not set) | Ajustar o fecho para não virar gancho de curiosidade vazia |
| Você pode estar pausando a campanha certa por causa do relatório errado. | Atribuição | Culpa o relatório, não o leitor. Passa |
| Mais dados não consertam uma pergunta mal feita. | Atribuição | |
| GA4 e Shopify não precisam bater para serem úteis. | Atribuição | |
| O melhor criativo da jornada pode parecer o pior no último clique. | Atribuição | |
| Um ROAS menor pode sustentar uma decisão melhor. | ROAS | |
| Três lugares para olhar antes de pausar uma campanha. | Atribuição | |
| Cinco causas de "(not set)" em compras de e-commerce. | (not set) | Ressalva: o verbete proíbe tratar causa como universal. Abrir dizendo que a causa depende do relatório |
| Quatro números que eu reconcilio antes de mexer na verba. | Atribuição · ROAS | |
| A tela que eu abro antes de acreditar em qualquer ROAS. | ROAS | |
| A pergunta que faz quatro relatórios pararem de competir. | Atribuição | |
| A plataforma não é a vilã. Decidir sem reconciliação é. | Atribuição | Redação do vilão em uma linha |
| Se você procura uma fonte da verdade, começou pela pergunta errada. | Atribuição | |
| Instalar GA4 não significa ter mensuração. | Atribuição | |
| Dashboard bonito não corrige dado ruim. | Atribuição | |
| Quem decide verba por uma tela só está escolhendo no escuro. | Atribuição | |
| Antes de aumentar a verba hoje, confira estes três sinais. | ROAS | |
| A campanha parecia campeã — até eu cruzar com os pedidos da loja. | Atribuição | Só com P-03 ou caso registrado |
| Duas telas discordavam; a resposta apareceu numa terceira. | Atribuição | |
| Veja como eu reconcilio gerenciador, GA4, loja e financeiro. | Atribuição | |
| Vou traduzir o relatório de aquisição para uma decisão de verba. | Atribuição | |

### EM FILA — destravam com o verbete

| Gancho | Verbete que falta | Camada |
|---|---|---|
| O tráfego direto cresceu. Mas talvez essas pessoas não tenham vindo direto. | Direct | T1 |
| Tráfego direto nem sempre é gente digitando seu endereço. | Direct | T1 |
| Quer descobrir em 20 segundos se a sua compra está duplicando? | Deduplicação | T1 |
| Uma única tag duplicada pode fazer seu ROAS parecer melhor do que é. | Deduplicação | T1 |
| O erro que duplica compras quando você usa GA4 e GTM. | Deduplicação | T1 |
| Em 30 segundos, vou provar se o purchase dispara duas vezes. | Deduplicação | T1 |
| Antes de remover a tag antiga, confirme se a nova compra está deduplicada. | Deduplicação | T1 |
| Server-side melhora a coleta, mas não cria uma verdade única. | Server-side | T1 |
| A sua Shopify tem 100 pedidos. Por que o GA4 mostra só 72? | Pedidos sem sessão | T2 · números precisam sair do Banco |
| O filtro que separa pedido sem sessão de atribuição quebrada. | Pedidos sem sessão | T2 |
| Seu painel pode parecer normal enquanto a coleta já está quebrada. | Data layer | T2 |
| Não troque o tema da Shopify antes de validar este evento. | Data layer | T2 |
| Sete sinais de que seu rastreamento quebrou em silêncio. | Data layer | T2 |
| O erro de transaction_id que faz a venda sumir do teste. | transaction_id | T2 |
| A loja culpou o tráfego. O problema estava num ID repetido. | transaction_id | T2 · exige caso registrado |
| Os seis eventos mínimos de um funil de e-commerce. | Eventos de funil | T2 · risco de virar "curso de GA4" |
| Este é o checklist que uso para auditar compra ausente no GA4. | Pedidos sem sessão | T2 |
| Esta é a ordem certa para investigar uma queda de conversões. | (múltiplos) | T2 |
| O melhor alarme de rastreamento cabe numa divisão semanal. | (múltiplos) | T2 |

### BLOQUEADOS — tema temporário

| Gancho | Motivo |
|---|---|
| Se você usa GA4 com Google Ads, revise isto depois da mudança de 15 de junho. | Consent Mode é T3. Exige checagem na documentação oficial e aprovação de Artur |
| Seu consentimento pode estar cortando sinais sem mostrar erro. | Idem |

### REPROVADOS

| Gancho | Regra violada |
|---|---|
| Eu segui 154 pedidos e descobri por que a origem desaparecia. | Caso de terceiro em primeira pessoa. O caso é de um post do r/GoogleAnalytics, registrado na própria aba de pesquisa como fonte externa |
| Metade dos pedidos que você compara talvez nunca tenha tido uma sessão. | Proporção sem fonte no Banco de Provas |
| Você está comparando pedido com sessão — e chamando a diferença de bug. | Acusa o leitor. Reescrever: "Pedido e sessão são unidades diferentes. A diferença entre eles não é bug" |
| Esta UTM transforma campanha paga em tráfego direto. | Contraria as limitações do verbete UTM. O efeito típico é fragmentação, não direct garantido. Reescrever com "pode" |
| Não publique sua medição antes de fazer este teste no DebugView. | Ferramenta como protagonista, sem verbete |
| O detalhe do checkout que devolve a origem da venda. | Esconde a resposta para gerar curiosidade. Sem verbete |
| O faturamento caiu semanas depois de um criativo ser pausado. | Afirma resultado sem caso registrado no Banco de Provas |

---

## Ganchos já publicados

Rastreio para não repetir gancho literal em intervalo curto (doc 06). O gancho literal não se repete; a tese se repete sempre.

| Gancho | Formato | Alcance | Data |
|---|---|---|---|
| O problema não é a Meta. Nem o GA4. É comparar números que respondem perguntas diferentes. | Reel | 150 | ~07/2026 |
| Você desligou o anúncio errado ontem. | Reel | 144 | ~07/2026 |
| Você pode estar investindo mais dinheiro com base na leitura errada. | Carrossel | 131 (repost) | ~07/2026 |
| Como descobrir de onde cada venda realmente veio | Carrossel | 15 | ~07/2026 |
| A Meta disse ROAS 4,1. O GA4 disse 1,9 | Carrossel | 9 | ~07/2026 |
| Você aumenta a verba. A venda não acompanha | Carrossel | 7 | ~07/2026 |
| Suas campanhas mostram 567 vendas, faturamento mostra 317 | Carrossel | 6 | ~07/2026 |
| Meu Custo por Aquisição de cliente caiu | Reel | 48 | ~07/2026 |
| Foi mérito da campanha ou coincidência? | Reel | 46 | ~07/2026 |

⚠ O gancho do 567 vs 317 usa número ausente do Banco de Provas. Ver pendência 5 do doc 09.

## Como adicionar

Todo gancho novo entra com: gancho literal · categoria · verbete amarrado · estado · motivo quando reprovado. Gancho sem verbete amarrado entra como `EM FILA`, nunca como `LIBERADO`.
