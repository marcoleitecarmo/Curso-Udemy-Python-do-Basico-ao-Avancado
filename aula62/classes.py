class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando....')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando....')

    def falar(self):
        print('Cliente falando.')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
