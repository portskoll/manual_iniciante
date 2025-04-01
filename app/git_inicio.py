import streamlit as st

def app():
    st.markdown("""
    # Guia Completo: Trabalhando com Git e GitHub

    ## Introdução
    O **Git** é uma ferramenta de controle de versão amplamente usada para rastrear mudanças no código-fonte e colaborar entre desenvolvedores. O **GitHub**, por sua vez, é uma plataforma baseada na web que utiliza o Git para facilitar a hospedagem e o gerenciamento de repositórios.

    ---

    ## Configuração Inicial

    - **Verificar se o Git está instalado**:
    ```bash
    git --version
    ```

    - **Configurar suas credenciais no Git**:
    ```bash
    git config --global user.name "Seu Nome"
    git config --global user.email "seu-email@example.com"
    ```

    - **Verificar configurações atuais**:
    ```bash
    git config --list
    ```

    ---

    ## Comandos Essenciais do Git

    ### Inicializando um Repositório

    - **Criar um novo repositório Git local**:
    ```bash
    git init
    ```

    - **Clonar um repositório existente do GitHub**:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```

    ### Gerenciando Alterações

    - **Verificar o status do repositório**:
    ```bash
    git status
    ```

    - **Adicionar arquivos específicos para serem rastreados**:
    ```bash
    git add <NOME_ARQUIVO>
    ```

    - **Adicionar todas as alterações**:
    ```bash
    git add .
    ```

    - **Criar um commit com uma mensagem descritiva**:
    ```bash
    git commit -m "Descrição das alterações"
    ```

    - **Exibir o histórico de commits**:
    ```bash
    git log
    ```

    ### Sincronizando com o GitHub

    - **Conectar o repositório local a um remoto**:
    ```bash
    git remote add origin <URL_DO_REPOSITORIO>
    ```

    - **Enviar alterações para o GitHub**:
    ```bash
    git push origin main
    ```

    - **Atualizar o repositório local com mudanças do remoto**:
    ```bash
    git pull origin main
    ```

    ---

    ## Branches no Git

    - **Criar uma nova branch**:
    ```bash
    git branch <NOME_BRANCH>
    ```

    - **Mudar para uma branch existente**:
    ```bash
    git checkout <NOME_BRANCH>
    ```

    - **Criar e mudar para uma nova branch ao mesmo tempo**:
    ```bash
    git checkout -b <NOME_BRANCH>
    ```

    - **Mesclar uma branch à branch atual**:
    ```bash
    git merge <NOME_BRANCH>
    ```

    - **Listar todas as branches**:
    ```bash
    git branch
    ```

    - **Remover uma branch**:
    ```bash
    git branch -d <NOME_BRANCH>
    ```

    ---

    ## Resolvendo Conflitos

    - **Após um conflito de merge, resolver manualmente os arquivos indicados**:
      1. Edite os arquivos com conflitos.
      2. Remova as marcações de conflitos (`<<<<<<<`, `=======`, `>>>>>>>`).
      3. Adicione as alterações resolvidas:
         ```bash
         git add <NOME_ARQUIVO>
         ```
      4. Finalize o merge com um commit:
         ```bash
         git commit -m "Resolvido o conflito"
         ```

    ---

    ## Trabalhando com Tags

    - **Criar uma tag**:
    ```bash
    git tag <NOME_TAG>
    ```

    - **Exibir todas as tags**:
    ```bash
    git tag
    ```

    - **Empurrar tags para o repositório remoto**:
    ```bash
    git push origin <NOME_TAG>
    ```

    - **Remover uma tag localmente**:
    ```bash
    git tag -d <NOME_TAG>
    ```

    - **Remover uma tag do repositório remoto**:
    ```bash
    git push origin --delete <NOME_TAG>
    ```

    ---

    ## Comandos Úteis para Limpeza

    - **Restaurar um arquivo modificado ao estado original**:
    ```bash
    git checkout -- <NOME_ARQUIVO>
    ```

    - **Remover mudanças não commitadas no repositório**:
    ```bash
    git reset --hard
    ```

    - **Excluir todos os arquivos não rastreados**:
    ```bash
    git clean -f
    ```

    ---

    ## Trabalhando com GitHub

    - **Criar um repositório no GitHub**:
      Acesse o site do [GitHub](https://github.com) e clique em "New Repository". 

    - **Gerar uma chave SSH para o GitHub**:
      1. Gere a chave:
         ```bash
         ssh-keygen -t rsa -b 4096 -C "seu-email@example.com"
         ```
      2. Adicione a chave ao agente SSH:
         ```bash
         eval $(ssh-agent -s)
         ssh-add ~/.ssh/id_rsa
         ```
      3. Adicione a chave no GitHub em **Settings > SSH and GPG keys**.

    - **Clonar um repositório usando SSH**:
    ```bash
    git clone git@github.com:<NOME_USUARIO>/<REPOSITORIO>.git
    ```

    ---

    ## Contribuição em Projetos Open Source

    - **Fazer um fork de um repositório**:
      Clique no botão "Fork" no GitHub para criar uma cópia do repositório no seu perfil.

    - **Clonar o repositório forkado**:
    ```bash
    git clone <URL_FORK>
    ```

    - **Criar uma nova branch para suas alterações**:
    ```bash
    git checkout -b <NOME_BRANCH>
    ```

    - **Enviar suas alterações para o fork**:
    ```bash
    git push origin <NOME_BRANCH>
    ```

    - **Abrir um Pull Request (PR)**:
      No GitHub, clique em "Pull Requests" no repositório original para propor suas alterações.

    ---

    ## Dicas Finais

    - Sempre crie commits com mensagens claras e descritivas.
    - Use branches para organizar diferentes funcionalidades ou correções.
    - Sincronize frequentemente com o repositório remoto para evitar conflitos.

    Esse guia cobre os comandos mais úteis do Git e as práticas fundamentais para trabalhar com o GitHub. Explore e pratique para dominar o fluxo de trabalho! 🚀
    """)


