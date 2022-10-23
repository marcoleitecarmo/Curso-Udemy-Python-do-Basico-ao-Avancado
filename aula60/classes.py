class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def inserir_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FORAM APAGADOS')
