"""Banco C: questões autorais, sem reprodução de questões oficiais.

Referências de escopo e estilo: programa CPA e caderno público do exame-piloto.
Dificuldade estimada pelo autor; sem calibração psicométrica oficial.
Valores, taxas e personagens de exemplos numéricos são hipotéticos.
"""

SFN = "Sistema Financeiro Nacional"
PROD = "Produtos do mercado financeiro"
REL = "Relacionamento com o cliente"
INOV = "Inovação e desenvolvimento de mercado"

PROGRAM = "https://www.anbima.com.br/data/files/6A/52/6F/A1/BED73910B07B2739B82BA2A8/Programa-Detalhado-CPA-ANBIMA.pdf"
MODELS = "https://www.anbima.com.br/data/files/DF/86/EE/B6/EB6F8910C03A3F89B82BA2A8/Caderno-de-questoes-CPA.pdf"

MCQ_C = []


def mcq(theme, pd, topic, context, options, explanation, difficulty="Médio"):
    MCQ_C.append(dict(
        theme=theme, pd=pd, topic=topic, pd_verified=True,
        context=context, options=options, correct=0,
        explanation=explanation, difficulty=difficulty,
        origin="Autoral · Banco C",
        references=[PROGRAM, MODELS],
    ))


# SISTEMA FINANCEIRO NACIONAL: 10
mcq(SFN, "1.1.1.1.2", "Órgãos normativos e supervisores",
    "Uma profissional prepara treinamento para novos atendentes. Ela precisa distinguir quem estabelece diretrizes gerais para os seguros privados de quem supervisiona as seguradoras. Qual associação deve constar do material?",
    [
        "CNSP como órgão normativo do setor e Susep como supervisora das entidades sob sua competência.",
        "Susep como órgão normativo máximo e CVM como supervisora das seguradoras.",
        "CMN como supervisor direto das seguradoras e CNSP como entidade de autorregulação privada.",
        "CNPC como órgão normativo dos seguros privados e Previc como supervisora das seguradoras.",
    ],
    "O CNSP estabelece diretrizes e normas da política de seguros privados, enquanto a Susep supervisiona as entidades de seu âmbito. A Previc atua sobre previdência complementar fechada; o CNPC integra esse outro segmento. A CVM supervisiona o mercado de valores mobiliários.",
    "Fácil")

mcq(SFN, "1.2.2", "Intermediação e desintermediação",
    "Uma indústria compara um empréstimo bancário com uma emissão de debêntures que investidores adquirirão por meio de uma distribuidora. O diretor acredita que a presença da distribuidora torna as duas captações idênticas. Como esclarecer a diferença?",
    [
        "No empréstimo, o banco assume o crédito contra a indústria; na emissão, os investidores passam a ser credores da emissora, mesmo havendo distribuição intermediada.",
        "Na emissão, a distribuidora substitui a indústria como devedora dos títulos adquiridos pelos investidores.",
        "No empréstimo, os depositantes se tornam credores diretos da indústria, sem exposição ao banco.",
        "A contratação de uma distribuidora transfere ao Banco Central o risco de inadimplência das debêntures.",
    ],
    "A distinção está em quem capta e assume a obrigação financeira. No crédito bancário, o banco concede o empréstimo; na emissão de dívida, a empresa deve aos titulares dos títulos. A participação de uma distribuidora na colocação não a transforma automaticamente em devedora ou garantidora.")

mcq(SFN, "1.3.4.1", "Retorno nominal e real",
    "Em uma simulação, uma aplicação rendeu 10,25% em um ano e a inflação do mesmo período foi 5%. Desconsiderando tributos e custos, qual foi o aumento aproximado do poder de compra do investidor?",
    ["5,00%.", "5,25%.", "10,25%.", "15,25%."],
    "O retorno real é (1 + 0,1025) / (1 + 0,05) − 1 = 0,05, ou 5%. Subtrair diretamente a inflação gera apenas uma aproximação; somá-la ou usar o retorno nominal não mede o ganho de poder de compra.",
    "Difícil")

mcq(SFN, "1.3.2", "Taxas equivalentes",
    "Uma cliente vê uma taxa efetiva de 1% ao mês, com capitalização composta, em uma simulação de 12 meses. Para comparar com outra proposta expressa ao ano, sem custos e tributos, qual taxa anual equivalente deve utilizar?",
    ["Aproximadamente 12,68% ao ano.", "Exatamente 12,00% ao ano.", "Aproximadamente 1,12% ao ano.", "Exatamente 13,00% ao ano."],
    "A taxa anual equivalente é (1,01)^12 − 1, aproximadamente 12,68%. Multiplicar 1% por 12 obtém uma taxa proporcional, não a taxa efetiva equivalente em capitalização composta. As unidades de tempo devem ser compatibilizadas.",
    "Difícil")

mcq(SFN, "1.3.3.2.3", "Valor presente",
    "Para quitar uma despesa de R$ 11.000 daqui a um ano, um cliente pode aplicar hoje a uma taxa efetiva hipotética de 10% ao ano. Sem impostos ou custos e mantendo a aplicação até a data, de quanto precisa dispor hoje?",
    ["R$ 10.000.", "R$ 9.900.", "R$ 11.000.", "R$ 12.100."],
    "O valor presente é 11.000 / 1,10 = R$ 10.000. O desconto correto divide o valor futuro pelo fator de acumulação; retirar 10% diretamente de R$ 11.000 não é equivalente a descontar pela taxa de 10%.")

mcq(SFN, "1.3.7", "Sistema de Amortização Constante",
    "Um financiamento hipotético de R$ 12.000 será pago em 10 meses pelo SAC, com juros de 1% ao mês sobre o saldo devedor no início de cada período. Sem tarifas ou seguros, qual será a primeira prestação?",
    ["R$ 1.320.", "R$ 1.200.", "R$ 1.212.", "R$ 1.440."],
    "No SAC, a amortização é constante: 12.000 / 10 = R$ 1.200. Os primeiros juros são 1% de R$ 12.000, ou R$ 120. Assim, a primeira prestação é R$ 1.320; as seguintes caem porque os juros incidem sobre saldo menor.")

mcq(SFN, "1.3.8.1", "Desconto bancário simples",
    "Uma empresa antecipa um recebível de valor nominal de R$ 10.000, com vencimento em três meses. O contrato da simulação utiliza desconto bancário simples de 2% ao mês sobre o valor nominal, sem outros encargos. Qual valor líquido será recebido?",
    ["R$ 9.400.", "R$ 9.411,76.", "R$ 9.800.", "R$ 10.600."],
    "O desconto comercial simples é 10.000 × 0,02 × 3 = R$ 600. O valor recebido é 10.000 − 600 = R$ 9.400. Dividir por 1,06 corresponderia a outra modalidade de desconto; usar apenas um mês ignora o prazo contratado.",
    "Difícil")

mcq(SFN, "1.2.4.2", "Instrumentos de política monetária",
    "O Banco Central reduz o recolhimento compulsório de determinada modalidade de depósito. Uma cliente pergunta como essa medida pode afetar a oferta de crédito. Qual explicação reconhece o mecanismo e seus limites?",
    [
        "Pode liberar liquidez e favorecer a oferta de crédito, mas os empréstimos também dependem de demanda, risco e decisões das instituições.",
        "Obriga os bancos a reduzir imediatamente todas as taxas de empréstimo no mesmo percentual da redução do compulsório.",
        "Retira recursos disponíveis dos bancos, porque aumenta a parcela dos depósitos que deve permanecer recolhida.",
        "Substitui a análise de crédito dos clientes, pois os recursos liberados passam a ter garantia automática do Tesouro.",
    ],
    "O compulsório vincula parcela dos recursos captados. Sua redução pode ampliar a liquidez disponível, mas isso não garante concessão de crédito nem redução automática de taxas. O resultado depende também da demanda e da avaliação de risco.")

mcq(SFN, "1.4.7", "Portabilidade de custódia",
    "Um investidor deseja transferir a custódia de ações de sua titularidade para outra instituição, sem vender os ativos nem mudar seu titular. Antes de iniciar, ele pergunta o que deve conferir. Qual orientação é adequada?",
    [
        "Verificar procedimentos, dados de titularidade, elegibilidade e eventuais pendências; transferir custódia não equivale a vender e recomprar.",
        "Vender as ações obrigatoriamente antes de solicitar a transferência, pois a custódia não pode mudar com a posição mantida.",
        "Escolher um novo titular para os ativos, porque transferir custódia exige mudança de propriedade.",
        "Usar a cotação histórica de compra como garantia do valor que as ações terão depois da transferência.",
    ],
    "A portabilidade de custódia, nas condições descritas, mantém os ativos e a titularidade. Procedimentos e pendências precisam ser verificados. A operação não implica venda obrigatória, alteração de proprietário ou garantia de preço de mercado.")

mcq(SFN, "1.4.12", "Transparência na remuneração da distribuição",
    "Uma cliente encontra dois canais que oferecem a mesma aplicação e pergunta se o atendimento chamado de 'gratuito' significa ausência de remuneração. Qual resposta é mais transparente?",
    [
        "Pode haver remuneração indireta na distribuição; devem ser explicados o modelo aplicável, os custos e os potenciais conflitos, conforme as regras do canal.",
        "A ausência de cobrança avulsa significa que nenhuma parte da cadeia recebe remuneração pela distribuição.",
        "A remuneração só interessa ao cliente se for debitada separadamente no extrato bancário.",
        "A informação pode ser omitida se o produto tiver rentabilidade histórica superior ao de um concorrente.",
    ],
    "O atendimento pode ser remunerado de modo direto ou indireto. A transparência exige explicar o modelo e os conflitos pertinentes, e não inferir gratuidade total pela ausência de débito avulso. Rentabilidade histórica não substitui a informação sobre custos.")

# PRODUTOS DO MERCADO FINANCEIRO: 16
mcq(PROD, "2.1.1.1.2", "Preço e taxa de títulos prefixados",
    "Um cliente comprou um título prefixado com vencimento em cinco anos. Um mês depois, as taxas exigidas pelo mercado para títulos equivalentes subiram. Ele precisa vender antes do vencimento. Mantidos os demais fatores, o que tende a acontecer?",
    [
        "O preço de mercado tende a cair; vender antes do vencimento pode gerar retorno diferente da taxa contratada.",
        "O preço tende a subir para compensar o comprador pela elevação das taxas disponíveis no mercado.",
        "O preço fica inalterado, porque a taxa contratada impede oscilações antes do vencimento.",
        "O emissor deve recomprar pelo valor aplicado corrigido pela nova taxa de mercado.",
    ],
    "Preço e taxa de desconto têm relação inversa. Quando o mercado passa a exigir taxa maior, o valor presente dos pagamentos fixados tende a cair. A taxa contratada não garante o mesmo retorno em uma venda antecipada.")

mcq(PROD, "2.1.1.1.2", "Fluxo de recebimento de títulos públicos",
    "Uma cliente quer uma sequência de recebimentos para complementar renda em data futura, e não apenas um único pagamento final. Ao apresentar títulos do Tesouro com estruturas de fluxo distintas, qual informação deve orientar a escolha?",
    [
        "As datas, a duração e a forma de atualização dos recebimentos, além dos riscos e das regras para saída antes do horizonte planejado.",
        "Somente a taxa anual informada, pois o calendário de recebimentos não altera o planejamento financeiro.",
        "Somente o nome do título, porque qualquer título público paga renda mensal desde a aquisição.",
        "A taxa do último mês, substituindo a necessidade de avaliar o prazo de acumulação e o fluxo de pagamentos.",
    ],
    "O produto deve combinar com o fluxo de caixa necessário ao objetivo. Há diferenças entre acumulação, pagamentos periódicos e pagamento único. A condição de título público não torna todos os fluxos iguais nem elimina os efeitos de uma venda antecipada.",
    "Fácil")

mcq(PROD, "2.1.1.1.7", "Classificação de risco de crédito",
    "Um relatório melhora a classificação de risco de uma empresa emissora de dívida. Um cliente conclui que a debênture ficou 'sem risco'. Qual esclarecimento é adequado?",
    [
        "A classificação expressa uma avaliação de risco de crédito e pode mudar; não constitui garantia de pagamento nem elimina risco de preço e liquidez.",
        "A melhora do rating transfere a responsabilidade de pagamento da empresa para a agência classificadora.",
        "O rating passa a garantir o preço de venda da debênture até o vencimento.",
        "A melhora permite dispensar a análise de prazo e concentração, pois o risco de perda foi eliminado.",
    ],
    "Rating é uma opinião de risco de crédito, sujeita a revisão, e não seguro ou garantia. Uma melhora pode afetar a percepção de risco, mas não elimina inadimplência possível, oscilação de preço ou dificuldade de venda.")

mcq(PROD, "2.1.1.1.4", "Mercado primário e secundário de dívida",
    "Uma companhia captou recursos ao emitir debêntures. Meses depois, uma investidora vende parte de seus títulos a outro investidor no mercado secundário. Quem recebe os recursos dessa segunda negociação, desconsiderando custos?",
    [
        "A investidora vendedora; a companhia não recebe nova captação por essa troca entre investidores.",
        "A companhia emissora, porque cada negociação secundária corresponde a uma nova emissão de dívida.",
        "A companhia e a investidora em partes iguais, independentemente do preço negociado.",
        "A agência de classificação, que redistribui os valores à companhia após atualizar o risco.",
    ],
    "Na emissão primária, os recursos captados destinam-se à emissora, conforme a operação. Na negociação secundária, o comprador paga ao titular que vende o título; a emissora permanece devedora das obrigações contratadas.",
    "Fácil")

mcq(PROD, "2.1.1.2.2.2.6", "Eventos societários: desdobramento",
    "Uma investidora possui 300 ações cotadas a R$ 90 antes de um desdobramento de uma ação em três. Considerando apenas o efeito mecânico do evento, sem oscilação de mercado, como fica a posição?",
    ["900 ações a aproximadamente R$ 30 cada, mantendo R$ 27.000.", "300 ações a aproximadamente R$ 30 cada, totalizando R$ 9.000.", "900 ações a aproximadamente R$ 90 cada, totalizando R$ 81.000.", "100 ações a aproximadamente R$ 270 cada, mantendo R$ 27.000."],
    "O desdobramento multiplica a quantidade por três e divide o preço teórico por três. O valor econômico da posição não aumenta só por esse ajuste. Reduzir a quantidade corresponderia a um grupamento, não ao evento descrito.")

mcq(PROD, "2.1.1.2.2.2.8", "Direito de subscrição e diluição",
    "Um acionista detém 100 das 1.000 ações de uma companhia. A empresa emitirá mais 500 ações da mesma espécie, oferecendo subscrição proporcional aos atuais acionistas. Quantas novas ações ele deve subscrever para manter sua participação de 10%, sem outras alterações?",
    ["50 ações.", "10 ações.", "100 ações.", "150 ações."],
    "Ele possui 100 / 1.000 = 10%. Para manter a proporção, deve adquirir 10% das 500 novas ações, ou 50. Passará a deter 150 de 1.500 ações. Sem subscrever, sua participação percentual seria diluída.",
    "Difícil")

mcq(PROD, "2.1.2.2.4", "Classes e subclasses de fundos",
    "Uma investidora compara duas classes de um mesmo fundo com carteiras distintas. Uma delas teve prejuízo. O atendimento precisa explicar a diferença entre classes com patrimônio segregado e subclasses. Qual afirmação está correta?",
    [
        "Cada classe possui patrimônio segregado; subclasses de uma mesma classe compartilham o patrimônio dessa classe, embora possam ter condições diferenciadas previstas nas regras.",
        "Cada subclasse tem patrimônio separado, mas as classes respondem indistintamente por todas as obrigações do fundo.",
        "Classes e subclasses são apenas nomes comerciais e não têm efeito sobre a organização patrimonial.",
        "A segregação impede qualquer classe de registrar perda com seus próprios investimentos.",
    ],
    "A segregação patrimonial ocorre entre classes. Subclasses integram a mesma classe, podendo diferenciar condições como público-alvo e taxas, nos limites aplicáveis. Segregação não é proteção contra perdas da própria carteira.")

mcq(PROD, "2.1.2.2.19.3", "Prestadores de serviços dos fundos",
    "O regulamento de uma classe identifica administrador fiduciário e gestor. Uma cliente pergunta quem toma as decisões de compra e venda dos ativos, dentro da política de investimento. Qual resposta é adequada?",
    [
        "O gestor toma as decisões de investimento; o administrador fiduciário exerce suas atribuições próprias de administração e funcionamento da estrutura.",
        "O administrador fiduciário define cada operação e o gestor apenas distribui as cotas ao público.",
        "O custodiante escolhe os ativos e garante que a carteira não tenha rentabilidade negativa.",
        "O distribuidor substitui o gestor sempre que um cotista solicita a compra de um ativo específico.",
    ],
    "A gestão da carteira compete ao gestor, conforme a política de investimento e a regulação. Administração fiduciária, custódia e distribuição são funções distintas. Nenhuma delas implica garantia automática de rentabilidade.",
    "Fácil")

mcq(PROD, "2.1.2.2.10", "Cotização e pagamento de resgate",
    "Uma classe informa, em seu documento de regras, cotização do resgate em D+30 e pagamento em D+2 após a cotização. Uma cliente precisa de dinheiro em dez dias e considera aplicar hoje. Qual alerta é essencial?",
    [
        "O dinheiro não estará disponível no prazo de dez dias; cotização e pagamento são etapas diferentes que precisam ser somadas conforme o calendário das regras.",
        "O pagamento ocorre em dois dias contados do pedido, porque o prazo de cotização não interfere no recebimento.",
        "A cotização em D+30 só se aplica a aplicações, e nunca a pedidos de resgate.",
        "O distribuidor pode assegurar pagamento em dez dias mesmo sem essa previsão nos documentos da classe.",
    ],
    "Cotização é a conversão das cotas no valor de resgate; pagamento é a entrega dos recursos. O prazo de pagamento após a cotização não substitui o prazo anterior. A necessidade em dez dias é incompatível com as condições descritas.")

mcq(PROD, "2.1.2", "Taxa de performance: cálculo simplificado",
    "Em um exemplo didático, R$ 10.000 tornam-se R$ 11.500 antes da performance. No mesmo intervalo, o benchmark acumula 10%. A regra hipotética cobra 20% apenas do ganho monetário que exceder o benchmark, sem outros ajustes ou taxas. Qual será a cobrança?",
    ["R$ 100.", "R$ 300.", "R$ 500.", "R$ 30."],
    "O benchmark levaria R$ 10.000 a R$ 11.000. O excedente é 11.500 − 11.000 = R$ 500; 20% disso são R$ 100. O cálculo é uma simplificação explicitada no enunciado: contratos reais podem exigir linha d'água, periodicidade e outros ajustes.",
    "Difícil")

mcq(PROD, "2.1.1.1.11", "Comparação de rentabilidade líquida",
    "Para um exercício, duas aplicações de mesmo prazo, risco e liquidez pagam, respectivamente, 120% e 95% de um mesmo indicador. A primeira sofre imposto de 20% sobre todo o rendimento e a segunda é isenta. Use cálculo proporcional, sem outros custos. Qual oferece maior rendimento líquido?",
    [
        "A primeira, equivalente a 96% do indicador depois do imposto.",
        "A segunda, porque 120% menos 20 pontos percentuais resulta em 90% do indicador.",
        "As duas, porque o imposto faz a primeira cair exatamente para 95% do indicador.",
        "A primeira, mantendo os 120%, pois o imposto incide apenas sobre o valor originalmente aplicado.",
    ],
    "Com as premissas fornecidas, o rendimento líquido da primeira é 120% × (1 − 0,20) = 96% do indicador, acima de 95%. O imposto foi dado como hipótese de cálculo, não como alíquota universal ou tabela tributária vigente.")

mcq(PROD, "2.2.3", "Portabilidade de previdência",
    "Uma cliente possui PGBL e quer reduzir os custos migrando os recursos para outro PGBL elegível à portabilidade. Um atendente sugere resgatar tudo para a conta corrente e depois contratar o novo plano. Qual encaminhamento preserva a distinção entre as operações?",
    [
        "Verificar a portabilidade direta e suas condições; resgatar e reaplicar não é o mesmo procedimento e pode antecipar tributação.",
        "Resgatar para a conta corrente, pois todo resgate de previdência é tratado como portabilidade se houver reaplicação no mesmo dia.",
        "Transferir diretamente para VGBL, pois a mudança de modalidade é requisito para qualquer portabilidade.",
        "Escolher apenas pela rentabilidade passada, dispensando a análise de taxas e das características do plano de destino.",
    ],
    "A portabilidade elegível transfere recursos entre planos compatíveis sem convertê-los em resgate ao participante. Resgatar pode gerar incidência tributária e não equivale à transferência direta. Devem ser verificados carências, compatibilidade e condições dos planos.")

mcq(PROD, "2.3.1", "Custo do crédito e capacidade de pagamento",
    "Duas propostas liberam hoje R$ 10.000 e têm o mesmo calendário de 24 parcelas mensais. A primeira cobra 24 parcelas de R$ 500 e tarifa inicial de R$ 300 paga à parte. A segunda cobra 24 parcelas de R$ 505 sem tarifa inicial. Sem outros custos, qual análise é adequada?",
    [
        "A segunda tem menor desembolso total, R$ 12.120 contra R$ 12.300; convém confirmar o CET e a capacidade de pagamento.",
        "A primeira é necessariamente mais barata, porque sua parcela é R$ 5 menor, independentemente da tarifa.",
        "As duas custam o mesmo, pois liberam igual valor inicial e têm igual prazo.",
        "A segunda custa R$ 12.420, pois a tarifa da primeira deve ser somada às duas propostas.",
    ],
    "A primeira soma 24 × 500 + 300 = R$ 12.300; a segunda, 24 × 505 = R$ 12.120. Comparar somente a parcela ignora custos. O CET considera os fluxos e encargos; a soma nominal não substitui seu cálculo nem a avaliação da capacidade de pagamento.")

mcq(PROD, "2.3.7", "Crédito para capital de giro",
    "Uma loja paga fornecedores em 30 dias e recebe dos clientes em 60 dias. O negócio é operacionalmente viável, mas sofre falta temporária de caixa nesse intervalo. Qual análise é mais coerente antes de contratar crédito?",
    [
        "Mapear o ciclo financeiro e a necessidade de capital de giro, comparando prazo e custo da linha com as entradas esperadas.",
        "Escolher financiamento para um imóvel, pois qualquer necessidade temporária deve ser tratada como compra de ativo permanente.",
        "Adotar crédito rotativo sem prazo de saída, usando o limite disponível como substituto de um fluxo de caixa.",
        "Comparar apenas a taxa nominal, ignorando o momento das entradas e o custo efetivo da operação.",
    ],
    "O descasamento entre pagamento e recebimento gera necessidade de capital de giro. A solução requer avaliar montante, prazo, custos e viabilidade do caixa futuro. Uma linha inadequada ao ciclo pode transformar uma falta temporária em endividamento persistente.")

mcq(PROD, "2.5.2.1", "Franquia e cobertura de seguro",
    "Uma apólice hipotética de automóvel cobre determinado dano material de R$ 8.000 e estabelece franquia dedutível de R$ 2.000. Não há outros limites ou exclusões aplicáveis. Qual valor a seguradora pagará nesse exemplo?",
    ["R$ 6.000.", "R$ 8.000.", "R$ 2.000.", "R$ 10.000."],
    "Pelas condições explicitadas, a parcela a cargo do segurado é R$ 2.000. A indenização é 8.000 − 2.000 = R$ 6.000. A leitura das condições é essencial: o exemplo não afirma que todos os seguros tenham a mesma modalidade de franquia.")

mcq(PROD, "2.5.1", "Seguro de vida e objetivos de proteção",
    "Um casal com filhos pequenos quer proteger a renda familiar caso um dos responsáveis faleça durante os próximos dez anos. Já mantém reserva de emergência separada. Qual critério deve orientar primeiro a análise do seguro?",
    [
        "Coberturas, capital segurado, prazo, exclusões e prêmio compatíveis com a necessidade de proteção dos dependentes.",
        "A expectativa de resgatar o dobro dos prêmios ao fim do prazo, mesmo quando não há essa previsão contratual.",
        "A contratação do maior prêmio disponível, usando seu valor como indicador suficiente de qualidade da proteção.",
        "A substituição de toda a reserva de emergência pelo seguro, pois o seguro libera recursos a qualquer solicitação.",
    ],
    "O objetivo descrito é proteção contra um evento coberto. A análise começa pela necessidade financeira dos dependentes e pelas condições contratuais. Seguro não equivale automaticamente a reserva com liquidez ou a produto com resgate garantido.",
    "Fácil")

# RELACIONAMENTO COM O CLIENTE: 9
mcq(REL, "3.1.4", "Patrimônio e liquidez",
    "Uma cliente possui imóvel de R$ 500.000, aplicação com liquidez de R$ 20.000 e dívida de R$ 120.000. Suas despesas essenciais são de R$ 5.000 mensais. Sem outras posições, qual diagnóstico é correto?",
    [
        "O patrimônio líquido é R$ 400.000 e a aplicação líquida cobre quatro meses das despesas; o imóvel não equivale a caixa imediato.",
        "O patrimônio líquido é R$ 520.000 e toda essa quantia está disponível para emergências.",
        "O patrimônio líquido é R$ 640.000, pois a dívida deve ser somada aos ativos.",
        "O patrimônio líquido é R$ 20.000, porque imóveis não integram o patrimônio pessoal.",
    ],
    "Ativos de R$ 520.000 menos obrigações de R$ 120.000 resultam em patrimônio líquido de R$ 400.000. A aplicação de R$ 20.000 cobre quatro meses de despesas de R$ 5.000. Patrimônio líquido e liquidez imediata são conceitos diferentes.")

mcq(REL, "3.1.3.2", "Orçamento e formação de metas",
    "Um cliente recebe R$ 6.000 líquidos e gasta R$ 5.400 por mês. Sem dívidas, quer juntar R$ 12.000 em 12 meses; desconsidere rendimentos. Qual orientação explicita corretamente a distância até a meta?",
    [
        "Ele precisa poupar R$ 1.000 mensais; o excedente atual de R$ 600 deixa uma diferença de R$ 400 que exige ajuste de renda, gastos ou prazo.",
        "O excedente de R$ 600 basta, pois em 12 meses acumula R$ 12.000 sem precisar de rendimento.",
        "Ele pode alcançar a meta sem mudança se aplicar todo o salário, desconsiderando as despesas essenciais.",
        "O correto é escolher primeiro o produto mais rentável, sem verificar quanto será possível aportar.",
    ],
    "A meta exige 12.000 / 12 = R$ 1.000 ao mês. O orçamento libera apenas 6.000 − 5.400 = R$ 600. Faltam R$ 400 mensais; não se deve compensar a diferença presumindo rentabilidade elevada ou ignorando necessidades básicas.")

mcq(REL, "3.1.1", "Ciclo de vida e objetivos",
    "Duas clientes têm 35 anos. Uma é responsável pela renda de três dependentes e usará dinheiro em seis meses; a outra possui renda estável, reserva formada e objetivo de vinte anos. Qual conclusão é adequada?",
    [
        "A mesma idade não determina a mesma carteira; objetivos, horizonte, capacidade financeira e tolerância ao risco devem ser considerados individualmente.",
        "Ambas devem ter a mesma alocação em renda variável, porque a idade é suficiente para definir risco.",
        "A primeira deve assumir mais risco para compensar o prazo curto, independentemente dos dependentes.",
        "A segunda pode dispensar avaliação de perfil, porque a existência de reserva define automaticamente um perfil arrojado.",
    ],
    "O ciclo de vida é um componente do planejamento, não uma regra única de alocação. Prazo, dependentes, liquidez, capacidade de suportar perdas e tolerância ao risco podem tornar necessidades muito diferentes, mesmo entre pessoas da mesma idade.",
    "Fácil")

mcq(REL, "3.4.2.6", "Adequação após mudança financeira",
    "Um cliente antes estável perdeu parte da renda e passará a retirar recursos da carteira para despesas essenciais. Seu questionário ainda registra a situação antiga. Antes de recomendar novo produto com carência longa, qual é o encaminhamento mais adequado?",
    [
        "Atualizar as informações relevantes e reavaliar a adequação à nova necessidade de liquidez e capacidade de suportar perdas.",
        "Manter a classificação antiga até o vencimento administrativo do formulário, sem considerar a informação recebida.",
        "Avaliar apenas a rentabilidade passada do produto, porque ela compensa a redução da renda.",
        "Solicitar que o cliente aumente a tolerância a perdas no questionário para preservar as recomendações anteriores.",
    ],
    "A recomendação deve refletir a situação atual conhecida. Mudanças de renda e retiradas necessárias afetam capacidade de risco e liquidez. Alterar respostas para adequar o cadastro ao produto inverte o processo de suitability.")

mcq(REL, "3.4.2", "Conflitos de interesse na recomendação",
    "Uma campanha interna aumenta a remuneração na venda de um produto. Duas alternativas podem atender à cliente, mas têm custos e riscos diferentes. O profissional divulga a comissão e acredita que isso basta para recomendar a mais remunerada. Como proceder?",
    [
        "Além de informar o conflito, comparar adequação, riscos, custos e objetivos; a divulgação não substitui a recomendação no interesse da cliente.",
        "Recomendar a de maior remuneração, pois a simples divulgação elimina qualquer problema de adequação.",
        "Apresentar somente a alternativa da campanha para não confundir a cliente com informações sobre custos.",
        "Usar a meta de vendas como critério principal e avaliar o perfil apenas depois da contratação.",
    ],
    "Transparência é necessária, mas não torna automaticamente adequada uma recomendação. O profissional deve gerir conflitos e fundamentar a escolha nos interesses e necessidades da cliente, comparando custos e riscos pertinentes.")

mcq(REL, "3.4.6", "LGPD e bases legais",
    "Uma instituição precisa conservar determinados registros de identificação para cumprir obrigação legal. Um cliente revoga o consentimento de marketing e pede que tudo seja apagado imediatamente. Qual resposta separa corretamente as finalidades?",
    [
        "Interromper o marketing baseado no consentimento revogado e avaliar a manutenção dos registros que tenham outra base legal e prazo de retenção aplicável.",
        "Continuar todas as campanhas porque a existência de obrigação legal autoriza qualquer uso comercial dos dados.",
        "Apagar inclusive registros legalmente obrigatórios, pois toda operação com dados depende exclusivamente de consentimento.",
        "Transferir os dados a parceiros antes de apagar o cadastro para preservar a possibilidade de campanhas futuras.",
    ],
    "A LGPD prevê diferentes bases legais. A revogação do consentimento afeta os tratamentos que dele dependem, mas não elimina automaticamente obrigações legais de conservação. Cada finalidade exige base válida, necessidade e limitação de uso.")

mcq(REL, "3.4.5", "Diligência diante de operação atípica",
    "Uma cliente com movimentação habitual modesta recebe transferências elevadas e solicita repasse imediato a contas de terceiros. Isso não prova crime. Qual atitude combina diligência e tratamento correto?",
    [
        "Aplicar os procedimentos internos de atualização e análise, registrar os fatos e encaminhar aos responsáveis por PLD/FTP sem prejulgar a cliente.",
        "Concluir publicamente que houve lavagem e explicar aos demais clientes por que o atendimento foi interrompido.",
        "Dividir os repasses em valores menores para reduzir a chance de a operação ser identificada pelos controles.",
        "Ignorar o desvio do padrão porque receber recursos por transferência eletrônica elimina risco de lavagem.",
    ],
    "Atipicidade é um sinal para análise, não uma conclusão de culpa. O profissional deve coletar e registrar informações pelos procedimentos autorizados e encaminhar a análise ao fluxo competente, mantendo sigilo e sem ajudar a contornar controles.")

mcq(REL, "3.4.3", "Atendimento acessível e autonomia",
    "Uma cliente com deficiência visual comparece com acompanhante para conhecer produtos. O acompanhante responde antes dela e pede para escolher em seu lugar, sem procuração ou representação legal. Como conduzir o atendimento?",
    [
        "Dirigir-se à cliente, oferecer informação acessível e verificar sua vontade e eventual representação antes de aceitar instruções de terceiros.",
        "Transferir automaticamente a decisão ao acompanhante, presumindo incapacidade em razão da deficiência.",
        "Pedir que a cliente assine sem leitura para evitar constrangimento ou demora no atendimento.",
        "Recusar atendimento individual e permitir contratação apenas quando houver acompanhante, em qualquer situação.",
    ],
    "Deficiência não permite presumir incapacidade. A informação deve ser acessível e a vontade da cliente respeitada. A atuação de terceiros depende de poderes válidos, e não de mera presença no atendimento.",
    "Fácil")

mcq(REL, "3.4.2.2", "Registro e continuidade do atendimento",
    "Um cliente relata que precisa usar uma aplicação para pagar uma cirurgia em 45 dias. O profissional identifica a necessidade, mas não registra o prazo no histórico e repassa o atendimento a um colega. Qual melhoria reduz o risco de orientação inconsistente?",
    [
        "Registrar objetivo, prazo, restrições e encaminhamentos no canal autorizado, com acesso limitado a quem necessita continuar o atendimento.",
        "Guardar os dados somente em um celular pessoal, evitando que fiquem nos sistemas da instituição.",
        "Registrar apenas o saldo investido, porque informações sobre prazo não afetam a escolha de produtos.",
        "Compartilhar o prontuário médico completo com toda a equipe comercial, independentemente de necessidade.",
    ],
    "O histórico pertinente dá continuidade ao relacionamento e sustenta a adequação. O registro deve limitar-se ao necessário, em canal autorizado e com acesso apropriado; não é justificativa para coletar ou divulgar dados sensíveis excessivos.")

# INOVAÇÃO E DESENVOLVIMENTO DE MERCADO: 5
mcq(INOV, "4.3", "Critérios ASG e comunicação de sustentabilidade",
    "Dois fundos divulgam informações ASG. Um incorpora fatores ASG à análise de riscos; outro declara objetivo específico de investimento sustentável. Uma cliente entende que as duas descrições significam a mesma coisa. Qual explicação é mais adequada?",
    [
        "Integrar fatores ASG não equivale, por si só, a assumir um objetivo sustentável específico; é preciso ler estratégia, critérios e divulgações de cada fundo.",
        "Qualquer menção a ASG garante que a carteira contém somente empresas de impacto socioambiental positivo.",
        "O fundo que integra ASG deixa de estar sujeito a riscos de crédito e de mercado.",
        "A denominação do fundo dispensa a análise dos ativos e da política de investimento.",
    ],
    "Integração de fatores ASG e objetivo sustentável específico não são expressões intercambiáveis. A avaliação depende da estratégia efetiva e de sua transparência. Rótulos não garantem impacto, retorno ou ausência de risco.")

mcq(INOV, "4.4.5.2", "Stablecoins: referência e riscos",
    "Um cliente considera uma stablecoin que busca acompanhar uma moeda fiduciária. Ele acredita que a referência de preço equivale a uma garantia de resgate em qualquer situação. Qual risco deve ser esclarecido?",
    [
        "O vínculo pretendido pode falhar; reservas, emissor, liquidez e mecanismos de resgate precisam ser avaliados.",
        "O uso de blockchain transfere automaticamente a obrigação de resgate ao banco central da moeda de referência.",
        "A paridade pretendida torna desnecessária a avaliação da contraparte e da qualidade das reservas.",
        "A possibilidade de negociação contínua garante liquidez suficiente para vender qualquer quantidade ao valor de referência.",
    ],
    "Stablecoin busca relativa estabilidade em relação a uma referência, mas isso não garante paridade permanente ou resgate irrestrito. Estrutura de reservas, riscos operacionais, contraparte e liquidez influenciam essa capacidade.")

mcq(INOV, "4.5.4", "Open Insurance",
    "Uma cliente autoriza, pelos canais do ecossistema, o compartilhamento de dados de seguros para receber propostas mais adequadas. Um vendedor promete aprovação automática e redução garantida do prêmio. Qual esclarecimento é correto?",
    [
        "O compartilhamento autorizado pode facilitar a comparação e personalização, mas não garante aceitação do risco ou preço menor.",
        "A autorização dispensa a seguradora de avaliar o risco e obriga a oferta de cobertura integral.",
        "O compartilhamento altera automaticamente a apólice vigente, mesmo sem contratação de nova proposta.",
        "A autorização permite usar os dados para qualquer finalidade futura, sem limites de escopo ou validade.",
    ],
    "Open Insurance facilita compartilhamento padronizado e autorizado, dentro das regras do ecossistema. Não elimina a análise de risco nem garante condição comercial. Compartilhar dados não equivale a contratar ou alterar uma apólice.",
    "Fácil")

mcq(INOV, "4.6.1", "IA generativa e revisão humana",
    "Uma instituição usa IA generativa para preparar respostas sobre investimentos. Em um teste, o sistema cita uma regra inexistente com linguagem convincente. Qual medida trata esse risco sem supor que a fluência do texto comprova sua precisão?",
    [
        "Exigir conferência em fontes confiáveis, limites de uso e revisão adequada antes de aplicar a orientação ao atendimento.",
        "Aumentar o tamanho da resposta, pois textos mais longos deixam de conter informações inventadas.",
        "Publicar sem revisão se a resposta tiver vocabulário técnico e não apresentar erro de gramática.",
        "Treinar apenas com campanhas comerciais e dispensar atualização das referências regulatórias.",
    ],
    "IA generativa pode produzir conteúdo plausível e incorreto. Controles devem incluir verificação, governança, proteção de dados e revisão proporcional ao risco. Linguagem fluente não demonstra exatidão jurídica ou financeira.")

mcq(INOV, "4.7.6.4", "Adquirentes e subadquirentes",
    "Uma pequena loja usa uma plataforma para aceitar cartões, sem contratar diretamente cada adquirente. A dona quer entender por que aparecem diferentes participantes no fluxo do pagamento. Qual explicação é mais apropriada?",
    [
        "Uma subadquirente pode intermediar o relacionamento comercial e operacional com adquirentes; funções, liquidação, prazos e custos precisam ser identificados no contrato.",
        "A presença de uma subadquirente faz o pagamento deixar de depender de qualquer arranjo, emissor ou adquirente.",
        "A adquirente é o consumidor que apresenta o cartão e escolhe o número de parcelas.",
        "A subadquirente se torna automaticamente o banco central responsável por garantir todas as vendas da loja.",
    ],
    "O ecossistema de cartões pode reunir emissor, bandeira, adquirente e facilitadores, como subadquirentes. O contrato deve esclarecer atribuições, custos, prazos e riscos; o uso de um intermediário não elimina os demais participantes.")


# Árvores simplificadas do simulado: 3 etapas × 3 alternativas.
TREES_C = []


def step(situation, prompt, choices):
    return dict(situation=situation, prompt=prompt, options=[
        dict(text=text, isBest=(index == 0), feedback=feedback)
        for index, (text, feedback) in enumerate(choices)
    ])


def tree(theme, pd, topic, title, intro, steps, difficulty="Médio"):
    TREES_C.append(dict(
        theme=theme, pd=pd, topic=topic, pd_verified=True,
        title=title, intro=intro, steps=steps, difficulty=difficulty,
        origin="Autoral · Banco C",
        references=[PROGRAM, MODELS],
    ))


tree(PROD, "2.1.2.2.10", "Resgate e compatibilidade com prazo",
     "Pagamento de imóvel e calendário de resgate",
     "Bianca possui uma aplicação líquida e precisa pagar a entrada de um imóvel em 45 dias. Está considerando transferir o valor a uma classe de fundo que promete retorno potencial maior.",
     [
         step("As regras da classe indicam cotização de resgate em D+60 e pagamento dois dias depois. Bianca ainda não aplicou.",
              "Qual deve ser o primeiro esclarecimento?",
              [
                  ("O prazo de saída não atende ao pagamento em 45 dias; é preciso preservar acesso ao valor necessário.",
                   "A necessidade tem data definida e anterior ao prazo de conversão. Potencial de retorno não resolve incompatibilidade de liquidez."),
                  ("O prazo de dois dias de pagamento é suficiente, pois substitui os 60 dias de cotização.",
                   "Pagamento e cotização são etapas diferentes. Não se pode ignorar o período anterior à disponibilização dos recursos."),
                  ("O retorno potencial compensa esperar, então o prazo contratual não precisa ser considerado.",
                   "O compromisso tem data e valor. Eventual retorno maior não altera o vencimento da obrigação."),
              ]),
         step("Bianca pergunta se pode aplicar apenas uma parte. A entrada exigirá R$ 80.000; ela tem exatamente R$ 80.000 disponíveis e não conta com outra fonte confirmada.",
              "Como avaliar essa possibilidade?",
              [
                  ("Não comprometer o valor já integralmente necessário com uma aplicação que não permite saída no prazo.",
                   "Não existe excedente confirmado. Mesmo uma alocação parcial retiraria liquidez do montante necessário à obrigação."),
                  ("Aplicar metade, pois diversificar produtos elimina o problema de datas de resgate.",
                   "Diversificação não transforma resgate longo em liquidez imediata; ainda faltaria parte do pagamento."),
                  ("Aplicar tudo e solicitar crédito no futuro sem comparar seu custo.",
                   "Crédito futuro não está assegurado e pode acrescentar custos e riscos que não foram avaliados."),
              ]),
         step("Bianca decide preservar a liquidez da entrada. Quer considerar a classe de prazo longo para uma futura sobra.",
              "Qual fechamento é adequado?",
              [
                  ("Registrar a necessidade e, quando houver excedente, reavaliar perfil, prazo, riscos, custos e regras de resgate.",
                   "A decisão deve se apoiar no conjunto de condições e ser revista para o objetivo e a situação financeira futura."),
                  ("Registrar apenas o retorno passado, pois já foi identificado que o produto pode ser usado no futuro.",
                   "Retorno passado não substitui a avaliação de adequação e dos prazos na data de uma possível aplicação."),
                  ("Prometer retorno mínimo para que ela aceite retomar a conversa quando sobrar dinheiro.",
                   "Potencial de retorno não autoriza garantia inexistente. O fechamento deve ser transparente."),
              ]),
     ])

tree(PROD, "2.1.1.2.2.2.8", "Subscrição e decisão do acionista",
     "Participação acionária após aumento de capital",
     "Daniel possui 200 das 2.000 ações de uma companhia. Ela anuncia emissão de mais 1.000 ações da mesma espécie, com direito de subscrição proporcional. Todos os números são hipotéticos.",
     [
         step("Daniel quer manter sua participação percentual e pergunta quantas novas ações precisaria adquirir.",
              "Qual cálculo está correto?",
              [
                  ("Subscrever 100 novas ações para continuar com 10% das 3.000 ações após a emissão.",
                   "A participação inicial é 200 / 2.000 = 10%. Ele precisaria de 10% das 1.000 novas ações, passando a 300 de 3.000."),
                  ("Subscrever 200 ações, pois é necessário repetir toda a quantidade já detida.",
                   "O direito proporcional é calculado sobre a nova emissão. Adquirir 200 elevaria a participação, não apenas a manteria."),
                  ("Não subscrever, porque a participação percentual permanece constante em qualquer aumento de capital.",
                   "Sem adquirir novas ações, ele manteria 200, mas o total aumentaria para 3.000, reduzindo sua participação percentual."),
              ]),
         step("Daniel não quer ampliar a concentração na empresa e precisa verificar alternativas para seus direitos.",
              "Qual orientação respeita sua autonomia?",
              [
                  ("Ler o aviso e os prazos, verificar possibilidade de negociação dos direitos e avaliar a decisão frente à carteira.",
                   "Exercer não é a única análise pertinente. A negociação depende das características do direito e dos prazos da operação."),
                  ("Exercer obrigatoriamente todos os direitos, independentemente de concentração ou necessidade de caixa.",
                   "Manter percentual não deve ser imposto se conflitar com objetivos, concentração ou disponibilidade financeira."),
                  ("Ignorar as datas, pois os direitos podem ser exercidos a qualquer momento depois da emissão.",
                   "Os direitos têm condições e prazos. Ignorá-los pode causar sua perda sem que o objetivo seja alcançado."),
              ]),
         step("Ele pergunta se o preço de subscrição inferior à cotação atual garante lucro.",
              "Qual resposta é adequada?",
              [
                  ("Não; o valor da ação pode mudar e a análise deve incluir condições da emissão, fundamentos, custos e riscos.",
                   "Uma diferença de preço observada hoje não garante resultado futuro nem torna a decisão livre de risco."),
                  ("Sim, a companhia deve recomprar as novas ações pela cotação atual se houver queda.",
                   "O direito de subscrição não implica essa obrigação de recompra pela companhia."),
                  ("Sim, manter a participação percentual impede qualquer perda financeira na posição.",
                   "Percentual de participação e valorização econômica são coisas distintas. A carteira pode perder valor."),
              ]),
     ], "Difícil")

tree(PROD, "2.3.7", "Crédito e ciclo financeiro",
     "Capital de giro para encomenda sazonal",
     "Renata administra uma pequena fábrica. Uma encomenda exigirá pagamentos agora e deverá gerar recebimento em quatro meses. Ela pede ajuda para comparar linhas de crédito.",
     [
         step("O atendente ainda não conhece os valores e o calendário da encomenda.",
              "Qual levantamento deve vir antes da escolha da linha?",
              [
                  ("Estimar entradas e saídas, necessidade efetiva de caixa e capacidade de pagar nas datas contratadas.",
                   "A avaliação do ciclo financeiro indica montante e prazo necessários e se a operação é suportável."),
                  ("Escolher o maior limite aprovado, porque crédito disponível deve ser integralmente utilizado.",
                   "O limite é uma autorização máxima, não uma medida automática da necessidade ou da capacidade de pagamento."),
                  ("Escolher a linha com menor prestação, sem comparar prazo total ou encargos.",
                   "Parcela menor pode decorrer de prazo maior e custo total superior. Também é necessário compatibilizar os fluxos."),
              ]),
         step("Duas linhas atendem ao calendário. Uma tem juros anunciados menores, mas inclui tarifa e seguro facultativo na proposta.",
              "Como comparar corretamente?",
              [
                  ("Solicitar a discriminação dos encargos e o CET, esclarecendo a opção do seguro e comparando os fluxos completos.",
                   "A taxa anunciada pode não representar o custo efetivo. Serviços facultativos devem ser esclarecidos e a análise deve considerar as condições efetivas."),
                  ("Comparar só a taxa de juros, porque tarifas e seguro não representam saída de caixa.",
                   "Custos adicionais podem alterar a comparação e devem entrar na avaliação da proposta efetivamente contratada."),
                  ("Aceitar o seguro sem explicação para preservar o acesso a qualquer informação sobre o crédito.",
                   "O cliente deve compreender as condições e opções. Informação sobre custo não deve depender da aceitação de produto facultativo."),
              ]),
         step("A projeção supõe recebimento integral no quarto mês. Renata admite que o comprador já atrasou pagamentos em outras operações.",
              "Qual análise complementa a decisão?",
              [
                  ("Simular atraso e necessidade de caixa adicional, verificando margem de segurança e alternativas antes de contratar.",
                   "Um cenário de atraso testa a capacidade de pagar mesmo quando o fluxo esperado não se realiza no prazo."),
                  ("Considerar o atraso irrelevante porque a previsão média coincide com o vencimento.",
                   "Coincidência entre previsão e vencimento não elimina risco de liquidez se não houver margem para atraso."),
                  ("Aumentar o limite e aplicar o excedente em produto sem liquidez até depois do vencimento.",
                   "Essa decisão acrescenta custo e descasamento, em vez de tratar a vulnerabilidade do fluxo de caixa."),
              ]),
     ])

tree(PROD, "2.5.2.2", "Coberturas e exclusões de seguro",
     "Seguro residencial e expectativa de cobertura",
     "João quer proteger sua residência e ter ajuda para uma hospedagem temporária se um evento coberto impedir o uso do imóvel. Ele recebeu uma proposta e ainda não a contratou.",
     [
         step("João diz que 'seguro residencial cobre qualquer imprevisto'.",
              "Como iniciar a orientação?",
              [
                  ("Identificar os riscos que ele deseja cobrir e comparar com coberturas, limites, franquias e exclusões da proposta.",
                   "O nome comercial não garante cobertura universal. É necessário relacionar a necessidade com as condições contratuais."),
                  ("Confirmar a cobertura universal, desde que o prêmio esteja em dia.",
                   "Pagar o prêmio não inclui riscos excluídos nem amplia automaticamente os limites contratados."),
                  ("Avaliar somente o valor total do prêmio, pois as condições são padronizadas para toda residência.",
                   "Preço isolado não permite saber se as necessidades foram atendidas; coberturas e limites podem variar."),
              ]),
         step("A proposta cobre danos materiais em determinados eventos, mas não inclui cobertura específica para despesas de hospedagem temporária.",
              "Qual esclarecimento evita uma expectativa indevida?",
              [
                  ("Dano material e hospedagem temporária são necessidades diferentes; verificar cobertura adicional ou alternativa adequada.",
                   "A proteção do bem não significa automaticamente cobertura de toda despesa de acomodação durante uma impossibilidade de uso."),
                  ("A cobertura de danos materiais implica pagamento de qualquer hospedagem escolhida, sem limite.",
                   "A indenização depende das condições. Não se deve presumir cobertura de hospedagem ausente da proposta."),
                  ("A ausência pode ser ignorada e negociada somente depois do sinistro.",
                   "O sinistro não cria cobertura não contratada. A análise deve ocorrer antes da contratação."),
              ]),
         step("João quer contratar, mas planeja ampliar a residência e adquirir novos bens.",
              "Qual providência é coerente para a continuidade?",
              [
                  ("Registrar as condições entendidas e orientar revisão dos valores e riscos quando a residência ou os bens mudarem.",
                   "A proteção deve acompanhar a exposição real. Alterações relevantes exigem reavaliação das informações e das condições."),
                  ("Garantir indenização sem limites, independentemente dos valores declarados e da apólice.",
                   "O profissional não pode prometer cobertura ilimitada que o contrato não prevê."),
                  ("Recomendar omitir a ampliação do imóvel para evitar possível ajuste do prêmio.",
                   "Omissão de informações relevantes pode prejudicar a adequação da cobertura e a análise do risco."),
              ]),
     ])

# RELACIONAMENTO: 6 árvores
tree(REL, "3.4.3", "Acessibilidade e compreensão",
     "Atendimento inclusivo com preservação de autonomia",
     "Márcia tem deficiência auditiva e procura a instituição para compreender alternativas de aplicação. Ela prefere comunicação escrita e possui capacidade para decidir por conta própria.",
     [
         step("O atendimento habitualmente é feito por telefone e por explicações verbais rápidas.",
              "Como adaptar o início da conversa?",
              [
                  ("Perguntar pelo canal acessível de sua preferência e oferecer informações escritas claras, preservando sua participação.",
                   "A adaptação deve atender à necessidade informada pela cliente e permitir que ela compreenda e decida."),
                  ("Solicitar que um familiar receba todas as orientações e decida, mesmo sem autorização.",
                   "A deficiência não autoriza transferir automaticamente a decisão ou o acesso aos dados a terceiros."),
                  ("Reduzir a quantidade de informação sobre riscos para tornar a conversa mais curta.",
                   "Acessibilidade exige apresentar a informação adequadamente, não omitir riscos importantes."),
              ]),
         step("Márcia relata não compreender a diferença entre prazo de resgate e vencimento do título.",
              "Qual é a melhor forma de verificar entendimento?",
              [
                  ("Usar exemplos de datas e pedir que ela explique, com suas palavras, quando conseguiria acessar o dinheiro.",
                   "A confirmação de compreensão ajuda a corrigir equívocos concretos sem presumir que a assinatura significa entendimento."),
                  ("Obter assinatura de ciência e encerrar o esclarecimento, porque o formulário substitui a explicação.",
                   "O registro formal não substitui informação compreensível e verificação de entendimento."),
                  ("Repetir o mesmo texto técnico em letras maiores, sem alterar o exemplo ou ouvir a dúvida.",
                   "A questão envolve compreensão de conceitos. Repetir a mesma linguagem pode manter a dificuldade."),
              ]),
         step("Ela escolhe uma alternativa adequada e pede uma cópia das condições no canal escrito utilizado.",
              "Como concluir?",
              [
                  ("Fornecer as condições pelo canal autorizado e acessível e registrar a decisão e os esclarecimentos pertinentes.",
                   "A cliente deve ter acesso às condições. O registro preserva a continuidade e a transparência do atendimento."),
                  ("Enviar somente ao familiar para evitar que a cliente tenha trabalho ao ler.",
                   "Isso retira autonomia e pode divulgar dados a terceiro sem fundamento."),
                  ("Fornecer apenas o nome do produto, deixando prazos e custos para consulta futura se houver problema.",
                   "As condições precisam estar disponíveis antes e no fechamento, e não apenas depois de um problema."),
              ]),
     ])

tree(REL, "3.1.3", "Orçamento com renda variável",
     "Planejamento de caixa de uma profissional autônoma",
     "Camila é autônoma. A renda mensal oscila entre R$ 3.000 e R$ 8.000, enquanto as despesas essenciais são de R$ 3.500. Ela quer assumir um aporte fixo elevado.",
     [
         step("Camila usa o melhor mês como referência para decidir o valor do aporte.",
              "Qual diagnóstico deve vir primeiro?",
              [
                  ("Analisar o histórico e a sazonalidade das entradas, as despesas e a reserva para meses de menor renda.",
                   "A capacidade sustentável de poupar depende da variação do caixa, e não apenas de um pico de faturamento."),
                  ("Fixar um aporte com base nos R$ 8.000, porque o maior valor já ocorreu e pode ser repetido.",
                   "Um mês excepcional não garante capacidade recorrente de aporte ou de pagamento das despesas."),
                  ("Fixar o aporte no valor total dos R$ 3.500 de despesas, para compensar a instabilidade.",
                   "A necessidade de gasto não se transforma em capacidade de poupança. O orçamento precisa ser equilibrado."),
              ]),
         step("Em um mês de renda de R$ 3.000, sem outras entradas, Camila manterá as despesas essenciais de R$ 3.500.",
              "O que esse cenário exige considerar?",
              [
                  ("Um déficit de R$ 500 antes de qualquer aporte; planejar o uso de reserva e ajustes, evitando financiar aportes com dívida cara.",
                   "Receita menos despesa resulta em −R$ 500. Poupar de forma nominal enquanto se cria dívida cara pode agravar a situação."),
                  ("Um excedente de R$ 500, pois a diferença entre renda e despesa sempre representa poupança.",
                   "A ordem da conta importa: as despesas superam a renda, portanto existe déficit, não excedente."),
                  ("Um aporte mínimo de R$ 3.000, pois os gastos essenciais não devem entrar no plano de investimentos.",
                   "Investimentos e gastos precisam ser vistos em conjunto. O valor necessário à subsistência não pode ser ignorado."),
              ]),
         step("Camila aceita criar uma regra de aportes que respeite a renda variável.",
              "Qual plano é mais coerente?",
              [
                  ("Estabelecer uma meta flexível de poupança sobre excedentes, reforçar a reserva e revisar o plano com a evolução do caixa.",
                   "A flexibilidade permite poupar nos meses favoráveis sem presumir uma renda fixa inexistente."),
                  ("Contratar aporte automático irreversível e recorrer ao cheque especial nos meses fracos.",
                   "O plano deve reduzir vulnerabilidade. Obrigar aporte financiado por crédito caro cria um risco adicional."),
                  ("Eliminar toda meta e usar a renda dos melhores meses sem qualquer registro.",
                   "A renda variável exige planejamento adaptado, não ausência de controle e de objetivos."),
              ]),
     ])

tree(REL, "3.2.1", "Planejamento de objetivos concorrentes",
     "Dois objetivos, dois horizontes de tempo",
     "Rafael e Lúcia querem reservar recursos para a matrícula universitária da filha em 18 meses e para aposentadoria em 22 anos. Ambos dizem aceitar oscilações moderadas.",
     [
         step("O casal pede uma única aplicação para todo o dinheiro.",
              "Como organizar a análise?",
              [
                  ("Separar os valores, prazos, prioridades e necessidades de liquidez de cada objetivo antes de escolher produtos.",
                   "A tolerância geral a risco não torna os horizontes iguais. A análise por objetivo evita comprometer obrigações próximas."),
                  ("Adotar o prazo de 22 anos para todos os recursos porque é o objetivo de maior duração.",
                   "A matrícula tem data próxima. Usar só o prazo mais longo ignora uma obrigação independente."),
                  ("Adotar a maior rentabilidade histórica como critério único para as duas metas.",
                   "Desempenho passado não resolve diferenças de prazo, liquidez e capacidade de suportar perdas."),
              ]),
         step("A matrícula exige R$ 30.000 e já está integralmente provisionada. A parcela tem pouca margem para perdas antes do pagamento.",
              "Qual orientação é coerente para essa parcela?",
              [
                  ("Priorizar preservação e disponibilidade no prazo, sem confundir a tolerância geral do casal com a capacidade de perda dessa meta.",
                   "A capacidade de suportar perdas deve ser avaliada à luz do compromisso específico e da possibilidade de recompor recursos."),
                  ("Buscar risco elevado para reduzir o custo da universidade com ganhos esperados, mesmo sem margem para perda.",
                   "A expectativa de ganho não elimina o risco de faltar dinheiro para uma obrigação já definida."),
                  ("Bloquear o valor por 22 anos, pois a aposentadoria deve substituir a matrícula como referência.",
                   "Isso comprometeria a disponibilidade do dinheiro no prazo da matrícula."),
              ]),
         step("O casal quer avançar também no plano de aposentadoria.",
              "Qual deve ser o encaminhamento?",
              [
                  ("Avaliar aportes sustentáveis, carteira compatível e revisões periódicas sem presumir retorno garantido pelo horizonte longo.",
                   "Prazo longo permite planejar de forma distinta, mas não elimina risco nem dispensa acompanhamento e adequação."),
                  ("Tratar 22 anos como garantia de recuperação de qualquer perda e concentrar todo o aporte em um ativo.",
                   "Horizonte longo não garante retorno ou recuperação e não substitui gestão de concentração."),
                  ("Suspender o acompanhamento até o ano da aposentadoria para evitar ajustes no plano.",
                   "Mudanças de renda, família, metas e mercado podem exigir revisões ao longo do período."),
              ]),
     ])

tree(REL, "3.4.5", "Cadastro e movimentação por terceiros",
     "Recursos de terceiros em conta pessoal",
     "Patrícia, cliente da instituição, recebe um crédito relevante incompatível com o padrão anterior. Um conhecido a acompanha e procura dar todas as instruções de movimentação.",
     [
         step("Ainda não há informação suficiente sobre origem dos recursos, finalidade ou eventual representação.",
              "Qual é o primeiro encaminhamento adequado?",
              [
                  ("Confirmar a vontade da cliente, verificar poderes de terceiros e solicitar informações pelos procedimentos de diligência.",
                   "A análise precisa identificar quem instrui a operação e a legitimidade da atuação de terceiros, sem prejulgar a cliente."),
                  ("Aceitar as ordens do acompanhante, pois a presença física equivale a procuração.",
                   "Estar presente não confere representação. A vontade da titular e os poderes devem ser verificados."),
                  ("Ensinar a dividir a transferência para que não seja analisada internamente.",
                   "Não se deve ajudar a contornar controles de monitoramento e diligência."),
              ]),
         step("As explicações permanecem inconsistentes e o terceiro pressiona pelo envio imediato.",
              "Como tratar a situação?",
              [
                  ("Registrar os fatos e acionar o fluxo interno de PLD/FTP e de segurança, observando os procedimentos aplicáveis à operação.",
                   "A pressão e inconsistência exigem análise formal. A decisão operacional deve seguir regras e responsáveis competentes."),
                  ("Acusar a cliente de crime para que a responsabilidade pela decisão fique com ela.",
                   "Atipicidade não prova crime e não autoriza acusação. O atendimento deve manter diligência e sigilo."),
                  ("Executar primeiro e omitir o comportamento do terceiro no registro.",
                   "O registro incompleto prejudica a análise; a urgência comercial não afasta os procedimentos de controle."),
              ]),
         step("Patrícia pergunta se será feita alguma comunicação às autoridades.",
              "Qual conduta respeita o tratamento sigiloso?",
              [
                  ("Informar apenas o que pode ser esclarecido sobre procedimentos, sem revelar eventual comunicação sigilosa nem antecipar conclusões.",
                   "A análise e eventual comunicação seguem fluxo restrito. O profissional não deve divulgar comunicações sigilosas ou orientar como evitá-las."),
                  ("Prometer avisá-la antes de qualquer comunicação para que consiga cancelar a operação.",
                   "Aviso prévio de eventual comunicação sigilosa compromete o controle e pode configurar divulgação indevida."),
                  ("Enviar por mensagem particular um relatório interno para que o acompanhante possa conferir.",
                   "Relatórios internos não devem ser repassados a terceiros sem fundamento e autorização cabíveis."),
              ]),
     ], "Difícil")

tree(REL, "3.4.2", "Adequação sem promessa de recuperação",
     "Pressa para recuperar uma perda",
     "Eduardo sofreu uma perda de R$ 8.000 e quer recuperá-la em dois meses. Ele precisará do dinheiro para despesas previsíveis e demonstra ansiedade com o resultado.",
     [
         step("Eduardo pede o produto de maior retorno esperado da plataforma.",
              "Qual deve ser a primeira abordagem?",
              [
                  ("Acolher a preocupação e levantar prazo, necessidade de caixa e capacidade de suportar nova perda antes de qualquer recomendação.",
                   "O atendimento precisa separar a reação à perda da situação financeira e da adequação de uma nova decisão."),
                  ("Usar a perda como justificativa para dispensar suitability e priorizar o retorno potencial.",
                   "A ocorrência de perda não elimina a exigência de adequação nem transforma risco em solução garantida."),
                  ("Prometer recuperação em dois meses desde que ele aceite uma carteira mais volátil.",
                   "Volatilidade não assegura recuperação em prazo definido. Prometer esse resultado seria enganoso."),
              ]),
         step("A análise mostra que uma nova perda impediria o pagamento de despesas essenciais.",
              "Qual orientação é compatível com essa capacidade financeira?",
              [
                  ("Priorizar os compromissos e a liquidez necessária, explicando que buscar recuperação rápida pode ampliar a perda.",
                   "O risco de comprometer despesas essenciais limita a capacidade de assumir nova exposição para perseguir um resultado de curto prazo."),
                  ("Contratar crédito para aumentar a aplicação de risco e reduzir o tempo de recuperação esperado.",
                   "A alavancagem acrescenta custo e potencial de perda, especialmente grave quando faltaria dinheiro para necessidades essenciais."),
                  ("Considerar apenas que ele se declarou corajoso, ignorando a impossibilidade de absorver uma perda.",
                   "Tolerância declarada e capacidade financeira são dimensões distintas; ambas importam."),
              ]),
         step("Eduardo compreende que a recomposição pode exigir mais tempo e aportes.",
              "Como encerrar o atendimento?",
              [
                  ("Construir um plano realista, registrar limites e reavaliar periodicamente, sem garantir prazo de recuperação.",
                   "Um plano sustentável combina orçamento, objetivos e adequação. O registro e o acompanhamento ajudam a evitar decisões impulsivas."),
                  ("Definir um retorno fixo necessário e apresentá-lo como rendimento contratualmente assegurado.",
                   "Uma meta financeira não cria garantia de mercado ou obrigação de resultado inexistente."),
                  ("Recomendar operações sucessivas até o saldo voltar ao valor anterior, independentemente dos custos.",
                   "Giro excessivo pode ampliar despesas e risco e não assegura recuperação."),
              ]),
     ])

tree(REL, "3.4.3.1.3", "Reclamação e rastreabilidade do atendimento",
     "Contestação sobre prazo de disponibilidade",
     "Sônia reclama que não recebeu o dinheiro de um resgate na data esperada. Ela afirma ter entendido que o pagamento seria imediato. O profissional ainda não verificou os registros.",
     [
         step("Sônia está irritada e pede solução urgente.",
              "Qual deve ser a primeira ação?",
              [
                  ("Ouvir o relato, identificar a operação e verificar pedido, horário e regras de cotização e pagamento, sem prometer o que não foi confirmado.",
                   "Acolher e verificar dados permite distinguir erro operacional, informação inadequada ou expectativa diferente das condições contratadas."),
                  ("Concluir que ela interpretou mal e encerrar a reclamação sem examinar os documentos.",
                   "Não se deve atribuir culpa antes de apurar os fatos nem recusar o tratamento da reclamação."),
                  ("Prometer crédito imediato por conta da instituição, mesmo sem autorização ou apuração.",
                   "Uma promessa sem fundamento pode agravar o problema e não substitui a análise e o fluxo competente."),
              ]),
         step("A verificação identifica falha no encaminhamento do pedido dentro do processo interno.",
              "Qual é a conduta mais adequada?",
              [
                  ("Registrar a falha, acionar o responsável pela correção e informar à cliente um prazo de retorno verificável.",
                   "O atendimento deve dar encaminhamento rastreável e comunicar o que é conhecido, com prazo de acompanhamento."),
                  ("Alterar retroativamente o registro para que pareça que a cliente solicitou depois.",
                   "Modificar registros para esconder falha viola a integridade do atendimento e prejudica a apuração."),
                  ("Atribuir a falha a um parceiro sem confirmar sua participação e aguardar sem protocolo.",
                   "A responsabilização deve ser apurada. A cliente precisa de encaminhamento e possibilidade de acompanhar a demanda."),
              ]),
         step("Sônia pede cópia do protocolo e quer saber qual canal usar se a solução não vier.",
              "Como concluir?",
              [
                  ("Fornecer protocolo, condições de acompanhamento e canais formais de reclamação e escalonamento aplicáveis.",
                   "Rastreabilidade e canais de recurso permitem acompanhar a solução e buscar revisão pelos meios adequados."),
                  ("Condicionar o protocolo à contratação de um novo produto para manter o relacionamento.",
                   "O tratamento da reclamação não deve ser condicionado a nova contratação comercial."),
                  ("Pedir que ela retire a reclamação antes de informar o prazo de resposta.",
                   "A informação e o encaminhamento não dependem da desistência da reclamação."),
              ]),
     ])


assert len(MCQ_C) == 40
assert len(TREES_C) == 10
