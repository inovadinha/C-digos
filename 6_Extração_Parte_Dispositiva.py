# Este código cria um excel com o nome do acórdão e a parte dispositiva

import os
import docx
import pandas as pd
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Caminho para a pasta com os documentos DOCX
docx_folder_path = r"insira aqui o caminho para a pasta que contém os acórdãos"

# Expressões de início e fim
inicio_expressions = ["9. Acórdão:", "9.\tAcórdão:", "9. Acórdão", "9.  Acórdão:", "9.  Acórdão", "9.Acórdão:", "9.Acórdão", "9.   Acórdão:", "8. Acórdão:", "9. \tAcórdão:"]
fim_expression = "10. Ata"

# Palavras de parada em português
stop_words = set(stopwords.words('portuguese'))

# Adicionando palavras de parada adicionais
additional_stop_words = ['que', 'quem', 'o', 'a', 'do', 'da', 'de', 'para', 'com', 'à', 'no', 'na', 'nos', 'nas', 'se', 'em']
stop_words.update(additional_stop_words)

# Lista para armazenar os trechos extraídos e os nomes dos arquivos
extracoes = []

# Contador de arquivos processados
contador = 0

# Tempo de início
start_time = time.time()

# Lendo cada arquivo na pasta
for filename in os.listdir(docx_folder_path):
    if filename.endswith(".docx"):
        doc = docx.Document(os.path.join(docx_folder_path, filename))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        full_text = ' '.join(full_text)

        # Encontrando o início e o fim do trecho
        inicio = next((i for i in inicio_expressions if i in full_text), None)
        if inicio:
            inicio_index = full_text.rindex(inicio)  # Alteração aqui
            fim_index = full_text.index(fim_expression) if fim_expression in full_text else None

            # Extraindo o trecho
            if fim_index:
                trecho = full_text[inicio_index:fim_index]

                # Removendo as palavras de parada
                word_tokens = word_tokenize(trecho)
                trecho_filtrado = [w for w in word_tokens if not w in stop_words]

                # Adicionando o trecho filtrado e o nome do arquivo à lista
                extracoes.append([filename, ' '.join(trecho_filtrado)])

        # Incrementando o contador de arquivos processados
        contador += 1

        # Verificando se já se passou um minuto
        if time.time() - start_time >= 60:
            print(f"{contador} arquivos processados.")
            start_time = time.time()

# Criando um DataFrame com as extrações
df = pd.DataFrame(extracoes, columns=['Acordao', 'Parte_Dispositiva'])

# Salvando o DataFrame como uma planilha do Excel
df.to_excel(r"insira aqui o caminho onde a planilha com os resultados será criada", index=False)
