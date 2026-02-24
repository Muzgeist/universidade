from modules.mysql import MySQL
from modules.aluno import Aluno

import sys


from PySide6.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

class TelaCadastro():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        
        self.labels = []
        self.campos = []
        
        self.janela.setWindowTitle("cadastro Aluno")
        self.janela.resize(1200, 600)
        
    def criar_componentes(self):
        self.labels.append(QLabel("digite seu nome"))
        self.labels.append(QLabel("digite seu Email"))
        self.labels.append(QLabel("digite seu cpf"))
        self.labels.append(QLabel("digite seu telefone"))
        self.labels.append(QLabel("digite seu endereco"))
        
        for label in self.labels:
            self.layout.addWidget(label)
            
            campo = QLineEdit()
            self.campos.append(campo)
            self.layout.addWidget(campo)
            
        botao_cadasttro = QPushButton("cadastrar")
        self.layout.addWidget(botao_cadasttro)
        
        self.janela.setLayout(self.layout)
        botao_cadasttro.clicked.connect(self.cadastrar)
        
        
        

    def cadastrar(self):
        aluno = Aluno(
            campo_nome.text(),
            campo_email.text(),
            campo_cpf.text(),
            campo_telefone.text(),
            campo_endereco.text()
        )
        
        banco = MySQL()
        banco.connect()
        
        aluno.cadastrar(banco)
    
        banco.disconnect()
    
        

#janela = QWidget()
#janela.setWindowTitle("Cadastro Aluno")
#janela.resize(1200, 600)
#janela.show()
#layout = QVBoxLayout()
#componentes
#label_nome = QLabel("digite seu nome: ")
#campo_nome = QLineEdit()

#label_email = QLabel("digite seu Email: ")
#campo_email = QLineEdit()

#label_cpf = QLabel("digite seu cpf: ")
#campo_cpf = QLineEdit()

#label_telefone = QLabel("digite seu telefone: ")
#campo_telefone = QLineEdit()

#label_endereco = QLabel("digite seu Endereço: ")
#campo_endereco = QLineEdit()

#botao = QPushButton("cadastrar")

#layout.addWidget(label_nome)
#layout.addWidget(campo_nome)

#layout.addWidget(label_email)
#layout.addWidget(campo_email)

#layout.addWidget(label_cpf)
#layout.addWidget(campo_cpf)

#layout.addWidget(label_telefone)
#layout.addWidget(campo_telefone)

#layout.addWidget(label_endereco)
#layout.addWidget(campo_endereco)

layout.addWidget(botao)

janela.setLayout(layout)


botao.clicked.connect(cadastro)
janela.show()
sys.exit(app.exec())



