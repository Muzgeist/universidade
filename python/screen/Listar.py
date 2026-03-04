from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)


class Listar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.configurar_janela()
        self.criar_componentes()
        self.carregar_dados()

    def configurar_janela(self):
        self.janela.setWindowTitle("Listagem de Alunos")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.6)
        altura = int(screen.height() * 0.7)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

        self.janela.setStyleSheet("""
            QWidget {
                background-color: #000000;
            }
        """)

    def criar_componentes(self):

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "CPF", "Telefone", "Matricula"]
        )
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #050505;
                color: #ccffcc;  /* verde claro quase branco */
                gridline-color: #39FF14; /* verde neon */
                font-size: 14px;
                border: 2px solid #39FF14;
            }

            QHeaderView::section {
                background-color: #000000;
                color: #39FF14;
                border: 1px solid #39FF14;
                padding: 4px;
                font-weight: bold;
            }

            QTableWidget::item {
                border: 1px solid #39FF14;
            }

            QTableWidget::item:selected {
                background-color: #39FF14;
                color: black;
            }
        """)

        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("Atualizar")

        botao_atualizar.setStyleSheet("""
            QPushButton {
                background-color: #000000;
                color: #39FF14;
                border: 2px solid #39FF14;
                padding: 10px;
                font-size: 15px;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #39FF14;
                color: black;
            }
        """)

        self.layout.addWidget(botao_atualizar)

        botao_atualizar.clicked.connect(self.carregar_dados)

    def carregar_dados(self):

        self.banco.connect()
        alunos = Aluno.listar(self.banco)
        self.banco.disconnect()

        self.tabela.setRowCount(len(alunos))

        for linha, aluno in enumerate(alunos):
            self.tabela.setItem(linha, 0, QTableWidgetItem(str(aluno["id"])))
            self.tabela.setItem(linha, 1, QTableWidgetItem(aluno["nome"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(aluno["email"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(aluno["cpf"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(aluno["telefone"]))

            if aluno["matricula"] == True:
                self.tabela.setItem(linha, 5, QTableWidgetItem("True"))
            else:
                self.tabela.setItem(linha, 5, QTableWidgetItem("False"))