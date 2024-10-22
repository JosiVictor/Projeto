import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import gzip
import os

# Carregar os dados
calories_df = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/calories.csv')
exercise_df = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/exercise.csv')

# Unir os datasets
df = pd.merge(exercise_df, calories_df, on='User_ID')

print(df)

# Converter a variável categórica Gender para numérica
df['Gender'] = df['Gender'].map({'male': 0, 'female': 1})

# Preparar os dados
X = df.drop(columns=['Calories', 'User_ID'])
y = df['Calories']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestRegressor(n_estimators=100, max_depth=None, min_samples_split=2, random_state=42)
model.fit(X_train, y_train)

# Previsão
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Salvar o modelo treinado sem compressão
model_path = 'C:/Users/Josi/ProjetoTP1/trained_model.pkl'
joblib.dump(model, model_path)

# Configurar a API FastAPI
app = FastAPI()

# Definindo um modelo para os dados de entrada
class InputData(BaseModel):
    Gender: int
    Age: int
    Height: int
    Weight: int
    Duration: int
    Heart_Rate: int
    Body_Temperature: float

# Carregar o modelo salvo
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise Exception(f"Modelo não encontrado em {model_path}. Verifique o caminho do arquivo.")


@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}

@app.post("/previsao/")
def predict_calories(data: InputData):
    input_df = pd.DataFrame([data.dict()])
    predicted_calories = model.predict(input_df)[0]
    return {"predicted_calories": predicted_calories}
