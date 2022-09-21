def mostrar_mensagem():
    print("olá")

def somar_numeros():
    x = int(input("N1: "))
    y = int(input("N2: "))
    a = x + y 
    print("a soma é: ", a)

def coisa(n1, n2, n3):
    maior = -1000000000000000
    if (n1 > n2 and n1 > n3):
        maior = n1
    elif(n2 > n1 and n2 > n3):
        maior = n2
    elif(n3 > n1 and n3> n2):
        maior = n3
    print(maior)