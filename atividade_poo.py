import mysql.connector


def salvar(dis):
    cursor = banco.cursor()

    sql = "INSERT INTO disciplina VALUES(%s, %s, %s, %s, %s)"
    valores = (None, dis.nome, dis.ch, dis.professor, dis.chr)

    cursor.execute(sql, valores)

    banco.commit()
    cursor.close()
    

def lerDados():
    cursor = banco.cursor()

    sql = ("SELECT * FROM disciplina")

    cursor.execute(sql)

    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)
        print("Codigo: ", linha[0])
        print("Nome: ", linha[1])
        print("Ch: ", linha[2])
        print("Professor: ", linha[3])
        print("chr: ", linha[4])
        print()


class Disciplina:
    def __init__(self):
        self.codigo = 0
        self.nome = ""
        self.ch = 0
        self.professor = ""
        self.chr = 0.0

dis = Disciplina()
dis.nome = input("Informe o nome da disciplina: ")
dis.ch = int(input("Carga horaria: "))
dis.professor = (input("nome professor: "))
dis.chr = dis.ch * 50 / 60

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="algoritmos"
)



salvar(dis)

lerDados()

banco.close()