# 🎮 Bebeto: O Mestre das Moedas

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, foi idealizado e prototipado um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que o projeto possui:

### 1. Documentação do Agente

- **Caso de Uso:**
- **Persona e Tom de Voz:**
- **Arquitetura:**
- **Segurança:**

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `jovem_perfil.json` | JSON | Identificar idade, objetivos (ex: celular novo) e quem é o responsável validador |
| `missões_concluidas.csv` | CSV | Histórico de aprendizado (quais aulas o jovem já "zerou") |
| `dicionario_kids.json` | JSON | Tradução de termos técnicos para analogias simples (ex: Dividendos = Frutos da árvore) |
| `extrato_mesada.csv` | CSV | Analisar como o jovem está distribuindo sua mesada entre gastos e poupança |

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

- Chatbot interativo
- Integração com LLM
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que e o que foi utilizado durante o processo?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── dicionario_kids.json          # Dicionário Kids (JSON)
│   ├── extrato_mesada.csv            # Extrato Mesada (CSV)
│   ├── jovem_perfil.json             # Jovem Perfil (JSON)
│   └── missões_concluidas.csv        # Missõe Concluídas (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # Código Fonte em python
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

