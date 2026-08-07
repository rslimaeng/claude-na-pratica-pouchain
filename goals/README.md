# Ondas de produção

1 onda = 1 goal. Nenhuma onda começa antes de o Rafael validar a anterior no navegador.
O plano completo está em [`../../PLANO-DE-PRODUCAO.md`](../../PLANO-DE-PRODUCAO.md).

| Onda | Goal | Entrega | Status |
|---|---|---|---|
| 1 | [`goal-01-infra-e-padrao.md`](goal-01-infra-e-padrao.md) | Infra · tokens · landing · hub M1 · **aulas 1.1 e 1.3** | ✅ validada, com 5 ajustes aplicados na onda 2 |
| **2** | [`goal-02-fechar-o-m1.md`](goal-02-fechar-o-m1.md) | **Aulas 1.2 e 1.4** · validador nas 4 aulas · conserto de layout · gates executáveis | 🟡 aguardando teste de mesa |
| **2-bis** | [`goal-02-bis-linguagem-de-rotina.md`](goal-02-bis-linguagem-de-rotina.md) | **Os 4 padrões de linguagem** aplicados em tudo que já existia. Nome de rotina + recurso oficial do Claude · dor-mãe ligada aos níveis · bloco "o que não fazemos" · gate G12 | ✅ no ar. Volta em `antes-da-linguagem-de-rotina` |
| 3 | a definir | Hub M2 + aulas 2.1 · 2.2 · 2.3 | ⏸️ |
| 4 | a definir | M2: aulas 2.4 · 2.5 · 2.6 | ⏸️ |
| 5 | a definir | M2: aulas 2.7 · 2.8 | ⏸️ |
| 6 | a definir | Hub M3 + aulas 3.1 · 3.2 · 3.3 | ⏸️ |
| 7 | a definir | M3: aulas 3.4 · 3.5 · 3.6 | ⏸️ |
| 8 | a definir | Aula 3.7 + entregável final + plano de 30 dias | ⏸️ |
| 9 | a definir | `recursos/` + `kit-participante.zip` montado | ⏸️ |

## O protocolo de 3 passos

Toda aula passa pelos três antes de ser considerada pronta:

1. **Produção**, o terminal produz segundo a anatomia e o goal da onda
2. **Auditoria**, `python3 goals/gates.py` rodado da raiz. São 12 gates e o script sai com código 1 se algum falhar
3. **Teste de mesa (Rafael)** 🔴, ele roda o exercício de verdade e confere se a saída bate com o gabarito

O passo 3 é o único que pega *"o exercício não funciona"*. Nenhuma auditoria de código detecta isso.

> **Regra dos gates:** gate com exceção permanente deixa de ser gate. Se o script acusa, o conserto é no código. E gate que procura uma palavra não pode rodar contra o arquivo que enuncia a regra sobre ela, senão se auto-reprova.
