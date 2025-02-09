from dotenv import load_dotenv, dotenv_values
import streamlit as st

import base64

env = dotenv_values('.env')

def extrair_nome_sei(string):
    # Divide a string na primeira ocorrência do parêntese
    nome = string.split('(')[0]
    # Remove espaços extras no início ou fim
    return nome.strip()

def get_image_as_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

   