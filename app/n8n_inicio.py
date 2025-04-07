import streamlit as st

def app():
    st.markdown("""
    # Manual de Automação e N8N

    ## Introdução
    Este guia fornece instruções básicas para configurar e trabalhar com o N8N, uma ferramenta poderosa para automação de fluxos de trabalho.

    ---

    ## Prompt
    ### O que é?
    Um **prompt** é uma entrada de texto ou comando que orienta a execução de uma tarefa ou fluxo no N8N.

    ### Exemplo:
    - Configurar um nó para receber um prompt de entrada do usuário:
      ```bash
      "Qual é o seu nome?"
      ```

    ---

    ## Base de Conhecimento
    ### O que é?
    A base de conhecimento é um repositório de informações que pode ser usado para alimentar fluxos automatizados.

    ### Exemplo:
    - Criar um nó que consulta uma base de dados para buscar informações:
      ```sql
      SELECT * FROM usuarios WHERE ativo = 1;
      ```

    ---

    ## APIs e Integrações
    ### O que são?
    APIs permitem que o N8N se conecte a serviços externos para enviar ou receber dados.

    ### Exemplo:
    - Configurar um nó HTTP para consumir uma API REST:
      ```json
      {
        "method": "GET",
        "url": "https://api.exemplo.com/usuarios",
        "headers": {
          "Authorization": "Bearer SEU_TOKEN"
        }
      }
      ```

    ---

    ## Webhooks
    ### O que são?
    Webhooks são URLs que recebem dados em tempo real de outros sistemas.

    ### Exemplo:
    - Configurar um nó webhook no N8N para receber notificações:
      ```bash
      POST https://seu-n8n.com/webhook/novo_usuario
      ```

    ---

    ## Fluxo
    ### O que é?
    Um fluxo no N8N é uma sequência de nós conectados que executam tarefas automatizadas.

    ### Exemplo:
    - Criar um fluxo que recebe dados de um webhook, processa e envia para uma API:
      ```text
      Webhook -> Transformação -> API
      ```

    ---

    ## Temperatura
    ### O que é?
    A temperatura é um parâmetro usado em modelos de IA para controlar a aleatoriedade das respostas.

    ### Exemplo:
    - Configurar a temperatura em um nó de IA:
      ```json
      {
        "temperature": 0.7
      }
      ```

    ---

    ## Top-p
    ### O que é?
    O Top-p é outro parâmetro usado em modelos de IA para limitar as respostas a um subconjunto mais provável.

    ### Exemplo:
    - Configurar o Top-p em um nó de IA:
      ```json
      {
        "top_p": 0.9
      }
      ```

    ---

    ## Modelos de IA
    ### O que são?
    Modelos de IA são algoritmos treinados para realizar tarefas específicas, como processamento de linguagem natural.

    ### Exemplo:
    - Configurar um nó para usar um modelo GPT:
      ```json
      {
        "model": "gpt-4",
        "prompt": "Explique o que é N8N."
      }
      ```

    ---

    ## Dicas Finais
    - Explore a documentação oficial do N8N para aprender mais sobre cada funcionalidade.
    - Teste seus fluxos em um ambiente seguro antes de colocá-los em produção.
    - Use integrações e APIs para expandir as possibilidades de automação.

    Este manual cobre os fundamentos necessários para começar a criar fluxos de automação com o N8N de forma eficiente e organizada. 🚀
    """)



