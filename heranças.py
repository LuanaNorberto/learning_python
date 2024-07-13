# Heranças

class Animal:
    def __init__(self,nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return 'Latido'
    
cachorro = Cachorro('Rex')

print(cachorro.fazer_som())