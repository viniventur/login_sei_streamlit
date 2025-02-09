import pandas as pd
import os
import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv, dotenv_values
env = dotenv_values('.env')

from utils import *
from sidebar import *

import warnings
warnings.filterwarnings('ignore')
import base64
import time

st.set_page_config(page_title='Login SEI', page_icon='src/assets/logo_sei.png')


if "login_efetuado" not in st.session_state:
    st.error('Erro, sessão não efetuada, redirecionando...')
    sair()

if st.session_state.login_efetuado == False:
    st.error('Erro, sessão não efetuada, redirecionando...')
    sair()

# Config Layout (condicional de local ou online)

def modulos_menu():

    if st.session_state.acesso == 'ADMIN':

        # Filtrar os módulos a partir do índice 2   
        modulos_filtrados = {k: v for k, v in modulos.items() if (int(k) >= 1)} # filtrar modulos sem pagina de login
    else:
        # Filtrar os módulos a partir do índice 2 e retirar o admin
        modulos_filtrados = {k: v for k, v in modulos.items() if (int(k) >= 1) & (int(k) < 5)} # filtrar modulos sem pagina de login

    # Variáveis para armazenar os valores
    nome_modulos = []
    links_modulos = []
    nome_links = []


    # Iterando sobre o dicionário
    for key, values in modulos_filtrados.items():
        nome_modulos.append(values[0])   # Nome do módulo
        links_modulos.append(values[1]) # Link do módulo
        # icones_modulos.append(values[2]) # Ícone do módulo
        nome_links.append([nome_modulos, links_modulos])
    
    return nome_modulos, nome_links, links_modulos


def mudar_modulo(modulo_selecionado, nome_modulos, links_modulos):

    # Identificando o módulo selecionado
    if modulo_selecionado:
        # Obtém o índice da seleção para localizar o link correto
        modulo_index = nome_modulos.index(modulo_selecionado)
        link_selecionado = links_modulos[modulo_index]
                
        with st.spinner("Redirecionando..."):
            st.switch_page(link_selecionado)

st.markdown(hide_style, unsafe_allow_html=True)

def main():

    st.session_state.pag = 'inicio'

    run_sidebar()

    # Criar um contêiner fixo no topo da página

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

    if st.button(":material/logout: Sair", key='sair', help='Clique para deslogar', use_container_width=True):
        sair()
        
    nome_modulos, nome_links, links_modulos = modulos_menu()

    icones_modulos = ['compass', 'equals', 'shield']

    modulo_selecionado = option_menu(
        menu_title=f'Olá, {st.session_state.nome_usuario}! O que deseja acessar?',
        options=nome_modulos,
        menu_icon="menu-app",
        orientation='vertical',
        default_index=0
    ) # option_menu nao suporta icones sem ser do bootstrap

    # Identificando o módulo selecionado
    if modulo_selecionado != 'Início':
        # Obtém o índice da seleção para localizar o link correto
        modulo_index = nome_modulos.index(modulo_selecionado)
        link_selecionado = links_modulos[modulo_index]
                
        with st.spinner("Redirecionando..."):
            st.switch_page(link_selecionado)
    
if __name__ == "__main__":
    main()