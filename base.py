"""
# PARTE 1

Criar função chamada criarVetor que recebe um número inteiro por parâmetro represetando
o tamanho de um vetor. A função deve criar o vetor, preencher com valores aleatórios
entre 1 e 200 e retornar o vetor. No algoritmo principal, solicite o tamanho
do vetor para o usuário e crie o vetor utilizando a função.

# PARTE 2

Crie um procedimento chamado exibirVetor para exiba na tela o vetor recebido por parâmetro.

# PARTE 3

Crie uma função chamada somaImpares que calcule e retorne a soma de todos os números
ímpares de um vetor recebido por parâmetro. No algoritmo principal, apresente a soma na tela.

# PARTE 4

Implemente um procedimento chamado busca que recebe por parâmetro um número
informado pelo usuário. O procedimento deve, usando a busca sequencial, exibir
uma mensagem na tela dizendo se o número está ou não presente em um vetor
também recebido por parâmetro.

# PARTE 5

Implemente uma função chamada ordenar que recebe dois parâmetros: um vetor de números inteiros e o nome de um algoritmo de ordenação(bolha, inserção ou seleção).
Ordene e retorne o vetor recebido de acordo com o parâmetro de ordenação.
DETALHE: um procedimento com as três implementações(que tem no moodle)
"""

import random

def criarVetor (num1):
    v = [0] * num1
    for i in range(0, len(v)):
        v[i] = random.randint(1, 200)
    return v

def exibirVetor (vtr):
    for i in range(0, len(vtr)):
        print(vtr[i], " ", end = "")

def somaImpares (v):
    soma_impares = 0
    for i in range(0, len(v)):
        if (v[i] % 2 == 1):
            soma_impares += v[i]
    return soma_impares

def buscar (num1, vet):
    for i in range (0, len(vet)):
        if(vet[i] == num1):
            print("achei")
            return True
    print("não esta no vetor")

def ordenar (v, ord):
    if(ord == "bolha".upper()):
            for j in range (0 , len(v)):
                for i in range(0, len(v) - 1):
                    if (v[i] > v[i+1]):
                        c = v[i]
                        v[i] = v[i + 1]
                        v[i + 1] = c

    elif(ord == "iserção".upper()):
        for i in range(1, len(v)):
            valor = v[i]
            i_ant = i - 1

            while(i_ant >= 0 and v[i_ant] > valor):
                v[i_ant+1] = v[i_ant]
                i_ant -= 1

            v[i_ant+1] = valor

    elif(ord == "seleção".upper()):
        for i in range(0, len(v)-1):
            menor = v[i]
            i_menor = i

            for j in range(i+1, len(v)):
                if(v[j] < menor):
                    menor = v[j]
                    i_menor = j

            temp = v[i]
            v[i] = menor
            v[i_menor] = temp

    return v