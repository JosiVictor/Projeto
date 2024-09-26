# Estrutura do Projeto Utilizando CRISP-DM e TDSP

## Introdução
Este projeto tem como objetivo desenvolver uma aplicação para prever calorias queimadas durante exercícios físicos, alinhada aos princípios da Agenda 2030 e aos pilares ESG. A solução utiliza dados de desempenho e técnicas de modelagem para fornecer recomendações personalizadas para os usuários.

### Alinhamento com os Objetivos de Desenvolvimento Sustentável (ODS)
O projeto atende ao **ODS 3: Saúde e Bem-Estar**, que visa garantir uma vida saudável e promover o bem-estar para todos em todas as idades. A aplicação contribui para este objetivo ao fornecer aos usuários uma ferramenta que ajuda a monitorar e melhorar sua saúde física, incentivando práticas de exercício físico e alimentação equilibrada.

## Metodologia CRISP-DM

### 1. Business Understanding
Desenvolver um aplicativo que estima a quantidade de calorias queimadas com base em informações do usuário, como gênero, idade, altura, peso e duração do exercício. O objetivo é oferecer recomendações personalizadas para atividades físicas com base na previsão de calorias queimadas.
**Metas e Indicadores:**
- Alcançar uma precisão de previsão de calorias que seja útil e precisa para os usuários.
- Garantir que o aplicativo seja fácil de usar e entenda as recomendações fornecidas.

### 2. Data Understanding
**Fontes de Dados:**
- **Dados sobre atividades físicas e calorias queimadas**: Utilizados para treinar o modelo de previsão de calorias queimadas durante exercícios físicos. Estes dados incluem informações sobre diferentes tipos de atividades e suas respectivas calorias queimadas por hora, com base no peso do usuário.
- **Dados de perfil do usuário**: Informações sobre gênero, idade, altura, peso e duração do exercício físico, que são utilizadas como entradas para a aplicação e para a previsão das calorias queimadas.
**Exploração Inicial:**
- Análise dos dados para entender a distribuição das variáveis e a relação entre elas.
- Identificação de valores ausentes e inconsistências nos dados.

### 3. Data Preparation
- Limpeza dos dados: remoção de valores ausentes e tratamento de outliers.
- Transformação dos dados: conversão de variáveis categóricas em numéricas e normalização das variáveis numéricas.
- Criação de um conjunto de dados de treino e teste para a modelagem.

### 4. Modeling
- **Random Forest:** Para prever as calorias queimadas com base nas características do usuário.
  - Ajuste dos hiperparâmetros do modelo para melhorar a precisão.

### 5. Evaluation
**Métricas de Avaliação:**
- **Erro Quadrático Médio (MSE):** Para avaliar a precisão das previsões de calorias queimadas.
- **R² Score:** Para medir a adequação do modelo às variáveis preditoras.
**Resultados:**
- O modelo atingiu uma precisão satisfatória, com MSE dentro do intervalo aceitável e um R² Score indicando boa capacidade de previsão.

### 6. Deployment
- Desenvolvimento de um aplicativo web usando Streamlit para permitir que os usuários insiram suas informações e obtenham previsões de calorias queimadas.
- O modelo treinado foi integrado ao aplicativo para fornecer previsões em tempo real.


## Metodologia TDSP

### 1. Project Scoping
- Definição do problema: Prever calorias queimadas com base em dados do usuário.
- Entregas: Aplicativo funcional com previsão de calorias e recomendações de atividades.

### 2. Data Collection
- Coleta de dados sobre diferentes tipos de atividades físicas e suas respectivas calorias queimadas por hora. Esses dados foram extraídos de um dataset específico contendo informações sobre várias atividades e a quantidade de calorias queimadas com base no peso do usuário.
- Inclui informações sobre gênero, idade, altura, peso e duração do exercício, usadas como entradas para a previsão de calorias queimadas na aplicação.
- Os datasets foram baixados e integrados no ambiente de desenvolvimento para a criação do modelo de previsão e para a construção da interface do usuário na aplicação.

### 3. Data Preparation
- Limpeza e transformação dos dados conforme descrito na fase de preparação do CRISP-DM.

### 4. Modeling
- Implementação do modelo Random Forest e ajuste dos parâmetros para otimização.

### 5. Deployment
- Criação do aplicativo Streamlit.
- Testes de usabilidade.

### 6. Operationalization
- Monitoramento contínuo do desempenho do modelo.
