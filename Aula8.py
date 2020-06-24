#--- Módulos e funções anonimas com lambda(anonima pq o valor vai para a variavel ) ---#

from Aula7 import Calculadora
from Aula8ContaLetras import contaLetras

calculadora = Calculadora(5, 10)
print(calculadora.soma())

lista = ['paralelepipedo', 'systemas']
print(contaLetras(lista))

soma = lambda a, b: a + b
print('soma lambda: {}'.format(soma(3,5)))

contarCaracteres = lambda lista: [len(x) for x in lista]
print('Conta Caracteres Lambda: {}'.format(contarCaracteres(lista)))


#dicionário
calculadoraDict = {
    'soma': lambda a, b: a + b, 
    'subtrair': lambda a, b: a - b, 
    'multiplicar': lambda a, b: a * b, 
    'dividir': lambda a, b: a / b,
}

somaDict = calculadoraDict['soma']
SubtrairDict = calculadoraDict['subtrair']
multiplicarDict = calculadoraDict['multiplicar']
dividirDict = calculadoraDict['dividir']
print('A soma dict é: {}'.format(somaDict(3,5)))
print('A subtração dict é: {}'.format(SubtrairDict(8,5)))
print('A multiplicação dict é: {}'.format(multiplicarDict(3,5)))
print('A divisão dict é: {}'.format(dividirDict(15,5)))


valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)
print(resultado)