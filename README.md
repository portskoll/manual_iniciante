# Manual Iniciante com Streamlit

Este projeto é uma aplicação desenvolvida com [Streamlit](https://streamlit.io/) que serve como um guia interativo para iniciantes em diversas tecnologias, como Python, Docker, DevOps, Kubernetes, Git e Linux. A aplicação também inclui uma seção "Sobre Mim" para apresentar o autor.

## Estrutura do Projeto

### Principais Arquivos

- **`app/main.py`**: Arquivo principal que gerencia a navegação entre as diferentes seções do guia.
- **`app/about.py`**: Seção "Sobre Mim", apresentando o autor.
- **`app/python_inicio.py`**: Guia básico de configuração e uso do Python.
- **`app/docker_inicio.py`**: Guia introdutório ao Docker.
- **`app/devops_inicio.py`**: Guia sobre práticas e ferramentas DevOps.
- **`app/kubernetes_inicio.py`**: Guia introdutório ao Kubernetes.
- **`app/git_inicio.py`**: Guia básico de uso do Git e GitHub.
- **`app/linux_inicio.py`**: Guia sobre comandos e estrutura de diretórios no Linux.
- **`Dockerfile`**: Configuração para criar uma imagem Docker da aplicação.
- **`requirements.txt`**: Lista de dependências do projeto.

## Pré-requisitos

- Python 3.12 ou superior
- [Streamlit](https://streamlit.io/)
- Docker (opcional, para rodar a aplicação em contêiner)

## Como Executar o Projeto

### 1. Configuração Local

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd manual_iniciante
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   streamlit run app/main.py
   ```

### 2. Usando Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t manual_iniciante .
   ```

2. Execute o contêiner:
   ```bash
   docker run -p 8501:8501 manual_iniciante
   ```

3. Acesse a aplicação no navegador em: [http://localhost:8501](http://localhost:8501)

## Funcionalidades

- **Python**: Guia para configuração de ambiente virtual, instalação de pacotes e organização de projetos.
- **Docker**: Introdução ao uso de contêineres e comandos essenciais.
- **DevOps**: Práticas e ferramentas para integração e entrega contínua.
- **Kubernetes**: Noções básicas de orquestração de contêineres.
- **Git**: Comandos básicos e fluxo de trabalho com Git e GitHub.
- **Linux**: Estrutura de diretórios e comandos úteis.
- **Sobre Mim**: Apresentação do autor.

## Estrutura de Navegação

A navegação entre as seções é feita por meio de um menu lateral, implementado com o componente `streamlit-option-menu`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.


## Contato

Para dúvidas ou sugestões, entre em contato pelo [LinkedIn](https://www.linkedin.com/in/portskoll).
````