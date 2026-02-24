from modules.mysql import MySQL

class Aluno:
    def __init__(self, nome, email, cpf, telefone, endereco):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.matricula = True

    def cadastrar(self, db=MySQL()):
        query = f"""
            INSERT INTO alunos(
            nome,
            email,
            cpf,
            telefone,
            endereco
        ) Values(
            '{self.nome}',
            '{self.email}',
            '{self.cpf}',
            '{self.telefone}',
            '{self.endereco}'
        )
        """
        db.execute_query(query)
    def editar(self):
        pass
    
    def transferir(self):
        pass