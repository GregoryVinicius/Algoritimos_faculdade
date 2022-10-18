from random import randint

def num_usu():
    num_usu = input("insira um numero: ")
    num_usu = int(num_usu)
    return num_usu

def num_ale(num):
    num_ale = randint(1, num)
    return num_ale

def mes(mes_usuario):
    mt = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if (mes_usuario >= 1 or mes_usuario <= 12):
        for i in range(0, len(mt) + 1):
            if (mes_usuario - 1 == i):
                m = print(f"o mês escolhido foi {mt[i]}")
    else:
        print("Mês invalido")
    return m
    
def qua(num):
    result = num ** 2
    return result

def retan(base, altura):
    result = base * altura
    return result

def trian(base, altura):
    result = (base * altura) / 2
    return result

def trape(base_maior, base_menor, altura):
    result = (base_maior + base_menor) * altura / 2
    return result

def fatFor (num):
    for i in range (1, num):
        fat *= i
    return fat

def fatSemFor (num):
    if(num == 1 or num == 0):
        return 1
    else:
        return num * fatSemFor(num - 1)

def encotrarMaior(v):
    maior = -1000000000000
    for i in range(0, len(v)):
        if(v[i] > maior):
            maior = v[i]
    return maior

def encontrarMenor(v):
    menor = 10000000000
    for i in range(0, len(v)):
        if(v[i] < menor):
            menor = v[i]
    return menor

def encontrarMedia(v):
    soma = 0
    for i in range(0, len(v)):
        soma += v[i]
    media = soma / len(v)
    return media

def vet2(v):
    v2 = [0] * len(v)
    for i in range (0, len(v)):
        v2[i] = v[i] * 2
    return v2

def dataExtenso (dd, mm, aaaa):
    data = print(dd, "de", mes(mm), "de", aaaa)
    return data

def numInverso (num):
