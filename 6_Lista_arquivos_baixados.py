import os

# Caminho da pasta onde estão os arquivos
diretorio = r"D:\TCC\Acórdãos"

# Caminho da pasta onde o arquivo .txt será salvo
diretorio_saida = r"D:\TCC"

# Cria uma lista com o nome de todos os arquivos (sem a extensão)
lista_arquivos = [os.path.splitext(arquivo)[0] for arquivo in os.listdir(diretorio)]

# Cria o arquivo .txt e escreve os nomes dos arquivos
with open(os.path.join(diretorio_saida, 'JaBaixados.txt'), 'w') as f:
    for item in lista_arquivos:
        f.write("%s\n" % item)
