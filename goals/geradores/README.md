# Geradores

As páginas de demonstração e as duas planilhas **não são escritas à mão**. Saem daqui, e é por isso que os números batem com o gate G13.

| Script | Gera |
|---|---|
| `gera_demos.py` + `demos_conteudo.py` | As 4 páginas `m1/aN/demonstracao/index.html`. Conteúdo separado da renderização: editar conteúdo é editar o dicionário em `demos_conteudo.py` |
| `gera_pcp.py` | `m1/a1-ecossistema-e-fisica/exercicio/pedidos-em-producao.xlsx` · 120 OS |
| `gera_cotacoes.py` | `m1/a1-ecossistema-e-fisica/demonstracao/cotacoes-fornecedores.xlsx` · 104 linhas |
| `regera_exemplo.py` | ⚠️ **Migração de uma vez só, já executada.** Ele casava com o texto antigo da página, então rodar de novo não faz nada e não avisa |

**Rode da raiz do repo**, nesta ordem se mexer nas planilhas:

```
python3 goals/geradores/gera_pcp.py
python3 goals/geradores/gera_cotacoes.py
python3 goals/geradores/gera_demos.py
python3 goals/gates.py
```

**Se você mexer numa planilha**, os dois scripts imprimem um relatório com todos os números novos. **A página `exemplo/` não se atualiza sozinha**, e é aí que o `regera_exemplo.py` engana: ele foi escrito para casar com o texto antigo, então hoje roda e não troca nada, em silêncio. O que protege é o **G13**, que recalcula do `.xlsx` e reprova a página quando o número não bate. Confie no gate, não no script.

> ⚠️ **`random.seed(2481)` nos dois geradores de planilha é obrigatório.** Sem ele os números mudam a cada execução e todas as páginas passam a mentir. Se precisar mexer numa probabilidade, rode e **releia o relatório impresso**: os números novos precisam entrar nas páginas antes de o G13 passar.

**O `gera_demos.py` também é um gate:** ele varre 19 frases de direção de cena e acusa antes de gravar. Página de demonstração é do aluno, nunca roteiro de palco. Ver `../../CLAUDE.md` §9.
