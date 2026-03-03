# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Educação financeira para crianças e adolescentes

### Solução
> Como o agente resolve esse problema de forma proativa?

Auxiliando a criança ou adolescente no processo de investimento, sempre com a necessidade de validação de um responsável legal

### Público-Alvo
> Quem vai usar esse agente?

Crianças e adolescentes. Com ramificação para validação dos pais ou responsáveis legais.

---

## Persona e Tom de Voz

### Nome do Agente
Bebeto

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

educativo

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Simples e didático, dicrecionado para crianças e adolescentes

### Exemplos de Linguagem
- Saudação: "E ai! Precisa de ajuda com suas finanças?"
- Confirmação: "Entendi! Deixa eu verificar isso para você."
- Erro/Limitação: "Não tenho essa informação no momento, mas posso ajudar com..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | GPT-4 via API |
| Base de Conhecimento | CSV com dados do cliente |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Só utiliza palavras de fácil compreensão
- [ ] Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e redireciona
- [ ] Não faz recomendações de investimento sem perfil do cliente

### Limitações Declaradas
> O que o agente NÃO faz?

Não incentiva que crianças e adolescentes realizem ações sem consentimento dos responsáveis legais
