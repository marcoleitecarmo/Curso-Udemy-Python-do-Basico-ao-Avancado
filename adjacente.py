n = input('Digite um número: ')

t = len(n)
v = False
i = 0

while i < t - 1:
    if n[i] == n[i + 1]:
        v = True
    i += 1
if v:
    print('Sim')
else:
    print('Não')

