# x = [0] * 6
# x[0] = 10
# x[1] = 30
# x[2] = 5
# x[3] = 2
# x[4] = 15
# x[5] = 8
# [10, 30, 5, 2, 15, 8]
# [10, 30, 5, 2, 15, 8]
# [10, 5, 30, 2, 15, 8]
# [10, 5, 2, 30, 15, 8]
# [10, 5, 2, 15, 30, 8]
# [10, 5, 2, 15, 8, 30]
# a = 10
# b = 20
# c = b
# b = a
# a = c
# print(a, b, c)
# organização bolha
# for j in range (0 , len(x) - 1):
#     for i in range(0, len(x) - 1):
#         if (x[i] > x[i+1]):
#      c = x[i]
#      x[i + 1] = x[i]
#      x[i] = x[i + 1]
# organização seleção
# for i in range(0, len(x) - 1):
#     menor = x[i]
#     p_menor = i
#     for j in range(i+1 , len(x)):
#         if (menor > x[j]):
#             menor = x[j]
#             p_menor = j
#     c = x[i]
#     x[i] = menor
#     x[p_menor] = c
# print(x)
# organização 
# for i in range(1, len(x)):
#     valor = x[i]
#     j = i - 1
#     while (j + 1 >= 0 and x[j] > valor):
#         x[j + 1] = x [j]
#         j -= 1
#     x[j + 1] = valor
# i_valor = -1
# procurar = int(input("insira um valor para procurar no vetor"))
# for i in range (0, len(x)):
#     if (x[i] == procurar):
#         print("tem o numero que vc quer")
#         i_valor = i
#         Break# if (i_valor >= -1):
#     print("achoei na posição", i_valor)
# else:
#     print("não achamos")
# i_valor = -1
# i = 0
# f = len(x) - 1
# print(x)
# valor = int(input("Valor: "))
# while(i <= f):
#     m = int((i + f) / 2)
#     if (valor == x[m]):
#         i_valor = m
#         Break
#     elif(valor > x[m]):
#         i = m + 1
#     else:
#         f = m - 1
# if (i_valor >= 0):
#     print("achou")
# else:
#     print("não achou")
# ex encontrar o numero 3 na busca binaria
v = [0] * 10
v[0] = 1
v[1] = 3
v[2] = 5
v[3] = 7
v[4] = 9
v[5] = 11
v[6] = 13
v[7] = 15
v[8] = 17
v[9] = 19

i_valor = -1
i = 0 
f = len(v) - 1
valor = int(input("pesquise um valor: "))

while(i <= f):
    m = int((i+f)/2)
    if(v[m] == valor):
        i_valor = m 
        break
    elif(valor > v[m]):
        i = m + 1
    else:
        f = m - 1

if(i_valor >= 0):
    print("achou")
else:
    print("não achou")