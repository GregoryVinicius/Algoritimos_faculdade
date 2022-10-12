# 1 ) abrir arquivos de dados.txt e mostrar na tela 
# a ) qual o maior numero que tem no arquivo dados.txt
# b ) qual a media dos numeros que tem no arquivo dados.txt
# c ) quantos pares tem no arquivo dados.txt

arq = open("dados.txt", "r")

conteudo = arq.readlines()
maior = int(conteudo[0])
media = 0
pares = 0

for i in range(0,len(conteudo)):
    nome = int(conteudo[i])
    if (nome > maior):
        maior = nome

    media += nome

    if(nome % 2 == 0):
        pares += 1

media = media / i

print("o maior é:", maior)
print("a media é:", media)    
print("existem", pares, "pares")

arq.close()