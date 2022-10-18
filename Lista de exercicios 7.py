import random
# ex 1 
# a)
# for i in range(1,101):
#     print(i)
# b)
# for i in range (100, 0, -1):
#     print(i)
# c)
# for i in range (1 , 101, 2):
#     print(i + 1)
# d)
# for i in range (1, 101, 2):
#     print(i)
# e)
# soma = 0
# for i in range (1, 101):
#     soma = soma + i
# print(soma)
# f)
# for a in range(1,2):
#     x = int(input("informe um valor: "))
#     y = int(input("informe o segundo valor: "))

#     x = x - 1
#     y = y + 1

#     if (x < y):
#         for i in range (x, y):
#             x = x + i 
#         print (x)
#     else:
#         print("Insira o menor valor primeiro!!!")

# g)

# j = int(input("insira um valor para fatorar: "))
# if (j > 0):
#     for i in range(1, j):
#         j = i * j
#     print(j)
# else:
#     print("Não são permitidos valores negativos!!!")

# ex 2 
# x = 0
# for i in range (1 , 6):
#     y = int(input("Insira um valor: "))
#     if (y > x):
#         x = y
# print(x, "atualmente é seu maior valor")

# ex 3
# y = 0
# for i in range (0, 5):
#     x = int(input("insira um valor: "))
#     y = x + y
#     z = y / 5
# print("a soma dos numeros é:", y)
# print ("a media dos numeros é:", z)

# ex 4 
# for i in range (1, 50, 2):
#     print(i, "é um numero impar")

# ex 5
# x = 1.99
# print("Lojas Quase Dois - Tabela de preços")
# for i in range (1, 51):
#     y = x * i
#     print(i,"- R$", y)

# ex 6 
# x = int (input ("insira um numero para ver sua tabuada: "))

# for i in range (1, 11):
#     z = x * i
#     print(x, "x", i, "=", z)

# ex 7 

# for i in range (0, 3):
#     x = int (input ("insira um numero para ver sua tebuada: "))
#     for u in range (1, 11):
#         z = x * u
#         print(x, "x", u, "=", z)