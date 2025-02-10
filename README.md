# Login SEI com Streamlit App

<div style="display: flex; align-items: center;">
    <img src="src/assets/logo_sei.png" alt="SEI" width="50" style="margin-right: 10px;">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" width="150" style="margin-right: 10px;">
    <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white" alt="Selenium" width="140">
</div>

## Descrição do projeto

Este projeto visa utilizar o Sistema Eletrônico de Informações (SEI) como ferramenta de autenticação em aplicativos em **Streamlit** por meio de automações e raspagens implementadas com o **Selenium**.

## Principais Características

- **Automatização Segura**: Nenhuma informação de login ou senha é armazenada, garantindo a privacidade dos usuários.
- **Ausência de Cache em Dados Sensíveis**: O login não é salvo em cache, evitando a retenção de credenciais.
- **Interatividade Simples**: Os dados de login são inseridos diretamente no app e preenchidos automaticamente no SEI.
- **Execução na Nuvem**: O aplicativo funciona na nuvem do Streamlit, utilizando **Chromedriver headless**, inclusive se acessado em dispositivos móveis.
- **Disponível Online**: O app pode ser acessado pelo link: [log-in-sei.streamlit.app](https://log-in-sei.streamlit.app/)



## Estrutura do Projeto

1. **Página de Login**
   - Interface inicial com campos de entrada para credenciais.
   - A navegação entre páginas é bloqueada até que o login seja efetuado.
   - O sidebar fica desativado até a autenticação ser validada.

2. **Extração de Órgãos Disponíveis**
   - Raspagem da lista de órgãos diretamente da tela de login do SEI.
   - Dados dos órgãos disponíveis armazenados em cache para otimizar a seção de outros usuários.
   - Implementado em `utils/login.py` na função `lista_orgaos_login()`.

3. **Automação do Login**
   - O **Chromedriver** é utilizado para preencher e submeter as credenciais.
   - O usuário é automaticamente redirecionado após o login.
   - Disponível em `utils/login.py` na função `login_sei()`.

4. **Gerenciamento de Sessão com `st.session_state`**
   - A variável `login_efetuado` impede a navegação caso o login não tenha sido realizado.
   - Garante que apenas usuários autenticados possam acessar as demais páginas do aplicativo.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `Streamlit`: Para construção do aplicativo.
  - `Selenium`: Para automação e raspagem de dados utilizando o **chromedriver**.

## Como Executar o Projeto

1. **Clone o Repositório**
    ```
    git clone https://github.com/viniventur/login_sei_streamlit.git
    cd login_sei_streamlit
    ```

2. **Crie um Ambiente Virtual e Instale as Dependências**
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3. **Adicione o site do seu SEI no secrets.toml**

    ```
    SITE_SEI = "URL"
    ```


4. **Execute o Aplicativo**

    ```
    streamlit run pag_login.py
    ```

## Licença

Este projeto é licenciado sob a Licença MIT.