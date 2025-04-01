import streamlit as st

def app():
    st.markdown("""
    # Manual de Configuração e Uso do Python

    ## Introdução
    Este guia fornece instruções básicas para configurar e trabalhar com o Python em seu ambiente local, incluindo a criação de ambientes virtuais e a instalação de pacotes.

    ---

    ## Configuração Inicial

    1. **Baixar e Instalar o Python**:
       - Acesse o site oficial do Python: [python.org](https://www.python.org/).
       - Baixe a versão desejada e instale em uma pasta na raiz do seu disco (ex.: `C:\Python312`).

    2. **Criar uma Pasta para o Projeto**:
       - Crie uma pasta no seu disco onde será desenvolvido o projeto.

    3. **Abrir o Projeto no VS Code**:
       - Abra o Visual Studio Code e carregue a pasta que você criou para o projeto.

    4. **Abrir um Terminal no VS Code**:
       - No VS Code, abra o terminal integrado (atalho: `CTRL + ``).

    ---

    ## Ambiente Virtual

    ### Criando o Ambiente Virtual
    - Para criar um ambiente virtual, execute o comando abaixo (usando o caminho da versão do Python que deseja utilizar):
      ```bash
      "C:\caminho_para_python\python.exe" -m venv venv
      ```
      > Exemplo: `"C:\Python312\python.exe" -m venv venv`

    ### Ativando o Ambiente Virtual
    - No terminal, ative o ambiente virtual com o comando:
      ```bash
      .\\venv\Scripts\\activate
      ```

    ### Desativando o Ambiente Virtual
    - Para desativar o ambiente virtual, use:
      ```bash
      deactivate
      ```

    ### Configurando o Python Interpreter no VS Code
    - No VS Code, pressione `CTRL + SHIFT + P` e procure por **Python: Select Interpreter**. Escolha o interpretador do ambiente virtual recém-criado.

    ---

    ## Trabalhando com Pacotes Python

    1. **Verificar a Versão do Python**:
       ```bash
       python --version
       ```

    2. **Instalar Pacotes no Projeto**:
       - Use o comando abaixo para instalar pacotes:
         ```bash
         pip install nome_do_pacote
         ```

    3. **Ver os Pacotes Instalados**:
       - Liste todos os pacotes instalados no ambiente virtual e suas versões:
         ```bash
         pip list
         ```

    4. **Criar o Arquivo `requirements.txt`**:
       - Gere um arquivo `requirements.txt` contendo todos os pacotes instalados no ambiente virtual:
         ```bash
         pip freeze > requirements.txt
         ```
       - O arquivo será gerado na raiz do projeto e pode ser utilizado para reproduzir o ambiente em outra máquina.

    ---

    ## Organização do Projeto

    1. **Estrutura de Diretórios**:
       - Crie uma pasta dentro do projeto chamada, por exemplo, `app`, para organizar os arquivos Python.

    2. **Rodar Arquivos Python**:
       - Navegue até a pasta do arquivo no terminal (ex.: `cd app`) e execute:
         ```bash
         python nome_arquivo_python.py
         ```

    ---

    ## Dicas Finais
    - Certifique-se de criar o ambiente virtual em cada novo projeto para isolar dependências.
    - Use o arquivo `requirements.txt` para replicar o ambiente:
      ```bash
      pip install -r requirements.txt
      ```

    Este manual cobre os fundamentos necessários para configurar seu ambiente Python e começar a desenvolver projetos de forma organizada e eficiente. 🚀
    """)



