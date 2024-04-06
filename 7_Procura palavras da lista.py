# Este código parte de um Excel com o nome do acórdão, a parte dispositiva e uma lista de palavras inibidoras da inovação, gerando uma planilha com a quantidade de palavras detectadas

import pandas as pd
import numpy as np

# Carregando as planilhas
xls = pd.ExcelFile('insira aqui o caminho para a planilha com a parte dispositiva dos acórdãos')
df1 = pd.read_excel(xls, 'ParteDispositiva')
df2 = pd.read_excel(xls, 'Palavras')

# Obtendo a lista de expressões
expressoes = df2['PalavrasInibidoras'].tolist()

# Verificando a existência das expressões e contando as ocorrências
for expressao in expressoes:
    df1[expressao] = df1['Parte_Dispositiva'].apply(lambda x: str(x).lower().count(expressao.lower()))

# Salvando a planilha atualizada
df1.to_excel('insira o caminho para a planiha que será criada', index=False)
