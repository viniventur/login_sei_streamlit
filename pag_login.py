import pandas as pd
import streamlit as st
from dotenv import load_dotenv, dotenv_values
env = dotenv_values('.env')

from utils import *
from sidebar import *

import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title='Login SEI', page_icon='src/assets/logo_sei.png', initial_sidebar_state="collapsed")

# Config Layout (condicional de local ou online)

if is_local():
    
    # Aplicar CSS para esconder o sidebar
    hide_style = """
    """
else:

    # Aplicar CSS para esconder o sidebar
    hide_style = """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }

        [data-testid="stBaseButton-headerNoPadding"] {
            display: none;
        }

        #MainMenu {visibility: hidden}
        header {visibility: hidden}
        </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

def main():

    st.session_state.pag = 'login'
    st.session_state.acesso = ''

    run_sidebar()

    # Criar um contêiner fixo no topo da página
    header = st.container()

    logo_path_SEI= 'src/assets/logo_sei.png'
    logo_base64_SEI = get_image_as_base64(logo_path_SEI)

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 80px;">
            <img src="data:image/png;base64,{logo_base64_SEI}" style="margin-right: 35px; width: 150px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px; text-align: center;">
            <h1 style="font-size: 35px; margin: 0;">Login SEI em Streamlit</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

### Olá! Bem vindo extrator de dados do SEI

    with st.container():

        st.write(f'''
                 
                 :warning: As senhas fornecidas não são armazenadas, servindo apenas para o sistema logar no SEI e carregar as informações.                 
                 
                 ''')
        
    # Input para o usuário
    usuario = st.text_input('Usuário SEI:', placeholder="Digite seu usuário do SEI.")

    # Input para a senha (caracteres ocultos)
    senha = st.text_input('Senha SEI:', type='password', placeholder="Digite sua senha do SEI.")

    # Lista de orgaos login
    with st.spinner('Obtendo órgãos disponíveis no SEI...'):
        lista_orgaos = lista_orgaos_login()
        orgao = st.selectbox("Órgão:", lista_orgaos)

    # Login
    if st.button(":material/login: Acessar"):

        with st.spinner('Carregando...'):
            if orgao == lista_orgaos[0]:
                st.error(f"Informe o órgão.")
                return
       
        login_sei(usuario, senha, orgao)
        
if __name__ == "__main__":
    main()