#--- Metodos, Funções / Classes ---#
    #def soma(a, b):
    #    return a + b

class Carro:
    def __init__(self):
        self.motor = 'desligado'
        self.movimento = False

    def ligar(self):
        self.motor = 'ligado'
    
    def acelerar(self):
        if self.motor == 'ligado':
            self.movimento = True

    def carro_em_movimento(self):
        return self.movimento

carro = Carro()
carro.acelerar()
carro_em_movimento = carro.carro_em_movimento()

print(carro_em_movimento)

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def mutiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b

calcular = Calculadora(10, 20)
print(calcular.soma())

print(calcular.subtrair())
print(calcular.mutiplicar())
print(calcular.dividir())
