class Forma:
    def calcular_area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return (3.14 * self.raio) ** 2

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

circulo = Circulo(5)
retangulo = Retangulo(10, 20)

print(f"A área do circulo é de {circulo.calcular_area()} e a área do retangulo é de {retangulo.calcular_area()}")