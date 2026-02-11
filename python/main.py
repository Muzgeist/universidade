from modules.aluno import Aluno
from modules.mysql import MySQL

banco = MySQL()

banco.connect()

aluno = Aluno(
    "Jose Maria",
    "Jose.Maria@email.com",
    "98765432110",
    "031987043654"
    "Rua paineiras eldorado 1300",
    )

query = aluno.cadastrar()
# print (query)

banco.execute_query(query)

banco.disconnect()

