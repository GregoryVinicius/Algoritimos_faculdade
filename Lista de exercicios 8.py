from operator import invert
import random
import math
from typing import Counter
from unicodedata import decimal
import collections

#ex 1 a)
# num = 0
# while(num < 100):
#     num += 1
#     print(num)

# ex 1 b)

# num = 0 
# soma = 0
# while(num <= 100):
#     soma += num
#     print(soma)
#     num = num + 1

# ex 1 c)

# num = 50

# while (num <= 100):
#     if (num % 2 == 0):
#         print(num)
#     num += 1

# ex 1 d)

# num = 1

# while (num <= 50):
#     if (num % 2 == 1):
#         print(num)
#     num += 1

# ex 1 e)

# num = 1
# soma = 0
# while (num <= 100):
#     if (num % 2 == 0):
#         soma += num
#     num += 1
# print(soma)

# ex 1 f) 

# x = int(input("insira o menor valor: "))
# y = int(input("insira o maior valor: "))

# while(x <= y):
#     print(x)
#     x += 1

# ex 1 g)

# x = int(input("insira o menor valor: "))
# y = int(input("insira o maior valor: "))
# soma = 0

# while(x <= y):
#     soma += x
#     x += 1
# print(soma)

# ex 1 h)
# x = int(input("insira o menor valor: "))
# y = int(input("insira o maior valor: "))

# while(x <= y):
#     if(x % 2 == 1):
#         print(x)
#     x += 1

# ex 2 a)

# x = int(input("insira um numero para saber a sua tabuada: "))
# mult = 1
# while (mult <= 10):
#     resutado = mult * x
#     print(x, "x", mult, "=", resutado)
#     mult += 1

# ex 2 b)

# x = int(input("insira um numero para começar a tabuada: "))
# y = int(input("insira outro numero para ver a tabuada ate ele terminar: "))
# z = int(input("insira o numero para ver a tabuada: "))

# while(x <= y):
#     resutado = z * x
#     print(z, "x", x, "=", resutado)
#     x += 1

# ex 3

# n = int (input("insira um valor para saber seu fatorial: "))
# fator = 1
# resutado = 1
# while(fator <= n):
#     resutado *= fator
#     print(resutado)
#     fator += 1

# ex 4 
# n = int(input("informe o valor de n: "))

# resultado = 0
# i = 1
# while(i <= n):
#     resultado = resultado + (1 / i)
#     i += 1
#     print(resultado)

# ex 5 a)

# num_certo = random.randint(1, 10)
# print(num_certo)
# num_usuario = int(input("Acertou, ganhou! Tente acertar um numero aleatorio: "))
# if(num_usuario == num_certo):
#     print("Você ganhou !!!")
# else:
#     print("Você perdeu !!!")


# ex 5 b, c, d)
# i = 1
# erros = 0


# while(i == 1 ):
#     num_certo = random.randint(1, 10)
#     print(num_certo)
#     num_usuario = int(input("Acertou, ganhou! Tente acertar um numero aleatorio: "))
#     if(num_usuario == num_certo):
#         print("Você ganhou !!!")
#         print(erros)
#         i += 1
#     else:
#         print("Você perdeu !!!, tente denovo")
#         erros += 1
# ex 6

# x = 0
# if (x < 4):
#     while(x < 4):
#         print("====== Menu Principal ======")
#         print("1. Par ou ímpar?")
#         print("2. Potência XY")
#         print("3. Raiz quadrada")
#         print("4. Sair")
#         x = int(input("insira a opção desejada: "))
#         if(x == 1):
#             num_usuaio = int(input("insira seu numero: "))
#             condição = input(("escolha par ou impar: ")).upper()
#             num_ale = random.randint(1, 2)
#             if(condição == "PAR" and ((num_usuaio + num_ale) % 2) == 0):
#                 print("Você ganhou!!!")
#             elif(condição == "IMPAR" and (num_usuaio + num_ale)% 2 == 1):
#                 print("Você ganhou!!!")
#             else:
#                 print("você perdeu")
#         elif(x == 2):
#             x = int(input("insira um valor para ser a base: "))
#             y = int(input("insira um valor para ser o expoente: "))
#             result =x ** y
#             print("seu resutado é", result)
#         elif(x == 3):
#             x = int(input("insira um valor ver sua raiz quadrada: "))
#             raiz = math.sqrt(x)
#             print(raiz)
#         elif(x == 4):
#             print("Fechando programa.")
# else:
#      print("opção invalida")

# ex 7

# x = 0
# if (x < 4):
#     while(x < 4):
#         print("====== Menu Principal ======")
#         print("1. Fazer a tabuada do 1 ao 10 para um número X")
#         print("2. Apresentar os múltiplos de X entre 1 e 100")
#         print("3. Apresentar a soma dos números de 1 a 100")
#         print("4. Sair do programa")
#         x = int(input("insira a opção desejada: "))
#         if (x == 1):
#             mult = int(input("insira um numero para ver sua tabuada: "))
#             for i in range (1, 11):
#                 result = mult * i
#                 print(mult, "x", i, "=", result)
#         elif(x == 2):
#             i = 1
#             mult = int(input("insira um numero para ver seus múltiplos de 1 a 100: "))
#             for i in range (0, 101, mult):
#                 if(i != 0):
#                     print(i)
#         elif(x == 3):
#             soma = 0
#             for i in range(1, 101):
#                 soma = i + soma
#             print(soma)
#         elif(x == 4):
#             print("fechando programa.")
#         else:
#             print("Opção invalida.")
# else:
#     print("opção invalida.")

# ex 8)O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios
#  de 1,99 e agora possui uma loja de conveniências. Faça um programa que
#  implemente uma caixa registradora. O programa deverá receber um número
#  desconhecido de valores referentes aos preços das mercadorias. O valor
#  “0” (zero) deve ser informado pelo operador para indicar o final da 
#  compra. O programa deve então mostrar o total da compra e perguntar o
#  valor em dinheiro que o cliente forneceu, para então calcular e mostrar
#  o valor do troco. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 10.00
# Produto 4: R$ 0
# Total: R$ 18.00
# Dinheiro: R$ 20.00
# Troco: R$ 2.00
# n = 0
# x = 1
# total = 0
# while(x != 0):
#     x = int(input(f"Produto {n+1}: "))
#     n += 1
#     if (x != 0):
#         total += x
#     else:
#         print("total: R$", total)
#         pag = int(input("dinheiro: "))
#         troco = pag - total
#         print("Troco:", troco)

# ex 9) O Departamento Estadual de Meteorologia lhe contratou para
#  desenvolver um programa que leia sete temperaturas, e informe ao
#  final a menor e a maior temperatura, além da média das temperaturas. 
# maior = -1000
# menor = 1000
# media = 0
# for i in range (1, 8):
#     temp = int(input("informe a temperatura: "))
#     if(temp > maior):
#         maior = temp
#     elif(temp < menor):
#         menor = temp
#     media += temp
# print(maior)
# print(menor)
# print(media / 7)

# ex 10) Faça um programa que calcule e mostre a média aritmética de N
#  notas informadas pelo usuário. O programa pode parar de pedir notas
#  quando o usuário informar -1, por exemplo. 

# media = 0
# n = 0
# soma = 0
# while(n > -1):
#     n = int(input("informe a proxima nota: "))
#     if(n > -1):
#         media += 1
#         soma += n
#     print("informe '-1'para ver a media.")
# print(soma / media)

# ex 11) Faça um programa que calcule o valor total investido por um
#  colecionador em sua coleção de CDs e o valor médio gasto em cada um 
#  deles. O usuário deverá informar a quantidade de CDs e o valor pago
#  em cada um. 

# quant = int(input("Insira quantos CDs você tem em sua coleção: "))
# quant += 1
# valor = 0
# for i in range(1, quant):
#     x = int(input(f"informe o valor do {i}: "))
#     valor += x
# print("o valor total investido é",valor)
# print("a media de cada CD é", valor / (quant - 1))

# ex 12) Uma academia deseja fazer um questionário entre seus clientes
#  para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
#  para isto você deve fazer um programa que pergunte a cada um dos
#  clientes da academia seu código, sua altura e seu peso. O final da
#  digitação de dados deve ser dada quando o usuário digitar 0 (zero)
#  no campo código. Ao encerrar o programa também deve ser informados
#  os códigos e valores do cliente mais alto, do mais baixo, do mais
#  gordo e do mais magro, além da média das alturas e dos pesos dos
#  clientes 

# gordo = 0
# magro = 10000000
# alto = 0
# baixo = 1000000
# x = 1
# y = 0
# for i in range(1, 5):
#     while (x == 1):
#         usuario = int(input("insira seu codigo de aluno: "))
#         peso = float(input("insira seu peso: "))
#         altura = float(input("insira sua altura: "))
#         if(peso > gordo):
#             usuario_gordo = usuario
#             gordo = peso
#         if(peso < magro):
#             usuario_magro = usuario
#             magro = peso
#         if(altura > alto):
#             usuario_alto = usuario
#             alto = altura
#         if(altura < baixo):
#             usuario_baixo = usuario
#             baixo = altura
#         x = int(input("se quiser finalizar digite '0', caso queira repetir digite '1': "))
#     x = int(input("se quiser finalizar digite '0', caso seja outro aluno digite '1': "))

# print("usuario mais gordo é", usuario_gordo)
# print("usuario mais magro é", usuario_magro)
# print("usuario mais alto é", usuario_alto)
# print("usuario mais baixo é", usuario_baixo)

# ex 13) Em uma competição de ginástica, cada atleta recebe votos de sete
#  jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo
#  a média dos votos restantes. Você deve fazer um programa que receba o
#  nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em
#  sua apresentação e depois informe a sua média, conforme a descrição
#  acima informada (retirar o melhor e o pior salto e depois calcular a
#  média com as notas restantes). As notas não são informados ordenadas.
#  Um exemplo de saída do programa deve ser conforme o exemplo abaixo: 

# nome = input("insira o nome do/a atleta: ")

# melhor = 0
# pior = 11
# media = 0

# print("Lojas Tabajara")
# print("Atleta:", nome)
# for i in range (1, 8):
#     nota = float(input(f"insira a {i}ª nota: "))
#     if (nota > melhor):
#         melhor = nota
#     if(nota < pior):
#         pior = nota
#     media += nota
# media = (media - melhor) - pior
# print("Resultado final:")
# print("Atleta:", nome)
# print("Melhor nota:", melhor)
# print("Pior nota", pior)
# print("Média:", media / 5)

# ex 14) Supondo que a população de um país A seja da ordem de 80.000
#  habitantes com uma taxa anual de crescimento de 3% e que a população
#  de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
#  Faça um programa que calcule e apresente o número de anos necessários
#  para que a população do país A ultrapasse ou iguale a população do
#  país B, mantidas as taxas de crescimento de cada um.

# a = 80000
# b = 200000
# ano = 0

# while(a < b):
#     a += a * 0.03
#     b += b * 0.015
#     ano += 1
# print(a)
# print(b)
# # print("demorou", ano, "anos para alcançar")
# centena = 0
# decimal = 0
# unitario = 0
# x = int(input("insira um numero de 1 até 999: "))
# while(x > 0):
#     while(x > 100):
#         if (x < centena):
#             x -= (centena - 100)
#         elif(x >= centena):        
#             centena += 100
#             print(x , centena)
#     while(x > 10):
#         if(x < decimal):
#             x -= (decimal - 10)
#         elif(x >= decimal):
#             decimal += 10
#             print(x, decimal)
#     while(x > 1):
#         if(x < unitario):
#             x -= (unitario - 1)
#         elif(x >= unitario):
#             unitario += 1
#             print(x, unitario)
        
#     print(x)

# unitario *= 100
# centena /= 100
# print(unitario, decimal, unitario)

# soma = 0
# media = 0
# for i in range(1, 6):
#     x = int(input(f"insira o {i}º valor: "))
#     soma += x
# media = soma / 5
# print("a soma e", soma)
# print("a media e", media)

# lista 2
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma
#  mensagem caso o valor seja inválido e continue pedindo até que o
#  usuário informe um valor válido.
# while(TRUE):
#     x = int(input("informe um valor entre 0 e 10: "))
#     if(x < 10 and x > 0):
#         print("valor valido.")
#         break
#     else: 
#         print("valor invalido.")

# Faça um programa que leia um nome de usuário e a sua senha e não
# aceite a senha igual ao nome do usuário, mostrando uma mensagem de
# erro e voltando a pedir as informações.

# while (TRUE):
#     nome = input("Nome: ")
#     senha = input("Senha:")
#     if (nome == senha):
#         print("senha não pode ser igual ao nome.")
#     else:
#         break


# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# while(True):
#     nome = input("Nome:")
#     nome_cont = "aaa"
#     idade = int(input("Idade: "))
#     sal = float(input("Salario: "))
#     sexo = input("Sexo(f ou m): ")
#     est_civ = input("Estado Civil(s, c, v, d): ")
#     if((nome > nome_cont) and (idade > 0 and idade < 150) and (sal > 0) and (sexo == "f" or sexo == "m")and (est_civ == "s" or est_civ == "c" or est_civ == "v" or est_civ == "d")):
#         print ("deu certo")
#         break
#     else:
#         print("algum campo invalido.")

# Supondo que a população de um país A sej a da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa 
# que calcule e escreva o número de anos necessários para que a população 
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas 
# de crescimento.
# ano = 0

# while(True):
#     a = int (input("insira a população da cidade A: "))
#     b = int (input("insira a população da cidade B: "))
#     porc_a = float (input("qual a porcentagem de crecimento da cidade A: "))
#     porc_b = float (input("qual a porcentagem de crecimento da cidade B: "))
#     while(True):
#         if (porc_a > porc_b):    
#             a += a * porc_a
#             b += b * porc_b
#             ano += 1
#             if(a >= b):
#                 print ("demorou", ano, "anos")
#                 break
#         else:
#             print("valor incorreto.(a cidade A não pode ter um valor de crecimento menor que a da cidade B)")
#     reiniciar = input ("Quer simular novamente: ").upper()
#     if(reiniciar == "NÃO"):
#         print("ate a proxima.")
#         break



