from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)


class Cadastrar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastrar Aluno")

        screen = self.app.primaryScreen()
        tamanho = screen.availableGeometry()

        largura = int(tamanho.width() * 0.4)
        altura = int(tamanho.height() * 0.6)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

        self.janela.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: #dff6ff; /* azul quase branco */
                font-size: 14px;
            }

            QLabel {
                color: #00f0ff;
                font-weight: bold;
                margin-top: 8px;
            }

            QLineEdit {
                background-color: #050505;
                color: #dff6ff;
                border: 2px solid #00f0ff;
                padding: 6px;
                border-radius: 6px;
            }

            QLineEdit:focus {
                border: 2px solid #33f5ff;
                background-color: #0a0a0a;
            }

            QPushButton {
                background-color: #000000;
                color: #00f0ff;
                border: 2px solid #00f0ff;
                padding: 10px;
                font-size: 15px;
                border-radius: 8px;
                margin-top: 15px;
            }

            QPushButton:hover {
                background-color: #00f0ff;
                color: black;
            }
        """)

    def criar_componentes(self):
        componentes = {
            "nome": "Digite seu nome:",
            "email": "Digite seu email:",
            "cpf": "Digite seu CPF:",
            "telefone": "Digite seu telefone:",
            "endereco": "Digite seu endereço:",
        }

        for chave, valor in componentes.items():
            label = QLabel(valor)
            campo = QLineEdit()

            self.layout.addWidget(label)
            self.layout.addWidget(campo)

            self.campos[chave] = campo

        botao_Cadastrar = QPushButton("Cadastrar")
        self.layout.addWidget(botao_Cadastrar)

        botao_Cadastrar.clicked.connect(self.cadastrar)

    def validar_campos(self):
        nome = self.campos["nome"].text().strip()
        email = self.campos["email"].text().strip()
        cpf = self.campos["cpf"].text().strip()
        telefone = self.campos["telefone"].text().strip()
        endereco = self.campos["endereco"].text().strip()

        if not nome:
            QMessageBox.warning(self.janela, "Erro de validação", "Nome é obrigatório.")
            return False

        if "@" not in email or "." not in email:
            QMessageBox.warning(self.janela, "Erro de validação", "Email inválido.")
            return False

        if not cpf.isdigit() or len(cpf) != 11:
            QMessageBox.warning(self.janela, "Erro de validação", "CPF deve conter 11 números.")
            return False

        if not telefone.isdigit():
            QMessageBox.warning(self.janela, "Erro de validação", "Telefone deve conter apenas números.")
            return False

        if not endereco:
            QMessageBox.warning(self.janela, "Erro de validação", "Endereço é obrigatório.")
            return False

        return True

    def cadastrar(self):

        if not self.validar_campos():
            return

        aluno = Aluno(
            self.campos["nome"].text().strip(),
            self.campos["email"].text().strip(),
            self.campos["cpf"].text().strip(),
            self.campos["telefone"].text().strip(),
            self.campos["endereco"].text().strip(),
        )

        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)

            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno cadastrado com sucesso!"
            )

            self.limpar_campos()

        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao cadastrar: {e}"
            )

        finally:
            self.banco.disconnect()

    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()