from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_data():
    # Configurar o ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # URL da página que você deseja raspar
    url = 'URL_DA_PAGINA'
    driver.get(url)

    # Esperar a página carregar
    time.sleep(3)

    # Localizar e coletar os dados desejados
    elementos = driver.find_elements(By.CLASS_NAME, 'NOME_DA_CLASSE')
    
    dados = [element.text for element in elementos]

    driver.quit()
    
    return dados

if __name__ == "__main__":
    dados_coletados = scrape_data()
    print(dados_coletados)
