class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
r = Retangulo(base, altura)
print("Área: " + str(r.area()))
print("Perímetro: " + str(r.perimetro()))