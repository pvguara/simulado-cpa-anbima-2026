import json

MCQ = []

def add_mcq(theme, pd, context, options, correct, explanation, difficulty="Médio"):
    MCQ.append({
        "theme": theme,
        "pd": pd,
        "context": context,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "difficulty": difficulty,
    })

SFN = "Sistema Financeiro Nacional"
PROD = "Produtos do mercado financeiro"
REL = "Relacionamento com o cliente"
INOV = "Inovação e desenvolvimento de mercado"

# ---------------- SFN (10 questões) ----------------

add_mcq(SFN, "1.1.1", "Durante uma reunião de equipe, um analista recém-contratado pergunta qual órgão é responsável por definir as diretrizes gerais da política monetária, cambial e creditícia do país, sem executar operações no mercado. Qual é a resposta correta?",
    ["O Conselho Monetário Nacional (CMN), órgão normativo máximo do Sistema Financeiro Nacional.",
     "O Banco Central do Brasil (BC), que executa a política monetária no dia a dia.",
     "A Comissão de Valores Mobiliários (CVM), responsável pela regulação do mercado de capitais.",
     "A ANBIMA, entidade de autorregulação do mercado financeiro."],
    0,
    "O CMN é o órgão normativo máximo do SFN: define diretrizes de política monetária, cambial e creditícia, mas não executa operações — a execução cabe ao Banco Central. CVM regula valores mobiliários e ANBIMA é autorreguladora, não órgão normativo.")

add_mcq(SFN, "1.1.2", "Um cliente pergunta a seu assessor qual instituição é responsável por autorizar o funcionamento de bancos, fiscalizar o cumprimento das normas prudenciais e executar a política monetária definida pelo CMN. A resposta correta é:",
    ["O Banco Central do Brasil (BC).",
     "A Superintendência de Seguros Privados (SUSEP).",
     "A Superintendência Nacional de Previdência Complementar (PREVIC).",
     "O Conselho Nacional de Seguros Privados (CNSP)."],
    0,
    "O Banco Central supervisiona instituições financeiras, autoriza seu funcionamento e executa a política monetária. SUSEP supervisiona seguradoras, PREVIC supervisiona fundos de pensão (EFPC) e CNSP é órgão normativo do setor de seguros.")

add_mcq(SFN, "1.1.2", "Uma corretora de valores deseja saber qual entidade fiscaliza o mercado de capitais, regula a emissão e negociação de valores mobiliários e protege os investidores contra práticas irregulares como manipulação de mercado. Essa entidade é:",
    ["A Comissão de Valores Mobiliários (CVM).",
     "O Banco Central do Brasil (BC).",
     "O Conselho Nacional de Previdência Complementar (CNPC).",
     "A B3 S.A."],
    0,
    "A CVM é o órgão supervisor do mercado de capitais, responsável por regular e fiscalizar a emissão e negociação de valores mobiliários e coibir práticas irregulares. O BC supervisiona o SFN de forma mais amplas ligado a moeda e crédito; a B3 é operadora de mercado, não supervisora.")

add_mcq(SFN, "1.1.2", "Uma entidade de previdência complementar aberta (EAPC) que comercializa planos PGBL está sujeita à fiscalização de qual órgão?",
    ["Superintendência de Seguros Privados (SUSEP).",
     "Superintendência Nacional de Previdência Complementar (PREVIC).",
     "Comissão de Valores Mobiliários (CVM).",
     "Banco Central do Brasil (BC)."],
    0,
    "A SUSEP supervisiona seguradoras e entidades abertas de previdência complementar (EAPC), que comercializam PGBL e VGBL. A PREVIC supervisiona as entidades fechadas de previdência complementar (fundos de pensão).")

add_mcq(SFN, "1.2.4", "Em reunião do Copom, o comitê decidiu elevar a meta para a taxa Selic. Um cliente pergunta ao assessor qual é o efeito esperado dessa decisão sobre a economia. A explicação mais adequada é:",
    ["A elevação da meta Selic tende a encarecer o crédito e reduzir o consumo e o investimento, contribuindo para conter a inflação.",
     "A elevação da meta Selic reduz automaticamente o IPCA no mês seguinte, sem impacto sobre o crédito.",
     "A elevação da meta Selic é usada exclusivamente para desvalorizar o real frente ao dólar.",
     "A elevação da meta Selic não influencia o custo do crédito, apenas a rentabilidade da poupança."],
    0,
    "A política monetária contracionista (alta de juros) encarece o crédito e desestimula consumo/investimento, sendo um instrumento de controle da inflação por meio da transmissão aos preços dos ativos e à atividade econômica, com efeitos que ocorrem com defasagem — não instantaneamente.")

add_mcq(SFN, "1.2.3", "Um cliente lê uma notícia sobre o aumento do déficit primário do governo e questiona seu assessor sobre o que esse indicador representa. A resposta correta é:",
    ["O déficit primário representa o resultado das receitas menos despesas do governo, excluindo o pagamento de juros da dívida pública.",
     "O déficit primário representa apenas o saldo da balança comercial do país.",
     "O déficit primário é o total da dívida pública acumulada ao longo dos anos.",
     "O déficit primário mede exclusivamente a variação cambial do período."],
    0,
    "O resultado primário é a diferença entre receitas e despesas do governo, sem considerar os juros da dívida pública. Já o resultado nominal inclui o pagamento de juros. Esse conceito está diretamente ligado à política fiscal e à Lei de Responsabilidade Fiscal.")

add_mcq(SFN, "1.2.5", "Uma empresa exportadora quer entender por que a taxa de câmbio à vista pode diferir da taxa referencial usada pelo Banco Central para fins de cálculo de operações. O assessor deve explicar que essa taxa de referência é a:",
    ["Taxa PTAX, calculada pelo Banco Central com base em consulta a instituições autorizadas a operar no mercado de câmbio.",
     "Taxa Selic, definida pelo Copom a cada 45 dias.",
     "Taxa DI, calculada pela B3 a partir dos Depósitos Interfinanceiros.",
     "Taxa TR, usada para remuneração da caderneta de poupança."],
    0,
    "A taxa PTAX é a taxa de câmbio de referência calculada pelo Banco Central, usada como parâmetro em diversas operações financeiras e contratos indexados ao dólar. TR e Selic/DI não são taxas de câmbio.")

add_mcq(SFN, "1.2.6", "Um investidor deseja comparar dois indicadores de inflação e pergunta a diferença entre o IPCA e o IGP-M. A explicação correta é:",
    ["O IPCA mede a variação de preços ao consumidor final (uso do IBGE como referência oficial de meta de inflação), enquanto o IGP-M inclui preços no atacado, construção civil e consumidor, sendo mais sensível a variações cambiais e de commodities.",
     "O IPCA e o IGP-M medem exatamente a mesma cesta de produtos, apenas em datas diferentes.",
     "O IGP-M é o índice oficial usado pelo Copom para definir a meta de inflação.",
     "O IPCA é calculado pela FGV e o IGP-M pelo IBGE."],
    0,
    "O IPCA (IBGE) é o índice oficial de referência para a meta de inflação definida pelo CMN. O IGP-M (FGV) tem maior peso de preços no atacado e é mais volátil a câmbio e commodities, sendo comum em contratos de aluguel.")

add_mcq(SFN, "1.4.3", "Um gerente de relacionamento é questionado por um cliente sobre por que os bancos precisam manter um determinado nível de capital próprio em relação aos seus ativos ponderados pelo risco. Essa exigência está relacionada a:",
    ["Aos Acordos de Basileia, que estabelecem índices mínimos de capital para mitigar riscos de liquidez, crédito e alavancagem excessiva no sistema financeiro.",
     "À exigência do Fundo Garantidor de Créditos (FGC) para cobertura de depósitos.",
     "À exigência da CVM para registro de fundos de investimento.",
     "Ao cálculo do Imposto sobre Operações Financeiras (IOF)."],
    0,
    "Os Acordos de Basileia (I, II e III) definem parâmetros mínimos de capital regulatório para bancos, visando reduzir o risco sistêmico e a alavancagem excessiva, protegendo a estabilidade do sistema financeiro.")

add_mcq(SFN, "1.4.10", "Um cliente com grande volume de recursos e conhecimento de mercado deseja acessar produtos restritos a investidores qualificados. Segundo a Resolução CVM nº 30, para ser classificado como investidor qualificado, uma pessoa natural deve, entre outros critérios:",
    ["Comprovar possuir investimentos financeiros em valor superior ao mínimo estabelecido pela norma e atestar por escrito sua condição mediante termo próprio.",
     "Ter apenas mais de 18 anos de idade, sem qualquer exigência patrimonial.",
     "Ser necessariamente sócio-administrador de uma instituição financeira.",
     "Possuir qualquer valor investido em poupança."],
    0,
    "A classificação de investidor qualificado exige comprovação de recursos financeiros investidos acima do valor mínimo fixado pela CVM (ou determinadas certificações profissionais), além de declaração formal — trata-se de um enquadramento regulatório com critérios objetivos, não apenas idade.")

# ---------------- PRODUTOS (16 questões) ----------------

add_mcq(PROD, "2.1.1.1.3", "Um cliente pergunta a diferença entre um CDB e uma LCI em termos de garantia e tributação. A explicação correta é:",
    ["Ambos são cobertos pelo FGC até o limite vigente, mas o CDB tem incidência de IR conforme a tabela regressiva, enquanto a LCI é isenta de IR para pessoa física.",
     "O CDB é isento de IR para pessoa física e a LCI é tributada pela tabela regressiva.",
     "Somente a LCI é garantida pelo FGC; o CDB não possui essa garantia.",
     "Ambos são isentos de IR e não contam com garantia do FGC."],
    0,
    "Tanto o CDB quanto a LCI contam com garantia do FGC até o limite vigente. O CDB é tributado pela tabela regressiva do IR (22,5% a 15%, conforme o prazo), enquanto a LCI (assim como a LCA) é isenta de IR para pessoas físicas, por se destinarem ao fomento de setores específicos (imobiliário e agronegócio).")

add_mcq(PROD, "2.1.1.1.1", "Um investidor com perfil conservador busca proteção contra a variação da inflação para um objetivo de longo prazo, como a aposentadoria. Dentre os títulos públicos federais, a opção mais alinhada a esse objetivo é:",
    ["O Tesouro IPCA+ (NTN-B), que corrige o valor investido pela inflação mais uma taxa de juros prefixada.",
     "O Tesouro Selic (LFT), pois sua rentabilidade é atrelada exclusivamente à inflação.",
     "O Tesouro Prefixado (LTN), por eliminar totalmente o risco de mercado no longo prazo.",
     "Todos os títulos públicos federais têm exatamente a mesma exposição ao risco de inflação."],
    0,
    "O Tesouro IPCA+ (NTN-B) protege o poder de compra do investidor ao corrigir o principal pela inflação (IPCA) e agregar uma taxa de juros real, sendo adequado a objetivos de longo prazo como aposentadoria. O Tesouro Selic acompanha a taxa Selic/CDI, não a inflação diretamente, e o prefixado tem maior risco de mercado diante de mudanças na expectativa de juros.")

add_mcq(PROD, "2.1.1.1.4", "Uma empresa do setor de energia capta recursos por meio de debêntures de infraestrutura para financiar um projeto de longo prazo. Sobre a tributação desse produto para pessoa física, é correto afirmar que:",
    ["As debêntures incentivadas (Lei nº 12.431) são isentas de Imposto de Renda para pessoas físicas, como incentivo ao financiamento de projetos de infraestrutura.",
     "Todas as debêntures, incentivadas ou não, são isentas de IR para pessoa física.",
     "As debêntures incentivadas têm tributação pela tabela regressiva, com alíquota mínima de 22,5%.",
     "As debêntures incentivadas só podem ser adquiridas por investidores qualificados."],
    0,
    "As debêntures incentivadas de infraestrutura (Lei 12.431/2011) contam com isenção de IR para pessoas físicas como forma de estimular o financiamento privado de projetos de infraestrutura. Debêntures comuns seguem a tabela regressiva normal de renda fixa.")

add_mcq(PROD, "2.1.1.1.5", "Um cliente pretende investir em um Certificado de Recebíveis Imobiliários (CRI) buscando isenção fiscal e exposição ao setor imobiliário. O assessor deve esclarecer que o CRI:",
    ["É isento de Imposto de Renda para pessoa física, mas não conta com a garantia do Fundo Garantidor de Créditos (FGC).",
     "Conta com garantia do FGC, assim como o CDB.",
     "É tributado pela tabela regressiva do IR, sem qualquer isenção.",
     "Só pode ser emitido por instituições financeiras bancárias."],
    0,
    "O CRI (assim como o CRA) é isento de IR para pessoa física, mas, diferentemente do CDB/LCI/LCA, não é garantido pelo FGC — o risco de crédito está associado aos recebíveis que dão suporte à operação, o que exige atenção redobrada do investidor.")

add_mcq(PROD, "2.1.3.2", "Um cliente resgata cotas de um fundo de renda fixa após 400 dias de aplicação e pergunta qual alíquota de Imposto de Renda incidirá sobre o rendimento. Considerando a tabela regressiva aplicável a esse tipo de fundo, a alíquota correta é:",
    ["15%, pois aplicações com prazo superior a 720 dias têm alíquota de 15%, mas entre 361 e 720 dias a alíquota é de 17,5%.",
     "22,5%, independentemente do prazo de aplicação.",
     "0%, pois fundos de renda fixa são isentos de IR para pessoa física.",
     "20%, alíquota fixa para todos os fundos de investimento."],
    0,
    "A tabela regressiva de IR para fundos de renda fixa (não isentos) segue: até 180 dias 22,5%; de 181 a 360 dias 20%; de 361 a 720 dias 17,5%; acima de 720 dias 15%. Com 400 dias de aplicação, a alíquota correta é 17,5%.")

add_mcq(PROD, "2.1.1.2.2", "Um cliente recebe Juros sobre Capital Próprio (JCP) de uma empresa investida e pergunta sobre a diferença tributária em relação ao recebimento de dividendos. A resposta correta é:",
    ["O JCP sofre retenção de Imposto de Renda na fonte (15%), enquanto os dividendos são isentos de IR para o acionista.",
     "Tanto o JCP quanto os dividendos são isentos de IR para o investidor pessoa física.",
     "O JCP é isento de IR e os dividendos sofrem retenção de 15% na fonte.",
     "Ambos sofrem tributação de 22,5% na fonte, sem exceções."],
    0,
    "Os dividendos distribuídos por empresas são isentos de IR para o acionista, pois já houve tributação na pessoa jurídica. Já o JCP é dedutível para a empresa pagadora e sofre retenção de IR de 15% na fonte para o beneficiário — uma distinção tributária importante.")

add_mcq(PROD, "2.1.2.2", "Segundo a Resolução CVM nº 175, um fundo de investimento pode ser estruturado com divisão em classes e subclasses de cotas. Sobre a segregação patrimonial entre classes, é correto afirmar que:",
    ["Cada classe de cotas possui patrimônio segregado, respondendo apenas pelas obrigações e direitos a ela vinculados, salvo disposição em contrário no regulamento.",
     "Todas as classes de um mesmo fundo compartilham obrigatoriamente o mesmo patrimônio, sem qualquer segregação.",
     "A segregação patrimonial entre classes foi extinta pela Resolução CVM 175.",
     "Somente fundos fechados podem ter classes com patrimônio segregado."],
    0,
    "A Resolução CVM 175 trouxe a estrutura de fundos organizados em classes (e subclasses) de cotas, com segregação patrimonial entre elas como regra geral — cada classe responde por suas próprias obrigações, o que reduz o risco de contágio entre estratégias distintas dentro do mesmo veículo.")

add_mcq(PROD, "2.1.2.3.6", "Um cliente com apetite por diversificação entre renda fixa, ações, câmbio e derivativos, sem uma classificação rígida de concentração em uma única classe de ativos, é mais adequado para investir em um fundo do tipo:",
    ["Fundo multimercado, que permite alocação diversificada entre diferentes classes de ativos e estratégias.",
     "Fundo de ações, que deve manter no mínimo 67% da carteira em ações.",
     "Fundo cambial, que deve manter ao menos 80% da carteira em ativos relacionados à variação de moeda estrangeira.",
     "Fundo de renda fixa, restrito a títulos de dívida."],
    0,
    "Os fundos multimercados possuem política de investimento que permite combinar diversas classes de ativos (renda fixa, ações, câmbio, derivativos) e estratégias, sendo adequados a investidores que buscam diversificação sem se limitar a uma única classe.")

add_mcq(PROD, "2.1.2.2.20", "Um cliente percebe que, mesmo sem resgatar suas cotas, o número de cotas de seu fundo de renda fixa diminui periodicamente. O assessor deve explicar que esse efeito é conhecido como:",
    ["Come-cotas, a antecipação semestral do Imposto de Renda incidente sobre a rentabilidade, feita por meio da redução da quantidade de cotas.",
     "Taxa de saída, cobrada apenas em caso de resgate antecipado.",
     "Taxa de performance, cobrada sobre o rendimento acima de um benchmark.",
     "Come-cotas é uma taxa de administração adicional cobrada mensalmente."],
    0,
    "O come-cotas é a antecipação do IR (nos meses de maio e novembro) sobre fundos de renda fixa e multimercado (exceto fundos de ações), recolhida pela redução da quantidade de cotas do investidor, com base na alíquota mínima da tabela regressiva (15% ou 20%, dependendo do fundo).")

add_mcq(PROD, "2.1.4", "Um investidor busca renda mensal isenta de IR investindo em Fundos de Investimento Imobiliário (FIIs) negociados em bolsa. Sobre a tributação dos rendimentos distribuídos por FIIs a pessoas físicas, é correto afirmar que:",
    ["Os rendimentos distribuídos mensalmente são isentos de IR para pessoa física, desde que atendidos requisitos legais (como pulverização e negociação em bolsa), mas o ganho de capital na venda das cotas é tributado.",
     "Os rendimentos distribuídos e o ganho de capital são integralmente isentos de IR para qualquer investidor.",
     "Os rendimentos distribuídos são tributados pela tabela regressiva de renda fixa.",
     "FIIs não distribuem rendimentos periódicos, apenas valorização de cota."],
    0,
    "Rendimentos periódicos distribuídos por FIIs a pessoas físicas são isentos de IR quando atendidos os requisitos legais (cotas negociadas em bolsa/mercado de balcão organizado, fundo com no mínimo 50 cotistas e cotista com menos de 10% das cotas, entre outros). Já o ganho de capital obtido na venda das cotas é tributado, geralmente à alíquota de 20%.")

add_mcq(PROD, "2.1.1.4", "Um cliente conservador se interessa por um Certificado de Operações Estruturadas (COE) com garantia de capital protegido. O assessor deve explicar que esse tipo de estrutura:",
    ["Garante a devolução, no mínimo, do capital investido no vencimento, ainda que o cenário de mercado embutido no derivativo não se realize, mas normalmente não distribui rendimentos intermediários.",
     "Garante sempre um retorno mínimo acima da inflação, independentemente do cenário de mercado.",
     "Elimina totalmente o risco de crédito do emissor.",
     "É garantido pelo FGC, assim como o CDB."],
    0,
    "No COE de capital protegido, o investidor tem a garantia contratual de reaver, no mínimo, o capital principal no vencimento, mesmo que o cenário de mercado vinculado ao derivativo não se confirme — mas ainda existe risco de crédito do emissor, e o COE não é garantido pelo FGC.")

add_mcq(PROD, "2.2.2", "Um cliente com renda alta e que costuma declarar Imposto de Renda pelo modelo completo pergunta qual regime tributário de previdência complementar tende a ser mais vantajoso para contribuições de longo prazo. A orientação tecnicamente adequada é:",
    ["Avaliar o regime regressivo, cuja alíquota decresce com o tempo de permanência (chegando a 10% acima de 10 anos), sendo mais indicado para aportes de longo prazo sem previsão de resgate próximo.",
     "O regime progressivo é sempre mais vantajoso, independentemente do prazo de permanência.",
     "A escolha do regime tributário não afeta a alíquota final de IR na previdência complementar.",
     "O regime regressivo tem alíquota fixa de 27,5%, superior ao progressivo."],
    0,
    "No regime regressivo, a alíquota de IR diminui com o tempo de permanência do recurso (de 35% para aportes de até 2 anos até 10% para prazos superiores a 10 anos), sendo mais adequado para quem pretende manter o investimento por longos períodos, sem necessidade de resgates de curto prazo.")

add_mcq(PROD, "2.2.1", "Um cliente autônomo, que declara IR pelo modelo simplificado e não tem contribuições dedutíveis relevantes, pergunta se deve optar por PGBL ou VGBL. A orientação correta é:",
    ["O VGBL é mais adequado, pois a dedução fiscal do PGBL (até 12% da renda bruta anual) só é vantajosa para quem declara pelo modelo completo e contribui para o INSS ou regime próprio.",
     "O PGBL é sempre mais vantajoso, independentemente do modelo de declaração de IR.",
     "PGBL e VGBL têm exatamente o mesmo tratamento tributário, sem qualquer diferença.",
     "O VGBL permite deduzir até 12% da renda bruta anual na declaração de IR."],
    0,
    "O benefício fiscal do PGBL (dedução de até 12% da renda bruta anual) só se aplica a quem declara pelo modelo completo e contribui para a previdência social. Para quem usa o modelo simplificado, o VGBL é mais adequado, pois no resgate a tributação incide apenas sobre os rendimentos, e não sobre o valor total aportado como ocorre no PGBL.")

add_mcq(PROD, "2.3.4", "Um cliente aposentado busca uma linha de crédito com taxas de juros mais baixas, descontada diretamente do benefício mensal. A modalidade mais adequada é o:",
    ["Crédito consignado, que costuma oferecer taxas de juros menores por ter o pagamento garantido via desconto direto na folha ou benefício.",
     "Cheque especial, por ter taxas de juros mais baixas do mercado.",
     "Cartão de crédito rotativo, indicado para dívidas de longo prazo.",
     "Crédito Direto ao Consumidor (CDC) sem qualquer garantia."],
    0,
    "O crédito consignado tende a apresentar taxas de juros mais baixas porque o pagamento é descontado diretamente da folha de pagamento ou do benefício previdenciário, reduzindo o risco de inadimplência para a instituição financeira — diferentemente do cheque especial e do rotativo do cartão, que estão entre as modalidades de crédito mais caras do mercado.")

add_mcq(PROD, "2.3.2", "Um cliente utiliza o limite do cartão de crédito e paga apenas o valor mínimo da fatura, entrando no crédito rotativo. O assessor deve alertá-lo que essa modalidade:",
    ["Está entre as linhas de crédito mais caras do mercado, com incidência de juros elevados sobre o saldo não pago, sendo recomendável migrar para uma linha de crédito com taxas menores caso a dívida não seja paga rapidamente.",
     "Tem taxas de juros equivalentes às do crédito consignado.",
     "É a opção de crédito mais barata disponível para pessoas físicas.",
     "Não gera incidência de juros, apenas de IOF."],
    0,
    "O crédito rotativo do cartão está entre as modalidades mais caras do mercado, com juros elevados incidindo sobre o saldo devedor. Por isso, boas práticas de orientação financeira recomendam evitar sua manutenção por longos períodos, buscando linhas de crédito mais baratas para consolidar a dívida quando necessário.")

add_mcq(PROD, "2.5.1", "Um cliente de meia-idade, com dependentes financeiros, busca uma proteção que garanta cobertura por toda a vida, com possibilidade de acumulação de valor. Dentre os seguros de vida, a modalidade mais alinhada a esse objetivo é o seguro de vida:",
    ["Vida inteira (whole life), que oferece cobertura permanente e pode acumular valor de resgate ao longo do tempo.",
     "Temporário (term life), que oferece cobertura apenas por um período determinado, geralmente sem acumulação de valor.",
     "Prestamista, vinculado exclusivamente à quitação de um financiamento específico.",
     "Todos os seguros de vida têm exatamente as mesmas características e coberturas."],
    0,
    "O seguro de vida inteira (vida integral) oferece cobertura permanente enquanto o segurado mantiver o pagamento dos prêmios, com possibilidade de acumulação de valor de resgate — diferente do seguro temporário, que cobre apenas um período definido e é geralmente mais barato, mas sem esse componente de acumulação.")

# ---------------- RELACIONAMENTO (9 questões) ----------------

add_mcq(REL, "3.1.2", "Um cliente de 28 anos, solteiro, sem dependentes e com estabilidade profissional, está na fase inicial de acumulação de capital do seu ciclo de vida financeiro. Considerando esse momento, a orientação mais adequada do assessor é:",
    ["Priorizar a formação de reserva de emergência e, na sequência, aumentar gradualmente a exposição a ativos de maior risco e potencial de retorno, dado o horizonte de investimento mais longo.",
     "Concentrar 100% dos recursos em produtos de baixíssima liquidez e longo prazo, sem qualquer reserva de emergência.",
     "Recomendar exclusivamente produtos de previdência complementar com resgate apenas após os 65 anos.",
     "Priorizar a preservação de capital, típica de investidores próximos à fase de distribuição de renda."],
    0,
    "Na fase de acumulação de capital (early career), com horizonte de investimento mais longo e menor necessidade de liquidez imediata para despesas correntes, a orientação técnica recomenda primeiro constituir reserva de emergência e, depois, aumentar gradualmente a exposição a ativos de maior risco, aproveitando o tempo disponível para a recuperação de eventuais perdas.")

add_mcq(REL, "3.1.3", "Um cliente pergunta qual seria o valor ideal de reserva de emergência e em que tipo de ativo ela deveria ser mantida. A orientação técnica mais adequada é:",
    ["Manter de 3 a 6 meses de despesas médias mensais em ativos de alta liquidez, como Tesouro Selic ou fundos com resgate em D+0/D+1.",
     "Investir toda a reserva de emergência em ações, buscando maior rentabilidade.",
     "Manter a reserva de emergência em produtos com carência de resgate superior a 2 anos, para evitar uso impulsivo.",
     "A reserva de emergência deve ser aplicada preferencialmente em COE com capital protegido."],
    0,
    "A reserva de emergência deve equilibrar liquidez e segurança, sendo recomendado manter de 3 a 6 meses de despesas (o múltiplo pode variar conforme a estabilidade de renda do cliente) em ativos de alta liquidez e baixo risco, como Tesouro Selic ou fundos DI com resgate rápido — nunca em ativos de risco ou baixa liquidez.")

add_mcq(REL, "3.4.2", "Ao aplicar o processo de suitability previsto no Código de Distribuição da ANBIMA, um assessor identifica que um cliente com perfil conservador deseja investir a totalidade de seus recursos em um fundo de ações. A conduta correta é:",
    ["Alertar formalmente o cliente sobre a inadequação do produto ao seu perfil, documentar a orientação e, caso o cliente insista, registrar por escrito sua decisão, mantendo a transparência do processo.",
     "Realizar a operação normalmente, pois a decisão final é sempre do cliente, sem qualquer necessidade de alerta ou registro.",
     "Recusar-se a atender o cliente e encerrar o relacionamento comercial.",
     "Alterar o perfil do cliente no sistema para 'agressivo' sem nova avaliação, apenas para viabilizar a operação."],
    0,
    "O suitability exige adequação do produto ao perfil, objetivos e situação financeira do cliente. Quando há desenquadramento, o profissional deve alertar formalmente o cliente, documentar a orientação dada e, se o cliente ainda assim optar pela operação, registrar essa decisão por escrito — nunca alterar o perfil sem reavaliação apenas para viabilizar a venda.")

add_mcq(REL, "3.4.5", "Um gerente percebe que um cliente pessoa física realizou, em curto espaço de tempo, diversos depósitos em espécie de valores fracionados, abaixo do limite de reporte automático, em contas distintas. Essa prática pode caracterizar indício de:",
    ["Fracionamento de operações (smurfing), uma técnica de lavagem de dinheiro que deve ser tratada com base na abordagem de risco e comunicada nos termos da regulamentação de PLD/FT.",
     "Uma prática legítima e comum de gestão de caixa, sem necessidade de qualquer análise adicional.",
     "Uma estratégia válida de diversificação de investimentos.",
     "Uma operação de suitability inadequada, mas sem relação com lavagem de dinheiro."],
    0,
    "O fracionamento de depósitos para evitar limites de reporte (smurfing) é um indício clássico de lavagem de dinheiro. A regulamentação de PLD/FT exige que a instituição adote uma abordagem baseada em risco, com monitoramento contínuo e comunicação de operações suspeitas às autoridades competentes.")

add_mcq(REL, "3.4.6", "Um cliente solicita que o assessor compartilhe seus dados cadastrais e histórico de investimentos com uma empresa parceira, sem qualquer finalidade contratual clara. Considerando a Lei Geral de Proteção de Dados (LGPD), a conduta adequada do profissional é:",
    ["Explicar que o compartilhamento de dados pessoais exige base legal e, em geral, consentimento específico e informado do titular, não podendo ocorrer de forma indiscriminada.",
     "Compartilhar os dados livremente, pois o cliente é o titular das informações e não há qualquer restrição legal.",
     "Compartilhar os dados apenas verbalmente, sem registro, para evitar formalidades.",
     "A LGPD se aplica somente a dados de pessoas jurídicas, não de pessoas físicas."],
    0,
    "A LGPD estabelece que o tratamento e compartilhamento de dados pessoais precisam de base legal (como consentimento específico, informado e inequívoco do titular, ou outra hipótese prevista em lei), sendo vedado o compartilhamento indiscriminado sem finalidade e transparência claras para o titular dos dados.")

add_mcq(REL, "3.4.1", "Segundo o Código de Conduta Ética para profissionais certificados pela ANBIMA, ao identificar um conflito entre os interesses da instituição e os interesses do cliente, a conduta esperada do profissional é:",
    ["Priorizar os interesses do cliente, agindo com integridade, transparência e zelando pela adequação do produto ao seu perfil.",
     "Priorizar sempre os interesses comerciais da instituição, independentemente do impacto ao cliente.",
     "Ignorar o conflito de interesses, desde que a operação seja legal.",
     "Encaminhar a decisão exclusivamente para a área de compliance, sem qualquer conduta ativa do profissional."],
    0,
    "Os princípios éticos do Código ANBIMA colocam o interesse do cliente e a integridade do mercado no centro da atuação profissional. O profissional certificado deve zelar pela transparência, adequação (suitability) e agir de forma diligente, mesmo diante de potenciais conflitos de interesse com metas comerciais.")

add_mcq(REL, "3.4.7", "Um profissional obtém, em razão de sua função, informação relevante e ainda não divulgada ao mercado sobre uma fusão entre duas companhias abertas, e a utiliza para negociar ações antes da divulgação pública. Essa conduta configura:",
    ["Uso indevido de informação privilegiada (insider trading), uma infração penal prevista na Lei nº 6.385/76.",
     "Uma prática legítima de análise fundamentalista antecipada.",
     "Front running, por se tratar de negociação para benefício de terceiros antes de uma ordem do cliente.",
     "Uma conduta permitida, desde que o profissional não seja administrador da companhia."],
    0,
    "A utilização de informação privilegiada e não pública para obter vantagem em operações no mercado de capitais caracteriza insider trading (art. 27-D da Lei 6.385/76), uma infração penal grave e distinta do front running, que envolve negociar antes de executar ordens de terceiros para benefício próprio.")

add_mcq(REL, "3.2", "Um cliente com dívidas de cartão de crédito em aberto pergunta se deve priorizar o pagamento da dívida ou iniciar novos investimentos com sua reserva disponível. A orientação técnica mais adequada, considerando que a taxa de juros do rotativo do cartão costuma ser muito superior ao retorno esperado de investimentos de baixo risco, é:",
    ["Priorizar a quitação da dívida de alto custo antes de iniciar novos investimentos, pois o custo do crédito rotativo normalmente supera com folga a rentabilidade de aplicações conservadoras.",
     "Investir primeiro em ações, já que o retorno de longo prazo tende a superar qualquer taxa de juros de crédito.",
     "Não há relação entre o custo do crédito e a decisão de investir; ambas devem ocorrer simultaneamente, sem prioridade.",
     "Sempre priorizar a manutenção de investimentos de longo prazo, mesmo com dívidas de curto prazo em aberto."],
    0,
    "Como parte da gestão financeira pessoal, é uma boa prática priorizar a quitação de dívidas cujo custo de juros seja muito superior à rentabilidade esperada dos investimentos disponíveis — o que normalmente ocorre com o rotativo do cartão de crédito, uma das linhas mais caras do mercado.")

add_mcq(REL, "3.4.3", "Durante o atendimento, um cliente demonstra insatisfação recorrente com a demora nas respostas do assessor. Entre as técnicas de atendimento recomendadas para reconstruir a confiança do cliente, a mais adequada é:",
    ["Praticar escuta ativa, reconhecer o problema, gerenciar expectativas de forma transparente sobre prazos e agir proativamente na solução.",
     "Ignorar a reclamação e seguir o roteiro comercial padrão, sem qualquer ajuste.",
     "Transferir imediatamente o cliente para outro profissional, sem qualquer tratativa.",
     "Oferecer um produto de maior rentabilidade como forma de compensação, sem tratar a causa da insatisfação."],
    0,
    "As boas práticas de atendimento recomendam escuta ativa, reconhecimento do problema, gerenciamento transparente de expectativas e ação proativa para resolver a causa da insatisfação — construindo confiança de forma sustentável, em vez de apenas oferecer compensações que não tratam a raiz do problema.")

# ---------------- INOVAÇÃO (5 questões) ----------------

add_mcq(INOV, "4.1", "Um gestor de fundos avalia empresas considerando critérios ambientais, sociais e de governança, além dos indicadores financeiros tradicionais. Essa abordagem é conhecida como:",
    ["Investimento ESG (Environmental, Social and Governance), que incorpora fatores de sustentabilidade e governança na análise e tomada de decisão de investimento.",
     "Investimento estritamente passivo, replicando índices de mercado sem qualquer filtro adicional.",
     "Investimento alavancado, focado exclusivamente em derivativos.",
     "Investimento de renda fixa tradicional, sem qualquer critério extrafinanceiro."],
    0,
    "ESG (Environmental, Social and Governance) é a integração de critérios ambientais, sociais e de governança corporativa na análise de investimentos, buscando identificar riscos e oportunidades não captados apenas pelos indicadores financeiros tradicionais.")

add_mcq(INOV, "4.4.3", "Um cliente pergunta como funciona um contrato inteligente (smart contract) em uma rede blockchain. A explicação mais adequada é:",
    ["É um programa autoexecutável registrado em blockchain, que executa automaticamente cláusulas contratuais quando condições predefinidas são atendidas, sem necessidade de intermediário.",
     "É um contrato tradicional em papel, apenas digitalizado e armazenado em nuvem.",
     "É um tipo de criptomoeda utilizada exclusivamente para pagamentos internacionais.",
     "É uma modalidade de seguro de vida oferecida por fintechs."],
    0,
    "Um smart contract é um código autoexecutável registrado em uma rede blockchain, que aplica automaticamente as regras contratuais predefinidas (por exemplo, liberar um pagamento) quando certas condições são satisfeitas, eliminando a necessidade de um intermediário para validar a execução.")

add_mcq(INOV, "4.4.4", "Uma gestora estuda representar a fração de um imóvel físico por meio de um registro digital negociável em blockchain, permitindo o investimento fracionado por diversos investidores. Esse processo é conhecido como:",
    ["Tokenização de ativos, que permite representar digitalmente a propriedade fracionada de um ativo real, com potencial de aumento de liquidez.",
     "Sandbox regulatório, um ambiente controlado para testes de novos modelos de negócio.",
     "Open finance, o compartilhamento de dados financeiros entre instituições com consentimento do cliente.",
     "DeFi (finanças descentralizadas), voltado exclusivamente à emissão de criptomoedas."],
    0,
    "A tokenização é o processo de representar digitalmente, em blockchain, a propriedade (ou fração dela) de um ativo real — como imóveis, obras de arte ou ativos financeiros — permitindo negociação fracionada e, potencialmente, maior liquidez a ativos tradicionalmente pouco líquidos.")

add_mcq(INOV, "4.5.1", "Um cliente autoriza o compartilhamento de seus dados bancários e de histórico de crédito entre diferentes instituições financeiras, por meio de uma infraestrutura regulada, para obter condições de crédito mais vantajosas. Essa funcionalidade é viabilizada pelo:",
    ["Open Finance, que permite o compartilhamento padronizado e consentido de dados e serviços financeiros entre instituições, ampliando a concorrência e a oferta de produtos personalizados.",
     "Sistema de Pagamentos Instantâneos (SPI), voltado exclusivamente a transferências via PIX.",
     "Fundo Garantidor de Créditos (FGC), que garante depósitos até determinado limite.",
     "Sistema Especial de Liquidação e Custódia (Selic), usado para liquidação de títulos públicos."],
    0,
    "O Open Finance é a infraestrutura regulada (Bacen e CVM) que permite o compartilhamento de dados e serviços financeiros entre instituições, sempre com o consentimento do cliente, ampliando a concorrência, a personalização de ofertas e o acesso a melhores condições de crédito e investimento.")

add_mcq(INOV, "4.6.3", "Uma instituição financeira implementa um assistente virtual baseado em inteligência artificial generativa para atendimento inicial de clientes, esclarecendo dúvidas frequentes sobre produtos. Sobre essa aplicação, é correto afirmar que:",
    ["A IA generativa pode ampliar a eficiência e a disponibilidade do atendimento, mas não substitui a responsabilidade do profissional certificado em recomendações complexas de suitability e adequação ao perfil do cliente.",
     "A IA generativa elimina totalmente a necessidade de profissionais certificados em qualquer etapa do relacionamento com o cliente.",
     "Assistentes virtuais de IA não podem, sob qualquer hipótese regulatória, ser usados por instituições financeiras.",
     "A IA generativa é utilizada exclusivamente para operações de tesouraria, sem aplicação em atendimento ao cliente."],
    0,
    "A IA generativa (chatbots, assistentes virtuais) amplia a eficiência e a escala do atendimento a dúvidas frequentes, mas não substitui a responsabilidade e o julgamento do profissional certificado nas etapas mais complexas do relacionamento, como a avaliação de suitability e a recomendação personalizada de produtos.")

assert len(MCQ) == 40, f"Esperado 40 MCQ, obtido {len(MCQ)}"

# ---------------- Árvores de decisão (10) ----------------

TREES = []

def add_tree(theme, title, intro, steps):
    TREES.append({"theme": theme, "title": title, "intro": intro, "steps": steps})

# Helper to build a step
def step(situation, prompt, options):
    # options: list of (text, isBest, feedback)
    return {
        "situation": situation,
        "prompt": prompt,
        "options": [{"text": t, "isBest": b, "feedback": f} for (t, b, f) in options],
    }

# --- Produtos (4 árvores) ---

add_tree(PROD, "Reserva de emergência de um cliente conservador",
    "Marina, 34 anos, perfil conservador, acaba de receber um bônus de R$ 30.000 e ainda não possui reserva de emergência formada.",
    [
        step(
            "Marina pergunta onde deve alocar o valor destinado à reserva de emergência.",
            "Qual seria a orientação mais adequada?",
            [
                ("Recomendar Tesouro Selic ou fundo DI com resgate em D+0/D+1, priorizando liquidez e baixo risco.", True,
                 "Correto. A reserva de emergência exige liquidez imediata e baixíssimo risco — o Tesouro Selic e fundos DI com resgate rápido atendem a esse objetivo."),
                ("Recomendar um CDB com carência de 720 dias, pela maior rentabilidade.", False,
                 "Incorreto. A falta de liquidez imediata torna esse produto inadequado para reserva de emergência, mesmo com rentabilidade maior."),
                ("Recomendar ações de empresas de dividendos, buscando renda passiva.", False,
                 "Incorreto. Ações têm volatilidade incompatível com o objetivo de segurança e liquidez imediata da reserva de emergência."),
            ],
        ),
        step(
            "Marina aceita a sugestão e pergunta quanto deveria manter reservado, considerando que suas despesas mensais somam R$ 6.000.",
            "Qual valor de reserva você recomendaria?",
            [
                ("Entre R$ 18.000 e R$ 36.000 (equivalente a 3 a 6 meses de despesas).", True,
                 "Correto. A prática recomendada é manter de 3 a 6 meses de despesas médias em ativos líquidos, ajustando conforme a estabilidade da renda do cliente."),
                ("Apenas R$ 6.000, equivalente a um mês de despesas.", False,
                 "Incorreto. Esse valor é insuficiente para cobrir imprevistos por um período razoável."),
                ("O valor total do bônus, R$ 30.000, mesmo excedendo a necessidade calculada.", False,
                 "Incorreto. Alocar recursos além do necessário em reserva de emergência reduz a eficiência da carteira, já que esse dinheiro tem baixo retorno esperado."),
            ],
        ),
        step(
            "Após formar a reserva ideal, Marina pergunta o que fazer com o restante do bônus.",
            "Qual seria a orientação mais adequada nesse momento?",
            [
                ("Avaliar objetivos de médio/longo prazo e o perfil de risco de Marina antes de sugerir novos produtos, iniciando pelo processo de suitability.", True,
                 "Correto. Após a reserva de emergência, a alocação do excedente deve respeitar o processo de suitability, considerando objetivos, horizonte e perfil de risco antes de qualquer recomendação."),
                ("Investir imediatamente todo o restante em um fundo multimercado agressivo, já que Marina tem dinheiro disponível.", False,
                 "Incorreto. Recomendar produtos sem avaliar o perfil de risco (perfil conservador) viola o dever de suitability."),
                ("Sugerir que Marina gaste o valor em consumo, já que reserva de emergência já está formada.", False,
                 "Incorreto. Embora seja uma decisão pessoal de Marina, o papel do assessor é orientar sobre alternativas de planejamento financeiro, não incentivar consumo."),
            ],
        ),
    ])

add_tree(PROD, "Escolha entre PGBL e VGBL",
    "Ricardo, 40 anos, é CLT, contribui para o INSS e declara Imposto de Renda pelo modelo completo. Ele quer iniciar uma previdência privada.",
    [
        step(
            "Ricardo pergunta se deve escolher PGBL ou VGBL para maximizar o benefício fiscal.",
            "Considerando o perfil de Ricardo, qual seria a orientação correta?",
            [
                ("Indicar o PGBL, já que ele declara pelo modelo completo e pode deduzir as contribuições até o limite de 12% da renda bruta anual.", True,
                 "Correto. O PGBL é vantajoso para quem declara pelo modelo completo e contribui para a previdência social, permitindo deduzir até 12% da renda bruta anual tributável."),
                ("Indicar o VGBL, pois sempre oferece a maior dedução fiscal possível.", False,
                 "Incorreto. O VGBL não permite dedução das contribuições na declaração de IR; o benefício fiscal do PGBL é mais adequado ao perfil de Ricardo."),
                ("Informar que a escolha entre PGBL e VGBL não afeta a tributação de Ricardo.", False,
                 "Incorreto. A escolha entre os produtos tem impacto direto na base de cálculo do IR e na dedutibilidade das contribuições."),
            ],
        ),
        step(
            "Ricardo pergunta qual regime de tributação escolher, já que pretende manter o investimento por mais de 15 anos.",
            "Qual seria a orientação mais adequada?",
            [
                ("Regime regressivo, pois a alíquota de IR diminui com o tempo, chegando a 10% para prazos superiores a 10 anos.", True,
                 "Correto. Para investimentos de longo prazo sem previsão de resgate próximo, o regime regressivo tende a ser mais vantajoso, já que a alíquota mínima (10%) é atingida após 10 anos."),
                ("Regime progressivo, pois a alíquota é sempre menor que no regime regressivo.", False,
                 "Incorreto. O regime progressivo segue a tabela do IR sobre a renda (podendo chegar a 27,5%), sendo geralmente menos vantajoso para quem pretende manter o investimento por muitos anos."),
                ("A escolha do regime tributário não pode ser feita no momento da contratação.", False,
                 "Incorreto. A escolha do regime tributário (progressivo ou regressivo) é feita no momento da adesão ao plano e, uma vez optado pelo regressivo, normalmente não pode ser revertida."),
            ],
        ),
        step(
            "Ricardo pergunta se pode migrar de uma seguradora para outra sem perder o tempo de permanência já contabilizado para fins de alíquota regressiva.",
            "Qual é a orientação técnica correta?",
            [
                ("Sim, por meio da portabilidade externa, respeitando regras e carências, sem a necessidade de resgatar o plano e sem perda do tempo de permanência já contabilizado.", True,
                 "Correto. A portabilidade externa permite a migração entre instituições sem resgate do plano e preservando o histórico de permanência para efeito da tabela regressiva, respeitadas as regras e carências vigentes."),
                ("Não, a portabilidade de planos de previdência complementar não é permitida pela regulamentação.", False,
                 "Incorreto. A portabilidade externa é um direito previsto na regulamentação de previdência complementar."),
                ("Sim, mas o tempo de permanência é sempre zerado ao portar o plano para outra instituição.", False,
                 "Incorreto. Uma das vantagens da portabilidade é justamente a preservação do tempo de permanência já contabilizado."),
            ],
        ),
    ])

add_tree(PROD, "Diversificação de carteira para perfil moderado",
    "Camila, perfil moderado, já possui reserva de emergência formada e deseja diversificar parte de sua carteira além da renda fixa tradicional.",
    [
        step(
            "Camila pergunta que tipo de fundo permitiria exposição a diferentes classes de ativos, sem concentrar 100% em ações.",
            "Qual seria a recomendação mais adequada ao perfil de Camila?",
            [
                ("Um fundo multimercado, com alocação diversificada entre renda fixa, ações, câmbio e derivativos, conforme a estratégia do gestor.", True,
                 "Correto. Fundos multimercados oferecem diversificação entre classes de ativos, sendo mais alinhados a um perfil moderado que busca risco intermediário em relação a fundos de ações puros."),
                ("Um fundo de ações, com no mínimo 67% da carteira concentrada nesse tipo de ativo.", False,
                 "Incorreto. A concentração mínima de 67% em ações tende a gerar volatilidade elevada, incompatível com o perfil moderado de Camila."),
                ("Um fundo cambial, com concentração mínima de 80% em ativos relacionados à variação de moeda estrangeira.", False,
                 "Incorreto. A concentração em moeda estrangeira não oferece a diversificação ampla que Camila busca, além de possuir riscos específicos elevados."),
            ],
        ),
        step(
            "Camila pergunta se a taxa de administração é a única forma de remuneração cobrada pelo fundo.",
            "Qual é a resposta correta?",
            [
                ("Não; muitos fundos multimercados também cobram taxa de performance sobre o rendimento que exceder um benchmark previamente definido.", True,
                 "Correto. Além da taxa de administração, é comum a cobrança de taxa de performance, calculada sobre o retorno que superar um benchmark (como o CDI), conforme regras definidas no regulamento."),
                ("Sim, a taxa de administração é sempre a única forma de remuneração em qualquer fundo de investimento.", False,
                 "Incorreto. Muitos fundos, especialmente os multimercados, também cobram taxa de performance."),
                ("Não; a única remuneração adicional possível é a taxa de ingresso, cobrada de todos os fundos.", False,
                 "Incorreto. A taxa de ingresso não é cobrada por todos os fundos, e a remuneração adicional mais comum em multimercados é a taxa de performance."),
            ],
        ),
        step(
            "Camila pergunta o que aconteceria com a tributação do fundo se ela resgatar em menos de 6 meses.",
            "Qual é a orientação tecnicamente correta?",
            [
                ("A alíquota de IR seria de 20%, conforme a tabela regressiva para fundos não isentos (aplicações entre 181 e 360 dias), além da possível incidência de IOF regressivo se o resgate ocorrer em menos de 30 dias.", True,
                 "Correto. Pela tabela regressiva, resgates entre 181 e 360 dias têm alíquota de 20% de IR; resgates com menos de 30 dias também podem sofrer incidência de IOF regressivo sobre o rendimento."),
                ("A alíquota de IR seria fixa em 15%, independentemente do prazo de permanência.", False,
                 "Incorreto. A alíquota de 15% é aplicável apenas para prazos superiores a 720 dias."),
                ("Não haveria qualquer tributação, pois fundos multimercados são isentos de IR.", False,
                 "Incorreto. Fundos multimercados (não isentos) seguem a tabela regressiva de IR aplicável a fundos de renda fixa/multimercado."),
            ],
        ),
    ])

add_tree(PROD, "Avaliação de crédito para o cliente",
    "Fernando precisa de R$ 8.000 para uma reforma doméstica e pergunta ao assessor qual linha de crédito seria mais vantajosa.",
    [
        step(
            "Fernando é aposentado e recebe benefício do INSS mensalmente.",
            "Entre as opções de crédito disponíveis, qual tende a ser a mais vantajosa em termos de custo para Fernando?",
            [
                ("Crédito consignado, com desconto direto no benefício e taxas de juros historicamente mais baixas que outras modalidades.", True,
                 "Correto. Por ter o pagamento garantido via desconto em folha/benefício, o crédito consignado costuma oferecer taxas de juros mais baixas do que o cheque especial, o cartão rotativo ou o CDC sem garantia."),
                ("Cheque especial, por permitir uso imediato sem burocracia.", False,
                 "Incorreto. O cheque especial está entre as linhas de crédito mais caras do mercado, sendo indicado apenas para necessidades de curtíssimo prazo."),
                ("Cartão de crédito rotativo, por não exigir aprovação de crédito adicional.", False,
                 "Incorreto. O rotativo do cartão de crédito também está entre as modalidades mais caras, não sendo recomendado para financiar valores dessa magnitude."),
            ],
        ),
        step(
            "Fernando pergunta qual seria a margem de financiamento permitida para o consignado, considerando seu benefício mensal.",
            "O que o assessor deve esclarecer sobre a margem de consignação?",
            [
                ("A margem de consignação é limitada por regulamentação, restringindo o percentual do benefício que pode ser comprometido com descontos de empréstimos consignados.", True,
                 "Correto. A regulamentação estabelece um limite máximo do benefício que pode ser comprometido com descontos de crédito consignado, para preservar a capacidade de pagamento do cliente."),
                ("Não existe qualquer limite para a margem de consignação; o cliente pode comprometer 100% do benefício.", False,
                 "Incorreto. Existe um limite regulatório para a margem de consignação, justamente para evitar o superendividamento do beneficiário."),
                ("A margem de consignação é definida exclusivamente pelo próprio cliente, sem qualquer regra do órgão pagador.", False,
                 "Incorreto. A margem é definida por regulamentação e verificada pelo órgão pagador do benefício, não sendo uma escolha livre do cliente."),
            ],
        ),
        step(
            "Fernando questiona se poderia usar o CDC (Crédito Direto ao Consumidor) como alternativa, dando um bem como garantia.",
            "Qual é a orientação tecnicamente adequada?",
            [
                ("Sim, o CDC pode ser contratado com garantia de um bem, o que tende a reduzir a taxa de juros em relação a uma operação sem garantia — mas ainda assim provavelmente resultará em custo maior que o consignado.", True,
                 "Correto. O CDC com garantia (alienação fiduciária de um bem) reduz o risco para a instituição e, portanto, a taxa de juros cobrada, mas geralmente ainda apresenta custo superior ao crédito consignado, dada a garantia mais robusta deste último (desconto direto em folha/benefício)."),
                ("Não, o CDC não pode ser contratado com qualquer tipo de garantia.", False,
                 "Incorreto. O CDC pode ser contratado com ou sem garantia, sendo comum o uso de bens como garantia para reduzir a taxa de juros."),
                ("Sim, e nesse caso o CDC sempre teria taxa de juros menor que o crédito consignado.", False,
                 "Incorreto. Ainda que a garantia reduza o custo do CDC, o crédito consignado tende a manter taxas mais baixas devido à garantia de pagamento via desconto direto."),
            ],
        ),
    ])

# --- Relacionamento com o cliente (6 árvores) ---

add_tree(REL, "Indício de lavagem de dinheiro",
    "Uma gerente de relacionamento percebe que um cliente pessoa física realizou, em uma semana, seis depósitos em espécie de R$ 9.800 cada, em agências diferentes, valores levemente abaixo do limite de reporte automático.",
    [
        step(
            "A gerente precisa decidir como agir diante desse padrão de movimentação.",
            "Qual é a conduta correta a ser adotada?",
            [
                ("Tratar o padrão como indício de fracionamento de operações (smurfing) e seguir os procedimentos internos de PLD/FT, incluindo análise baseada em risco e possível comunicação às autoridades competentes.", True,
                 "Correto. O padrão de depósitos fracionados, abaixo do limite de reporte, em diferentes agências, é um indício clássico de lavagem de dinheiro. A conduta correta é seguir a política interna de PLD/FT baseada em risco, podendo resultar em comunicação de operação suspeita."),
                ("Ignorar o padrão, pois cada depósito individualmente está abaixo do limite de reporte automático.", False,
                 "Incorreto. O padrão de fracionamento, mesmo com valores individuais abaixo do limite, é justamente a técnica usada para evitar o reporte automático, exigindo atenção adicional."),
                ("Comunicar diretamente o cliente sobre a suspeita antes de qualquer análise interna.", False,
                 "Incorreto. Alertar o cliente sobre a suspeita de lavagem de dinheiro pode comprometer a investigação e violar o dever de confidencialidade sobre comunicações de operações suspeitas."),
            ],
        ),
        step(
            "Durante a análise, o cliente afirma que os depósitos são para 'organizar melhor o orçamento pessoal' e pede que a gerente não registre nada.",
            "Qual deve ser a postura da gerente?",
            [
                ("Manter o registro e a análise interna independentemente da explicação informal do cliente, seguindo o princípio de conheça seu cliente (KYC) e a política de PLD/FT da instituição.", True,
                 "Correto. Explicações informais não substituem os procedimentos formais de KYC e PLD/FT. A instituição deve manter seus registros e análises de risco, independentemente da justificativa apresentada verbalmente pelo cliente."),
                ("Aceitar a explicação verbal e não registrar nada, pois o cliente é conhecido da agência.", False,
                 "Incorreto. Conhecer o cliente não dispensa a instituição de seguir os procedimentos formais de monitoramento e registro de operações."),
                ("Excluir o histórico de movimentações do cliente do sistema, a pedido dele.", False,
                 "Incorreto. Essa conduta seria uma grave violação da regulamentação e das normas internas de compliance, além de configurar possível ilícito."),
            ],
        ),
        step(
            "Após a análise, a área de compliance confirma que o padrão é suspeito e decide pela comunicação formal.",
            "Qual é o procedimento correto a partir desse ponto?",
            [
                ("A comunicação deve ser feita às autoridades competentes, sem informar o cliente sobre a existência da comunicação, conforme previsto na regulamentação de PLD/FT.", True,
                 "Correto. A regulamentação de PLD/FT determina que a comunicação de operações suspeitas seja feita sem dar ciência ao envolvido, preservando a efetividade das investigações e evitando percepção de aviso prévio (tipping-off)."),
                ("O cliente deve ser informado imediatamente sobre a comunicação realizada, para garantir transparência.", False,
                 "Incorreto. Informar o cliente sobre a comunicação de suspeita viola a regulamentação e pode comprometer investigações em curso."),
                ("A comunicação só pode ser feita com autorização expressa do cliente.", False,
                 "Incorreto. A comunicação de operações suspeitas é uma obrigação legal da instituição, independentemente de qualquer autorização do cliente."),
            ],
        ),
    ])

add_tree(REL, "Pedido de flexibilização no cadastro",
    "Um cliente antigo pede ao assessor que atualize seu cadastro de forma simplificada, sem preencher novamente o questionário de suitability, alegando que 'já se conhecem há anos'.",
    [
        step(
            "O assessor precisa decidir como responder ao pedido do cliente.",
            "Qual é a conduta correta?",
            [
                ("Explicar a importância do processo de suitability e KYC para a adequação e proteção do próprio cliente, orientando-o a preencher a atualização cadastral completa.", True,
                 "Correto. O princípio de 'conheça seu cliente' e o processo de suitability precisam ser mantidos atualizados periodicamente, independentemente do tempo de relacionamento, para garantir a adequação dos produtos ao perfil vigente do cliente."),
                ("Atender ao pedido e manter o cadastro antigo, já que o relacionamento é de longa data.", False,
                 "Incorreto. Cadastros desatualizados comprometem a análise de adequação (suitability) e a proteção do cliente, além de violarem normas de KYC."),
                ("Preencher o questionário sozinho, com base no que lembra do cliente, sem contato direto com ele.", False,
                 "Incorreto. A atualização cadastral deve refletir as informações reais e atuais fornecidas pelo próprio cliente, não suposições do profissional."),
            ],
        ),
        step(
            "O cliente insiste e menciona que pretende investir uma quantia elevada em um produto de maior risco, e não quer 'perder tempo com burocracia'.",
            "Qual é a orientação técnica correta?",
            [
                ("Reforçar que a atualização cadastral é ainda mais relevante diante de uma decisão de maior risco, pois protege tanto o cliente quanto a instituição, e é pré-requisito para a adequação do produto.", True,
                 "Correto. Diante de uma decisão de investimento de maior risco e valor elevado, a atualização do processo de suitability se torna ainda mais crítica, permitindo avaliar se o produto é realmente adequado ao perfil e à capacidade financeira atual do cliente."),
                ("Permitir a operação sem atualização cadastral, já que o valor elevado sugere maior sofisticação do cliente.", False,
                 "Incorreto. Maior sofisticação presumida não substitui o processo formal de suitability exigido pela regulamentação."),
                ("Sugerir que o cliente procure outra instituição que não exija esse processo.", False,
                 "Incorreto. O processo de suitability é uma exigência regulatória aplicável a toda a distribuição de produtos de investimento, não uma escolha discricionária da instituição."),
            ],
        ),
        step(
            "O cliente concorda em atualizar o cadastro, mas o resultado do novo questionário indica um perfil mais conservador do que ele esperava.",
            "Como o assessor deve proceder frente ao resultado?",
            [
                ("Informar o resultado ao cliente de forma transparente e orientá-lo sobre a inadequação do produto de maior risco ao perfil identificado, documentando a orientação.", True,
                 "Correto. O resultado do suitability deve ser comunicado com transparência, e qualquer desenquadramento entre o produto pretendido e o perfil do cliente deve ser formalmente alertado e documentado."),
                ("Alterar as respostas do questionário para que o resultado corresponda ao perfil desejado pelo cliente.", False,
                 "Incorreto. Alterar respostas para forçar um resultado específico é uma grave violação ética e regulatória do processo de suitability."),
                ("Ignorar o resultado do questionário e seguir com a operação de maior risco normalmente.", False,
                 "Incorreto. Ignorar o resultado do suitability contraria diretamente o objetivo de proteção do cliente e as normas de conduta da ANBIMA."),
            ],
        ),
    ])

add_tree(REL, "Conflito de interesse na recomendação de produtos",
    "Um assessor recebe uma meta comercial e uma remuneração adicional para distribuir um fundo próprio da instituição, mesmo havendo, no mercado, produtos de terceiros com histórico melhor e custos mais baixos para o perfil do cliente.",
    [
        step(
            "Um cliente moderado pede uma recomendação de fundo para parte de sua carteira.",
            "Qual deve ser a conduta do assessor diante desse conflito de interesse?",
            [
                ("Avaliar e apresentar as opções mais adequadas ao perfil e objetivo do cliente, informando com transparência sobre a existência de incentivos ou remuneração diferenciada relacionados a determinados produtos.", True,
                 "Correto. O interesse do cliente deve estar no centro da recomendação. Havendo conflito de interesse (como incentivos comerciais), o profissional deve ao menos ser transparente sobre sua existência, sem que isso comprometa a adequação da recomendação ao perfil do cliente."),
                ("Recomendar exclusivamente o fundo próprio da instituição, por gerar maior remuneração ao assessor, sem mencionar as demais opções disponíveis.", False,
                 "Incorreto. Priorizar a remuneração própria em detrimento da adequação ao cliente, sem transparência, viola os princípios éticos do Código ANBIMA."),
                ("Recusar-se a fazer qualquer recomendação, para evitar lidar com o conflito de interesse.", False,
                 "Incorreto. O papel do assessor é justamente gerenciar o conflito de interesse de forma transparente e ética, e não evitar o atendimento ao cliente."),
            ],
        ),
        step(
            "O cliente pergunta diretamente se o assessor recebe alguma comissão diferenciada pela venda do fundo próprio.",
            "Qual é a resposta adequada?",
            [
                ("Responder com transparência sobre a existência (ou não) de remuneração diferenciada, conforme as regras de transparência na remuneração do canal de distribuição previstas no Código ANBIMA.", True,
                 "Correto. O Código de Distribuição da ANBIMA prevê regras de transparência na remuneração do canal de distribuição, exigindo que o profissional seja transparente sobre incentivos que possam influenciar sua recomendação."),
                ("Negar a existência de qualquer diferença de remuneração, mesmo que ela exista, para não comprometer a venda.", False,
                 "Incorreto. Prestar informação falsa ao cliente sobre remuneração constitui grave violação ética e regulatória."),
                ("Recusar-se a responder, alegando que essa informação é confidencial e não pode ser compartilhada com o cliente.", False,
                 "Incorreto. As regras de transparência exigem que esse tipo de informação seja acessível ao cliente quando questionada."),
            ],
        ),
        step(
            "Após a explicação transparente, o cliente decide investir em um fundo de terceiros, com custos mais baixos, mesmo isso gerando menor remuneração ao assessor.",
            "Qual deve ser a conduta final do assessor?",
            [
                ("Processar a operação conforme a decisão informada do cliente, sem qualquer tentativa de reverter a escolha em benefício da remuneração própria.", True,
                 "Correto. Uma vez informado com transparência e mantendo o consentimento esclarecido, o cliente tem autonomia para decidir. O assessor deve respeitar a decisão, sem insistir em alternativas que priorizem sua remuneração em detrimento do interesse do cliente."),
                ("Insistir repetidamente para que o cliente reconsidere e opte pelo fundo próprio da instituição.", False,
                 "Incorreto. Insistir para reverter uma decisão informada do cliente, motivado por remuneração própria, configura conduta antiética."),
                ("Processar a operação, mas registrar internamente uma recomendação contrária à vontade do cliente, sem informá-lo.", False,
                 "Incorreto. Não há justificativa ética ou regulatória para registrar recomendações ocultas contrárias à decisão informada e autônoma do cliente."),
            ],
        ),
    ])

add_tree(REL, "Planejamento para aposentadoria",
    "Paulo, 45 anos, pergunta ao assessor como estruturar um plano de aposentadoria para os próximos 20 anos, considerando que hoje não possui nenhuma reserva formal para esse objetivo.",
    [
        step(
            "Paulo pergunta qual é o primeiro passo do planejamento financeiro para esse objetivo.",
            "Qual é a etapa inicial mais adequada, segundo o processo de planejamento financeiro pessoal?",
            [
                ("Definir os objetivos financeiros específicos de Paulo (valor desejado, idade-alvo) e avaliar sua situação financeira atual (receitas, despesas, patrimônio e dívidas).", True,
                 "Correto. O processo de planejamento financeiro pessoal começa pela definição clara dos objetivos da clientela e pela avaliação detalhada da situação financeira atual, antes de qualquer recomendação de produto."),
                ("Recomendar imediatamente um fundo de ações de longo prazo, sem qualquer levantamento prévio.", False,
                 "Incorreto. Recomendar produtos antes de entender objetivos e situação financeira viola o processo estruturado de planejamento e o dever de suitability."),
                ("Sugerir que Paulo contrate exclusivamente um plano de previdência complementar, sem avaliar outras alternativas.", False,
                 "Incorreto. A previdência complementar pode ser parte da solução, mas a recomendação de qualquer produto deve vir após a etapa de avaliação de objetivos e situação financeira."),
            ],
        ),
        step(
            "Após o levantamento, verifica-se que Paulo tem capacidade de poupança mensal, mas nenhuma reserva de emergência.",
            "Qual deve ser a prioridade na estruturação do plano?",
            [
                ("Constituir primeiro a reserva de emergência, e só então direcionar os aportes remanescentes para o objetivo de aposentadoria de longo prazo.", True,
                 "Correto. A reserva de emergência é a base da pirâmide de planejamento financeiro, protegendo o cliente contra imprevistos sem necessidade de resgatar investimentos de longo prazo em condições desfavoráveis."),
                ("Direcionar 100% da capacidade de poupança para o plano de aposentadoria desde o primeiro mês, ignorando a reserva de emergência.", False,
                 "Incorreto. Sem reserva de emergência, qualquer imprevisto financeiro poderia forçar o resgate antecipado dos investimentos de longo prazo, prejudicando o objetivo de aposentadoria."),
                ("Sugerir que Paulo não poupe neste momento, aguardando uma reavaliação em 5 anos.", False,
                 "Incorreto. Adiar o início da poupança reduz o efeito dos juros compostos ao longo do tempo, prejudicando o objetivo de aposentadoria em 20 anos."),
            ],
        ),
        step(
            "Com a reserva de emergência em formação, Paulo pergunta que tipo de produto de previdência seria mais adequado para o horizonte de 20 anos, considerando que ele contribui para o INSS e declara IR pelo modelo completo.",
            "Qual seria a recomendação técnica mais adequada?",
            [
                ("PGBL com regime de tributação regressivo, aproveitando a dedução fiscal (até 12% da renda bruta) e a alíquota decrescente para o longo prazo.", True,
                 "Correto. Para quem declara pelo modelo completo, contribui ao INSS e tem horizonte de longo prazo sem previsão de resgate, o PGBL com regime regressivo combina o benefício fiscal da dedução com a menor alíquota final de IR."),
                ("VGBL com regime progressivo, por ser sempre a combinação mais vantajoso para qualquer perfil.", False,
                 "Incorreto. Para o perfil de Paulo (declaração completa, contribuinte do INSS, longo prazo), o PGBL com regime regressivo tende a ser mais vantajoso do que essa combinação."),
                ("Não recomendar previdência complementar, pois não há qualquer vantagem tributária nesse tipo de produto.", False,
                 "Incorreto. A previdência complementar oferece vantagens tributárias específicas (dedução no PGBL e/ou alíquotas decrescentes no regime regressivo) que podem ser relevantes para objetivos de longo prazo como a aposentadoria."),
            ],
        ),
    ])

add_tree(REL, "Suspeita de uso de informação privilegiada",
    "Durante uma conversa informal, um cliente executivo de uma companhia aberta comenta que 'em breve' sua empresa anunciará uma fusão relevante ainda não divulgada ao mercado, e pergunta se deveria comprar mais ações da própria companhia antes do anúncio.",
    [
        step(
            "O cliente pede a opinião do assessor sobre a operação.",
            "Qual deve ser a conduta do assessor diante desse pedido?",
            [
                ("Alertar o cliente que negociar com base nessa informação configura uso indevido de informação privilegiada (insider trading), uma infração penal, e recusar-se a orientar ou viabilizar a operação nesses termos.", True,
                 "Correto. A negociação com base em informação relevante ainda não divulgada ao mercado caracteriza insider trading (art. 27-D da Lei 6.385/76). O assessor deve alertar o cliente sobre a ilegalidade e não deve, em qualquer hipótese, incentivar ou viabilizar a operação nessas condições."),
                ("Orientar o cliente a comprar as ações rapidamente, antes do anúncio, para maximizar o ganho.", False,
                 "Incorreto. Essa conduta configuraria participação em uso indevido de informação privilegiada, uma infração penal grave."),
                ("Ignorar o comentário e processar a ordem de compra normalmente, sem qualquer alerta.", False,
                 "Incorreto. Mesmo sem incentivar ativamente, processar a operação com conhecimento da informação privilegiada pode comprometer o profissional e a instituição."),
            ],
        ),
        step(
            "O cliente insiste, argumentando que 'é só uma opinião entre amigos' e que a decisão final será dele mesmo.",
            "Qual deve ser a postura do assessor?",
            [
                ("Reiterar o alerta sobre a ilegalidade da conduta, recusar-se a processar qualquer operação vinculada a essa informação e considerar reportar a situação à área de compliance, conforme as políticas internas.", True,
                 "Correto. Independentemente da relação pessoal, o profissional certificado tem o dever de agir com integridade e reportar situações que possam configurar infrações regulatórias, protegendo o mercado e a própria instituição."),
                ("Aceitar processar a ordem, já que a responsabilidade final seria apenas do cliente.", False,
                 "Incorreto. O profissional que processa a operação com conhecimento da informação privilegiada pode ser responsabilizado por participação na infração."),
                ("Sugerir que o cliente opere por meio de outra corretora, para que a instituição atual não seja envolvida.", False,
                 "Incorreto. Direcionar o cliente para viabilizar a mesma conduta ilegal em outra instituição não elimina a responsabilidade ética e pode configurar conivência com a infração."),
            ],
        ),
        step(
            "A área de compliance da instituição é notificada sobre o episódio.",
            "Qual é o procedimento mais adequado a ser seguido pela instituição a partir desse ponto?",
            [
                ("Registrar o episódio internamente, avaliar a necessidade de comunicação a órgãos reguladores/autorreguladores competentes e adotar as medidas de gestão de conflitos e monitoramento previstas na política de compliance.", True,
                 "Correto. A instituição deve documentar o episódio, avaliar a necessidade de comunicação (por exemplo, à CVM) e reforçar seus controles internos de monitoramento e gestão de conflitos, dentro da política de compliance vigente."),
                ("Nenhuma ação é necessária, pois a operação não chegou a ser executada.", False,
                 "Incorreto. Ainda que a operação não tenha sido executada, o episódio deve ser registrado e avaliado pela área de compliance como parte da gestão de riscos regulatórios."),
                ("Somente o cliente deve ser advertido verbalmente, sem qualquer registro formal do episódio.", False,
                 "Incorreto. A ausência de registro formal compromete a rastreabilidade e a efetividade dos controles internos de prevenção a ilícitos de mercado."),
            ],
        ),
    ])

add_tree(REL, "Gestão de expectativas após falha no atendimento",
    "Um cliente reclama que enviou uma solicitação de resgate há três dias e ainda não recebeu retorno do assessor, demonstrando forte insatisfação e ameaçando encerrar o relacionamento com a instituição.",
    [
        step(
            "O assessor entra em contato com o cliente para tratar a reclamação.",
            "Qual é a abordagem inicial mais adequada?",
            [
                ("Praticar escuta ativa, reconhecer a falha na comunicação e pedir desculpas de forma genuína, antes de apresentar qualquer solução.", True,
                 "Correto. A escuta ativa e o reconhecimento sincero do problema são a base para reconstruir a confiança do cliente, devendo preceder qualquer tentativa de solução ou justificativa."),
                ("Explicar imediatamente os motivos internos do atraso, sem antes ouvir a reclamação completa do cliente.", False,
                 "Incorreto. Justificar antes de ouvir integralmente a reclamação pode ser percebido como desconsideração com a insatisfação do cliente."),
                ("Minimizar a reclamação, informando que o prazo de três dias é considerado normal pela instituição.", False,
                 "Incorreto. Minimizar a percepção do cliente, especialmente diante de forte insatisfação, tende a agravar a situação em vez de reconstruir a confiança."),
            ],
        ),
        step(
            "Depois de ouvir o cliente, o assessor verifica que o resgate realmente não foi processado por uma falha operacional interna.",
            "Qual deve ser a conduta correta a partir dessa constatação?",
            [
                ("Assumir a responsabilidade pela falha, informar um prazo realista e verificável para a solução, e acompanhar ativamente até a resolução efetiva.", True,
                 "Correto. Uma gestão de expectativas eficaz envolve assumir a responsabilidade pela falha, comunicar prazos realistas e fazer o acompanhamento proativo até a resolução, em vez de apenas prometer uma solução genérica."),
                ("Atribuir a falha exclusivamente à área operacional, sem qualquer menção a um plano de solução com prazo.", False,
                 "Incorreto. Apenas transferir a culpa para outra área, sem apresentar um plano concreto de solução, não atende à expectativa do cliente nem resolve o problema."),
                ("Prometer que o problema nunca mais ocorrerá, sem detalhar qualquer prazo ou acompanhamento concreto para o caso atual.", False,
                 "Incorreto. Promessas genéricas sem prazo ou plano de acompanhamento tendem a não restaurar a confiança do cliente diante de uma falha concreta e ainda não resolvida."),
            ],
        ),
        step(
            "Após a resolução do resgate, o cliente ainda demonstra receio de que problemas semelhantes ocorram no futuro.",
            "Qual atitude do assessor contribui mais para a manutenção do relacionamento no longo prazo?",
            [
                ("Propor um canal de acompanhamento mais próximo (checkpoints periódicos) e reforçar a transparência sobre processos futuros, sem prometer perfeição absoluta.", True,
                 "Correto. Reforçar a transparência e propor um acompanhamento mais próximo demonstra comprometimento genuíno com a experiência do cliente, sendo mais eficaz e realista do que prometer que erros nunca mais ocorrerão."),
                ("Oferecer um produto de maior rentabilidade como forma de compensação pelo transtorno, sem qualquer relação com a causa do problema.", False,
                 "Incorreto. Oferecer produtos financeiros como compensação, sem tratar a causa da insatisfação (falha operacional/comunicação), pode gerar novos riscos de suitability, sem resolver a questão de confiança."),
                ("Evitar qualquer contato futuro proativo com o cliente, para não relembrá-lo do problema ocorrido.", False,
                 "Incorreto. Evitar contato proativo tende a aumentar a insegurança do cliente, ao contrário de reforçar a transparência e o acompanhamento."),
            ],
        ),
    ])

assert len(TREES) == 10, f"Esperado 10 árvores, obtido {len(TREES)}"

# Weight mapping for exam composition summary
WEIGHTS = {SFN: 20, PROD: 40, REL: 30, INOV: 10}

def counts_by_theme(items, key_theme="theme"):
    out = {}
    for it in items:
        out[it[key_theme]] = out.get(it[key_theme], 0) + 1
    return out

mcq_counts = counts_by_theme(MCQ)
tree_counts = counts_by_theme(TREES)

data = {
    "meta": {
        "title": "Simulado CPA — Certificado Profissional ANBIMA",
        "subtitle": "Formato oficial 2026 · 50 questões · 2h30 · 70% para aprovação",
        "duration_minutes": 150,
        "total_questions": len(MCQ) + len(TREES),
        "passing_pct": 70,
        "passing_correct": 35,
        "weights": WEIGHTS,
        "mcq_counts": mcq_counts,
        "tree_counts": tree_counts,
        "sources": [
            {"label": "ANBIMA — Estruturas das provas CPA, C-Pro R e C-Pro I", "url": "https://www.anbima.com.br/pt_br/noticias/definidas-as-estruturas-das-provas-para-as-novas-certificacoes-cpa-c-pro-r-e-c-pro-i-8A2AB2AE98F3AB840198FBE551005B27-00.htm"},
            {"label": "ANBIMA — Programa detalhado CPA", "url": "https://www.anbima.com.br/data/files/6A/52/6F/A1/BED73910B07B2739B82BA2A8/Programa-Detalhado-CPA-ANBIMA.pdf"},
            {"label": "ANBIMA — Edital dos Exames de Certificação Profissional", "url": "https://www.anbima.com.br/data/files/98/96/A6/10/9C24C910CF6A83C9F82BA2A8/Edital-dos-Exames-de-Certificacao-Profissional-Anbima.pdf"},
            {"label": "ANBIMA — Programa de estudos CPA, C-Pro I e C-Pro R (guia e cadernos de questões)", "url": "https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm"},
        ],
    },
    "mcq": MCQ,
    "trees": TREES,
}

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("MCQ:", len(MCQ), mcq_counts)
print("Trees:", len(TREES), tree_counts)
print("Total questions:", len(MCQ) + len(TREES))
