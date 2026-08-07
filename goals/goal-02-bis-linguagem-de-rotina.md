# Goal 02-bis · A linguagem de rotina

**Executada em 07/08/2026.** Não é onda de conteúdo novo: é ajuste de **superfície** no que já estava construído. A onda 3 continua sendo o Módulo 2.

**Ponto de retorno:** a tag `antes-da-linguagem-de-rotina`, no commit `c9d297e`.

```bash
git checkout antes-da-linguagem-de-rotina
```

## 1. De onde veio

Rafael mandou analisar a página de um curso concorrente de Claude para gestores. O pedido dele não era copiar conteúdo, era **linguagem**:

> *"o ponto aqui é a linguagem para a empresa sentir que está usando o Claude para negócios... eu acho que a pessoa da empresa vai entender a minha rotina, a minha atividade, o meu contexto."*

E o diagnóstico dele, que estava certo: **o vocabulário dos níveis é nosso, não do aluno.** Um coordenador de PCP lê *"Nível 2 · Contextualizar"* e não sabe nem se aquilo é a rotina dele, nem qual recurso do Claude ele vai usar.

Ele acrescentou a ressalva que virou parte da regra: *"não quero deixar de pegar os princípios andragógicos que a gente procurou no vault do Alan."*

## 2. Os 4 padrões, agora em `CLAUDE.md` §7-bis

| | Padrão | O que obriga |
|---|---|---|
| **P1** | Todo nome carrega **a rotina e o recurso oficial** | Nome interno vira comentário HTML. O nome oficial do Claude fica visível na trilha, no card do hub e no hero da aula |
| **P2** | Toda promessa tem **hora marcada** | Capacidade abstrata não gruda. Batida de calendário gruda |
| **P3** | 🔴 Nomeia-se **a espera, nunca a pessoa** | Curso in-company tem o analista na sala. A espera é o vilão |
| **P4** | Diz-se **o que o curso não faz**, em bloco visível | Evita que 20 pessoas cheguem ao M3 achando que vão programar |

**A andragogia não mudou.** Destino → origem → conceito → aplica → hook, a regra de 2 a 3 conceitos e o validador continuam idênticos. Isto foi troca de rótulo.

## 3. Os nomes aprovados

Fonte da verdade: **`CLAUDE.md` §5**. Nenhuma página inventa nome de nível; copia de lá.

| # | Vai para a tela | No Claude é |
|---|---|---|
| 0 | Por que ele piora na conversa longa | Chat · Janela de contexto |
| 1 | Pedir uma vez e receber pronto | Chat |
| 2 | Ele já começa sabendo as suas regras | Project · Instruções · `CLAUDE.md` |
| 3 | Cada tarefa puxa o seu próprio procedimento | Skill · Comando |
| 4 | Ele abre os arquivos onde você trabalha | Cowork · Conector (MCP) |
| 5 | Você prova que está certo antes de mandar | Checklist · rubrica · hook |
| 6 | Roda sem você apertar o play | Rotina agendada · plugin |

> ⚠️ **Correção feita durante a execução.** No mockup eu tinha dito que o nível **3** fecha o laço com a frase de abertura do curso. Está errado: *"quando eu vou pedir de novo ele faz de outro jeito"* é respondida na **aula 1.3, que é o nível 2**. O nível 3 ganhou promessa própria, sobre a tarefa ter método próprio.

**Níveis 0 e 1 usam chip cinza (`.rec.livre`)**, porque não são recurso nenhum: são o chat que a sala já usa. Isso comunica, sem escrever, que o valor começa antes de instalar qualquer coisa.

## 4. O que mudou em cada arquivo

| Arquivo | Mudança |
|---|---|
| `index.html` | Trilha com nome de rotina + coluna **No Claude é** · dor-mãe apontando qual nível mata cada etapa + faixa dos níveis 0 a 2 · bloco **o que estas 12 horas não fazem** |
| `m1/index.html` | Os 4 cards ganharam o chip do recurso |
| As 4 aulas | Chip `No Claude` no hero · kicker vira `Nível N de 6` · **`.destino-quando`**, a promessa com hora marcada |
| `CLAUDE.md` | §5 virou a tabela canônica de nomes · §7-bis, os 4 padrões · §9 ganhou o padrão "clica e abre o exemplo" |
| `_shared/design-tokens.md` | 6 componentes novos |
| `goals/gates.py` | **G12** |

## 5. A figura que resolveu um buraco que ninguém tinha visto

A dor-mãe tinha 4 etapas numeradas e a trilha tinha 7 níveis numerados, **na mesma página, sem nada ligando as duas numerações**. A pessoa lia a dor, concordava, e não sabia onde no curso aquilo morria.

Agora cada etapa diz o nível que a elimina. E a faixa de baixo responde de graça a pergunta que ia aparecer na primeira hora de aula:

> **Níveis 0, 1 e 2 não removem etapa nenhuma**, e é exatamente por isso que vêm primeiro: sem eles, o que está acima acontece uma vez e não repete igual amanhã.

## 6. G12 · o gate novo

Confere três coisas, e foi testado contra uma cópia quebrada de propósito antes de entrar:

1. Os 7 `.nivel-nome` da landing batem **exatamente** com a lista do `CLAUDE.md` §5
2. Toda linha da trilha tem pelo menos um `.rec`
3. Hero de aula e card do hub carregam o recurso

**Por que não um gate que procura a palavra proibida:** *alcançar* e *delegar* são verbos comuns do português e apareceriam em prosa legítima. Gate que gera falso positivo vira gate com exceção, e gate com exceção deixa de ser gate. Conferir a lista aprovada é preciso; caçar palavra não é.

## 7. Uma duplicação encontrada e desfeita

O primeiro rascunho do bloco P4 dizia *"não te deixa automático em 12 horas"*. **Isso já estava dito**, e melhor, no callout que fecha a landing, com a analogia da carteira de motorista. O item virou *"não entrega nada pronto para você usar"*, que é uma expectativa real de turma in-company e não estava em lugar nenhum.

## 8. Verificado

- 13/13 gates passando
- Renderizado conferido em 1280px e em 375px: **zero overflow horizontal** nas duas larguras
- Corrigidos ao ver renderizado: caixas do fluxo centradas verticalmente (número desalinhava com título de 2 linhas) · coluna do Excel apertada · chip do nível 0 quebrando dentro de si · **e um defeito de mobile que já existia antes**, o chip do módulo caindo na coluna 1 porque a media query mirava o `<span>` e não o `<div>` que o embrulha

## 9. Aberto

- 🔴 **Teste de mesa das 4 aulas continua pendente.** Esta onda não mexeu em exercício nem em gabarito
- **P2 foi aplicado só no destino das aulas.** Checkpoint e hook ainda estão em linguagem de capacidade
- A onda 3 (Módulo 2) segue bloqueada pelas duas descobertas da onda 2: skill do claude.ai é individual, e só o proprietário adiciona conector em Team/Enterprise
