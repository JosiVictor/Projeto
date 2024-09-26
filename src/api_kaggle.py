import pandas as pd
import zipfile
import os

# Caminho para a pasta de extração
extract_folder = 'C:\Users\Josi\ProjetoTP1\data'



# Caminho para o arquivo ZIP do primeiro dataset
zip_path = 'C:/Users/Josi/ProjetoTP1/fmendesdat263xdemos.zip'

os.makedirs(extract_folder, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    file_list = zip_ref.namelist()
    print("Arquivos no ZIP:", file_list)
    
    # Extrair arquivos
    zip_ref.extractall(extract_folder)

print(f'Arquivos extraídos para {extract_folder}')



# Caminho para o arquivo ZIP do segundo dataset
new_zip_path = 'C:/Users/Josi/ProjetoTP1/calories-burned-during-exercise-and-activities.zip'

with zipfile.ZipFile(new_zip_path, 'r') as zip_ref:

    new_file_list = zip_ref.namelist()
    print("Arquivos no novo ZIP:", new_file_list)
    
    # Extrair arquivos
    zip_ref.extractall(extract_folder)

print(f'Arquivos extraídos para {extract_folder}')


# Criar DataFrames
csv_files = [f for f in os.listdir(extract_folder) if f.endswith('.csv')]
dataframes = {}

for csv_file in csv_files:
    file_path = os.path.join(extract_folder, csv_file)
    dataframes[csv_file] = pd.read_csv(file_path)
    print(f"\nDados do arquivo {csv_file}:")
    print(dataframes[csv_file].head())

df_calories = dataframes.get('calories.csv')
df_exercise = dataframes.get('exercise.csv')
new_data = dataframes.get('burned_calories.csv')
