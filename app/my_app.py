import streamlit as st 
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import random

# Configurações de estilo e página
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://images.unsplash.com/photo-1434719079929-f61498a4828e");
    background-size: cover;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    color: #DAA520;
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

h1, h2, h3, h4, h5, h6, p {{
    color: #DAA520;
}}

.dataframe {{
    background-color: rgba(0, 0, 0, 0);  /* Cor de fundo do DataFrame */
}}
</style>
"""
st.set_page_config(layout="wide")
st.markdown(page_bg_img, unsafe_allow_html=True)

# Carregar o modelo (atualize o caminho se necessário)
modelo = joblib.load(r'C:/Users/Josi/ProjetoTP1/trained_model.pkl')

nomes_features = modelo.feature_names_in_

# Encoder de gênero
encoder_genero = LabelEncoder()
encoder_genero.fit(['Masculino', 'Feminino'])

# Carregar dados de calorias queimadas
calorias_quimadas = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/burned_calories.csv') 
calorias_quimadas.rename(columns={
    "Activity, Exercise or Sport (1 hour)": "Atividade",
    "Calories per kg": "Calorias_Por_Kg"
}, inplace=True)

# Função para a página de previsão de calorias
def pagina_previsao_calorias():
    st.title('Previsão de Queima Calórica')

    st.subheader('Insira seus dados abaixo:')

    genero = st.selectbox('Gênero', options=['Masculino', 'Feminino'])
    
    idade_opcoes = list(range(10, 101))
    idade = st.selectbox('Idade', options=idade_opcoes)
    
    altura = st.number_input('Altura (cm)', min_value=0, max_value=300)
    peso = st.number_input('Peso (kg)', min_value=0, max_value=200)

    # Duração padrão
    duracao_sugerida = 60  
    atividades_sugeridas = calorias_quimadas[calorias_quimadas['Calorias_Por_Kg'] * peso >= 0.1]

    # Codificar o gênero
    genero_codificado = encoder_genero.transform([genero])[0]

    # Dados de entrada para o modelo
    dados_entrada = pd.DataFrame({
        'Gender': [genero_codificado],
        'Age': [idade],
        'Height': [altura],
        'Weight': [peso],
        'Duration': [duracao_sugerida],
        'Body_Temp': [38],
        'Heart_Rate': [150]
    })

    dados_entrada = dados_entrada[nomes_features]
    calorias_previstas = modelo.predict(dados_entrada)[0]

    # Armazenar a previsão de calorias e peso no estado da sessão
    st.session_state.calorias_previstas = calorias_previstas
    st.session_state.peso = peso  
    st.session_state.altura = altura  

    st.subheader(f'Calorias Previstas: {calorias_previstas:.2f} kcal')

# Função para a página de atividades e calorias queimadas
def pagina_sugestoes_atividades():
    st.title('Sugestão de Atividades')

    calorias_previstas = st.session_state.get('calorias_previstas', None)
    peso = st.session_state.get('peso', None)

    if calorias_previstas is not None and peso is not None:
        

        calorias_quimadas = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/burned_calories.csv')
        calorias_quimadas.rename(columns={
            "Activity, Exercise or Sport (1 hour)": "Atividade",
            "Calories per kg": "Calorias_Por_Kg"
        }, inplace=True)

        calorias_quimadas['Calorias_Queimadas'] = calorias_quimadas['Calorias_Por_Kg'] * peso

        # Definir uma faixa de tolerância maior para selecionar atividades
        tolerancia = 40  
        atividades_filtradas = calorias_quimadas[
            (calorias_quimadas['Calorias_Queimadas'] >= (calorias_previstas - tolerancia)) &
            (calorias_quimadas['Calorias_Queimadas'] <= (calorias_previstas + tolerancia))
        ]

        #Sugestão de atividades filtradas
        if not atividades_filtradas.empty:
            fig = px.bar(atividades_filtradas,
                        x='Atividade',
                        y='Calorias_Queimadas',
                        labels={'Calorias_Queimadas': 'Calorias Queimadas', 'Atividade': 'Atividade'},
                        color='Calorias_Queimadas',
                        color_continuous_scale=px.colors.sequential.Viridis,
                        width=700,
                        height=400)

            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                xaxis_title_font=dict(color='#DAA520'),
                yaxis_title_font=dict(color='#DAA520'),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=-0.4,
                    xanchor="center",
                    x=0.5,
                    bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#DAA520')
                ),
                margin=dict(l=30, r=30, t=30, b=30)
            )


            # Remover a grade do gráfico
            fig.update_yaxes(showgrid=False)

            # Adicionar linha horizontal mostrando as calorias previstas
            fig.add_hline(y=calorias_previstas, line_color="red", line_dash="dash",
                        annotation_text="Calorias Previstas", annotation_position="top right")

            st.plotly_chart(fig)

            st.dataframe(atividades_filtradas[['Atividade', 'Calorias_Queimadas']], hide_index=True)
            
        else:
            st.warning("Por favor, realize a previsão de calorias primeiro.")

# Função para download de arquivo
def pagina_download_arquivo():
    st.title("Download de Arquivos")

    st.write("Dados disponíveis para download:")
    
    # Selecionar atividades
    atividades = calorias_quimadas['Atividade'].unique()
    atividades_selecionadas = st.multiselect('Selecione as atividades:', atividades)

    # Filtrar os dados de acordo com as atividades selecionadas
    if atividades_selecionadas:
        dados_filtrados = calorias_quimadas[calorias_quimadas['Atividade'].isin(atividades_selecionadas)]
    else:
        dados_filtrados = calorias_quimadas

    st.dataframe(dados_filtrados[['Atividade', 'Calorias_Por_Kg']], hide_index=True)

    csv = dados_filtrados.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Baixar dados de calorias queimadas como CSV",
        data=csv,
        file_name='calorias_queimadas.csv',
        mime='text/csv'
    )

# Função para exibir estatísticas
def pagina_estatisticas():
    st.title("Estatísticas de Atividades")

    col1, col2 = st.columns([1, 2])
    with col1:

        st.markdown("""
        *Nesta seção, você pode visualizar as estatísticas das atividades disponíveis, incluindo a distribuição de calorias queimadas por tipo de atividade*

    """, unsafe_allow_html=True)

    st.markdown("<h3 style='font-size: 20px;'>Selecione as atividades:</h3>", unsafe_allow_html=True)
    atividades = calorias_quimadas['Atividade'].unique()
    atividades_selecionadas = st.multiselect('', atividades)

    dados_filtrados = calorias_quimadas[calorias_quimadas['Atividade'].isin(atividades_selecionadas)]

    if not dados_filtrados.empty:
        fig = px.pie(
            dados_filtrados,
            names='Atividade',
            values='Calorias_Por_Kg',
            title='Distribuição de Calorias Queimadas por Atividade',
            color_discrete_sequence=px.colors.sequential.Viridis,
            width=800,
            height=400
            )

        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title_font=dict(color='#DAA520'),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5,
                bgcolor='rgba(0,0,0,0)',
                font=dict(color='#DAA520')
            ),
            margin=dict(l=30, r=30, t=30, b=30)
        )

        st.plotly_chart(fig)
    else:
        st.warning("Selecione pelo menos uma atividade para ver o gráfico.")

    st.subheader("Dados Filtrados")
    st.dataframe(dados_filtrados, hide_index=True)

# Navegação entre as páginas
if 'page' not in st.session_state:
    st.session_state.page = "Previsão de Queima Calórica"

opcoes_pagina = {
    "Previsão de Queima Calórica": pagina_previsao_calorias,
    "Sugestão de Atividades": pagina_sugestoes_atividades,
    "Estatísticas de Atividades": pagina_estatisticas,
    "Download de Arquivos": pagina_download_arquivo
}

st.sidebar.title("Navegação")
pagina_selecionada = st.sidebar.radio("Ir para", list(opcoes_pagina.keys()))

opcoes_pagina[pagina_selecionada]()
