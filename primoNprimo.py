n = int(input('Digite um número: '))

c = 1

while c <= n:
    if n % 2 == 1:
        c += 1
        print('primo')
        break
    else:
        print('Não primo')
        break
