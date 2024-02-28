# Importando as bibliotecas necessárias
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Cria um objeto de opções
chrome_options = Options()

# Define o caminho do executável do ChromeDriver
webdriver_service = Service(r"C:\Users\AMANDASALLESMARZOLAK\OneDrive - INSS\General - TCC MAP\Códigos\chromedriver.exe")

# Define a pasta de download padrão
prefs = {"download.default_directory" : r"C:\Users\AMANDASALLESMARZOLAK\OneDrive - INSS\General - TCC MAP\2 Dados secundários\3 TCU\2_Acordaos"}
chrome_options.add_experimental_option("prefs", prefs)

# Inicializa o driver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Lendo os dados do Excel
df = pd.read_excel(r"C:\Users\AMANDASALLESMARZOLAK\OneDrive - INSS\General - TCC MAP\2 Dados secundários\3 TCU\2_Baixar.xlsx")

# Define a linha inicial (ajuste este valor conforme necessário)
start_row = 912

# Iterando sobre cada linha do DataFrame a partir da linha inicial
for i in range(start_row - 1, len(df)):
    row = df.iloc[i]
    try:
        # Abrindo o site de busca
        driver.get("https://pesquisa.apps.tcu.gov.br/pesquisa/acordao-completo")

        # Preenchendo os campos de busca
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "numeroprocesso"))).send_keys(str(row["Processo"]))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "numero"))).send_keys(str(row["Número"]))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ano"))).send_keys(str(row["Ano"]))

        # Clicando no botão de pesquisa
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pesquisa-especifica > div > div.pesquisa-especifica__coluna > div.marcador_formulario_pesquisa > div.pesquisa-especifica__formulario > app-pesquisa-acordaos > div > form > app-barra-botoes-de-pesquisa > section > button.barra-botoes__pesquisar.mdc-button.mdc-button--raised.mat-mdc-raised-button.mat-primary.mat-mdc-button-base > span.mdc-button__label'))).click()

        # Clicando no botão de download
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#lista-resultado__itens > ul > li:nth-child(1) > div > div > div.lista-resultado__acoes > button.mat-mdc-menu-trigger.mat-mdc-tooltip-trigger.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted > span.mat-mdc-button-touch-target'))).click()

        # Clicando no botão de RTF
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mat-menu-panel-7 > div > button:nth-child(2) > span'))).click()

        # Aguardando o download do arquivo
        time.sleep(10)  # Ajuste este valor conforme necessário

        print(f"Arquivo da linha {i+1} baixado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro na linha {i+1}: {str(e)}")

print("Todos os arquivos foram baixados.")
