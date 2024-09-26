import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

calories_df = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/calories.csv')
exercise_df = pd.read_csv('C:/Users/Josi/ProjetoTP1/data/exercise.csv')

# Unir os datasets
df = pd.merge(exercise_df, calories_df, on='User_ID')

# Converter a variável categórica Gender para numérica
df['Gender'] = df['Gender'].map({'male': 0, 'female': 1})



X = df.drop(columns=['Calories', 'User_ID'])
y = df['Calories']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestRegressor(n_estimators=300, max_depth=None, min_samples_split=2, random_state=42)
model.fit(X_train, y_train)

# Previsão
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Salvar o modelo treinado
joblib.dump(model, 'trained_model.pkl')
