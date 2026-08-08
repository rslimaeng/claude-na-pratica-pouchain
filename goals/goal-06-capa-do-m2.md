# Goal 06 · Onda 29 · A capa do M2, a auditoria do site e o deep dive de Cowork

> **Base:** `aadd563` na `main` · **Status:** ✅ publicada em 08/08/2026.

Três pedidos do Rafael no mesmo dia, depois de fechar o M1: **atualizar a capa**,
**auditar o que é comunicação interna nossa** e **criar a página do Módulo 2**.

## 1 · A auditoria · o que o cliente lia e não devia

| Onde | Estava | Virou |
|---|---|---|
| Capa · M2 e M3 | *"disponível após a Onda 5"* e *"Onda 8"* | "ver o programa" e "o programa entra aqui em breve" |
| Capa · M1 | **"Em construção"**, e já estava errado | "Quatro aulas, disponível" |
| Capa · M2 e M3 | "Cowork na prática", "Code na prática" | Nome de rotina, seguindo o P1 |
| `kit/LEIA-ME.md` | "vem da onda 1 a 8", "pronto na Onda 9", apontando para `.csv` e `.md` que não existem mais. **Não era linkado** | Saiu do site, preservado em `KIT-DO-PARTICIPANTE.md` |
| `README.md` | A tabela "Onda / Entrega / Status" e o checklist "antes de publicar" | Reescrito para o cliente |

**O que eu quase reportei como defeito e não era:** os "Nível 3 de 6" dos heróis
e os "MORRE NO NÍVEL 4 · M2" da capa. **A capa apresenta a trilha com a coluna
Nível numerada de 0 a 6**, então o número aponta para algo que o cliente viu.
Conferi antes de mexer, e foi o que impediu um estrago.

**Camada 2, que continua aberta e é decisão do Rafael:** `CLAUDE.md` (391 linhas
com o perfil do público, a regra P3 e o modelo mental dele) e `goals/` (os meus
erros e as decisões pendentes) **são servidos pelo Pages e aparecem no repo
público**. Recomendação: mover os dois para `pouchain-claude-na-pratica/`. O
`CLAUDE.md` continua carregando das pastas-mãe e o `gates.py` continua rodando
de `site/`.

## 2 · A capa do M2

**A 1.4 comeu quatro aulas do M2 planejado.** O plano antigo tinha oito, e
`2.2 Quando vira skill`, `2.3 Anatomia`, `2.4 Construindo a sua` e
`2.5 Por que arquivo grande não custa` estão todas na 1.4 publicada. **O M2
ficou com seis**, e a 2.2 virou a ponte: *"a sua skill sai do navegador e vira
arquivo"*. A nota de cobertura da ementa diz isso em linguagem de cliente.

**O bloco dos três Claudes**, adaptado do print que o Rafael apontou:

- **Corte diferente do da 1.1 de propósito.** A 1.1 corta por *onde roda / o que
  alcança*. Aqui é **para quem cada um foi feito**, e a página linka para a 1.1
- **Ancorado num fato:** o aplicativo tem literalmente três abas, Chat, Cowork e
  Claude Code, confirmado por transcrição que mostra a tela
- **Cor semântica, não identidade.** O print original pinta os três de cores
  diferentes. Aqui os três são neutros e **só o Cowork acende**, porque é dele
  que o módulo trata. Três cores seria decoração, e o §8 não permite
- Fecha com a frase da Anthropic: **pensar · delegar · construir**

## 3 · O deep dive de Cowork

71 arquivos em três pastas. Achados completos em `../FATOS-VERIFICADOS.md` e o
plano de escrita por aula em `../PESQUISA-M2-COWORK.md`.

**Os três que mudaram coisa já escrita:**

1. 🔴 **A taxonomia dizia `Allow/Ask/Block` na aula 2.1.** É vocabulário do
   Claude Code, não do Cowork. O Cowork tem **dois modos** mais uma trava que não
   desliga. Corrigido na taxonomia e na capa
2. ✅ **A pendência crítica da tarefa agendada foi respondida** pelo Academy, e é
   promessa de ementa. Só roda com a máquina ligada, e **pega quando você volta
   avisando que atrasou**
3. 🔤 **O nome do botão da pasta mudou** entre maio e julho de 2026, e as duas
   fontes oficiais discordam. Nenhuma das duas resolve, porque **a turma usa a
   tela em português**

## Dois defeitos consertados no caminho

1. **O `<ul>` dentro do callout não tinha CSS nenhum.** O callout do M1 só usava
   `<p>`. O G7-ter não pega porque ele confere **classe** sem CSS, e eu usei uma
   **tag**
2. **O bloco de três colunas do fio estourava 82px para fora do card branco, e já
   estava no ar no hub do M1.** Herdado, corrigido nos dois

## Conferido

Desktop e 375px, sem overflow, grades colapsando, divisores dos três cards
alinhados. **29 gates, exit 0.**
