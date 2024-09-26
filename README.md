# Projeto de Previsão de Calorias Queimadas

## Descrição

Este projeto desenvolve uma aplicação para prever calorias queimadas durante exercícios físicos utilizando técnicas de Machine Learning e visualização de dados com Streamlit. A aplicação visa fornecer recomendações personalizadas de atividades físicas com base no perfil do usuário e na previsão de calorias queimadas.

## Estrutura do Projeto

- `api_kaggle.py`: Script para integração com a API do Kaggle para obter dados adicionais.
- `main.py`: Script de modelagem, que treina e avalia o modelo de previsão.
- `my_app.py`: Aplicação Streamlit para visualização e interação com os dados e previsões.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Instalação

1. Repositório: 
    ```
    cd <diretório do repositório>
    ```

2. Crie e ative um ambiente virtual:
     ```
     python -m venv venv
     venv\Scripts\activate.ps1
     ```

3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

## Uso

Para rodar a aplicação Streamlit, execute:
   ```
   streamlit run my_app.py
   ```
