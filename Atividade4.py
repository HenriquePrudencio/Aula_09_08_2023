class Animal:
    def falar(self):
        pass

class Catioro(Animal):
    def falar(self):
        return "Au Au"

class Gatineo(Animal):
    def falar(self):
        return "Miau"

def anima_falando(animal):
    print(animal.falar())

cao = Catioro()
gato = Gatineo()

anima_falando(cao)
anima_falando(gato)