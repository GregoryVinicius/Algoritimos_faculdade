# # EX 1 Para cada conjunto de valores abaixo, escreva o código necessário para criar vetores:
# # a)
# x = [0] * 9
# x[0] = 0
# x[1] = 4
# x[2] = 9
# x[3] = 18
# x[4] = 27
# x[5] = 41
# x[6] = 65
# x[7] = 88
# x[8] = 121

# # 2) a)
# print(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]) 

# # 2) b)
# print(x[8], x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0])

# # b)
# y = [0] * 4
# y[0] = "Rafael"
# y[1] = "Ayslan"
# y[2] = "Daniela"
# y[3] = "Frank"

# # 2) a)
# print(y[0], y[1], y[2], y[3])

# # 2) b)
# print(y[3], y[2], y[1], y[0])
# # c)

# z = [0] * 4
# z[0] = 3290.90
# z[1] = 128.50
# z[2] = 85.90
# z[3] = 789.31

# # 2) a)
# print(z[0], z[1], z[2], z[3])

# # 2) b)
# print(z[3], z[2], z[1], z[0])

# 3
# x = [0] * 5
# x[0] = int(input("insira o 1º numero: "))
# x[1] = int(input("insira o 2º numero: "))
# x[2] = int(input("insira o 3º numero: "))
# x[3] = int(input("insira o 4º numero: "))
# x[4] = int(input("insira o 5º numero: "))

# # 3) a)
# print(x[0], x[1], x[2], x[3], x[4])

# # 3) b)
# print(x[0] * 2, x[1]* 2, x[2] * 2, x[3] * 2, x[4] * 2)

# # 3) c)
# print(x[0] / 2, x[1] / 2, x[2] / 2, x[3] / 2, x[4] / 2)

# 4)
# cadastro = [0] * 4

# cadastro[0] = input("Nome completo: ")
# cadastro[1] = input("Endereço: ")
# cadastro[2] = input("Telefone: ") 
# cadastro[3] = input("E-mail: ")

# 4) a)

# print("Nome completo: \t", cadastro[0])
# print("Endereço: \t", cadastro[1])
# print("Telefone: \t", cadastro[2])
# print("E-mail: \t", cadastro[3])
"""
# 5)
num_deci = [0] * 4
num_deci[0] = float(input("insira um numero: "))
num_deci[1] = float(input("insira um numero: "))
num_deci[2] = float(input("insira um numero: "))
num_deci[3] = float(input("insira um numero: "))

# 5) a)

print("a soma dos seus numeros é:", num_deci[0] + num_deci[1] + num_deci[2] + num_deci[3])

# 5) b)

print("a media dos seus numeros é: ", (num_deci[0] + num_deci[1] + num_deci[2] + num_deci[3]) / 5)
"""
"""
1 - Crie procedimentos com parâmetros informados pelo usuário no programa
 principal:
a - Faça uma procedimento que soma dois números. Deve ser utilizado um
procedimento chamado somar(), que deve receber os números a serem
somados, somar os números e apresentar o resultado na tela.

b - Faça um procedimento que multiplica dois números. Deve ser utilizado 
um procedimento chamado multiplicar(), que deve receber os números e 
realizar a operação de multiplicação, apresentando o resultado na tela.

c - Faça um procedimento que calcule a raiz quadrada de um número 
chamado calcularRaiz(). O procedimento deve receber o número por 
parâmetro, efetuar o cálculo e apresentar o resultado.

d - Faça um procedimento que calcule a potência de um número (XY) 
chamado calcularPotencia(). O procedimento deve receber os números por 
parâmetro, efetuar o cálculo e apresentar o resultado.

e - Faça um procedimento que calcule a tabuada de 1 a 10 para um número 
chamado calcularTabuada(). O procedimento deve receber o número por 
parâmetro, efetuar o cálculo e apresentar o resultado.
"""

def menu():
    print ("-----------------Menu-----------------")
    print ("1 - Somar dois numeros.")
    print ("2 - Multiplicar dois numeros.")
    print ("3 - Calcular a raiz de um numero.")
    print ("4 - Calcular a potencia de um numero.")
    print ("5 - Calcular a tabuada de um numero.")
    print ("0 - Sair do programa.")

def somar(soma1, soma2):
    result = soma1 + soma2

    print("O resultado é:", result)

def multiplicar(mult1, mult2):
    result = mult1 * mult2
    print("O resultado é:", result)

def calcularRaiz(raiz1):
    result = raiz1 ** (1/2)
    print (result)

def calcularPotencia(pot1, pot2):
    result = pot1 ** pot2
    print(result)

def calcularTabuada(tab1):
    for i in range (1, 11):
        result = tab1 * i
        print(tab1, "X", i, "=", result)
while(True):
    menu()
    esc_usu = int(input("Digite o numero de oque quer fazer: "))
    if (esc_usu == 1):
        num1 = int(input("Primeiro numero a somar: "))
        num2 = int(input("Segundo numero a somar: "))
        somar(num1, num2)


    elif(esc_usu == 2):
        num1 = int(input("Primeiro numero a multiplicar: "))
        num2 = int(input("Segundo numero a multiplicar: "))
        multiplicar(num1, num2)

    elif(esc_usu == 3):
        num1 = int(input("Insira um numero para ver sua raiz: "))
        calcularRaiz(num1)

    elif(esc_usu == 4):
        num1 = int(input("Primeiro numero a base: "))
        num2 = int(input("Segundo numero o espoente: "))
        calcularPotencia(num1, num2)

    elif(esc_usu == 5):
        num1 = int(input("Insira um numero par ver sua tabuada: "))
        calcularTabuada(num1)
    
    elif(esc_usu == 0):
        print("Ate a proxima!!!")
        break

    else:
        print("opção invalida.")