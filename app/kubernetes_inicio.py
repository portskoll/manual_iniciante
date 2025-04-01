import streamlit as st

def app():
    st.markdown("""
    # Guia Completo: Docker e Kubernetes

    ## Introdução
    O Kubernetes (K8s) é uma plataforma de orquestração de contêineres que automatiza a implantação, o dimensionamento e o gerenciamento de aplicações em contêineres.

    ## Pré-requisitos
    - **Docker Desktop**: Necessário para criar e gerenciar contêineres
    - **kubectl**: CLI (Interface de Linha de Comando) do Kubernetes
    - **K3d**: Ferramenta para criar clusters Kubernetes locais usando Docker
    
    ## Arquitetura Básica do Kubernetes
    - **Pod**: Menor unidade do Kubernetes
    - **Node**: Máquina física ou virtual que executa os pods
    - **Cluster**: Conjunto de nodes gerenciados pelo Kubernetes
    - **Control Plane**: Componente que gerencia o cluster

    ---

    ## 1. Gerenciamento de Clusters

    ### Criação e Gerenciamento

    Criar cluster básico:
    ```bash
    k3d cluster create meu-cluster
    ```

    Criar cluster com múltiplos nodes:
    ```bash
    k3d cluster create --servers 3 --agents 3 --name cluster-prod
    ```

    Criar cluster com porta específica:
    ```bash
    k3d cluster create --port "8080:30000@loadbalancer"
    ```

    Listar clusters:
    ```bash
    k3d cluster list
    ```

    Deletar cluster:
    ```bash
    k3d cluster delete meu-cluster
    ```

    ### Contexto e Configuração

    Ver configuração atual:
    ```bash
    kubectl config view
    ```

    Mudar contexto:
    ```bash
    kubectl config use-context meu-contexto
    ```

    Ver todos os contextos:
    ```bash
    kubectl config get-contexts
    ```

    ---

    ## 2. Operações com Pods e Deployments

    ### Pods

    Listar todos os pods:
    ```bash
    kubectl get pods
    ```

    Listar pods com informações detalhadas:
    ```bash
    kubectl get pods -o wide
    ```

    Listar pods em todos os namespaces:
    ```bash
    kubectl get pods --all-namespaces
    ```

    Descrever pod específico:
    ```bash
    kubectl describe pod nome-do-pod
    ```

    Executar comando dentro do pod:
    ```bash
    kubectl exec -it nome-do-pod -- /bin/bash
    ```

    Ver logs do pod:
    ```bash
    kubectl logs nome-do-pod
    ```

    Acompanhar logs em tempo real:
    ```bash
    kubectl logs -f nome-do-pod
    ```

    ### Deployments

    Criar deployment:
    ```bash
    kubectl create deployment nginx --image=nginx
    ```

    Escalar deployment:
    ```bash
    kubectl scale deployment nginx --replicas=3
    ```

    Atualizar imagem:
    ```bash
    kubectl set image deployment/nginx nginx=nginx:1.19
    ```

    Ver histórico de deployment:
    ```bash
    kubectl rollout history deployment/nginx
    ```

    Fazer rollback:
    ```bash
    kubectl rollout undo deployment/nginx
    ```

    Rollback para revisão específica:
    ```bash
    kubectl rollout undo deployment/nginx --to-revision=2
    ```

    ---

    ## 3. Serviços e Networking

    ### Services

    Criar service:
    ```bash
    kubectl expose deployment nginx --port=80 --type=LoadBalancer
    ```

    Listar services:
    ```bash
    kubectl get services
    ```

    Port-forward:
    ```bash
    kubectl port-forward service/nginx 8080:80
    ```

    ### Networking

    DNS lookup dentro do cluster:
    ```bash
    kubectl run temp --rm -i --tty --image=busybox -- nslookup kubernetes.default
    ```

    Ver endpoints:
    ```bash
    kubectl get endpoints
    ```

    ---

    ## 4. Monitoramento e Diagnóstico

    ### Recursos do Cluster

    Ver todos os recursos:
    ```bash
    kubectl get all
    ```

    Ver consumo de recursos dos nodes:
    ```bash
    kubectl top nodes
    ```

    Ver consumo de recursos dos pods:
    ```bash
    kubectl top pods
    ```

    Ver eventos do cluster:
    ```bash
    kubectl get events --sort-by=.metadata.creationTimestamp
    ```

    ### Troubleshooting

    Verificar status dos componentes:
    ```bash
    kubectl get componentstatuses
    ```

    Descrever node:
    ```bash
    kubectl describe node nome-do-node
    ```

    Verificar logs do node:
    ```bash
    kubectl logs -n kube-system nome-do-node
    ```

    ---

    ## 5. Configuração e Segurança

    ### ConfigMaps e Secrets

    Criar ConfigMap:
    ```bash
    kubectl create configmap app-config --from-file=config.properties
    ```

    Criar Secret:
    ```bash
    kubectl create secret generic app-secret --from-literal=password=123456
    ```

    Listar ConfigMaps:
    ```bash
    kubectl get configmaps
    ```

    Listar Secrets:
    ```bash
    kubectl get secrets
    ```

    ### RBAC (Controle de Acesso)

    Listar roles:
    ```bash
    kubectl get roles --all-namespaces
    ```

    Listar role bindings:
    ```bash
    kubectl get rolebindings --all-namespaces
    ```

    ## Dicas Importantes
    1. Sempre use namespaces para organizar seus recursos
    2. Implemente limites de recursos (CPU/memória) para pods
    3. Utilize labels e annotations para melhor organização
    4. Mantenha backups regulares do cluster
    5. Monitore a saúde do cluster constantemente

    ## Boas Práticas
    - Use manifestos YAML para versionar configurações
    - Implemente health checks (liveness e readiness probes)
    - Utilize rolling updates para atualizações sem downtime
    - Configure auto-scaling quando necessário
    - Mantenha a segurança do cluster atualizada

    ---

    ## 6. Exemplo Prático: Implantação Flask + PostgreSQL

    ### Estrutura do Projeto
    Para este exemplo, precisaremos de dois arquivos de configuração:
    - `postgres-deployment.yaml`: Configuração do banco de dados
    - `flask-deployment.yaml`: Configuração da aplicação web

    ### Configuração do PostgreSQL
    Arquivo `postgres-deployment.yaml`:
    ```yaml
    # ConfigMap para variáveis não-sensíveis
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: postgres-config
    data:
      POSTGRES_DB: meuapp
      POSTGRES_USER: admin
    ---
    # Secret para senhas e dados sensíveis
    apiVersion: v1
    kind: Secret
    metadata:
      name: postgres-secret
    type: Opaque
    data:
      POSTGRES_PASSWORD: YWRtaW4xMjM=  # admin123 em base64
    ---
    # Volume persistente para dados
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: postgres-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
    ---
    # Deployment do PostgreSQL
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: postgres
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: postgres
      template:
        metadata:
          labels:
            app: postgres
        spec:
          containers:
            - name: postgres
              image: postgres:13
              ports:
                - containerPort: 5432
              envFrom:
                - configMapRef:
                    name: postgres-config
                - secretRef:
                    name: postgres-secret
              volumeMounts:
                - name: postgres-storage
                  mountPath: /var/lib/postgresql/data
          volumes:
            - name: postgres-storage
              persistentVolumeClaim:
                claimName: postgres-pvc
    ---
    # Serviço do PostgreSQL
    apiVersion: v1
    kind: Service
    metadata:
      name: postgres
    spec:
      selector:
        app: postgres
      ports:
        - port: 5432
      type: ClusterIP
    ```

    ### Configuração do Flask
    Arquivo `flask-deployment.yaml`:
    ```yaml
    # Deployment da aplicação Flask
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: flask-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: flask-app
      template:
        metadata:
          labels:
            app: flask-app
        spec:
          containers:
            - name: flask-app
              image: sua-imagem-flask:latest
              ports:
                - containerPort: 5000
              env:
                - name: DATABASE_URL
                  value: "postgresql://admin:admin123@postgres:5432/meuapp"
              readinessProbe:
                httpGet:
                  path: /health
                  port: 5000
                initialDelaySeconds: 5
                periodSeconds: 5
              livenessProbe:
                httpGet:
                  path: /health
                  port: 5000
                initialDelaySeconds: 15
                periodSeconds: 20
    ---
    # Serviço LoadBalancer para o Flask
    apiVersion: v1
    kind: Service
    metadata:
      name: flask-app
    spec:
      selector:
        app: flask-app
      ports:
        - port: 80
          targetPort: 5000
      type: LoadBalancer
    ```

    ### Aplicação Flask Básica
    Exemplo de código Flask compatível:
    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    import os

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db = SQLAlchemy(app)

    @app.route('/health')
    def health():
        return {'status': 'healthy'}

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    ```

    ### Comandos de Implantação

    Aplicar as configurações:
    ```bash
    kubectl apply -f postgres-deployment.yaml
    kubectl apply -f flask-deployment.yaml
    ```

    Verificar status dos pods:
    ```bash
    kubectl get pods
    ```

    Verificar serviços:
    ```bash
    kubectl get services
    ```

    Ver logs da aplicação:
    ```bash
    kubectl logs -l app=flask-app
    ```

    Remover a implantação:
    ```bash
    kubectl delete -f flask-deployment.yaml
    kubectl delete -f postgres-deployment.yaml
    ```

    ### Observações Importantes
    1. **Segurança**:
       - Em produção, use gerenciadores de segredos apropriados
       - Evite armazenar senhas em arquivos de configuração
       - Configure network policies adequadamente

    2. **Persistência**:
       - Os dados do PostgreSQL são persistentes através do PVC
       - Considere backup regular dos dados

    3. **Escalabilidade**:
       - A aplicação Flask está configurada com 3 réplicas
       - O LoadBalancer distribui o tráfego automaticamente

    4. **Monitoramento**:
       - Configurados health checks para garantir disponibilidade
       - Use as probes para garantir que a aplicação está saudável

    5. **Pré-requisitos**:
       - Cluster Kubernetes configurado
       - Imagem Docker da aplicação Flask disponível
       - Provedor de LoadBalancer configurado
       - Storage class disponível para PVC
    """)