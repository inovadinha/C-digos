# Este código procura acórdãos dentro de uma pasta e, se o arquivo tiver uma parte dispositiva, conta os caracteres e cria uma planilha indicando o resultado do processamento

import os
import re
import pandas as pd
from docx import Document
import unidecode
import time

# Caminho onde os arquivos estão salvos
caminho_dos_arquivos = r"insira aqui o caminho para a pasta onde a planilha com os resultados será salva"

# Expressões que estão sendo procuradas
expressoes = [
    "9. Acórdão:",
    "9.\tAcórdão:",
    "9. Acórdão",
    "9.  Acórdão:",
    "9.  Acórdão",
    "9.Acórdão:",
    "9.Acórdão" ,
    "9.   Acórdão:" ,
    "8. Acórdão:" ,
    "9. \tAcórdão:"
]

# Preparando os dados para a planilha Excel
dados = {"Nome do arquivo": [], "Resultado da busca": [], "Quantidade de caracteres": []}

# Percorrendo cada arquivo na pasta
arquivos = [arq for arq in os.listdir(caminho_dos_arquivos) if arq.endswith(".docx")]
total_arquivos = len(arquivos)
inicio = time.time()

for i, arquivo in enumerate(arquivos, start=1):
    doc = Document(os.path.join(caminho_dos_arquivos, arquivo))
    texto = " ".join([unidecode.unidecode(p.text) for p in doc.paragraphs])  # Extrai o texto do arquivo DOCX e remove acentos

    # Procurando as expressões no texto (desconsiderando a capitalização das letras, acentos e eventuais caracteres ocultos)
    match1 = None
    for expr in expressoes:
        matches = list(re.finditer(re.escape(unidecode.unidecode(expr)), texto, re.IGNORECASE))
        if matches:
            match1 = matches[-1]  # Considera apenas a última ocorrência
            break

    match2_space = re.search(re.escape(unidecode.unidecode("10. Ata")), texto, re.IGNORECASE)
    match2_tab = re.search(re.escape(unidecode.unidecode("10.\tAta")), texto, re.IGNORECASE)
    match2 = match2_space if match2_space else match2_tab

    if match1 and match2 and match1.end() < match2.start():
        # Se ambas as expressões foram encontradas e a última ocorrência da primeira ocorre antes da segunda, calcula a quantidade de caracteres entre elas
        texto_entre_expressoes = texto[match1.end():match2.start()]
        texto_entre_expressoes = re.sub(r'\s', '', texto_entre_expressoes)  # Remove espaços em branco, quebras de linha e caracteres ocultos
        quantidade_de_caracteres = len(texto_entre_expressoes)
        dados["Nome do arquivo"].append(arquivo)
        dados["Resultado da busca"].append("Arquivo com as expressões")
        dados["Quantidade de caracteres"].append(quantidade_de_caracteres)
    else:
        # Se as expressões não foram encontradas ou a primeira não ocorre antes da segunda
        dados["Nome do arquivo"].append(arquivo)
        dados["Resultado da busca"].append("Arquivo sem as expressões")
        dados["Quantidade de caracteres"].append(None)

    # Verifica se passou um minuto desde a última atualização
    if time.time() - inicio >= 60:
        print(f"{i} de {total_arquivos} arquivos processados.")
        inicio = time.time()

# Criando a planilha Excel
df = pd.DataFrame(dados)
df.to_excel(r"insira aqui o caminho para a planilha com os resultados, index=False)
