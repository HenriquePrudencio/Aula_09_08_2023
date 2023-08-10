class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        return "iiirrrrí"

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.raca = raca

    def obter_raca(self):
        return self.raca

    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def __init__(self, nome, especie, pelagem):
        super().__init__(nome, especie)
        self.pelagem = pelagem

    def obter_pelagem(self):
        return self.pelagem

    def emitir_som(self):
        return "Miau Miau"

animal = Animal("Spirit", "Cavalo")
print(animal.nome, animal.especie, animal.emitir_som())

cachorro = Cachorro("Maia", "Cachorro", "Labradora")
print(cachorro.nome, cachorro.especie, cachorro.obter_raca(), cachorro.emitir_som())

gato = Gato("Corona", "Gato", "Preto")
print(gato.nome, gato.especie, gato.obter_pelagem(), gato.emitir_som())