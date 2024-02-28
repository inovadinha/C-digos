# Importando as bibliotecas necessárias
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Definindo os caminhos para o EdgeDriver e para o arquivo Excel
    edgedriver_path = r"COLAR AQUI O CAMINHO PARA O ARQUIVO EDGEDRIVER"
    excel_path = r"COLAR AQUI O CAMINHO PARA SUA PLANILHA EXCEL COM OS DADOS A SEREM PESQUISADOS"

    # Lendo o arquivo Excel para um DataFrame pandas
    df = pd.read_excel(excel_path, sheet_name="Entidades")

    # Iniciando um driver do Edge
    driver = webdriver.Edge(service=Service(edgedriver_path))

    # Iterando sobre cada linha do DataFrame
    for index, row in df.iterrows():
        # Extraindo o valor da coluna "Nome"
        sigla = row["Nome"]

        # Navegando para a página de pesquisa do TCU
        driver.get("https://pesquisa.apps.tcu.gov.br/pesquisa/acordao-completo")

        # Configurando o tempo de espera
        wait = WebDriverWait(driver, 10)

        # Preenchendo o campo de pesquisa com o valor extraído
        entidade_input = wait.until(EC.presence_of_element_located((By.ID, "entidade")))
        entidade_input.clear()
        entidade_input.send_keys(sigla)

        # Definindo um intervalo de datas para a pesquisa
        data_inicio_input = driver.find_element(By.ID, "datainiciosessao")
        data_inicio_input.clear()
        data_inicio_input.send_keys("01/01/2013")

        data_fim_input = driver.find_element(By.ID, "datafimsessao")
        data_fim_input.clear()
        data_fim_input.send_keys("31/12/2022")

        # Clicando no botão de pesquisa
        pesquisar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Pesquisar']")))
        pesquisar_button.click()

        # Tentando extrair o número de resultados da pesquisa
        try:
            paginator_label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mat-mdc-paginator-range-label")))
            result_text = paginator_label.text.strip()

            if "Nenhum resultado encontrado" in result_text:
                result_count = 0
            else:
                result_count = int(result_text.split()[-1].replace(".", ""))
        except:
            result_count = 0

        # Adicionando o número de resultados ao DataFrame na coluna "Resultados"
        df.at[index, "Resultados"] = result_count

        # Salvando o DataFrame atualizado de volta no arquivo Excel
        df.to_excel(excel_path, sheet_name="Nome da coluna com o nome do órgão público", index=False)

    # Fechando o driver do Edge após iterar sobre todas as linhas do DataFrame
    driver.quit()

# Se o script for executado como um programa independente, a função `main()` será chamada
if __name__ == "__main__":
    main()
