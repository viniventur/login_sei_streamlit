import streamlit as st
from utils import *


def run_sidebar():

    if st.session_state.pag == 'login':
        with st.sidebar:

            st.title('Realize o login no SEI para navegar.')

            st.divider()

    else:


        with st.sidebar:

            nome_usuario = st.session_state.nome_usuario
        
            st.markdown(f'# <center> Olá, {nome_usuario}!', unsafe_allow_html=True)

            if st.button(":material/logout: Sair", help='Clique para deslogar', use_container_width=True):
                sair()


            st.sidebar.divider()

            # NAVEGACAO

            for modulo in range(1,4): # MODULOS COMPLETOS
            
                st.sidebar.page_link(modulos[modulo][1],
                        label=modulos[modulo][0],
                        icon=modulos[modulo][2])

            st.divider()
       






