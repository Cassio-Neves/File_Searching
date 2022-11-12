# Importação da lib responsável por "caminhar" pelo nosso computador
import os

# Entrada de dados do usúario
path = input("Digite o caminho: ")
keyword = input("Digite uma palavra-chave: ")

#Formatação do tamanho do arquivo
def size_format(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = "B"
    elif size < mega:
        size/=kilo
        text = 'K'

    elif size < giga:
        size/= mega
        text = "G"

    elif size < tera:
        size/=giga
        text = "T"
    else:
        size /= peta
        text = "P"
    size = round(size, 2)
    return f'{size} {text}'

#Passando e procurando os arquivos no caminho passado pelo User
count = 0
for root, directory, files in os.walk(path):
    for file in files:
        if keyword in file:
            try:
                count+=1
                full_path = os.path.join(root, file)
                file_name, ext_file = os.path.splitext(full_path)
                size = os.path.getsize(full_path)
                print(file)

                print()
                print(f'''Encontrei o arquivo: {file}
                Caminho: {path}
                Nome do arquivo: {file_name}
                Extensão: {ext_file}
                Tamanho: {size}
                Tamanho formatado: {size_format(size)}''')
                
            except PermissionError as e:
                print("Sem permissão neste aquivo")
            except FileNotFoundError as e:
                print("Arquivo não encontrado")
            except Exception:
                print(f"Erro desconhecido: {e}")
print(f'{count} arquivo(s) encontrado(s)')