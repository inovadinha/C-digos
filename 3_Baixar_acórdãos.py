# Este código parte de uma pasta com planilhas de excel com a relação de todos os acórdãos, de todos os órgãos, e baixa os acórdãos em uma pasta

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
import pyautogui

# Função para atualizar o navegador
def atualizar_navegador():
    # Simule a pressão da tecla F5 (recarregar)
    pyautogui.press('f5')

# Configurações iniciais
chrome_options = Options()
webdriver_service = Service(r"insira aqui o caminho para o executável do edgedriver")
prefs = {"download.default_directory": r"insira aqui o caminho para a pasta onde os arquivos serão salvos"}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Lendo os dados do Excel (altere o número das linhas que vai buscar, se necessário)
df = pd.read_excel(r"insira aqui o caminho para o Excel com a relação de órgãos e acórdãos")
start_row = 1
end_row = 10

# Tempo de espera entre atualizações (30 minutos = 1800 segundos)
intervalo_atualizacao = 30
tempo_inicial = time.time()

# Loop principal
for i in range(start_row - 1, end_row):
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

       time.sleep(2)

       # Clicando no botão de download
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#lista-resultado__itens > ul > li:nth-child(1) > div > div > div.lista-resultado__acoes > button.mat-mdc-menu-trigger.mat-mdc-tooltip-trigger.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base.ng-star-inserted > span.mat-mdc-button-touch-target'))).click()

       time.sleep(2)

       # Clicando no botão de RTF
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mat-menu-panel-7 > div > button:nth-child(2) > span'))).click()

       # Aguardando o download do arquivo
       time.sleep(30)  # Ajuste este valor conforme necessário

       print(f"Arquivo da linha {i+1} baixado com sucesso.")

       # Verifica se é hora de atualizar o navegador
       tempo_atual = time.time()
       if tempo_atual - tempo_inicial >= intervalo_atualizacao:
          atualizar_navegador()
          tempo_inicial = tempo_atual

    except Exception as e:
        print(f"Ocorreu um erro na linha {i+1}: {str(e)}")

print("Todos os arquivos foram baixados.")

# Encerra o driver
driver.quit()