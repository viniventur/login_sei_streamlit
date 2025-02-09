import os
from dotenv import dotenv_values
import streamlit as st
env = dotenv_values('.env')

def is_local():
    """Verifica se está rodando localmente"""
    return "IS_LOCAL" in env


# modulos
@st.cache_data(show_spinner=False)
def modulos():
    '''
        Retorna um dicionário com informações sobre os módulos disponiveis no sistema.

        Estrutura:
        - Chave (int): Identificador do módulo.
        - Valor (list): [Nome do módulo (str), Caminho do arquivo (str), Emoji (str)] - .


        Exemplo de uso:
            modulos = modulos()
            print(modulos_dict[1])  # Retorna ['Início', 'pages/Inicio.py', ':material/home:']
            print(modulos[0][1]) # Retorna o endereço do primeiro modulo
    '''
    modulos = {
        0: ['Login', 'pag_login.py'],
        1: ['Início', 'pages/Inicio.py', ':material/home:'],
        2: ['Dashboard 1', 'pages/dashboard_1.py', ':material/quick_reference_all:'],
        3: ['Dashboard 2', 'pages/dashboard_2.py', ':material/explore:'],
    }
    return modulos

modulos = modulos()

def voltar_inicio():
    with st.spinner('Redirecionando...'):
        st.switch_page(modulos[1][1])

