import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://images.unsplash.com/photo-1434719079929-f61498a4828e");
    background-size: cover;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    color: #DAA520;  /* Cor do texto do cabeçalho */
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

h1, h2, h3, h4, h5, h6, p {{
    color: #DAA520;  /* Cor do texto geral */
}}
</style>
"""
st.set_page_config(layout="wide")
st.markdown(page_bg_img, unsafe_allow_html=True)

model = joblib.load('trained_model.pkl.gz')

feature_names = model.feature_names_in_

label_encoder = LabelEncoder()
label_encoder.fit(['Masculino', 'Feminino'])



st.title('Previsão de Queima Calórica')

col1, col2 = st.columns([1,2], gap='large')

with col1:
    st.subheader('Insira seus dados abaixo:')

    col11, col12 = st.columns(2)

    with col11:
        # Entrada do usuário
        gender = st.selectbox('Gênero', options=['Masculino', 'Feminino'])
        age = st.number_input('Idade', min_value=0, max_value=120, value=25)
        duration = st.number_input('Duração do Exercício (min)', min_value=0, max_value=180, value=30)

    with col12:
        height = st.number_input('Altura (cm)', min_value=0, max_value=300, value=170)
        weight = st.number_input('Peso (kg)', min_value=0, max_value=300, value=70)
        

    # Codificar o gênero
    gender_encoded = label_encoder.transform([gender])[0]

    # Adicionar colunas que o modelo espera
    input_data = pd.DataFrame({
        'Gender': [gender_encoded],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Body_Temp': [38], # Valor padrão
        'Heart_Rate': [150] # Valor padrão
    })

    # Reordenar as colunas para corresponder à ordem esperada pelo modelo
    input_data = input_data[feature_names]

    predicted_calories = model.predict(input_data)[0]
    
    st.subheader(f'Total: {predicted_calories:.2f} kcal')

with col2:
    # Carregar o dataset com atividades e calorias queimadas
    burned_calories = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/burned_calories.csv')

    # Renomear a coluna
    burned_calories.rename(columns={
        "Activity, Exercise or Sport (1 hour)": "Activity",
        "Calories per kg": "Calories_Per_Kg"
    }, inplace=True)

    # Calcular as calorias queimadas por hora para cada atividade com base no peso do usuário
    burned_calories['Calories_Burned'] = burned_calories['Calories_Per_Kg'] * weight

    # Definir uma faixa de tolerância para selecionar atividades
    tolerance = 10
    filtered_activities = burned_calories[
        (burned_calories['Calories_Burned'] >= (predicted_calories - tolerance))
    ]

    st.subheader('Sugestão de Atividades:')
    st.dataframe(filtered_activities[['Activity', 'Calories_Burned']])
        




