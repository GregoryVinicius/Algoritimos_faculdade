import random
import math
import os
import time
import minhas_funcoes

# def soma():
#     x = int(input("primeiro valor: "))
#     y = int(input("segundo valor: "))
#     z = int(input("terceito valor: "))
#     soma = x + y + z
#     print("o resultado é:", soma)

# def raiz():
#     x = int(input("insira um valor para ver sua raiz: "))
#     raiz = math.sqrt(x)
#     print("a raiz é:",raiz)

# def sortear_numero():
#     print("sorteou o numero:", random.randint(0, 100))

# def limpar_tela():
#     if(os.name == "nt"):
#         os.system("cls")
#     else:
#         os.system("clear")

# def mostrar_menu():
#     print("1. somar 3 numeros")
#     print("2. mostrar raiz de um número")
#     print("3. sortear um numero de 0 a 100")
#     print("4. Sair")

# opção = 0

# while (opção != 4):
#     mostrar_menu
#     opção = int(input("opção: "))
#     if(opção == 1):
#         soma()
#         time.sleep(3)
#     elif(opção == 2):
#         raiz()
#         time.sleep(3)
#     elif(opção == 3):
#         sortear_numero()
#         time.sleep(3)
#     elif(opção == 4):
#         print("fechando programa")
#         time.sleep(3)
#     else:
#         print("fechando programa")
#         time.sleep(3)
#     limpar_tela()
# limpar_tela()


# implementar os 5 primeiros exercicios da apostila
# Exercício 01: O que é um procedimento?
# Os procedimentos são subalgoritmos responsáveis por executar um conjunto de instruções (conjunto de
# comandos). Estes comandos são executados sempre que o procedimento for chamado.
# Para definir um procedimento, utilizamos a palavra def seguida do nome do procedimento e um par de
# parênteses.

# Exercício 02: Qual é a sintaxe para se criar um procedimento?
# def nomeFuncao():
#    conjunto de instruções

# Exercício 03: Seja acao() um procedimento. Durante o algoritmo, como chamar este procedimento para que
# seu código seja executado?
# import acao()

# Exercício 04: O que são parâmetros? Para que eles servem?
# # Parâmetros são valores que são passados para o
# procedimento. Sempre que um procedimento precisar de valores para ser executado, estes valores devem ser
# fornecidos nos parâmetros. Os parâmetros sempre vem dentro dos parênteses.

# Exercício 05: Seja acao(a, b, c) um procedimento que recebe três números inteiros como parâmetro. Como
# chamar este procedimento para que seu código seja executado?
# import acao()
# print(a)
# print(b)
# print(c)

# implemetar um procedimento chamado 'coisa' o procedimento precisa de 3 valores numericos, e deve mostrar na tela
# qual dos 3 é o maior
v = [0] * 3
a = int(input("insira o 1º valor: "))
b = int(input("insira o 2º valor: "))
c = int(input("insira o 3º valor: "))

minhas_funcoes.coisa(a,b,c)
