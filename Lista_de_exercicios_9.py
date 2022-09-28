# 1 - Crie procedimentos com parâmetros informados pelo usuário no programa principal:
# a - Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados,
# somar os números e apresentar o resultado na tela.
#
# b - Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar
#  a operação de multiplicação, apresentando o resultado na tela.
#
# c - Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
#
# d - Faça um procedimento que calcule a potência de um número(XY) chamado calcularPotencia(). O procedimento deve receber os números por parâmetro,
# efetuar o cálculo e apresentar o resultado.
#
# e - Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve receber o número por parâmetro,
# efetuar o cálculo e apresentar o resultado.
from random import randint

def somar(a, b):
    resultado_soma = a + b
    print(resultado_soma)

def multiplicar(a, b):
    resultado_mult = a * b
    print(resultado_mult)

def calcularRaiz(a):
    resultado_raiz = a ** (1/2)
    print(resultado_raiz)

def calcular_potencia(a, b):
    resultado_potencia = a ** b
    print(resultado_potencia)

def calcular_tabuada(a):
    for i in range (1,11):
        resultado_tabuada = a * i
        print(a, "x", i, "=", resultado_tabuada)


# 2 - Crie procedimentos com parâmetros:

# a - Crie um procedimento que recebe um vetor de números inteiros por parâmetro. Esta função deve chamar imprimirVetor() e vai imprimir na tela todos os números do vetor informado.

# b - Faça um procedimento chamado encontrarMaior() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o maior valor do vetor.

# c - Faça um procedimento chamada encontrarMenor() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o menor valor do vetor.

v = [0] * 10
for i in range(0, len(v)):
    v[i] = randint(0, 100)

def imprimir_vetor(a):
    for i in range (0, len(v)):
        print(v[i])

# arrumar
v = [0] * 10
for i in range(0, len(v)):
    v[i] = randint(0, 100)

maior = -1000000000
def imprimir_vetor(a):
    for i in range(0, len(v)):
        if(v[i] > maior):
            maior = v[i]
    print(maior)

imprimir_vetor(v)

