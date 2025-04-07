import streamlit as st

def app():
    st.markdown("""
    # Manual de Dockerfile

    Este guia cobre as principais instruções de um Dockerfile e explica como utilizá-las para construir e configurar imagens Docker.

    ---

    ## **FROM**
    Define a imagem base para o container.
    ```dockerfile
    FROM ubuntu:latest  # Usando a imagem base do Ubuntu mais recente
    ```

    ---

    ## **RUN**
    Executa comandos no container durante a criação da imagem.
    ```dockerfile
    RUN apt-get update && apt-get install -y curl  # Atualiza pacotes e instala o curl
    ```

    ---

    ## **WORKDIR**
    Define o diretório de trabalho dentro do container.
    ```dockerfile
    WORKDIR /app  # Define o diretório de trabalho como /app
    ```

    ---

    ## **COPY**
    Copia arquivos do host para o sistema de arquivos do container.
    ```dockerfile
    COPY . /app  # Copia todos os arquivos do diretório atual para /app no container
    ```

    ---

    ## **ADD**
    Adiciona arquivos ou baixa diretamente de uma URL para o container.
    ```dockerfile
    ADD https://example.com/file.tar.gz /app/  # Baixa e adiciona um arquivo ao container
    ```

    ---

    ## **LABEL**
    Adiciona metadados à imagem.
    ```dockerfile
    LABEL maintainer="seuemail@exemplo.com"  # Define o mantenedor da imagem
    ```

    ---

    ## **ENV**
    Define variáveis de ambiente que podem ser usadas pelo container.
    ```dockerfile
    ENV PORT=8080  # Define a variável de ambiente PORT com o valor 8080
    ```

    ---

    ## **VOLUME**
    Cria um ponto de montagem para persistência de dados.
    ```dockerfile
    VOLUME /data  # Cria um volume para persistir dados no diretório /data
    ```

    ---

    ## **ARG**
    Define variáveis para serem passadas na criação da imagem.
    ```dockerfile
    ARG APP_VERSION=1.0  # Define uma variável de build chamada APP_VERSION
    ```

    ---

    ## **EXPOSE**
    Informa ao Docker que a imagem expõe uma porta específica.
    ```dockerfile
    EXPOSE 8080  # Expõe a porta 8080
    ```

    ---

    ## **USER**
    Define o usuário que executará os comandos no container.
    ```dockerfile
    USER nonrootuser  # Define um usuário não root para executar os comandos
    ```

    ---

    ## **CMD**
    Especifica o comando padrão a ser executado quando o container inicia.
    ```dockerfile
    CMD ["python", "app.py"]  # Executa o app.py com Python
    ```

    ---

    ## **ENTRYPOINT**
    Define o executável principal do container.
    ```dockerfile
    ENTRYPOINT ["python"]  # Define Python como o executável principal
    CMD ["app.py"]         # Passa app.py como argumento para o ENTRYPOINT
    ```

    ---

    ## **Exemplo para Aplicativo Python**
    ```dockerfile
    # Usando uma imagem base do Python
    FROM python:3.9-slim

    # Define o diretório de trabalho
    WORKDIR /app

    # Copia os arquivos do projeto para o container
    COPY requirements.txt .  # Copia o arquivo de dependências
    COPY app.py .            # Copia o arquivo principal do app

    # Instala as dependências do Python
    RUN pip install --no-cache-dir -r requirements.txt

    # Expõe a porta 5000 para o Flask
    EXPOSE 5000

    # Define o comando padrão para iniciar o app
    CMD ["python", "app.py"]
    ```

    ---

    ## **Exemplo para Aplicativo Node.js**
    ```dockerfile
    # Usando uma imagem base do Node.js
    FROM node:16

    # Define o diretório de trabalho
    WORKDIR /usr/src/app

    # Copia os arquivos do projeto para o container
    COPY package*.json ./  # Copia os arquivos de dependências do Node.js
    COPY . .               # Copia todo o código do projeto

    # Instala as dependências do Node.js
    RUN npm install

    # Expõe a porta 3000 para o Node.js
    EXPOSE 3000

    # Define o comando padrão para iniciar o app
    CMD ["npm", "start"]
    ```

    ---

    Este manual cobre os fundamentos necessários para criar e configurar imagens Docker com um Dockerfile. 🚀
    """)