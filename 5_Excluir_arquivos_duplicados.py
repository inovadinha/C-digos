import os
import send2trash

def delete_duplicates(directory):
    found_duplicates = False
    for filename in os.listdir(directory):
        if "(1)" in filename:
            file_path = os.path.join(directory, filename)
            send2trash.send2trash(file_path)
            print(f"Arquivo {filename} movido para a lixeira.")
            found_duplicates = True
    if not found_duplicates:
        print("Nenhum arquivo duplicado encontrado.")

# Substitua o caminho abaixo pelo caminho da sua pasta
delete_duplicates("D:\\TCC\\Acórdãos")
