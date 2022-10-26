import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "loja"
)

if(banco):
    print("Conectado com sucesso")
else:
    print("Erro na conecção") 

banco.close