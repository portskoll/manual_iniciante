import streamlit as st

def app():
    st.markdown("""
    # Docker: O Guia Definitivo para Desenvolvimento Moderno

    ## Introdução
    O Docker revolucionou a forma como desenvolvemos e implantamos aplicações, oferecendo uma solução elegante para o clássico problema "funciona na minha máquina". Com containers, você garante consistência entre ambientes de desenvolvimento, teste e produção.

    ---

    ## Configuração Inicial

    - **Primeiros Passos**:
      Comece instalando o Docker Desktop através do [site oficial](https://www.docker.com/products/docker-desktop). Esta ferramenta inclui tudo que você precisa para começar, incluindo Docker Engine, Docker CLI, Docker Compose e Docker Desktop Dashboard.
    
    - **Confirmando a Instalação**:
    ```bash
    docker --version
    docker info
    ```

    ---
                
    ## Ciclo de Vida de uma Aplicação Docker
    O processo de desenvolvimento com Docker segue um fluxo contínuo de construção, publicação e execução.
    Para atualizar ou iniciar uma aplicação, siga estes passos:

    ##### Nota: Se já existir uma imagem (local ou no Docker Hub), pule direto para o passo (2).
    
    - (1) Construa a imagem da sua aplicação
    ```bash
    docker build -t <NOME_DO_REPOSITORIO>/<NOME_IMAGEM>:<VERSAO> .
    ```
    - Publique a imagem no DockerHub (opcional, mas recomendado para equipes)
    ```bash
    docker push <NOME_DO_REPOSITORIO>/<NOME_IMAGEM>:<VERSAO>
    ```
    - Remova o container existente (se necessário)
    ```bash
    docker rm <ID_CONTAINER> -f
    ```
    - Baixe a última versão da imagem
    ```bash
    docker pull <NOME_DO_REPOSITORIO>/<NOME_IMAGEM>:<VERSAO>
    ```   
    - (2) Execute o container
    ```bash
    docker run -d -p 9090:8501 <NOME_DO_REPOSITORIO>/<NOME_IMAGEM>:<VERSAO>
    ```                      

    ### Estrutura do Dockerfile
    O Dockerfile é o blueprint da sua aplicação. Abaixo um exemplo prático e bem comentado:
    ```bash
    # Imagem base otimizada para Python
    FROM python:3.12-slim
    
    # Define o diretório de trabalho
    WORKDIR /app
    
    # Copia os arquivos da aplicação
    COPY app/ /app
    COPY requirements.txt .
    
    # Instala as dependências
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Configura a porta que será exposta
    EXPOSE 8501
    
    # Comando para iniciar a aplicação
    CMD ["streamlit", "run", "main.py"]
    ```

    ---

    ## Gerenciamento de Containers

    ### Comandos Essenciais para Containers
    - **Listar os containers ativos**:
    ```bash
    docker container ls
    ```

    - **Listar todos os containers (ativos e parados)**:
    ```bash
    docker container ls -a
    ```

    - **Iniciar um container parado**:
    ```bash
    docker start <CONTAINER_ID>
    ```

    - **Parar um container ativo**:
    ```bash
    docker stop <CONTAINER_ID>
    ```

    - **Forçar a interrupção de um container (Kill)**:
    ```bash
    docker container kill <CONTAINER_ID>
    ```

    - **Remover um container**:
    ```bash
    docker rm <CONTAINER_ID>
    ```

    - **Forçar a remoção de um container ativo**:
    ```bash
    docker rm -f <CONTAINER_ID>
    ```

    ### Debug e Logs
    - **Exibir logs de um container**:
    ```bash
    docker logs <CONTAINER_ID>
    ```

    - **Acompanhar os logs em tempo real**:
    ```bash
    docker logs -f <CONTAINER_ID>
    ```

    - **Inspecionar detalhes de um container**:
    ```bash
    docker inspect <CONTAINER_ID>
    ```

    ---

    ## Gerenciamento de Imagens

    ### Comandos Essenciais para Imagens
    - **Listar imagens disponíveis**:
    ```bash
    docker images
    ```

    - **Baixar uma imagem do DockerHub**:
    ```bash
    docker pull <NOME_IMAGEM>
    ```

    - **Remover uma imagem local**:
    ```bash
    docker rmi <NOME_IMAGEM>
    ```

    - **Construir uma nova imagem a partir de um Dockerfile**:
    ```bash
    docker build -t <NOME_IMAGEM>:<VERSAO> .
    ```

    - **Renomear ou alterar a tag de uma imagem**:
    ```bash
    docker tag <NOME_IMAGEM> <NOVO_NOME>:<NOVA_TAG>
    ```

    ---

    ## Criando e Gerenciando Serviços com Docker

    ### Testando Serviços Locais com Containers
    - **Rodar um servidor Nginx em uma porta específica**:
    ```bash
    docker run -d -p 8080:80 nginx
    ```

    - **Rodar um banco PostgreSQL com variáveis de ambiente**:
    ```bash
    docker run -d -e POSTGRES_DB=ecommerce -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=senha123 -p 5432:5432 postgres
    ```

    ---

    ## Trabalhando com Volumes

    - **Criar um volume para persistência de dados**:
    ```bash
    docker volume create <NOME_VOLUME>
    ```

    - **Listar os volumes existentes**:
    ```bash
    docker volume ls
    ```

    - **Inspecionar um volume**:
    ```bash
    docker volume inspect <NOME_VOLUME>
    ```

    - **Remover um volume**:
    ```bash
    docker volume rm <NOME_VOLUME>
    ```

    - **Montar um volume em um container**:
    ```bash
    docker run -v <NOME_VOLUME>:/caminho_no_container <IMAGEM>
    ```

    ---

    ## Redes no Docker

    - **Listar as redes disponíveis**:
    ```bash
    docker network ls
    ```

    - **Criar uma nova rede**:
    ```bash
    docker network create <NOME_REDE>
    ```

    - **Conectar um container a uma rede específica**:
    ```bash
    docker network connect <NOME_REDE> <CONTAINER_ID>
    ```

    - **Desconectar um container de uma rede**:
    ```bash
    docker network disconnect <NOME_REDE> <CONTAINER_ID>
    ```

    ---

    ## Avançado: Otimizando e Limpando Recursos

    - **Remover todos os containers parados**:
    ```bash
    docker container prune
    ```

    - **Remover todas as imagens não utilizadas**:
    ```bash
    docker image prune -a
    ```

    - **Remover volumes órfãos (não utilizados por nenhum container)**:
    ```bash
    docker volume prune
    ```

    ---

    ## Dicas Finais

    - **Utilizar o Docker Compose para orquestrar múltiplos containers**:
      Aprenda o básico sobre [Docker Compose](https://docs.docker.com/compose/) para gerenciar ambientes mais complexos.

    - **Gerar e inspecionar o arquivo Dockerfile para entender a base de uma imagem**:
    ```bash
    docker history <NOME_IMAGEM>
    ```

    Esse guia cobre tudo o que você precisa para começar e avançar no uso do Docker. Explore, pratique e aproveite o poder dos containers!
    """)

