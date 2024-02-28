import os
import pandas as pd

# Certifique-se de usar duas barras invertidas (\\) em caminhos no Windows
pasta = r"C:\Users\AMANDASALLESMARZOLAK\OneDrive - INSS\General - TCC MAP\2 Dados secundários\3 TCU\1_Planilhas_com_links"

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".xls"):
        xls_arquivo = os.path.join(pasta, arquivo)
        xlsx_arquivo = os.path.join(pasta, os.path.splitext(arquivo)[0] + ".xlsx")

        # Lê o arquivo *.xls
        df = pd.read_excel(xls_arquivo)

        # Salva o arquivo como *.xlsx
        df.to_excel(xlsx_arquivo, index=False)

        # Opcional: Remova o arquivo *.xls original após a conversão
        os.remove(xls_arquivo)

print("Conversão concluída com sucesso.")
