import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "algoritimo"
)

if(banco):
    print("Conectado com sucesso")
else:
    print("Erro na conecção")

cursor = banco.cursor()

sql = "INSERT INTO disciplina VALUES(%s, %s, %s, %s)"
valores = (None, "algoritimos", 160, "Rafael")

cursor.execute(sql, valores)

sql = "INSERT INTO disciplina VALUES(%s, %s, %s, %s)"
valores = (None, "banco de dados", 160, "Helio")

cursor.execute(sql, valores)

sql = "INSERT INTO disciplina VALUES(%s, %s, %s, %s)"
valores = (None, "engenharia de software", 80, "Zavan")

cursor.execute(sql, valores)

sql = "INSERT INTO disciplina VALUES(%s, %s, %s, %s)"

nome_dis = input("insira o nome da disciplina: ")
carga_hora = int(input("Insira a carga horaria: "))
nome_prof = input("Insira o nome do professor: ")

valores = (None, nome_dis, carga_hora, nome_prof)

cursor.execute(sql, valores)

banco.commit()


cursor.close
banco.close
