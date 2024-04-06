# Este código altera o formato das planilhas baixadas do site de pesquisa do TCU, com a relação de acórdãos de cada órgão

import os
import pandas as pd

# Certifique-se de usar duas barras invertidas (\\) em caminhos no Windows
pasta = r"insira aqui o caminho para a pasta que contém as planilhas com os acórdãos de cada órgão"

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
