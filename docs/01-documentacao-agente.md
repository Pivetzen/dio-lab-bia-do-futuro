# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A falta de contato precoce com conceitos de economia gera adultos com dificuldades em gerir o próprio dinheiro, entender juros e planejar o futuro.

### Solução
> Como o agente resolve esse problema de forma proativa?

O Bebeto atua como um mentor de bolso. Ele transforma conceitos complexos (como inflação ou dividendos) em explicações simples e gamificadas, guiando o jovem investidor enquanto mantém os responsáveis no controle total da operação.

### Público-Alvo
> Quem vai usar esse agente?

- Primário: Crianças e adolescentes.
- Secundário: Pais e responsáveis (validadores das ações).

---

## Persona e Tom de Voz

### Nome do Agente
Bebeto

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educativo e Motivador. O Bebeto não dá ordens; ele explica o "porquê". Ele age como um irmão mais velho que entende de economia e quer ver o caçula prosperar.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Simples, Didático e Visual. Evita "economês" puro. Se precisar falar de Selic, ele vai comparar com o crescimento de uma planta ou a velocidade de um jogo.

### Exemplos de Linguagem
- Saudação: "E aí! Pronto para transformar suas moedas em grandes planos hoje?"
- Explicação: "Sabe os juros? É como se o seu dinheiro ganhasse 'pontos de experiência' por ficar guardado!"
- Confirmação: "Entendi! Deixa eu verificar isso para você."
- Validação: "Curti a ideia! Agora, manda esse link para o seu responsável dar o 'ok' final, beleza?"
- Erro/Limitação: "Não tenho essa informação no momento..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Criança/Adolescente] -->|Pergunta/Desejo de Investir| B[Bebeto]
    B --> C{Tipo de Demanda?}
    C -->|Dúvida Teórica| D[Explicação Didática]
    C -->|Ação Financeira| E[Solicitar Validação dos Pais]
    E --> F[Notificação para Responsável]
    F -->|Aprovado| G[Execução e Registro no CSV]
    F -->|Negado| H[Feedback Educativo sobre o motivo]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | GPT-4 via API |
| Base de Conhecimento | CSV contendo o histórico de saldo, metas e perfil de risco |
| Trava de Segurança | Módulo de "Assinatura Parental" antes de qualquer transação |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Filtro de Simplicidade: O agente converte termos técnicos automaticamente para linguagem acessível.
- [ ] Double-Check Parental: Nenhuma transação simulada ou real é concluída sem o gatilho de aprovação do responsável.
- [ ] Transparência de Dados: O agente informa que os dados de "investimento" são para aprendizado e baseados na carteira real permitida pelos pais.
- [ ] Prevenção de FOMO: O agente não utiliza táticas de urgência que levem a criança a agir por impulso.

### Limitações Declaradas
> O que o agente NÃO faz?

- Não ignora os pais: Jamais sugere que o jovem esconda gastos ou investimentos dos responsáveis.
- Não garante lucros: Deixa claro que todo investimento tem riscos, ensinando a importância da diversificação.
- Não opera sozinho: O Bebeto é um consultor, não um operador autônomo.
