import streamlit as st

def app():
    st.title("About Me / Sobre Mim")
    
    # English Version
    st.markdown("""
    ## Hello, World! 👋

    My name is Henrique Kolle Portella, and I am passionate about technology, innovation, and collaboration.
    I am recently specializing in DevOps, and I love solving complex challenges while continuing to learn and grow.

    ### Skills:
    - 🌐 **Web Development**
    - 📊 **Data Analysis**
    - 🤖 **Artificial Intelligence**
    - 📦 **DevOps & Cloud Computing**
    
    ### Mission:
    I believe that technology is a tool to make the world a better place. My mission is to create solutions that improve lives, foster innovation, and bridge the gap between people and possibilities.

    If you’d like to connect, feel free to reach out through LinkedIn!
    """)

    # Portuguese Version
    st.markdown("""
    ## Olá, Mundo! 👋

    Meu nome é Henrique Kolle Portella, e sou apaixonado por tecnologia, inovação e colaboração.  
    Estou recentemente me especializando em DevOps, e adoro resolver desafios complexos enquanto continuo aprendendo e crescendo.

    ### Habilidades:
    - 🌐 **Desenvolvimento Web**
    - 📊 **Análise de Dados**
    - 🤖 **Inteligência Artificial**
    - 📦 **DevOps & Computação em Nuvem**
    
    ### Missão:
    Acredito que a tecnologia é uma ferramenta para tornar o mundo um lugar melhor. Minha missão é criar soluções que melhorem vidas, fomentem a inovação e aproximem pessoas de novas possibilidades.

    Se quiser entrar em contato, fique à vontade para me encontrar no LinkedIn!
    """)

    # LinkedIn Link
    st.markdown("[Connect with me on LinkedIn / Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/portskoll)")

