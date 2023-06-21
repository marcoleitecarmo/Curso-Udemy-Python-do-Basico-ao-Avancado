import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula.csv'


with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
