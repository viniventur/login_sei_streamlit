import time
import streamlit as st
import os

from utils.config import is_local, modulos, voltar_inicio
from utils.chrome_config import chrome


def excluir_driver():
    """Fecha o driver do Selenium se estiver aberto."""
    if 'driver' in st.session_state:
        try:
            st.session_state.driver.quit()
        except Exception as e:
            st.warning(f"Erro ao encerrar o driver: {e}")
        del st.session_state['driver']

def mudar_iframe(iframe):
    """Muda o frame no Selenium."""
    driver = st.session_state.driver

    if iframe == 'arvore':
        driver.switch_to.default_content()
        iframe_arvore = driver.find_element('name', "ifrArvore")
        driver.switch_to.frame(iframe_arvore)
    elif iframe == 'visualizacao':
        driver.switch_to.default_content()
        iframe_visualizacao = driver.find_element('name', "ifrVisualizacao")
        driver.switch_to.frame(iframe_visualizacao)
    elif iframe == 'default':
        driver.switch_to.default_content()

def sair():
    with st.spinner('Redirecionando...'):    
        excluir_driver()
        st.cache_resource.clear()
        st.cache_data.clear()
        st.session_state.clear()
        st.switch_page(modulos[0][1])

