
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

aluno.update({'nome': 'Pedro', 'nota_final': 'B'})

for keys, values in aluno.items():
    print(keys, values)
