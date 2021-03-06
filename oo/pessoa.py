class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} -olhos {cls.olhos}'


if __name__ == '__main__':
    roberto = Pessoa(nome='Roberto Macedo Santos')
    antonio = Pessoa(roberto, nome='Antonio')
    print(Pessoa.cumprimentar(antonio))
    print(id(antonio))
    print(antonio.cumprimentar())
    print(antonio.nome)
    print(antonio.idade)
    for filho in antonio.filhos:
        print(filho.nome)
    antonio.sobrenome = 'Silva'
    del antonio.filhos
    print(antonio.__dict__)
    print(roberto.__dict__)
    print(Pessoa.olhos)
    print(roberto.olhos)
    print(id(Pessoa.olhos), id(roberto.olhos), id(antonio.olhos))
    print(Pessoa.metodo_estatico(), antonio.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), antonio.nome_e_atributo_de_classe())