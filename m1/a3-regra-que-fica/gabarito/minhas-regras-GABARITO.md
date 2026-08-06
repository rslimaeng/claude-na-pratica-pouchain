# Gabarito comentado · As regras da minha função

> **O seu vai ser diferente do meu, e tudo bem.** Este é o texto de um **coordenador
> de PCP da Gráfica Aurora**, uma pessoa fictícia, de uma empresa fictícia. Se você
> é do Financeiro, do RH ou do Comercial, o seu vai ter outras linhas.
>
> **Compare a estrutura, não o conteúdo.** As perguntas certas são: as minhas cinco
> seções estão preenchidas? Cada linha minha veio de uma correção que eu de fato
> repeti? Ficou entre 20 e 40 linhas?
>
> Os blocos marcados com 💬 são o comentário do professor. Eles **não** entram no
> arquivo de verdade.

---

## 1. Quem eu sou e o que eu faço

Sou coordenador de PCP numa indústria gráfica de médio porte.
Programo a produção de duas máquinas offset e duas flexográficas.
Quem usa o que eu produzo: os líderes de máquina, na reunião diária das 8h,
e o gerente industrial, na reunião semanal.

> 💬 **Por que estas quatro linhas.** A última é a mais importante e é a que quase
> todo mundo esquece: **quem lê**. Sem ela, o Claude escreve para você. Com ela,
> ele escreve para a reunião, e o tom, o tamanho e o nível de detalhe mudam sozinhos.

---

## 2. Como a casa funciona

OS = ordem de serviço. Cada OS é um pedido de um cliente.
Tiragem = quantidade de peças impressas naquela OS.
"Fechar a OS" = liberar para faturamento. Não significa terminar a impressão.
Temos 4 máquinas: Offset 1, Offset 2, Flexo 1 e Flexo 2.
Offset é para tiragem alta e prazo mais longo. Flexo é para rótulo e prazo curto.
O relatório sai do sistema em CSV separado por ponto e vírgula.
Ele vem sujo: data em formatos diferentes, status ora em maiúscula ora não,
coluna com espaço no nome e linha em branco no meio. Normalize antes de analisar.

> 💬 **As três últimas linhas valem o arquivo inteiro.** Elas nasceram de uma correção
> que se repetia toda semana: *"as datas estão erradas"*. Escrevendo aqui uma vez,
> você nunca mais reclama disso.
>
> 💬 **A linha do "fechar a OS" é o tipo de coisa que só quem trabalha na casa sabe.**
> É exatamente por isso que ela precisa estar escrita: o Claude sabe muito sobre
> gráfica em geral e **nada** sobre a sua gráfica.

---

## 3. Como eu quero a resposta

Responda sempre em português do Brasil.
Use tabela sempre que houver mais de 3 itens para comparar.
Sem parágrafo de introdução e sem parágrafo de conclusão, eu colo direto na pauta.
Data no formato DD/MM/AAAA. Valor em reais, com vírgula decimal.
Quando falar de prazo, diga também quantos dias úteis faltam a partir de hoje.

> 💬 **Esta é a seção que mais devolve tempo**, e é a mais fácil de escrever: é só
> olhar as suas anotações das aulas 1.1 e 1.2 e transcrever o que você corrigiu
> mais de uma vez.
>
> 💬 A linha "sem introdução e sem conclusão" costuma ser a campeã de repetição na
> sala inteira, de todos os setores.

---

## 4. O que nunca fazer

Nunca invente número que não esteja no dado que eu mandei.
Nunca arredonde valor sem me avisar que arredondou.
Nunca conclua que uma OS está atrasada sem me mostrar a conta: prazo × data de hoje.
Não me devolva comunicado ou e-mail pronto para enviar, eu reviso antes, sempre.

> 💬 **A terceira linha é a mais valiosa das quatro.** "Me mostre a conta" transforma
> uma resposta que você teria que acreditar numa resposta que você consegue conferir
> em cinco segundos. Guarde essa ideia: ela vira um módulo inteiro no M3.
>
> 💬 Repare que nenhuma linha aqui diz "seja cuidadoso" ou "capriche". Regra que não
> dá para julgar como verdadeira ou falsa não é regra, é torcida.

---

## 5. Na dúvida

Se o dado estiver ambíguo ou faltando, me pergunte em vez de adivinhar.
Se você tiver menos de 80% de certeza sobre um número, sinalize em vez de afirmar.
Se a resposta puder ir para dois caminhos, me mostre os dois e diga qual você
escolheria, com o motivo.

> 💬 **É a seção mais curta e a que muda mais o dia a dia.** Sem ela, o Claude
> preenche buraco com hipótese plausível, e hipótese plausível dentro de um número
> é exatamente o erro que passa batido na reunião.

---

## 📏 Confira o seu

| Pergunta | Se a resposta for não |
|---|---|
| As cinco seções estão preenchidas? | Volte na que ficou vazia. Se você não tem nada a escrever ali, provavelmente ainda não reparou nas correções que faz |
| Cada linha veio de uma correção que você **repetiu**? | Apague a que você inventou agora. Regra sem dor de origem só ocupa espaço |
| Ficou entre 20 e 40 linhas? | Muito curto: falta olhar as anotações. Muito longo: você misturou regra de "sempre" com regra de "às vezes", e isso é o gancho da próxima aula |
| Alguma linha diz "seja cuidadoso", "capriche", "seja conciso"? | Reescreva. Se não dá para dizer se foi cumprida ou não, ele não tem como cumprir |
| Tem dado sensível aqui dentro? | Tire. Nome de pessoa, valor de contrato e tabela de preço não pública não entram |

---

*Gráfica Aurora é uma indústria gráfica fictícia criada para este treinamento.
Nomes, máquinas, clientes e valores são inventados.*
