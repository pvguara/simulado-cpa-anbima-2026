PROD = "Produtos do mercado financeiro"
REL = "Relacionamento com o cliente"

TREES_B = [

    # ---------------- PRODUTOS (4 árvores) ----------------

    {
        "theme": PROD,
        "title": "FII de tijolo x FII de papel para renda passiva",
        "intro": "Beatriz, 52 anos, perfil moderado, quer complementar sua renda mensal com fundos imobiliários e pergunta ao assessor qual tipo de FII escolher.",
        "steps": [
            {
                "situation": "Beatriz pergunta qual a diferença prática entre um fundo imobiliário 'de tijolo' e um 'de papel' antes de decidir onde alocar o dinheiro.",
                "prompt": "Qual é a explicação tecnicamente correta?",
                "options": [
                    {"text": "O fundo de tijolo investe em imóveis físicos (galpões, shoppings, lajes corporativas) e distribui rendimentos ligados a aluguéis, enquanto o fundo de papel investe majoritariamente em títulos de renda fixa imobiliária, como CRIs, com rendimentos ligados a juros e indexadores.", "isBest": True, "feedback": "Correto. Os FIIs de tijolo têm exposição direta a imóveis e ao risco de vacância/aluguel, enquanto os FIIs de papel investem em recebíveis imobiliários (como CRIs), com rendimentos mais próximos ao comportamento da renda fixa e sensibilidade a juros e crédito."},
                    {"text": "Ambos os tipos investem exclusivamente em imóveis físicos, mudando apenas o nome comercial dado pelo gestor.", "isBest": False, "feedback": "Incorreto. Fundos de papel não investem diretamente em imóveis físicos; sua carteira é composta principalmente por títulos de dívida imobiliária, como CRIs e LCIs."},
                    {"text": "O fundo de papel garante rendimento fixo mensal assegurado por lei, enquanto o de tijolo não paga rendimentos.", "isBest": False, "feedback": "Incorreto. Nenhum FII garante rendimento fixo por lei; ambos distribuem rendimentos variáveis conforme o desempenho dos ativos da carteira, respeitada a obrigatoriedade de distribuição mínima semestral de 95% do resultado auferido."},
                ],
            },
            {
                "situation": "Beatriz esclarece que seu objetivo é ter uma renda passiva estável e previsível todos os meses, com menor sensibilidade a vacância de imóveis.",
                "prompt": "Considerando esse objetivo, qual orientação é mais adequada?",
                "options": [
                    {"text": "Explicar que FIIs de papel reduzem a exposição direta à vacância, mas exigem análise de crédito, indexadores, concentração e liquidez; não há garantia de renda mensal estável.", "isBest": True, "feedback": "Correto. Menor exposição direta à vacância não significa risco menor em todas as dimensões nem renda previsível garantida. A capacidade dos devedores, indexadores e características da carteira precisam ser avaliados diante do objetivo de Beatriz."},
                    {"text": "Priorizar a alocação em FIIs de tijolo, pois imóveis físicos nunca ficam vagos e sempre geram renda constante.", "isBest": False, "feedback": "Incorreto. Imóveis físicos podem ficar vagos ou com inadimplência de locatários, o que reduz e torna mais volátil a distribuição de rendimentos nos FIIs de tijolo."},
                    {"text": "Concentrar 100% dos recursos em um único FII de tijolo com um único imóvel, para maximizar o rendimento mensal.", "isBest": False, "feedback": "Incorreto. Concentrar em um único fundo/imóvel aumenta o risco de concentração e de vacância, contrariando o objetivo de estabilidade buscado por Beatriz e o princípio de diversificação."},
                ],
            },
            {
                "situation": "Beatriz pergunta como é tributada a distribuição mensal de rendimentos que ela receberá dos FIIs, e se essa renda seria isenta de Imposto de Renda.",
                "prompt": "Qual é a orientação tecnicamente correta sobre a tributação dos rendimentos distribuídos por FIIs listados em bolsa?",
                "options": [
                    {"text": "Os rendimentos distribuídos por FIIs podem ser isentos para pessoa física quando cumpridos os requisitos legais de negociação, dispersão e participação; a isenção não abrange automaticamente o ganho na venda das cotas.", "isBest": True, "feedback": "Correto. É necessário conferir os requisitos de isenção aplicáveis ao fundo e ao beneficiário. Não se deve confundir o rendimento distribuído com ganho obtido ao vender cotas; são eventos com tratamento próprio."},
                    {"text": "Toda e qualquer distribuição de rendimento de FII é isenta de IR, independentemente de qualquer condição regulatória.", "isBest": False, "feedback": "Incorreto. A isenção está condicionada ao atendimento de requisitos legais específicos, não sendo incondicional para todos os FIIs em qualquer situação."},
                    {"text": "Os rendimentos distribuídos por FIIs seguem a tabela regressiva de IR, como nos fundos de renda fixa tradicionais.", "isBest": False, "feedback": "Incorreto. A distribuição de rendimentos de FIIs elegíveis à isenção não segue a tabela regressiva; ela é isenta de IR para pessoa física quando atendidos os requisitos legais, diferentemente da tributação de fundos de renda fixa."},
                ],
            },
        ],
    },

    {
        "theme": PROD,
        "title": "Estruturação de um COE para cliente moderado",
        "intro": "Henrique, 47 anos, perfil moderado, ouviu falar de um COE (Certificado de Operações Estruturadas) ligado ao Ibovespa e pergunta ao assessor se é uma boa opção.",
        "steps": [
            {
                "situation": "Henrique pergunta o que é, de fato, um COE e como ele consegue oferecer exposição a uma bolsa de valores.",
                "prompt": "Qual é a explicação tecnicamente correta sobre a estrutura de um COE?",
                "options": [
                    {"text": "O COE é um instrumento financeiro que combina, tipicamente, uma parcela de renda fixa (para proteção de parte ou de todo o capital) com uma parcela de derivativos (como opções), que geram o retorno vinculado ao desempenho de um índice ou ativo de referência, como o Ibovespa.", "isBest": True, "feedback": "Correto. O COE é estruturado a partir da combinação de renda fixa e derivativos, permitindo oferecer diferentes perfis de risco/retorno vinculados a índices, moedas, ações ou outros ativos de referência, com a modalidade de capital protegido sendo a mais comum para perfis mais conservadores."},
                    {"text": "O COE é uma modalidade de ação negociada diretamente na B3, com liquidez diária garantida por lei.", "isBest": False, "feedback": "Incorreto. O COE não é uma ação; é um título estruturado emitido por instituição financeira, geralmente sem liquidez diária garantida e com resgate condicionado às regras do próprio produto."},
                    {"text": "O COE garante, por definição legal, rentabilidade mínima equivalente ao CDI, independentemente do desempenho do ativo de referência.", "isBest": False, "feedback": "Incorreto. Não há garantia legal de rentabilidade mínima; o retorno do COE depende do cenário e da modalidade contratada (capital protegido ou capital em risco), podendo em alguns casos não haver rendimento algum."},
                ],
            },
            {
                "situation": "Henrique tem perfil moderado e não deseja correr risco de perder o capital investido, mas gostaria de participar de eventuais altas do Ibovespa.",
                "prompt": "Qual modalidade de COE é mais adequada ao objetivo e ao perfil de Henrique?",
                "options": [
                    {"text": "COE de capital protegido, no qual o valor principal investido é devolvido no vencimento mesmo em cenário de queda do índice, havendo ganho adicional apenas se o cenário de alta previsto se confirmar.", "isBest": True, "feedback": "Correto. O COE de capital protegido devolve o principal investido no vencimento, independentemente do desempenho do ativo de referência, e paga um retorno adicional condicionado ao cenário favorável — sendo compatível com um cliente que não aceita risco de perda do capital."},
                    {"text": "COE de capital em risco, pois oferece potencial de retorno maior e é a única modalidade disponível no mercado brasileiro.", "isBest": False, "feedback": "Incorreto. O COE de capital em risco pode gerar perda de parte ou de todo o principal investido, sendo incompatível com a exigência de Henrique de não perder capital; além disso, o capital protegido também é uma modalidade amplamente disponível no mercado."},
                    {"text": "Qualquer modalidade de COE, pois o capital investido é sempre garantido pelo Fundo Garantidor de Créditos (FGC) até o limite de cobertura.", "isBest": False, "feedback": "Incorreto. O COE não é garantido pelo FGC; a proteção do capital, quando existe, decorre exclusivamente da estrutura contratual do próprio produto (modalidade capital protegido), e não de um mecanismo de garantia externo."},
                ],
            },
            {
                "situation": "Henrique pergunta se poderá resgatar o valor investido no COE antes do vencimento, caso precise do dinheiro em uma emergência.",
                "prompt": "Qual é a orientação correta sobre a liquidez do COE?",
                "options": [
                    {"text": "O COE normalmente não possui liquidez diária nem mercado secundário relevante; o resgate antecipado, quando permitido pelo emissor, pode ocorrer com deságio e sem a garantia de proteção do capital prevista apenas para o vencimento.", "isBest": True, "feedback": "Correto. O COE é um produto de baixa liquidez, estruturado para ser mantido até o vencimento. A eventual saída antecipada depende de condições específicas do emissor e pode implicar perda de parte do capital, já que a proteção contratual normalmente só vale na data de vencimento."},
                    {"text": "O COE tem liquidez diária garantida, podendo ser resgatado a qualquer momento sem qualquer perda, assim como um fundo DI.", "isBest": False, "feedback": "Incorreto. O COE não tem liquidez diária como um fundo DI; a proteção do capital, quando prevista, normalmente é válida apenas no vencimento contratado."},
                    {"text": "Por isso, o COE é o produto mais indicado justamente para a reserva de emergência de qualquer cliente.", "isBest": False, "feedback": "Incorreto. A baixa liquidez e a possível ausência de proteção em resgates antecipados tornam o COE inadequado para reserva de emergência, que exige disponibilidade imediata dos recursos."},
                ],
            },
        ],
    },

    {
        "theme": PROD,
        "title": "Crédito consignado x CDC para necessidade de crédito",
        "intro": "Juliana, 38 anos, funcionária pública, precisa de R$ 15.000 para comprar um veículo usado e pergunta ao assessor qual linha de crédito contratar.",
        "steps": [
            {
                "situation": "Juliana pergunta se deveria contratar um crédito consignado, descontado direto em folha, ou um CDC com o próprio veículo em garantia.",
                "prompt": "Considerando o objetivo de menor custo financeiro, qual orientação inicial é mais adequada?",
                "options": [
                    {"text": "Explicar que ambas as modalidades podem ter taxas competitivas por contarem com algum tipo de garantia (desconto em folha no consignado, alienação fiduciária do bem no CDC), e que a comparação deve ser feita pelo Custo Efetivo Total (CET) de cada proposta antes da decisão.", "isBest": True, "feedback": "Correto. Tanto o consignado quanto o CDC com garantia tendem a ter taxas mais baixas do que linhas sem garantia, mas a comparação correta entre propostas concorrentes deve sempre considerar o Custo Efetivo Total (CET), que inclui juros, tarifas e demais encargos, e não apenas a taxa de juros nominal."},
                    {"text": "Recomendar diretamente o cheque especial, por ser a forma mais rápida de obter o crédito, sem necessidade de comparação de taxas.", "isBest": False, "feedback": "Incorreto. O cheque especial está entre as modalidades de crédito mais caras do mercado e não é adequado para financiar a compra de um bem de maior valor, como um veículo."},
                    {"text": "Afirmar que a taxa de juros nominal informada pela instituição já é suficiente para comparar as propostas, sem necessidade de outras informações.", "isBest": False, "feedback": "Incorreto. A taxa de juros nominal isolada pode não refletir o custo total da operação; o CET é o indicador correto para comparação, pois incorpora tarifas e demais encargos."},
                ],
            },
            {
                "situation": "Juliana esclarece que pretende comprometer uma parcela relevante de sua renda mensal com essa dívida e pergunta se há algum limite regulatório para isso no crédito consignado.",
                "prompt": "Qual é a orientação tecnicamente correta?",
                "options": [
                    {"text": "Sim, existe um limite regulatório para a margem consignável, que restringe o percentual da remuneração que pode ser comprometido com descontos de empréstimos consignados, justamente para preservar a capacidade de pagamento do tomador.", "isBest": True, "feedback": "Correto. A regulamentação estabelece um limite máximo de comprometimento da renda (margem consignável) para operações de crédito consignado, com o objetivo de evitar o superendividamento do tomador."},
                    {"text": "Não, o crédito consignado permite comprometer 100% da renda mensal do servidor, sem qualquer limite.", "isBest": False, "feedback": "Incorreto. Existe um limite regulatório de margem consignável; comprometer a totalidade da renda não é permitido."},
                    {"text": "O limite de comprometimento de renda é definido livremente pela instituição financeira, sem qualquer parâmetro regulatório.", "isBest": False, "feedback": "Incorreto. O limite da margem consignável decorre de regulamentação aplicável, e não de uma escolha discricionária de cada instituição."},
                ],
            },
            {
                "situation": "Após a análise, Juliana decide pelo CDC com o veículo em garantia, mas pergunta o que ocorre caso ela deixe de pagar as parcelas.",
                "prompt": "Qual é a explicação tecnicamente correta sobre a garantia do CDC com alienação fiduciária?",
                "options": [
                    {"text": "Em caso de inadimplência, a instituição financeira pode buscar a retomada (busca e apreensão) do bem dado em garantia por alienação fiduciária, para fins de venda e amortização do saldo devedor, seguindo o rito legal aplicável.", "isBest": True, "feedback": "Correto. Na alienação fiduciária, o bem financiado garante a operação; em caso de inadimplência, a instituição pode adotar as medidas legais para retomada e venda do bem, com o produto da venda sendo utilizado para amortizar o saldo devedor."},
                    {"text": "Nada ocorre com o bem, pois a alienação fiduciária é apenas uma formalidade sem efeito prático em caso de inadimplência.", "isBest": False, "feedback": "Incorreto. A alienação fiduciária tem efeito prático relevante: ela garante à instituição financeira o direito de retomada do bem em caso de inadimplência."},
                    {"text": "O bem passa a pertencer definitivamente ao cliente desde a assinatura do contrato, independentemente do pagamento das parcelas.", "isBest": False, "feedback": "Incorreto. Na alienação fiduciária, a propriedade do bem permanece com o credor (fiduciário) até a liquidação da dívida, sendo transferida ao devedor apenas após o pagamento integral."},
                ],
            },
        ],
    },

    {
        "theme": PROD,
        "title": "Seguro de vida para cliente com dependentes",
        "intro": "Roberto, 36 anos, casado e pai de duas crianças pequenas, é o principal responsável pelo sustento da família e pergunta ao assessor sobre contratar um seguro de vida.",
        "steps": [
            {
                "situation": "Roberto pergunta a diferença entre um seguro de vida temporário (por prazo determinado) e um seguro de vida inteira, e qual seria mais indicado para proteger a família enquanto os filhos são dependentes financeiramente.",
                "prompt": "Qual orientação é mais adequada à necessidade atual de Roberto?",
                "options": [
                    {"text": "Indicar o seguro de vida temporário, com prazo definido (por exemplo, até os filhos atingirem independência financeira), por oferecer cobertura de proteção com prêmios geralmente mais baixos para o mesmo capital segurado nesse período.", "isBest": True, "feedback": "Correto. O seguro de vida temporário cobre um período determinado, sendo adequado para proteger uma necessidade específica e temporária (como a dependência financeira dos filhos), normalmente com prêmio mais acessível do que o seguro de vida inteira para o mesmo capital segurado."},
                    {"text": "Indicar exclusivamente o seguro de vida inteira, pois é sempre a opção de menor custo para qualquer objetivo de proteção familiar.", "isBest": False, "feedback": "Incorreto. O seguro de vida inteira (cobertura vitalícia) tende a ter prêmios mais elevados do que o temporário para um mesmo capital segurado, não sendo necessariamente a opção de menor custo para uma necessidade temporária."},
                    {"text": "Informar que seguro de vida não é relevante para o planejamento financeiro familiar e sugerir que o valor do prêmio seja aplicado em ações.", "isBest": False, "feedback": "Incorreto. Para o responsável pelo sustento de dependentes, o seguro de vida tem papel relevante na proteção patrimonial e de renda da família em caso de sinistro, sendo parte do planejamento financeiro, e não um substituto de investimento em ações."},
                ],
            },
            {
                "situation": "Roberto pergunta como definir o capital segurado (valor da indenização) mais adequado para sua situação.",
                "prompt": "Qual é a orientação técnica mais adequada para essa definição?",
                "options": [
                    {"text": "Considerar as necessidades financeiras dos dependentes (despesas correntes, dívidas existentes, custos futuros como educação) e o horizonte necessário até que a família alcance independência financeira, dimensionando o capital segurado a partir dessa análise.", "isBest": True, "feedback": "Correto. O dimensionamento do capital segurado deve partir de uma análise das necessidades reais dos dependentes — despesas de manutenção, dívidas, educação dos filhos — e do tempo necessário até a independência financeira da família, e não de um valor arbitrário."},
                    {"text": "Contratar sempre o capital segurado máximo oferecido pela seguradora, independentemente do custo do prêmio ou da real necessidade da família.", "isBest": False, "feedback": "Incorreto. Contratar o capital máximo sem relação com a necessidade real pode gerar prêmios desproporcionais ao orçamento familiar, sem necessariamente otimizar a proteção adequada."},
                    {"text": "Definir o capital segurado com base apenas na renda mensal atual de Roberto, sem considerar despesas, dívidas ou horizonte de dependência dos filhos.", "isBest": False, "feedback": "Incorreto. Uma análise adequada deve considerar o conjunto de necessidades futuras da família (despesas, dívidas, horizonte), e não apenas a renda mensal isolada."},
                ],
            },
            {
                "situation": "Roberto pergunta se, ao final do prazo do seguro de vida temporário, ele receberá de volta os prêmios pagos, caso nada tenha acontecido.",
                "prompt": "Qual é a resposta tecnicamente correta?",
                "options": [
                    {"text": "Não; no seguro de vida temporário tradicional, os prêmios pagos remuneram a cobertura de risco durante o período contratado e não são devolvidos ao final, caso não ocorra o sinistro coberto.", "isBest": True, "feedback": "Correto. O seguro de vida temporário funciona como proteção pura contra o risco (mutualismo): os prêmios pagos custeiam a cobertura durante o período contratado e, salvo produtos específicos com cláusula de resgate, não são devolvidos ao segurado se o sinistro não ocorrer."},
                    {"text": "Sim, todo seguro de vida devolve integralmente os prêmios pagos ao final do contrato, com correção monetária.", "isBest": False, "feedback": "Incorreto. Essa característica não é padrão do seguro de vida temporário tradicional, que tem natureza de proteção contra o risco, e não de produto de acumulação com resgate garantido."},
                    {"text": "Sim, mas apenas se Roberto cancelar o contrato antes do término do prazo contratado.", "isBest": False, "feedback": "Incorreto. O cancelamento antecipado não gera, por padrão, devolução dos prêmios já pagos no seguro de vida temporário tradicional; a característica de resgate não é a regra geral desse tipo de produto."},
                ],
            },
        ],
    },

    # ---------------- RELACIONAMENTO COM O CLIENTE (6 árvores) ----------------

    {
        "theme": REL,
        "title": "Pedido para compartilhar dados de cliente sem autorização",
        "intro": "Um cliente pede ao assessor que compartilhe o extrato de investimentos e o telefone de outro cliente (seu ex-sócio), afirmando que precisa 'só confirmar uma informação' para resolver uma pendência entre eles.",
        "steps": [
            {
                "situation": "O assessor precisa decidir como responder ao pedido de compartilhamento de dados de outro cliente.",
                "prompt": "Qual é a conduta correta?",
                "options": [
                    {"text": "Recusar o pedido, explicando que o compartilhamento de dados pessoais e informações protegidas por sigilo bancário de outro cliente, sem autorização expressa deste, viola a LGPD e o dever de sigilo aplicável à instituição.", "isBest": True, "feedback": "Correto. O sigilo bancário e a LGPD protegem os dados pessoais e financeiros de cada cliente; compartilhar informações de um cliente com terceiros, sem seu consentimento expresso e sem base legal específica, constitui infração grave, independentemente da relação entre as partes envolvidas."},
                    {"text": "Compartilhar apenas o telefone do outro cliente, já que o extrato de investimentos seria a única informação realmente sigilosa.", "isBest": False, "feedback": "Incorreto. Dados de contato também são dados pessoais protegidos pela LGPD; qualquer compartilhamento sem autorização do titular, seja de contato ou de informações financeiras, é indevido."},
                    {"text": "Compartilhar as informações, pois o cliente solicitante já é correntista da mesma instituição e presumidamente confiável.", "isBest": False, "feedback": "Incorreto. Ser cliente da instituição não confere a ninguém o direito de acessar dados pessoais e financeiros de terceiros; a proteção de dados é individual e depende de autorização do próprio titular."},
                ],
            },
            {
                "situation": "O cliente insiste, afirmando que, se o assessor não ajudar, ele vai reclamar formalmente e ameaça encerrar a conta na instituição.",
                "prompt": "Qual deve ser a postura do assessor diante dessa pressão?",
                "options": [
                    {"text": "Manter a recusa de forma cordial e firme, reforçar os motivos legais e regulatórios da negativa, e orientar o cliente sobre os canais formais e legítimos disponíveis (como via judicial, se aplicável) para resolver a pendência com o ex-sócio.", "isBest": True, "feedback": "Correto. A pressão ou ameaça do cliente não altera a obrigação legal de sigilo; o profissional deve manter a recusa com transparência sobre os motivos e orientar sobre vias legítimas para a resolução do conflito entre as partes, sem comprometer a proteção de dados de terceiros."},
                    {"text": "Ceder ao pedido para evitar o encerramento da conta, já que a retenção do cliente seria prioridade sobre qualquer outra norma.", "isBest": False, "feedback": "Incorreto. Nenhuma meta comercial ou risco de perda de cliente justifica a violação do sigilo bancário e da LGPD."},
                    {"text": "Repassar apenas parte das informações solicitadas, como forma de meio-termo para acalmar o cliente sem resolver totalmente o pedido.", "isBest": False, "feedback": "Incorreto. Qualquer compartilhamento parcial de dados sem autorização do titular configura violação, não havendo meio-termo aceitável nesse tipo de situação."},
                ],
            },
            {
                "situation": "Diante da recusa, o cliente registra uma reclamação formal contra o assessor, alegando 'falta de cooperação'.",
                "prompt": "Qual deve ser a conduta da instituição ao analisar essa reclamação?",
                "options": [
                    {"text": "Analisar a reclamação e confirmar que a conduta do assessor foi correta e alinhada às normas de proteção de dados e sigilo bancário, documentando o caso e, se necessário, esclarecendo ao cliente reclamante os fundamentos legais da recusa.", "isBest": True, "feedback": "Correto. A instituição deve avaliar a reclamação com base nas normas aplicáveis, reconhecendo que a recusa do assessor em compartilhar dados de terceiros sem autorização foi a conduta regulatoriamente correta, e comunicar isso de forma transparente ao cliente reclamante."},
                    {"text": "Orientar o assessor a atender pedidos semelhantes no futuro, para reduzir o volume de reclamações desse tipo.", "isBest": False, "feedback": "Incorreto. Orientar o atendimento de pedidos que violam sigilo bancário e LGPD para reduzir reclamações contraria frontalmente a regulamentação e exporia a instituição a risco legal e reputacional."},
                    {"text": "Aplicar advertência ao assessor, presumindo que a reclamação do cliente automaticamente indica falha no atendimento.", "isBest": False, "feedback": "Incorreto. A reclamação deve ser analisada com base na conduta efetivamente exigida pela regulamentação; presumir falha apenas pela existência da reclamação, sem essa análise, seria incorreto e penalizaria uma conduta adequada."},
                ],
            },
        ],
    },

    {
        "theme": REL,
        "title": "Cliente pede dica com base em informação de bastidores de uma empresa",
        "intro": "Durante uma reunião, Cláudio, cliente investidor, conta que um amigo que trabalha no departamento financeiro de uma companhia aberta lhe revelou, em confidência, que o resultado trimestral 'vai surpreender positivamente o mercado', ainda não divulgado, e pede a opinião do assessor sobre comprar ações dessa empresa agora.",
        "steps": [
            {
                "situation": "Cláudio pergunta se deve aproveitar a informação do amigo para comprar ações antes da divulgação do resultado.",
                "prompt": "Qual deve ser a orientação do assessor?",
                "options": [
                    {"text": "Alertar Cláudio de que negociar com base em informação relevante ainda não divulgada ao mercado, obtida de fonte privilegiada, configura uso indevido de informação privilegiada (insider trading), sendo uma infração penal e administrativa grave, e desaconselhar totalmente a operação nesses termos.", "isBest": True, "feedback": "Correto. A negociação com base em informação relevante ainda não divulgada publicamente, mesmo obtida indiretamente por meio de terceiros, configura insider trading (art. 27-D da Lei 6.385/76), com sanções penais e administrativas para quem negocia e, potencialmente, para quem repassa a informação."},
                    {"text": "Orientar Cláudio a comprar uma quantidade moderada de ações, já que a informação foi obtida de forma informal e não diretamente da empresa.", "isBest": False, "feedback": "Incorreto. A forma como a informação foi obtida (mesmo de modo informal, por meio de um amigo) não descaracteriza o uso indevido de informação privilegiada; o que importa é o caráter relevante e não público da informação."},
                    {"text": "Sugerir que Cláudio aguarde apenas um dia após a conversa antes de comprar, para reduzir o risco de ser identificado.", "isBest": False, "feedback": "Incorreto. O simples decurso de um curto período não elimina o caráter de uso de informação privilegiada enquanto a informação relevante não for divulgada publicamente ao mercado."},
                ],
            },
            {
                "situation": "Cláudio argumenta que 'todo mundo faz isso' e pergunta se o assessor pelo menos poderia processar a ordem de compra sem fazer perguntas.",
                "prompt": "Qual deve ser a conduta do assessor?",
                "options": [
                    {"text": "Recusar-se a processar a ordem nessas condições, reiterar os riscos legais da conduta para o próprio Cláudio e, conforme as políticas internas de compliance, avaliar a necessidade de reportar o episódio.", "isBest": True, "feedback": "Correto. O profissional certificado deve agir com integridade e não pode simplesmente executar uma operação da qual tem ciência de que está fundamentada em informação privilegiada; a política interna de compliance deve ser seguida, o que pode incluir o registro e a avaliação do episódio."},
                    {"text": "Processar a ordem sem perguntas, pois a responsabilidade de verificar a legalidade da informação seria exclusivamente do cliente.", "isBest": False, "feedback": "Incorreto. O profissional que processa uma operação com conhecimento de que ela se baseia em informação privilegiada pode ser responsabilizado por participação na infração, não sendo isento apenas por 'não perguntar'."},
                    {"text": "Processar a ordem, mas por um valor menor do que o solicitado, como forma de reduzir parcialmente o risco.", "isBest": False, "feedback": "Incorreto. Reduzir o valor da operação não elimina a ilegalidade da conduta; a orientação correta é não viabilizar a operação nessas condições, independentemente do valor envolvido."},
                ],
            },
            {
                "situation": "Diante da recusa, Cláudio decide não insistir, mas pergunta se poderia, ao menos, comentar a informação com outros amigos investidores.",
                "prompt": "Qual é a orientação tecnicamente correta a ser dada a Cláudio?",
                "options": [
                    {"text": "Orientar que repassar a informação privilegiada a terceiros também pode configurar infração (tipificada como uso indevido de informação privilegiada por quem a repassa e por quem eventualmente negocia com base nela), devendo Cláudio evitar compartilhar ou usar essa informação até sua divulgação pública.", "isBest": True, "feedback": "Correto. A regulamentação sobre uso indevido de informação privilegiada não se limita a quem negocia diretamente; repassar informação relevante não divulgada a terceiros que venham a negociar com base nela também pode configurar infração, alcançando quem a compartilha."},
                    {"text": "Informar que compartilhar a informação é permitido, desde que Cláudio não negocie pessoalmente as ações.", "isBest": False, "feedback": "Incorreto. O simples repasse da informação privilegiada a terceiros também pode configurar infração, independentemente de Cláudio negociar pessoalmente ou não."},
                    {"text": "Sugerir que Cláudio compartilhe a informação apenas com familiares próximos, pois nesse caso não haveria qualquer restrição.", "isBest": False, "feedback": "Incorreto. Não há exceção para compartilhamento com familiares; a divulgação de informação relevante ainda não pública a qualquer terceiro pode configurar infração."},
                ],
            },
        ],
    },

    {
        "theme": REL,
        "title": "Cliente desorganizado pede ajuda com orçamento pessoal",
        "intro": "Vanessa, 29 anos, relata ao assessor que não sabe exatamente quanto gasta por mês, tem dívidas em cartão de crédito e nunca fez um levantamento de seu patrimônio, pedindo orientação para 'organizar a vida financeira'.",
        "steps": [
            {
                "situation": "Vanessa pergunta por onde deveria começar a organizar suas finanças, já que sente que 'o dinheiro simplesmente desaparece' todo mês.",
                "prompt": "Qual é a orientação inicial mais adequada, segundo o processo de planejamento financeiro pessoal?",
                "options": [
                    {"text": "Orientar Vanessa a levantar detalhadamente suas receitas e despesas mensais (fluxo de caixa) e montar um balanço patrimonial pessoal simples, listando bens, direitos e dívidas, antes de qualquer recomendação de produto de investimento.", "isBest": True, "feedback": "Correto. O primeiro passo do planejamento financeiro pessoal é o diagnóstico da situação atual, por meio do levantamento do fluxo de caixa (receitas e despesas) e do balanço patrimonial pessoal (ativos e passivos), o que permite identificar a origem dos problemas antes de qualquer recomendação de produto."},
                    {"text": "Recomendar imediatamente a aplicação de qualquer valor disponível em um fundo de investimento, para 'já começar a investir'.", "isBest": False, "feedback": "Incorreto. Recomendar produtos de investimento antes de organizar o fluxo de caixa e entender as dívidas existentes ignora a etapa de diagnóstico financeiro e pode ser inadequado, especialmente havendo dívidas de alto custo em aberto."},
                    {"text": "Sugerir que Vanessa contrate imediatamente um cartão de crédito com limite maior, para ter mais controle sobre os gastos.", "isBest": False, "feedback": "Incorreto. Aumentar o limite de crédito sem antes organizar o orçamento tende a agravar o problema de desorganização financeira relatado por Vanessa, em vez de solucioná-lo."},
                ],
            },
            {
                "situation": "Após o levantamento, verifica-se que Vanessa tem uma dívida rotativa no cartão de crédito, com juros elevados, e também alguma capacidade de poupança mensal.",
                "prompt": "Qual deve ser a prioridade na orientação a Vanessa?",
                "options": [
                    {"text": "Priorizar a quitação ou renegociação da dívida do cartão de crédito rotativo, dado o custo elevado dos juros, antes de direcionar recursos para investimentos, já que dificilmente algum investimento renderá mais do que o custo dessa dívida.", "isBest": True, "feedback": "Correto. O cartão de crédito rotativo está entre as modalidades de crédito mais caras do mercado; via de regra, nenhum investimento disponível rende o suficiente para compensar esse custo, de modo que a prioridade financeira deve ser eliminar ou renegociar essa dívida antes de iniciar novos investimentos."},
                    {"text": "Orientar Vanessa a manter a dívida do cartão como está e direcionar toda a capacidade de poupança para um fundo de ações, buscando rentabilidade superior aos juros do rotativo.", "isBest": False, "feedback": "Incorreto. Os juros do cartão rotativo tendem a ser muito superiores ao retorno esperado de qualquer investimento em condições normais de mercado, tornando essa estratégia financeiramente prejudicial a Vanessa."},
                    {"text": "Sugerir que Vanessa ignore a dívida por ora e foque em formar uma reserva de emergência equivalente a 12 meses de despesas antes de tratar do cartão de crédito.", "isBest": False, "feedback": "Incorreto. Adiar o tratamento de uma dívida de alto custo para formar uma reserva de emergência excessivamente elevada não é eficiente; a prioridade nesse cenário é reduzir o passivo mais caro."},
                ],
            },
            {
                "situation": "Depois de quitar a dívida do cartão, Vanessa pergunta como poderia acompanhar sua evolução financeira ao longo do tempo, para não repetir os mesmos erros.",
                "prompt": "Qual orientação contribui mais para a sustentabilidade do planejamento financeiro de Vanessa?",
                "options": [
                    {"text": "Sugerir a atualização periódica do orçamento e do balanço patrimonial pessoal (por exemplo, mensal ou trimestral), acompanhando indicadores como taxa de poupança e evolução do patrimônio líquido, ajustando o plano conforme mudanças na vida de Vanessa.", "isBest": True, "feedback": "Correto. O planejamento financeiro pessoal é um processo contínuo; o acompanhamento periódico do orçamento, do patrimônio líquido e da taxa de poupança permite identificar desvios e ajustar o plano ao longo do tempo, sustentando os resultados alcançados."},
                    {"text": "Informar que, uma vez organizado o orçamento e quitada a dívida, não é mais necessário qualquer acompanhamento futuro.", "isBest": False, "feedback": "Incorreto. O planejamento financeiro pessoal exige acompanhamento contínuo, já que mudanças na renda, despesas e objetivos de vida podem exigir ajustes periódicos ao plano."},
                    {"text": "Recomendar que Vanessa pare de acompanhar detalhes financeiros e apenas confie que seus gastos permanecerão controlados.", "isBest": False, "feedback": "Incorreto. A ausência de acompanhamento tende a repetir o padrão de desorganização relatado inicialmente por Vanessa, contrariando o objetivo de sustentabilidade financeira de longo prazo."},
                ],
            },
        ],
    },

    {
        "theme": REL,
        "title": "Pressão por produto de maior comissão em conflito com o perfil",
        "intro": "O gerente regional pede a um assessor que priorize a oferta de um fundo estruturado de maior comissão para bater a meta do mês, mesmo para clientes com perfil conservador, que normalmente não teriam esse produto recomendado.",
        "steps": [
            {
                "situation": "O assessor está atendendo Sônia, cliente conservadora, que não tem qualquer tolerância a perdas de capital declarada em seu perfil de suitability.",
                "prompt": "Qual deve ser a conduta do assessor diante da pressão do gerente para oferecer o fundo estruturado de maior comissão a Sônia?",
                "options": [
                    {"text": "Não recomendar o fundo estruturado a Sônia, já que ele é incompatível com o perfil conservador identificado no processo de suitability, priorizando a adequação ao cliente sobre a meta comercial e o incentivo de remuneração.", "isBest": True, "feedback": "Correto. O dever de adequação (suitability) exige que a recomendação de produtos esteja alinhada ao perfil de risco do cliente, independentemente de metas comerciais ou de remuneração diferenciada. Pressões internas não justificam o descumprimento desse dever."},
                    {"text": "Recomendar o fundo estruturado a Sônia, já que a orientação do gerente regional deve prevalecer sobre a análise individual de perfil do cliente.", "isBest": False, "feedback": "Incorreto. Nenhuma orientação interna de meta comercial pode se sobrepor ao dever regulatório de adequação do produto ao perfil do cliente; o profissional certificado é responsável por essa análise, independentemente de pressões hierárquicas."},
                    {"text": "Apresentar o fundo estruturado como se fosse adequado ao perfil de Sônia, omitindo os riscos envolvidos, para atender à meta sem gerar desconforto.", "isBest": False, "feedback": "Incorreto. Omitir riscos e apresentar informação distorcida sobre a adequação do produto ao perfil do cliente constitui grave violação ética e regulatória, além de configurar prática abusiva."},
                ],
            },
            {
                "situation": "O gerente insiste, argumentando que Sônia poderia simplesmente assinar um termo de ciência de risco, o que 'resolveria' juridicamente a questão da adequação.",
                "prompt": "Qual é a orientação tecnicamente correta sobre esse argumento?",
                "options": [
                    {"text": "Explicar que um termo de ciência de risco não substitui o dever de adequação (suitability); mesmo com a assinatura desse termo, a recomendação de um produto incompatível com o perfil do cliente permanece inadequada e sujeita a questionamento regulatório.", "isBest": True, "feedback": "Correto. A assinatura de termos de ciência de risco não afasta a responsabilidade da instituição e do profissional quanto à adequação do produto ao perfil do cliente; o dever de suitability é uma exigência regulatória que não pode ser contornada por documentos de aceite unilateral do risco."},
                    {"text": "Concordar que, com o termo de ciência de risco assinado, a operação se torna plenamente adequada e sem qualquer risco regulatório.", "isBest": False, "feedback": "Incorreto. O termo de ciência de risco não converte uma recomendação inadequada ao perfil em uma recomendação adequada; a análise de suitability continua sendo exigida e prevalece."},
                    {"text": "Sugerir que o termo seja assinado sem que Sônia leia o conteúdo, para agilizar o processo comercial.", "isBest": False, "feedback": "Incorreto. Além de não resolver a questão de adequação, induzir o cliente a assinar documentos sem compreensão do conteúdo constitui prática antiética e potencialmente abusiva."},
                ],
            },
            {
                "situation": "O assessor decide não recomendar o produto a Sônia e comunica sua decisão ao gerente, que ameaça registrar uma avaliação de desempenho negativa por 'baixa aderência às metas'.",
                "prompt": "Qual é o procedimento mais adequado para o assessor nessa situação?",
                "options": [
                    {"text": "Documentar a análise de suitability que fundamentou a não recomendação e, se necessário, reportar a pressão comercial indevida aos canais de compliance ou ouvidoria da instituição, preservando a conduta ética adotada.", "isBest": True, "feedback": "Correto. Documentar a análise técnica que fundamentou a decisão protege o profissional e demonstra o cumprimento do dever de adequação; diante de pressão indevida para violar normas de suitability, o reporte aos canais internos de compliance ou ouvidoria é a conduta adequada."},
                    {"text": "Ceder à pressão na próxima oportunidade com outro cliente conservador, para equilibrar a avaliação de desempenho.", "isBest": False, "feedback": "Incorreto. Ceder à pressão para recomendar produtos inadequados ao perfil de qualquer cliente, ainda que por motivos de avaliação de desempenho, viola o dever de suitability e as normas éticas aplicáveis."},
                    {"text": "Não fazer nada e aceitar silenciosamente a avaliação negativa, sem documentar ou relatar a situação a qualquer área interna.", "isBest": False, "feedback": "Incorreto. A ausência de documentação e de reporte da pressão comercial indevida deixa o profissional mais vulnerável e não contribui para a correção da prática inadequada dentro da instituição."},
                ],
            },
        ],
    },

    {
        "theme": REL,
        "title": "Cliente quer investir tudo sem entender os riscos",
        "intro": "Diego, 26 anos, recebeu uma herança de R$ 200.000 e pede ao assessor para aplicar 'o mais rápido possível' 100% do valor em um fundo de ações recomendado por um influenciador nas redes sociais, sem nunca ter investido antes.",
        "steps": [
            {
                "situation": "Diego demonstra pressa e afirma que 'já decidiu' investir tudo no fundo de ações indicado, sem querer detalhar mais informações sobre sua situação financeira.",
                "prompt": "Qual deve ser a conduta do assessor diante desse pedido?",
                "options": [
                    {"text": "Explicar que, antes de qualquer recomendação ou execução, é necessário aplicar o processo de suitability, avaliando o conhecimento, a experiência, a situação financeira e os objetivos de Diego, mesmo que isso implique não atender ao pedido imediatamente como solicitado.", "isBest": True, "feedback": "Correto. O processo de suitability é uma exigência regulatória que deve preceder qualquer recomendação ou execução de investimento, especialmente para um investidor sem experiência prévia que pretende concentrar a totalidade de um recurso relevante em um único produto de risco elevado."},
                    {"text": "Executar a operação exatamente como solicitada por Diego, já que a decisão final de investimento é sempre do cliente.", "isBest": False, "feedback": "Incorreto. Embora a decisão final seja do cliente, a instituição e o profissional certificado têm o dever de avaliar a adequação do produto ao perfil antes de viabilizar a operação, especialmente diante de sinais claros de desconhecimento dos riscos envolvidos."},
                    {"text": "Sugerir que Diego aplique ainda mais rapidamente, aproveitando a 'oportunidade' indicada pelo influenciador, para não perder o momento de mercado.", "isBest": False, "feedback": "Incorreto. Incentivar pressa em uma decisão de investimento relevante, sem avaliação de perfil, contraria o dever de zelar pelo melhor interesse do cliente e o processo de suitability."},
                ],
            },
            {
                "situation": "Após alguma resistência, Diego aceita responder ao questionário de suitability, que resulta em perfil moderado, e insiste em concentrar 100% da herança no fundo de ações indicado.",
                "prompt": "Qual é a orientação tecnicamente correta diante desse resultado?",
                "options": [
                    {"text": "Alertar Diego, de forma clara e documentada, que a concentração de 100% do patrimônio em um único fundo de ações não é compatível com o perfil moderado identificado, recomendando diversificação entre classes de ativos e horizontes.", "isBest": True, "feedback": "Correto. Mesmo diante do desejo do cliente, o dever de adequação exige que o profissional alerte sobre o desenquadramento entre a operação pretendida (concentração total em ações) e o perfil moderado identificado, orientando sobre diversificação e documentando o alerta."},
                    {"text": "Executar a operação sem qualquer alerta, já que o perfil moderado permite qualquer nível de exposição a ações.", "isBest": False, "feedback": "Incorreto. Um perfil moderado não implica que a concentração de 100% do patrimônio em um único fundo de ações seja adequada; a diversificação segue sendo recomendável e a ausência de alerta contraria o dever de suitability."},
                    {"text": "Alterar o resultado do questionário de suitability para um perfil mais arrojado, de forma a compatibilizá-lo com o pedido de Diego.", "isBest": False, "feedback": "Incorreto. Alterar respostas ou resultados do questionário de suitability para justificar uma operação pretendida pelo cliente é uma grave violação ética e regulatória do processo de adequação."},
                ],
            },
            {
                "situation": "Diante do alerta, Diego reconhece o risco, mas ainda decide, de forma consciente e informada, investir 60% da herança no fundo de ações e diversificar o restante conforme orientação do assessor.",
                "prompt": "Qual deve ser a conduta final do assessor?",
                "options": [
                    {"text": "Documentar formalmente o alerta dado e a decisão final e informada de Diego, executando a operação conforme a nova alocação (60% no fundo de ações e o restante diversificado), respeitando a autonomia do cliente após o processo de adequação e alerta devidamente cumprido.", "isBest": True, "feedback": "Correto. Uma vez cumprido o dever de suitability, com alerta claro sobre os riscos e registro documental da orientação, a decisão final de alocação cabe ao cliente. O assessor deve executar a operação conforme a decisão informada e consciente de Diego, com a devida documentação do processo."},
                    {"text": "Recusar-se a executar qualquer parte da operação, mesmo após o alerta devidamente comunicado e a decisão consciente do cliente.", "isBest": False, "feedback": "Incorreto. Uma vez cumprido o dever de informar e alertar sobre os riscos, e diante de uma decisão consciente e informada do cliente dentro de limites razoáveis, não há motivo para recusar integralmente a execução da operação."},
                    {"text": "Executar a operação sem registrar o alerta dado anteriormente, para simplificar o processo.", "isBest": False, "feedback": "Incorreto. A ausência de documentação do alerta e do processo de adequação compromete a rastreabilidade da conduta do profissional e da instituição, sendo uma prática inadequada mesmo que a operação final seja executada corretamente."},
                ],
            },
        ],
    },

    {
        "theme": REL,
        "title": "Cliente vítima de tentativa de golpe pergunta como proceder",
        "intro": "Márcia liga em pânico para o assessor contando que recebeu uma mensagem, supostamente da instituição financeira, pedindo para confirmar seus dados e uma senha de acesso ao aplicativo para 'liberar uma transferência suspeita', e pergunta se deve responder.",
        "steps": [
            {
                "situation": "Márcia ainda não respondeu à mensagem suspeita e pergunta ao assessor o que deve fazer imediatamente.",
                "prompt": "Qual é a orientação correta e imediata a ser dada a Márcia?",
                "options": [
                    {"text": "Orientar Márcia a não responder à mensagem, não clicar em links recebidos e não informar senhas, códigos de acesso ou dados sensíveis por telefone, SMS ou aplicativos de mensagem, reforçando que a instituição nunca solicita esse tipo de informação por esses canais.", "isBest": True, "feedback": "Correto. Práticas de segurança da informação recomendam nunca compartilhar senhas, códigos de autenticação ou dados sensíveis por canais não oficiais; instituições financeiras não solicitam esse tipo de dado por mensagens ou ligações, sendo esse pedido um forte indício de tentativa de fraude (phishing/engenharia social)."},
                    {"text": "Orientar Márcia a responder à mensagem confirmando os dados solicitados, para 'evitar problemas' com a suposta transferência suspeita.", "isBest": False, "feedback": "Incorreto. Responder e fornecer dados sensíveis é exatamente o objetivo de uma fraude por engenharia social; essa orientação exporia Márcia a risco real de golpe financeiro."},
                    {"text": "Informar que a instituição não tem qualquer responsabilidade sobre esse tipo de mensagem e que Márcia deve resolver o problema sozinha.", "isBest": False, "feedback": "Incorreto. Embora a fraude possa ter origem externa, o assessor deve orientar ativamente o cliente sobre a conduta de segurança adequada e sobre os canais oficiais da instituição para verificação e suporte."},
                ],
            },
            {
                "situation": "Márcia conta que, antes de ligar para o assessor, já havia informado por engano o código recebido por SMS em um link que acessou, e teme que sua conta tenha sido comprometida.",
                "prompt": "Qual deve ser a orientação imediata do assessor nesse cenário?",
                "options": [
                    {"text": "Orientar Márcia a contatar imediatamente os canais oficiais de segurança da instituição para bloquear o acesso, trocar senhas e verificar movimentações na conta, além de registrar um boletim de ocorrência sobre a tentativa de fraude.", "isBest": True, "feedback": "Correto. Diante da suspeita de comprometimento de dados de acesso, a prioridade é contatar imediatamente os canais oficiais de segurança da instituição para bloqueio preventivo, troca de credenciais e verificação de eventuais movimentações indevidas, além do registro formal do incidente."},
                    {"text": "Dizer a Márcia que, como o código já foi informado, não há mais nada a ser feito e que ela deve apenas aguardar para ver se ocorre algum problema.", "isBest": False, "feedback": "Incorreto. Existem medidas imediatas e eficazes a serem tomadas (bloqueio de acesso, troca de senha, verificação de movimentações) que podem reduzir ou evitar prejuízos, mesmo após o compartilhamento indevido do código."},
                    {"text": "Pedir que Márcia informe ao próprio assessor, por mensagem de texto, sua senha atual, para que ele verifique pessoalmente se há problemas na conta.", "isBest": False, "feedback": "Incorreto. Nenhum profissional da instituição deve solicitar senhas do cliente por qualquer canal; essa conduta reproduziria a mesma prática de risco da tentativa de fraude relatada."},
                ],
            },
            {
                "situation": "Após o bloqueio preventivo, verifica-se que houve uma tentativa de transferência indevida, mas que foi impedida a tempo pelos controles da instituição. Márcia pergunta como evitar cair em fraudes semelhantes no futuro.",
                "prompt": "Qual orientação de prevenção é mais adequada a ser dada a Márcia?",
                "options": [
                    {"text": "Orientar Márcia a sempre validar solicitações suspeitas diretamente pelos canais oficiais da instituição (aplicativo oficial, central telefônica conhecida), nunca compartilhar senhas ou códigos recebidos por mensagem, e manter atenção a sinais comuns de fraude, como urgência excessiva e pedidos de dados sensíveis.", "isBest": True, "feedback": "Correto. A prevenção eficaz contra fraudes de engenharia social envolve validar qualquer solicitação suspeita diretamente pelos canais oficiais, nunca compartilhar senhas/códigos por mensagens, e reconhecer padrões comuns de golpe, como urgência artificial e pedidos de informações sensíveis."},
                    {"text": "Recomendar que Márcia compartilhe sua senha apenas com pessoas de confiança, como familiares, para casos de emergência.", "isBest": False, "feedback": "Incorreto. Senhas e dados de acesso não devem ser compartilhados com ninguém, nem mesmo familiares, pois isso amplia o risco de uso indevido e compromete a segurança da conta."},
                    {"text": "Informar que, uma vez que a instituição tem controles antifraude eficientes, Márcia não precisa adotar qualquer cuidado adicional no futuro.", "isBest": False, "feedback": "Incorreto. Os controles institucionais reduzem o risco, mas não eliminam a necessidade de o próprio cliente adotar práticas de segurança, já que muitas fraudes dependem da ação da vítima ao fornecer voluntariamente dados sensíveis."},
                ],
            },
        ],
    },

]
