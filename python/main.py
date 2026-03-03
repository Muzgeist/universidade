from modules.aluno import Aluno
from modules.mysql import MySQL

banco = MySQL(
    '127.0.0.1',
    'root',
    '',
    'universidade'
)
banco = MySQL()

banco.connect()

consulta = Aluno.listar(banco)

aluno = Aluno(
    "Jose Maria",
    "Jose.Maria@email.com",
    "98765432110",
    "031987043654"
    "Rua paineiras eldorado 1300",
    )

query = aluno.cadastrar(banco)
# print (query)

#banco.execute_query(query)

banco.disconnect()

