# -*- coding: utf-8 -*-
"""
Conteudo das 4 paginas de demonstracao do M1, escrito PARA O ALUNO.

Regra de voz: nada aqui pode ser direcao de cena. Se a frase so faz sentido
dita pelo instrutor para a turma ("pergunte a sala", "espere o silencio",
"anote no quadro", "se travar, faca X"), ela nao entra. Vai para o roteiro
interno, fora do site publico.
"""

P_COTACAO = """Sou coordenador de Compras na Gráfica Aurora, indústria gráfica de médio
porte. Anexei o mapa de cotação da OS 2481, exportado do sistema: são 26
insumos cotados com 4 fornecedores, 104 linhas.
Hoje é 16/07/2026 e essa OS entra em máquina em 22/07/2026.

O arquivo vem sujo, como todo export: duas linhas de cabeçalho mescladas
antes da tabela, uma coluna com espaço no nome, data em três formatos,
valor ora como número ora como texto com vírgula, e uma linha em branco
no meio. Normalize antes de analisar e me diga o que normalizou.

Quatro coisas que eu preciso que você trate, porque são as que derrubam
a comparação e ninguém vê passando o olho:
- frete FOB não está no valor unitário, e muda o total
- condição à vista com desconto muda o total
- a unidade não é a mesma em todo mundo. Se alguém cotou em caixa
  fechada, converta para a unidade da minha quantidade antes de somar,
  e me avise quando isso acontecer
- se um fornecedor deixou de cotar algum item, o total dele não é
  comparável com o dos outros. Diga isso na cara, não no rodapé

TAREFA
Gere um Artifact HTML de uma página só, para eu imprimir e levar:

1. A recomendação em uma frase, no topo, com o valor e a data de entrega
2. Os quatro fornecedores lado a lado: total real (já com frete, desconto
   e unidade convertida), prazo, data de chegada, e quantos itens faltou
   cotar
3. Quem não entrega a tempo, e por quantos dias
4. Quem não dá para comparar, e por quê
5. Se dividir o pedido entre dois fornecedores sair melhor, mostre a conta
6. As perguntas que eu preciso fazer antes de fechar

ESTILO
Documento sóbrio de uma página. Fundo off-white, sem dark mode, sem
gradiente. Vermelho só para o que atrasa. Número grande onde eu preciso
bater o olho e decidir.

ANTES DE GERAR
Confirme comigo em 3 bullets: quantas linhas úteis você achou, como
normalizou, e que critério usou para recomendar. Espere meu OK."""

P_CORRECOES = """E o prazo de entrega? Considera que hoje é 16/07/2026 e a produção
entra em máquina em 22/07.

O frete do Delta e da Cearapel é FOB, não está no valor unitário.
Refaz a conta.

Repara que nem todo mundo cotou os 26 itens. Isso muda a comparação."""

P_PAUTA = """Anexei o relatório de OS em produção da Gráfica Aurora, exportado do
sistema hoje, 16/07/2026. São 120 linhas.

O que eu preciso: uma pauta para a reunião de produção de amanhã às 8h,
em uma página, que eu possa imprimir e levar.

O que é &quot;pronto&quot;: tem as OS atrasadas em ordem de atraso, a carga de
cada máquina, e no máximo três decisões que dependem de mim, coordenador
de PCP.

Restrições: o arquivo vem sujo do ERP, com cabeçalho mesclado, data em
três formatos, status em quatro caixas e tiragem ora número ora texto.
Normalize antes de analisar. Considere atrasada pela data de prazo,
nunca pelo campo de status.

Na dúvida: se algum dado estiver em branco, repetido ou contraditório,
pare e me pergunte. Não invente e não chute."""

P_REGRAS = """Sou coordenador de PCP na Gráfica Aurora, indústria gráfica de médio porte.

Temos 6 máquinas: Offset 1, Offset 2, Offset 3, Flexo 1, Flexo 2 e
Digital 1. Offset é tiragem alta e prazo mais longo. Flexo é rótulo e
prazo curto. Digital é tiragem pequena e prazo curto.

Quando eu pedir &quot;a situação das OS&quot;, entenda: as ordens em produção, o
que está atrasado e o que vence nos próximos três dias.

OS atrasada é a que passou da data de prazo e não foi entregue. Nunca use
o campo de status para isso: ele é preenchido à mão e não é confiável.

O mesmo cliente às vezes aparece com dois nomes no relatório. Agrupe antes
de contar.

Sempre responda em tabela, data em DD/MM/AAAA, sem introdução e sem
&quot;espero ter ajudado&quot;.

Termine sempre apontando o que precisa da minha decisão hoje.

Se faltar dado, pergunte. Não invente."""

P_SKILL = """---
name: fechar-cotacao
description: Use quando o usuário anexar propostas de fornecedores e pedir
  comparação, análise de cotação ou recomendação de compra. Também quando
  ele disser &quot;fecha essa cotação&quot; ou &quot;qual fornecedor eu escolho&quot;.
---

# Como a Gráfica Aurora fecha uma cotação

1. Monte a tabela com as propostas em preço por milheiro, nunca em preço
   total, porque as tiragens vêm diferentes.
2. Confira a unidade de cada linha. Se alguém cotou em caixa fechada,
   converta antes de somar.
3. Some frete e prazo de pagamento ao custo. Proposta mais barata com
   prazo pior costuma sair mais cara.
4. Se um fornecedor não cotou todos os itens, diga isso antes de comparar
   qualquer total.
5. Feche com uma recomendação em uma frase e o motivo dela.
6. Se faltar algum dado numa proposta, pare e pergunte. Não estime."""


AULAS = {
    # ══════════════════════════════════════════════════════ AULA 1.1
    "a1-ecossistema-e-fisica": dict(
        aula="1.1",
        title="Demonstração · Aula 1.1",
        desc="O mesmo pedido feito de dois jeitos, passo a passo, no Claude Chat: "
             "o pedido curto que não fecha e o pedido que já vem pronto.",
        h1="O mesmo pedido, de dois jeitos",
        lead=[
            "Tudo aqui roda no <strong>Claude Chat, no navegador</strong>. "
            "Você pode refazer sozinho depois, sem instalar nada.",
            "A planilha usada é de <strong>Compras</strong>, um mapa de cotação com "
            "104 linhas. A do seu exercício é de PCP. É de propósito: você vê o "
            "mecanismo acontecer num caso e refaz no seu.",
        ],
        arquivo=("cotacoes-fornecedores.xlsx",
                 "104 linhas de cotação · 4 fornecedores · 26 insumos · "
                 "exportado sujo, de propósito",
                 "cotacoes-fornecedores.xlsx"),
        passos=[
            dict(titulo="O pedido que todo mundo faz", blocos=[
                ("fazer", "Conversa nova, anexa a planilha de cotação e faz o pedido "
                          "mais curto possível. É assim que a pergunta chega no dia a dia."),
                ("prompt", ("pedido curto · uma linha",
                            "Analisa essas cotações e me diz qual fornecedor a gente deve escolher.",
                            True)),
                ("tela", "Sai uma resposta organizada, que escolhe um fornecedor e "
                         "defende a escolha com segurança."),
                ("repare", "Ela escolheu <b>pelo preço</b>. Não olhou prazo de entrega, "
                           "não olhou frete, e não conferiu se os quatro fornecedores "
                           "cotaram os 26 itens."),
            ]),
            dict(titulo="O que essa resposta não respondeu", blocos=[
                ("fazer", "São 104 linhas de cotação. Antes de corrigir, vale saber "
                          "exatamente o que ficou de fora, porque cada item da lista "
                          "abaixo muda a decisão de compra."),
                ("lista", ("O que falta", [
                    "O <b>prazo de entrega</b> de cada fornecedor",
                    "Se o <b>frete está incluso</b> no valor unitário ou não",
                    "A <b>condição de pagamento</b>, que muda o total",
                    "Se <b>todo mundo cotou os 26 itens</b>",
                    "Se <b>dividir o pedido</b> entre dois fornecedores sai melhor",
                ])),
                ("ensina", "Essa lista é o pedido bom. É ela, escrita antes, que faz o "
                           "passo 4 funcionar de primeira."),
            ]),
            dict(titulo="Corrigindo dentro da mesma conversa", blocos=[
                ("fazer", "Três correções, uma por mensagem, sem sair da conversa. "
                          "É o que a maioria faz quando a primeira resposta não serve."),
                ("prompt", ("as três correções · uma por mensagem", P_CORRECOES, False)),
                ("tela", "Já na primeira correção sai o número que interessa: o "
                         "fornecedor mais barato por unidade <b>chega seis dias depois "
                         "de a máquina rodar</b>."),
                ("repare", "Cada resposta melhora um pouco e <b>nenhuma fecha</b>. "
                           "Na terceira ele costuma voltar a falar do mais barato e "
                           "largar o prazo que foi pedido na primeira."),
                ("ensina", "Ele não esqueceu: <b>ele diluiu</b>. Quanto mais conversa "
                           "em cima da mesa, menos peso cada instrução tem. É exatamente "
                           "por isso que a conversa longa piora."),
            ]),
            dict(titulo="O mesmo pedido, só que escrito antes", blocos=[
                ("fazer", "Conversa nova, a mesma planilha, e um pedido que já vem com "
                          "tudo o que estava faltando no passo 2. Ele é longo de "
                          "propósito: <b>é o tamanho de um pedido que não precisa de "
                          "correção.</b>"),
                ("prompt", ("pedido pronto · abra para conferir, ou só copie",
                            P_COTACAO, False)),
                ("repare", "Ele <b>para antes de gerar</b> e confirma o plano em três "
                           "bullets, esperando o OK. São trinta segundos de conferência "
                           "contra um documento inteiro construído em cima de um "
                           "entendimento errado."),
            ]),
            dict(titulo="O que apareceu que ninguém tinha visto", blocos=[
                ("fazer", "Depois do OK, sai o documento de uma página. Com ele vêm "
                          "três achados que estavam escondidos nas 104 linhas."),
                ("lista", ("Os três achados", [
                    "O fornecedor <b>mais barato da lista deixou de cotar cinco itens</b>. "
                    "Aquele total nunca foi comparável com o dos outros",
                    "Um deles cotou a chapa CTP <b>em caixa com dez</b>, e não por "
                    "unidade. Somar direto multiplicaria esse item por dez",
                    "Sobra <b>um único fornecedor</b> que cotou os 26 itens e entrega a "
                    "tempo. E é o mais caro na conta ingênua",
                ])),
                ("ensina", "O mais barato era mais barato <b>porque estava incompleto</b>. "
                           "Uma rodada em vez de cinco, e três coisas que ninguém acharia "
                           "passando o olho numa planilha desse tamanho."),
            ]),
        ],
        fecho=("O que muda daqui para a frente",
               "O pedido curto parece mais rápido: são 11 palavras contra 300. "
               "Só que ele compra cinco rodadas de correção, e ainda deixa passar "
               "o que importa.",
               "Na <strong>seção 05 · Sua vez</strong> você faz as duas conversas com a "
               "planilha de PCP. <strong>A diferença é que agora você sabe por que a "
               "segunda funciona</strong>, em vez de copiar um prompt pronto."),
        rodape='Demonstração da <a href="../">aula 1.1</a> · Gráfica Aurora é uma '
               'indústria gráfica fictícia criada para o treinamento, e nenhum dado '
               'aqui é real',
    ),

    # ══════════════════════════════════════════════════════ AULA 1.2
    "a2-pedir-para-entregar": dict(
        aula="1.2",
        title="Demonstração · Aula 1.2",
        desc="O mesmo arquivo pedido de dois jeitos: a frase curta que devolve um "
             "resumo educado, e os três campos que fazem a primeira resposta já servir.",
        h1="O mesmo arquivo, dois pedidos",
        lead=[
            "A planilha é a mesma da aula 1.1: <strong>120 ordens de serviço</strong> "
            "da Gráfica Aurora, exportadas sujas do sistema.",
            "O que muda entre as duas conversas não é a ferramenta nem o arquivo. "
            "É <strong>o que estava escrito antes de apertar enter</strong>.",
        ],
        arquivo=("pedidos-em-producao.xlsx",
                 "120 ordens de serviço · 9 colunas · a mesma da aula 1.1",
                 "../../a1-ecossistema-e-fisica/exercicio/pedidos-em-producao.xlsx"),
        passos=[
            dict(titulo="O pedido de uma frase", blocos=[
                ("fazer", "Conversa nova, anexa a planilha e manda o pedido mais curto "
                          "que existe."),
                ("prompt", ("pedido curto", "Resuma esses pedidos.", True)),
                ("tela", "Um resumo educado: quantos pedidos existem, que alguns estão "
                         "atrasados, como estão distribuídos entre as máquinas."),
                ("repare", "Está tudo certo, e <b>não decide nada</b>. Para saber o que "
                           "fazer amanhã de manhã, você ainda teria que abrir a planilha "
                           "e olhar linha por linha."),
            ]),
            dict(titulo="Os três campos que faltaram", blocos=[
                ("fazer", "Numa OS de impressão ninguém deixa campo em branco. Um pedido "
                          "bem feito tem os mesmos três campos, e a diferença é só que "
                          "quase todo mundo manda sem preencher."),
                ("lista", ("Os três campos", [
                    "<b>O que é &quot;pronto&quot;</b> · em que ponto você considera a "
                    "resposta entregue",
                    "<b>Quais são as restrições</b> · o que ele precisa respeitar, "
                    "inclusive a sujeira do arquivo",
                    "<b>O que fazer na dúvida</b> · o que ele faz quando falta um dado",
                ])),
                ("ensina", "O terceiro é o que quase sempre fica vazio, e é o único que "
                           "muda o <b>comportamento</b> dele em vez da formatação da "
                           "saída. Sem ele, falta de dado vira número inventado."),
            ]),
            dict(titulo="O mesmo arquivo, com os três campos preenchidos", blocos=[
                ("fazer", "Conversa nova, a mesma planilha, e o pedido com os três "
                          "campos escritos. Repare que ele não usa nenhuma palavra "
                          "técnica: é a linguagem de uma OS."),
                ("prompt", ("pedido com os três campos", P_PAUTA, False)),
                ("tela", "Uma rodada. Sai a pauta de uma página, pronta para imprimir."),
                ("repare", "A resposta não ficou &quot;melhor&quot;. <b>O caminho até ela "
                           "ficou muito menor.</b> Essa é a conta que interessa: não a "
                           "qualidade da resposta, e sim quantas mensagens até ela servir."),
            ]),
            dict(titulo="O campo &quot;na dúvida&quot; valendo", blocos=[
                ("fazer", "A mesma planilha, com uma data de prazo apagada de propósito, "
                          "e exatamente o mesmo pedido."),
                ("tela", "Ele não preenche a data sozinho. Para e pergunta qual é."),
                ("repare", "Sem o terceiro campo, ele <b>estima</b> a data e segue. "
                           "O número entra na pauta, vai para a reunião, e ninguém "
                           "descobre que foi suposto."),
                ("ensina", "Os dois primeiros campos melhoram a resposta. O terceiro "
                           "evita um erro que só aparece depois, quando já virou decisão."),
            ]),
        ],
        fecho=("O que muda daqui para a frente",
               "Pedido bom não é talento de quem escreve prompt. São três campos "
               "preenchidos antes de mandar.",
               "Na <strong>seção 05 · Sua vez</strong> você preenche os três campos para "
               "uma tarefa da sua rotina e roda. <strong>O gabarito é referência, não "
               "resposta certa:</strong> o seu vai ser diferente, e tudo bem."),
        rodape='Demonstração da <a href="../">aula 1.2</a> · Gráfica Aurora é uma '
               'indústria gráfica fictícia criada para o treinamento',
    ),

    # ══════════════════════════════════════════════════════ AULA 1.3
    "a3-regra-que-fica": dict(
        aula="1.3",
        title="Demonstração · Aula 1.3",
        desc="O mesmo pedido antes e depois de as regras da casa estarem escritas "
             "num Project, e o número que muda por causa disso.",
        h1="O mesmo pedido, antes e depois das regras",
        lead=[
            "Aqui aparece a resposta para a frase que abriu o curso: "
            "<strong>&quot;quando eu vou pedir de novo, ele faz de outro jeito&quot;</strong>.",
            "As duas conversas usam o <strong>mesmo pedido</strong>, palavra por palavra. "
            "A única diferença é que a segunda roda dentro de um Project que já sabe "
            "como a casa funciona.",
        ],
        arquivo=("pedidos-em-producao.xlsx",
                 "120 ordens de serviço · a mesma planilha das aulas 1.1 e 1.2",
                 "../../a1-ecossistema-e-fisica/exercicio/pedidos-em-producao.xlsx"),
        passos=[
            dict(titulo="O pedido sem contexto nenhum", blocos=[
                ("fazer", "Conversa nova no Chat comum, sem anexar nada, com o pedido "
                          "mais natural do mundo. É como o pedido sai hoje."),
                ("prompt", ("pedido natural", "Me dá a situação das OS de hoje.", True)),
                ("tela", "Ele devolve a pergunta: quais dados, o que você chama de "
                         "situação, que tipo de análise."),
                ("repare", "Ele não está sendo lento. <b>Ele não sabe nada sobre a "
                           "casa</b>, e cada conversa nova começa do zero. É por isso "
                           "que a resposta sai diferente cada vez."),
            ]),
            dict(titulo="As regras da casa, escritas uma vez", blocos=[
                ("fazer", "Cria um Project e escreve nas Instruções o que ele precisa "
                          "saber para nunca mais perguntar aquilo. São oito ou nove "
                          "linhas, não duas páginas."),
                ("prompt", ("as regras, nas Instruções do Project", P_REGRAS, False)),
                ("repare", "Cada linha aqui responde <b>uma pergunta que ele fez no "
                           "passo 1</b>. Não é documentação: é a transcrição do que a "
                           "casa já sabia e nunca tinha escrito."),
            ]),
            dict(titulo="O mesmo pedido, dentro do Project", blocos=[
                ("fazer", "Sem sair do Project, anexa a planilha e manda exatamente o "
                          "mesmo pedido do passo 1. Nem uma palavra a mais."),
                ("tela", "Tabela, data em DD/MM/AAAA, sem introdução, e já apontando o "
                         "que precisa de decisão hoje."),
                ("repare", "<b>Nada disso foi pedido agora.</b> A única diferença entre "
                           "as duas conversas são as regras que ficaram guardadas."),
            ]),
            dict(titulo="O número que mudou, e por que ele mudou", blocos=[
                ("fazer", "Compare a resposta com a coluna Status da planilha, lado a lado."),
                ("tela", "A resposta diz <b>30 OS atrasadas</b>. O campo Status da "
                         "planilha marca <b>4</b>."),
                ("repare", "A OS 2442 e a OS 2490 estão as duas com <b>13 dias de "
                           "atraso</b>. O sistema marca só a primeira. A segunda aparece "
                           "como &quot;Aguardando papel&quot;, e ninguém olhando o "
                           "relatório saberia."),
                ("ensina", "A regra deixa de ser preferência de formatação e vira "
                           "<b>a coisa que muda o número que vai para a reunião</b>. "
                           "O campo de status é preenchido à mão, no fim do turno, por "
                           "quem está com pressa. A data de prazo não mente."),
            ]),
        ],
        fecho=("O que muda daqui para a frente",
               "Regra escrita uma vez vale para todas as conversas seguintes. É a "
               "diferença entre reexplicar a casa toda vez e chegar já sabendo.",
               "Na <strong>seção 05 · Sua vez</strong> você escreve as regras do seu "
               "setor e roda o mesmo pedido duas vezes, dentro e fora do Project. "
               "<strong>A comparação é o exercício.</strong>"),
        rodape='Demonstração da <a href="../">aula 1.3</a> · Gráfica Aurora é uma '
               'indústria gráfica fictícia criada para o treinamento',
    ),

    # ══════════════════════════════════════════════════════ AULA 1.4
    "a4-o-mapa": dict(
        aula="1.4",
        title="Demonstração · Aula 1.4",
        desc="Uma skill por dentro, o que faz ela entrar sozinha, e como decidir "
             "onde cada regra da sua área deve morar.",
        h1="A descrição decidindo sozinha",
        lead=[
            "Uma skill é <strong>um procedimento escrito em português</strong>. "
            "Não tem código, e é isso que faz você conseguir escrever a sua.",
            "O que decide se ela entra ou não numa conversa é a <strong>descrição</strong>, "
            "que fica no topo do arquivo. Ela é o item mais importante e o que mais "
            "se escreve mal.",
        ],
        passos=[
            dict(titulo="A skill por dentro", blocos=[
                ("fazer", "Este é o arquivo inteiro de uma skill da Gráfica Aurora, do "
                          "começo ao fim. Leia sem pressa."),
                ("prompt", ("fechar-cotacao.md · a skill inteira", P_SKILL, False)),
                ("repare", "Não tem <b>uma linha de programação</b>. Em cima, a "
                           "descrição, que diz <b>quando usar</b>. Embaixo, os passos, "
                           "que dizem <b>como fazer</b>. São duas coisas diferentes, e a "
                           "de cima é a que decide tudo."),
                ("ensina", "É uma ficha de acerto de máquina, escrita em português. "
                           "Enquanto parecer código, ninguém da sua área escreve a sua."),
            ]),
            dict(titulo="A que não entra, e a que entra sozinha", blocos=[
                ("fazer", "Primeiro um pedido que não combina com a descrição."),
                ("prompt", ("pedido que não combina",
                            "Me ajuda a escrever um e-mail para o cliente avisando do atraso.",
                            True)),
                ("tela", "A skill não é carregada. Ela não fica lá o tempo todo ocupando "
                         "espaço: só entra quando a tarefa bate."),
                ("fazer", "Agora um pedido que combina, sem chamar a skill pelo nome.", "Depois"),
                ("prompt", ("pedido que combina",
                            "Anexei as três propostas do papel couché. Qual fornecedor eu fecho?",
                            True)),
                ("repare", "Ela entrou <b>sozinha</b>. Quem decidiu isso foram as "
                           "palavras da descrição: <b>cotação</b>, <b>comparação</b>, "
                           "<b>qual fornecedor eu escolho</b>."),
                ("ensina", "Daqui sai a regra que vale o Módulo 2 inteiro: "
                           "<b>descrição vaga é skill que nunca roda</b>. A pessoa "
                           "escreve um procedimento bom e ele nunca é chamado."),
            ]),
            dict(titulo="Os outros dois gatilhos", blocos=[
                ("fazer", "A mesma tarefa pode ser puxada de três jeitos, e a diferença "
                          "entre eles é quem puxa."),
                ("lista", ("Quem dispara cada um", [
                    "<b>Skill</b> · ele decide, lendo a descrição. Você não chama",
                    "<b>Comando</b> · você decide, chamando pelo nome",
                    "<b>Conector</b> · a porta fica aberta e ele busca no sistema "
                    "quando precisa",
                ])),
                ("repare", "Desligue o conector e faça o mesmo pedido: a porta fechou e "
                           "ele não alcança mais o dado. <b>Não existe o lugar de "
                           "graça</b>, existe o lugar certo para aquela informação."),
            ]),
            dict(titulo="Onde cada regra da sua área deve morar", blocos=[
                ("fazer", "Três regras reais de uma gráfica. A pergunta para cada uma é "
                          "a mesma: <b>ele precisa saber disso sempre, às vezes ou nunca?</b>"),
                ("lista", ("As três, e onde elas moram", [
                    "&quot;Nunca escreva o nome do cliente por extenso em relatório que "
                    "sai da empresa.&quot; → <b>sempre</b>, e por isso vira regra do "
                    "Project",
                    "&quot;Ao comparar cotação, converta tudo para preço por milheiro.&quot; "
                    "→ <b>às vezes</b>, só quando a tarefa é cotação, e por isso vira skill",
                    "&quot;Toda proposta acima de cinquenta mil reais precisa de segunda "
                    "aprovação antes de sair.&quot; → esta divide qualquer sala",
                ])),
                ("ensina", "A terceira não é regra de estilo, é <b>cerca</b>. A pergunta "
                           "que resolve não é onde ela fica, é outra: <b>se ele esquecer "
                           "isso uma vez em cem, qual o tamanho do estrago?</b> "
                           "Quando a resposta é grande, aquilo não pode morar em texto "
                           "que ele lê e interpreta."),
            ]),
        ],
        fecho=("O que muda daqui para a frente",
               "A pergunta que você leva do Módulo 1 inteiro é uma só: esta "
               "informação precisa estar no contexto sempre, às vezes ou nunca?",
               "Na <strong>seção 05 · Sua vez</strong> você classifica as regras da sua "
               "área nessa tabela. <strong>É o insumo direto do Módulo 2</strong>, onde "
               "essas regras viram skill de verdade."),
        rodape='Demonstração da <a href="../">aula 1.4</a> · Gráfica Aurora é uma '
               'indústria gráfica fictícia criada para o treinamento',
    ),
}
