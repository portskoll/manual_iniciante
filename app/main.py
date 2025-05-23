import streamlit as st
from streamlit_option_menu import option_menu
import n8n_inicio, docker_inicio, devops_inicio, kubernetes_inicio, git_inicio, linux_inicio, dokerfile_inicio, about

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():

        st.set_page_config(layout="wide")
        with st.sidebar:
            
            app = option_menu(

                menu_title='App Menu',
                options=['Inicio Python', 'Inicio Docker', 'Inicio Dockerfile', 'Inicio Kubernetes', 'Inicio DevOps', 'Inicio Git', 'Inicio Linux', 'Inicio N8N', "About me"],
                icons=['filetype-py', 'box-seam', 'box-seam', 'diagram-3', 'gear-fill', 'git', 'terminal-fill', 'diagram-3', 'person'],
                menu_icon='list',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},}
            
            )
            
        if app == "Inicio Python":
            n8n_inicio.app()
        if app == "Inicio Docker":
            docker_inicio.app()
        if app == "Inicio Dockerfile":
            dokerfile_inicio.app()
        if app == "Inicio Kubernetes":
            kubernetes_inicio.app()
        if app == "Inicio DevOps":
            devops_inicio.app()
        if app == "Inicio Git":
            git_inicio.app()
        if app == "Inicio Linux":
            linux_inicio.app()
        if app == "Inicio N8N":
            n8n_inicio.app()
        if app == "About me":
            about.app()

    run()