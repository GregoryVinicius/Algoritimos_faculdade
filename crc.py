import base
vetor_usuario = int(input("insira um valor para criar um vetor: "))

v = base.criarVetor(vetor_usuario)


base.exibirVetor(v)
print()
soma_impares = base.somaImpares(v)

print("o resultado da soma é: ", soma_impares)


info_busca = int(input("insira um numero para fazer a busca: "))

base.buscar(info_busca, v)

met_usr = input("insira um metodo de ordenação: ").upper()

vtr_ord = base.ordenar(v, met_usr)

for i in range(0, len(vtr_ord)):
    print(vtr_ord[i])
