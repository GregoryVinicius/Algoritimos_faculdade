class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

class Professor:
    def __init__(self):
        self.nome = 0
        self.idade = 0
        self.salario = 0.0
        self.dataNasc = Data()
 
def exibirProfesso(professor):
    print("Nome:", professor.nome)
    print("Idade:", professor.idade)
    print("Salario: R$", professor.salario)

ayslan = Professor()
ayslan.nome = "Ayslan Posebom"
ayslan.idade = 41
ayslan.salario = 1100.90
ayslan.dataNasc.dia = 19 
ayslan.dataNasc.mes = 12
ayslan.dataNasc.ano = 1980

rafael = Professor()

rafael.nome = "Rafael Zottesso"
rafael.idade = 36
rafael.salario = 10000.00
rafael.dataNasc.dia = 14
rafael.dataNasc.mes = 5
rafael.dataNasc.ano = 1996


