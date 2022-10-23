import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos:')
    print('/A', 'Para listar todos os arquivos desta pasta', sep='\t')
    print('/D', 'Para listar todos os diretorios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '/A' in argumentos:
    so_arquivos = True

so_diretorios = False
if '/D' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)

