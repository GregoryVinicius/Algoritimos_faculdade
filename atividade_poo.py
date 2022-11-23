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

    dados = cursor.fetchall

    resultados = [Disciplina()] * cursor.rowcount

    i = 0

    for linha in dados:
        d = Disciplina()
        d.codigo = linha[0]
        d.nome = linha[1]
        d.ch = linha[2]
        d.professor = linha[3]
        d.chr = linha[4]

        resultados[i] = d
        i += 1

        return resultados

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