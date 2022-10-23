
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

novaLista = filter(lambda x: x > 5, lista)
for nova in novaLista:
    print(nova, end=', ')
