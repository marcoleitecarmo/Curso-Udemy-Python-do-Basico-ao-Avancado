def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)

# Mesma espressão em Lambda


mais = lambda x, y: x * y
print(f'função lambda =  {mais(2, 2)}')
