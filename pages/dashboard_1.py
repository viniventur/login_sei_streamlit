import pandas as pd
import os
import tempfile
import streamlit as st
from dotenv import load_dotenv, dotenv_values
env = dotenv_values('.env')

from utils import *
from sidebar import *

import warnings
warnings.filterwarnings('ignore')
import base64
import time

import plotly.express as px
import pandas as pd
import numpy as np


st.set_page_config(page_title='Login SEI', page_icon='src/assets/logo_sei.png')

if "login_efetuado" not in st.session_state:
    st.error('Erro, sessão não efetuada, redirecionando...')
    sair()

if st.session_state.login_efetuado == False:
    st.error('Erro, sessão não efetuada, redirecionando...')
    sair()

# Config Layout (condicional de local ou online)

def main():

    st.session_state.pag = 'dash1'

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
            <h1 style="font-size: 35px; margin: 0;">Dashboard 1</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Dividindo os botões em duas colunas
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button(":material/logout: Sair", key='sair', help='Clique para deslogar', use_container_width=True):
            sair()
    with col2:
        if st.button(":material/keyboard_return: Voltar ao Início", key='inicio', help='Clique para ir ao início', use_container_width=True):
            voltar_inicio()


    # Gerar dados aleatórios
    np.random.seed(42)
    df1 = pd.DataFrame({
        "Categoria": ["A", "B", "C", "D", "E"],
        "Valor": np.random.randint(10, 100, 5)
    })

   
    # Criar gráficos
    fig1 = px.bar(df1, x="Categoria", y="Valor", title="Gráfico de Barras - Valores Aleatórios")

    st.plotly_chart(fig1)
        
if __name__ == "__main__":
    main()