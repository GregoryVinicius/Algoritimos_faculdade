"""
Exercicio 
criar um sub-algoritimo chamado fatorial
"""

"""


def fatorial(x1):
    resultado = 1
    for i in range (x1,1,-1):
        resultado *= i 
    print("fatorial:",resultado)

fatorial(5)
# Variavel local
def mostraX():
    x = 20
    print(x)


x = 10
print(x)
mostraX()
print(x)

# Variavel Global
def mostraX():
    global x
    x = 20
    print(x)


x = 10
print(x)
mostraX()
print(x)
"""

def fatorial (fat):
    resultado = 1
    for i in range(fat, 0, -1):
        resultado *= i

    return resultado

print(fatorial(5))