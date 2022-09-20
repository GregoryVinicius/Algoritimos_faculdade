import random
import math
import os
import time

def soma():
    x = int(input("primeiro valor: "))
    y = int(input("segundo valor: "))
    z = int(input("terceito valor: "))
    soma = x + y + z
    print("o resultado é:", soma)

def raiz():
    x = int(input("insira um valor para ver sua raiz: "))
    raiz = math.sqrt(x)
    print("a raiz é:",raiz)

def sortear_numero():
    print("sorteou o numero:", random.randint(0, 100))

def limpar_tela():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    print("1. somar 3 numeros")
    print("2. mostrar raiz de um número")
    print("3. sortear um numero de 0 a 100")
    print("4. Sair")

opção = 0

while (opção != 4):
    mostrar_menu
    opção = int(input("opção: "))
    if(opção == 1):
        soma()
        time.sleep(3)
    elif(opção == 2):
        raiz()
        time.sleep(3)
    elif(opção == 3):
        sortear_numero()
        time.sleep(3)
    elif(opção == 4):
        print("fechando programa")
        time.sleep(3)
    else:
        print("fechando programa")
        time.sleep(3)
    limpar_tela()
limpar_tela()