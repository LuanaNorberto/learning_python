# Classes e objetos

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
pessoa1 = Pessoa('Alice',25)
print(pessoa1.nome)

# defini um nome e idade a uma pessoa, neste caso pessoa 1.
# depois imprimi apenas o nome da pesssoa, colocando pessoa 1 sinalizando o nome, neste caso, Alice. 