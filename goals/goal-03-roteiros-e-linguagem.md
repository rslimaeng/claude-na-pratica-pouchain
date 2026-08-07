# Goal 03 · Roteiros de demonstração e linguagem de rotina

**Executada em 07/08/2026**, em rodadas curtas de validação: o Rafael validava um ponto, pedia o ajuste, eu executava, ele passava para o próximo.

**Ponto de retorno anterior:** tag `antes-da-linguagem-de-rotina` (commit `c9d297e`).

## 1. A correção que reorganizou tudo

Eu tinha escrito no processo: *"toda aula mostra a saída pronta antes do exercício"*, e construído uma página de artefato pronto para a 1.1. **O Rafael reprovou:**

> *"Eu quero o exemplo pronto para executar na frente deles, e não algo que eu vou clicar e aparece já feito. A ideia é eles verem acontecendo e fazer similar. Entender o motivo de isso ter acontecido. Lembre-se, o treinamento é prático e andragógico."*

**Por que ele estava certo:** mostrar o resultado pronto entrega o conceito já resolvido. O aluno assiste mágica, e mágica não se aprende. A ordem é **experiência → pergunta → conceito**, nunca conceito → ilustração.

A regra errada estava no `CLAUDE.md` e teria contaminado as 15 aulas seguintes.

## 2. O roteiro de demonstração

Uma página por aula, em `m1/aN-slug/demonstracao/`. Cada momento traz seis blocos:

| Bloco | O que é |
|---|---|
| O que você faz | A ação concreta |
| O prompt | Literal e copiável. Nunca "escreva algo como" |
| 🔴 Aponte isto na tela | O dedo no que importa |
| **Pergunte à sala** | A pergunta que eles respondem **antes** da explicação |
| Por que este momento existe | O conceito, depois de a sala ter vivido |
| Se der errado | O plano B, escrito antes de precisar |

**O bloco que não pode faltar é `pergunte à sala`.** É o que separa demonstração de aula.

### Os quatro momentos de ouro

O padrão é sempre o mesmo: **a sala produz a resposta antes de saber que produziu.**

| Aula | Momento | O que a sala faz |
|---|---|---|
| 1.1 | 3 | Dita as correções do pedido vago. No momento 5 reconhece as próprias palavras no pedido situado |
| 1.2 | 2 | Preenche os três campos da OS em branco. O pedido que roda no momento 3 é o deles |
| 1.3 | 2 | Dita as regras do Project linha por linha, e o instrutor só digita |
| 1.4 | 4 | Classifica três regras em voz alta e **discorda na terceira, de propósito** |

**Cada roteiro tem plano B em todo momento.** O da 1.4 momento 2 é exemplar: se a skill não disparar, o roteiro manda comemorar e consertar a descrição ao vivo, porque nada ensina melhor que "descrição vaga é skill que nunca roda".

## 3. Os 4 padrões de linguagem

Nasceram da análise de um curso concorrente, que o Rafael mandou olhar pela **comunicação**, não pelo conteúdo. Estão em `CLAUDE.md` §7-bis.

| | Padrão |
|---|---|
| **P1** | Todo nome carrega **a rotina e o nome oficial do recurso** |
| **P2** | Toda promessa tem **hora marcada** |
| **P3** | 🔴 Nomeia-se **a espera, nunca a pessoa** |
| **P4** | Diz-se **o que o curso não faz**, em bloco visível |

**O diagnóstico dele:** *física, pedir, contextualizar, procedimentar* é andaime de projeto. Um coordenador de PCP lê "Nível 2 · Contextualizar" e não sabe nem se é a rotina dele, nem qual recurso vai usar.

### O que foi renomeado

| | De | Para |
|---|---|---|
| Módulo 1 | Fundamentos do ecossistema | **Escolher a ferramenta certa e onde guardar cada coisa** |
| Aula 1.1 | O ecossistema e a física | **Onde abrir, e por que ele piora no meio da conversa** |
| Aula 1.2 | Pedir para entregar | **Pedir de um jeito que a primeira resposta já sirva** |
| Aulas 1.3 e 1.4 | | mantidas: já eram linguagem de rotina |

Os **7 níveis** ganharam nome público em `CLAUDE.md` §5, que passa a ser a fonte da verdade do texto.

> ⚠️ **O nome da ementa contratada é outro**, e trocar sem mostrar o De/Para faz o cliente achar que sumiu conteúdo. O hub ganhou chip de ementa e nota de cobertura, igual às aulas.

## 4. Duração saiu da tela

> *"Tire o tempo das aulas. Até pra não gerar uma pressão, vamos manter controle interno só."*

**Mesma convenção que já valia no Mallory.** Tempo no material do aluno não informa, cobra.

| Onde | Tempo |
|---|---|
| Hero, destino, eyebrow, card do hub | ❌ removido, e `.aula-dur` deletada |
| Roteiro de demonstração | ✅ é aqui que vive |
| Landing, no que foi vendido | ✅ contrato |

## 5. Defeitos que a auditoria pegou de graça

1. **A aula 1.3 mostrava números errados.** "Offset 2 com 5" quando são 6, e a OS 2434 como atrasada quando o prazo dela é dali a cinco dias. Virou o gate **G13**, que recalcula do `.xlsx`
2. **As figuras da Onda 2 nunca entraram no breakout.** `.mapa`, `.os`, `.rodadas` estavam presas em 780px desde que nasceram
3. **Duplicação no bloco P4.** "Não te deixa automático em 12 horas" já estava dito, e melhor, no callout de fechamento
4. **Um defeito de mobile anterior a esta onda:** o chip do módulo caía na coluna 1 porque a media query mirava o `<span>` e não o `<div>`

## 6. Gates novos

| Gate | O que pega |
|---|---|
| **G12** | Nome de nível fora da lista aprovada, ou linha da trilha sem o recurso oficial |
| **G13** | Número sobre a Gráfica Aurora que não bate com o `.xlsx` |
| **G14** | Aula sem `demonstracao/`, ou roteiro sem `.pergunta`, `.aponte` e `.planoB` em cada momento |
| **G15** | Duração na tela do aluno, **e roteiro sem duração** |

**G12 e G15 foram testados contra cópias quebradas de propósito** antes de entrar.

**Por que o G12 não é caça-palavra:** *alcançar* e *delegar* são verbos comuns do português e apareceriam em prosa legítima. Conferir a lista aprovada é preciso; caçar palavra proibida gera falso positivo, e gate com exceção deixa de ser gate.

## 7. 🔴 O problema de relógio, aberto e do Rafael

| Aula | Demo | Exercício | Sobra para o resto |
|---|---|---|---|
| 1.1 | 12 | 12 | **1 min** 🔴 |
| 1.2, 1.3, 1.4 | 6 | 12 | 7 min |

**A 1.1 não fecha nos 25 minutos.** Duas saídas:

- **A** · enxugar para 7 min, juntando os momentos 1 e 2
- **B** · aceitar 35 min, porque é a aula de abertura e o momento 3 é o que compra as outras 11 horas

**Recomendação: B.** Mas isso muda a distribuição das 2h do M1, e a conta é do Rafael.

## 8. Aberto

- 🔴 **Teste de mesa das 4 aulas**, que nenhuma onda substitui
- **M2 e M3 ainda com nome antigo.** "Cowork na prática" carrega o recurso oficial mas não promete nada. Resolver quando o M2 for validado
- A onda 4 (Módulo 2) continua bloqueada pelas duas descobertas da onda 2: skill do claude.ai é individual, e só o proprietário adiciona conector em Team/Enterprise
