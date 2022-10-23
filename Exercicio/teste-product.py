from itertools import product, permutations

a = product('ABCD', repeat=2)

for cont in a:
    print(cont)
print('-' * 50)

r = permutations(range(3))

for lista in r:
    print(lista)
