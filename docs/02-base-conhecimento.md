# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `jovem_perfil.json` | JSON | Identificar idade, objetivos (ex: celular novo) e quem é o responsável validador |
| `missões_concluidas.csv` | CSV | Histórico de aprendizado (quais aulas o jovem já "zerou") |
| `dicionario_kids.json` | JSON | Tradução de termos técnicos para analogias simples (ex: Dividendos = Frutos da árvore) |
| `extrato_mesada.csv` | CSV | Analisar como o jovem está distribuindo sua mesada entre gastos e poupança |

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O agente utiliza Python para processar os dados e alimentar o contexto da conversa em tempo real.

```python
import pandas as pd
import json

# Carregando a jornada do pequeno investidor
historico_missoes = pd.read_csv('data/missões_concluidas.csv')
fluxo_mesada = pd.read_csv('data/extrato_mesada.csv')

# Dados de perfil e termos didáticos
with open('data/jovem_perfil.json', 'r', encoding='utf-8') as f:
    perfil_jovem = json.load(f)

with open('data/dicionario_kids.json', 'r', encoding='utf-8') as f:
    termos_didaticos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são injetados no contexto para que o Bebeto saiba exatamente em que "nível" o jovem está. Veja o exemplo de estrutura:

``` text

| PERFIL DO JOVEM INVESTIDOR | (data/jovem_perfil.json)
{
  "nome": "Lucas Vasconcelos",
  "idade": 14,
  "objetivo_principal": "PlayStation 5",
  "valor_objetivo": 4500.00,
  "poupado_atualmente": 1200.00,
  "mesada_media": 200.00,
  "perfil_aprendizado": "Curioso/Explorador",
  "responsavel_legal": "Mariana (Mãe)",
  "nivel_gamificacao": 2,
  "conquistas": ["Primeira Poupança", "Mestre do Cofrinho"]
}

| DICIONÁRIO DE ANALOGIAS |
{
  "Ações": "É como ser dono de um pedacinho de uma pizzaria. Se ela vende muito, seu pedaço vale mais!",
  "CDB": "É como emprestar seu brinquedo para o banco. Ele te devolve depois com uma 'figurinha' de agradecimento.",
  "Juros Compostos": "É o efeito 'bola de neve' no videogame: quanto mais tempo você sobrevive, mais pontos ganha por segundo.",
  "Inflação": "É o monstro que faz o preço da figurinha subir. Se antes custava 2 moedas, agora custa 3."
}
```

```text
| HISTORICO DE ATENDIMENTO DO CLIENTE | (data/historico_atendimento.csv):

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim
```
```text
[
  {
    "nome": "Tesouro Selic",
    "apelido_bebeto": "Escudo de Platina",
    "risco": "Quase zero (Segurança Máxima)",
    "rentabilidade": "Cresce junto com o Brasil",
    "aporte_minimo": 30.00,
    "vibe_do_investimento": "Para planos grandes que demoram meses (tipo um PC novo ou intercâmbio).",
    "explicacao_bebeto": "É como guardar seu XP no lugar mais seguro do mapa. O governo cuida dele pra você e devolve com bônus!"
  },
  {
    "nome": "CDB Liquidez Diária",
    "apelido_bebeto": "Poção de Velocidade",
    "risco": "Baixinho",
    "rentabilidade": "Um pouco mais que o cofrinho comum",
    "aporte_minimo": 1.00,
    "vibe_do_investimento": "Para aquele dinheiro que você pode precisar sacar no final de semana.",
    "explicacao_bebeto": "Seu dinheiro fica rendendo todo dia, mas se surgir um rolê de última hora, você resgata ele na hora com um clique!"
  },
  {
    "nome": "Ações (Empresas de Games/Tech)",
    "apelido_bebeto": "Modo Multiplayer",
    "risco": "Alto (Montanha-Russa)",
    "rentabilidade": "Pode subir muito ou cair rápido",
    "aporte_minimo": 50.00,
    "vibe_do_investimento": "Para quem quer ser 'sócio' das empresas que gosta.",
    "explicacao_bebeto": "Você vira dono de um pedacinho de empresas tipo a Apple ou Roblox. Se elas mandarem bem, seu dinheiro sobe. Se pisarem na bola, ele desce!"
  },
  {
    "nome": "Fundo de Cripto (Iniciante)",
    "apelido_bebeto": "Nível Hardcore",
    "risco": "Altíssimo (Cuidado!)",
    "rentabilidade": "Super Volátil",
    "aporte_minimo": 10.00,
    "vibe_do_investimento": "Apenas para testar com moedinhas que não vão fazer falta.",
    "explicacao_bebeto": "É o Velozes e Furiosos do dinheiro. É emocionante, mas só entre se seus pais deixarem e se você tiver estômago!"
  }
]
```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
### CONTEXTO DO USUÁRIO ###
- Jovem: Lucas Vasconcelos (14 anos)
- Mentor Responsável: Mariana (Mãe)
- Grande Objetivo: PlayStation 5 (Progresso: 26% concluído)
- Saldo para Investir: R$ 50,00 (da mesada atual)

### HISTÓRICO RECENTE ###
- 15/10: Lucas aprendeu o que é um CDB.
- 20/10: Pediu para investir R$ 30,00. A mãe (Mariana) aprovou.
- Hoje: Lucas quer saber por que o dinheiro não dobrou em uma semana.

### REGRAS DO BEBETO ###
1. Use a analogia de "Bola de Neve" para explicar o tempo.
2. Seja motivador, mas realista sobre prazos.
3. Se ele quiser investir mais, gere o link de "Pedido de Autorização" para a Mariana.

### EXEMPLO DE RESPOSTA DO BEBETO ###
- "Fala, Lucas! Cara, 26% do PS5 já está garantido, você tá mandando muito bem! 🎮
- Sobre o seu investimento: lembra da nossa conversa sobre a bola de neve? No começo ela parece pequena e lenta, mas quanto mais ela rola (tempo), mais neve ela gruda. O dinheiro no CDB é igual. Uma semana é só o primeiro centímetro da bola!
- Quer que eu te mostre um gráfico de quanto você pode ter se continuar guardando esses R$ 50,00 todo mês?"
```
