import streamlit as st
from PIL import Image


def app():

    imagem = Image.open("./img/devops.png")

    # Exibe a imagem com uma legenda e ajusta a largura para usar a largura da coluna
    st.image(imagem, caption="Esquema de processo DevOps", use_container_width=True)

    st.markdown("""
    # Guia Completo: Implementando DevOps na Empresa

    ## Introdução
    DevOps é uma filosofia que integra o **Desenvolvimento (Dev)** e as **Operações (Ops)** para melhorar a colaboração, automatizar processos e entregar software com alta qualidade de forma contínua. Ao derrubar as barreiras entre equipes, o DevOps acelera a entrega de valor e promove uma cultura de melhoria contínua e inovação.

    ---

    ## O Modelo CALMS

    O modelo **CALMS** representa os pilares essenciais do DevOps:

    - **Cultura (Culture):**  
      Incentiva a colaboração e a transparência entre equipes, promovendo um ambiente de confiança mútua e comunicação constante.

    - **Automatização (Automation):**  
      Automatizar builds, testes, deploys e monitoramento reduz erros manuais e acelera o fluxo de trabalho.

    - **Lean (Enxuto):**  
      Adotar práticas enxutas elimina desperdícios e otimiza processos, focando na entrega rápida de valor.

    - **Medida (Measurement):**  
      Monitoramento contínuo por meio de métricas e KPIs é crucial para identificar gargalos e promover aprimoramentos.

    - **Compartilhamento (Sharing):**  
      O compartilhamento de informações e feedbacks constantes fortalece a equipe e possibilita ajustes rápidos nos processos.

    ---

    ## Implementando DevOps na Empresa

    Para adotar uma cultura DevOps que realmente impulsione a produtividade, considere os seguintes passos:

    1. **Estabeleça uma Cultura Colaborativa**
       - Quebre as barreiras entre desenvolvimento e operações.
       - Realize reuniões regulares para alinhamento e feedback.
       - Promova treinamentos e incentive a troca de conhecimentos.

    2. **Automatize os Processos**
       - Implemente Integração Contínua (CI) e Entrega Contínua (CD) utilizando ferramentas como Jenkins, GitLab CI/CD ou CircleCI.
       - Automatize testes, builds e deploys para reduzir erros e aumentar a velocidade das entregas.

    3. **Adote Metodologias Lean e Ágeis**
       - Utilize Scrum ou Kanban para organizar o trabalho e promover a melhoria contínua.
       - Ajuste os processos para eliminar atividades desnecessárias e focar na eficiência.

    4. **Monitore e Meça Desempenho**
       - Utilize ferramentas de monitoramento como Prometheus, Grafana ou a stack ELK (Elasticsearch, Logstash, Kibana) para coletar métricas essenciais.
       - Estabeleça KPIs que realmente reflitam a performance e a qualidade do software entregue.

    5. **Incentive o Compartilhamento**
       - Utilize repositórios Git e mantenha a documentação atualizada.
       - Crie canais de comunicação e feedback entre todas as áreas envolvidas.

    ---

    ## Ferramentas Recomendadas

    **CI/CD e Automação:**
    ```bash
    # Exemplos: Jenkins, GitLab CI/CD, CircleCI
    ```

    **Infraestrutura como Código:**
    ```bash
    # Exemplos: Ansible, Terraform
    ```

    **Monitoramento e Logging:**
    ```bash
    # Exemplos: Prometheus, Grafana, ELK Stack, Splunk
    ```

    **Gerenciamento de Projetos:**
    ```bash
    # Exemplos: JIRA, Trello, Asana
    ```

    **Controle de Versão:**
    ```bash
    # Git (GitHub, GitLab, Bitbucket)
    ```

    ---

    ## Conclusão

    Implementar DevOps é uma jornada contínua que exige comprometimento com a melhoria dos processos e a colaboração entre equipes. Ao adotar o modelo **CALMS** e utilizar as ferramentas modernas disponíveis, sua empresa pode aumentar significativamente a produtividade, acelerar as entregas de software e criar um ambiente de trabalho mais inovador e colaborativo.

    Explore, adapte e otimize as práticas DevOps para atender às necessidades específicas do seu negócio e promover o sucesso contínuo!
    """, unsafe_allow_html=True)


