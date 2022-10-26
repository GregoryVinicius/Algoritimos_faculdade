class Aluno:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.email = ""
        self.sexo = False
        self.dataNascimento = Data()

class Data():
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0


a = Aluno()
a.name = "José do biri-biri"
a.age = 37
a.email = "Josedobiribiri@gmail.com"
a.sexo = True
a.dataNascimento.dia = 25
a.dataNascimento.mes = 10
a.dataNascimento.ano = 2022

b = Aluno()
b.name = "Grégory Vinicius"
b.age = 19
b.email = "gregoryviniciuscla@gmail.com"
b.sexo = True

print("Nome:", b.name)


d = Data()
d.dia = int(input("Dia: "))
d.mes = int(input("Mês: "))
d.ano = int(input("Ano: "))

print(f"Data: {d.dia}/{d.mes}/{d.ano}")