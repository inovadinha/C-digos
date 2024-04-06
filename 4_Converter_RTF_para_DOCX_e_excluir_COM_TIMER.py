# Este código converte os arquivos dos acórdãos, com formato RTF, para formato DOCX, para serem usados nas etapas seguintes

import os
import time
import win32com.client as win32

def convert_rtf_to_docx(path):
    # Cria uma instância do Microsoft Word
    word = win32.gencache.EnsureDispatch('Word.Application')

    # Obtenha a lista de todos os arquivos na pasta especificada
    files = os.listdir(path)
    rtf_files = [file for file in files if file.endswith(".rtf")]
    total_files = len(rtf_files)
    converted_files = 0

    start_time = time.time()

    # Percorre todos os arquivos .rtf na pasta especificada
    for filename in rtf_files:
        doc_path = os.path.join(path, filename)

        # Abre o arquivo .rtf
        doc = word.Documents.Open(doc_path)

        # Salva o arquivo como .docx (FileFormat=16 representa .docx)
        doc.SaveAs(doc_path.replace('.rtf', '.docx'), FileFormat=16)

        # Fecha o arquivo
        doc.Close()

        # Exclui o arquivo .rtf original
        os.remove(doc_path)

        converted_files += 1

        # Verifica se passou um minuto desde a última atualização
        if time.time() - start_time >= 60:
            print(f"{converted_files} de {total_files} arquivos foram convertidos.")
            start_time = time.time()

    # Fecha o Microsoft Word
    word.Quit()

    print(f"Conversão concluída. {converted_files} de {total_files} arquivos foram convertidos.")

# Substitua pelo caminho da pasta que contém os documentos
convert_rtf_to_docx(r"insira aqui o caminho para a pasta que contém os documentos")
