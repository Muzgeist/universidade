from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen
import sys
import math
import random

from screen.Cadastrar import Cadastrar
from screen.Listar import Listar

class SpiralTransition(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground)

        self.duration = 6000
        self.elapsed = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)

        self.particles = []
        self.max_radius = 0
        self.exploding = False

        self.base_color = QColor(0, 255, 0)  

    def start(self, callback, color):
        self.callback = callback
        self.base_color = color
        self.elapsed = 0
        self.particles.clear()
        self.exploding = False

        self.setGeometry(self.parent().rect())
        self.raise_()
        self.show()

        self.max_radius = math.hypot(self.width(), self.height())

        for _ in range(1000):
            angle = random.uniform(0, 360)
            radius = random.uniform(150, self.max_radius * 0.7)
            speed = random.uniform(1.2, 2.5)
            orbit_type = random.choice(["free", "core"])
            self.particles.append([angle, radius, speed, orbit_type])

        self.timer.start(16)

    def update_animation(self):
        self.elapsed += 16
        progress_ratio = min(self.elapsed / self.duration, 1)

        if self.elapsed < 3000:
            for p in self.particles:
                p[0] += p[2] * 2

        elif self.elapsed < 5200:
            for p in self.particles:
                if p[3] == "core":
                    p[1] *= 0.995
                    p[0] += 3
                else:
                    p[1] *= 0.97
                    p[0] += 2

        else:
            if not self.exploding:
                self.exploding = True
                new_particles = []
                for p in self.particles:
                    new_particles.append([
                        random.uniform(0, 360),
                        10,
                        random.uniform(8, 15),
                        "explosion"
                    ])
                self.particles.extend(new_particles)

            for p in self.particles:
                p[1] += p[2] * 2
                p[0] += random.uniform(-2, 2)

        if progress_ratio >= 1:
            self.timer.stop()
            self.callback()
            self.hide()

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2

        painter.fillRect(self.rect(), QColor(0, 0, 0, 110))

        for angle, radius, speed, mode in self.particles:
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))

            glow = QColor(self.base_color)
            glow.setAlpha(35)

            core = QColor(self.base_color)

            painter.setPen(QPen(glow, 6))
            painter.drawPoint(int(x), int(y))

            painter.setPen(QPen(core, 3))
            painter.drawPoint(int(x), int(y))

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(650, 400)
        self.janela.setLayout(self.layout)

        self.aplicar_estilo()

        self.spiral = SpiralTransition(self.janela)

        self.criar_botoes()

        self.janela.show()

    def aplicar_estilo(self):
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #0f0f14;
            }

            QPushButton {
                color: white;
                border-radius: 30px;
                padding: 18px;
                font-size: 18px;
            }

            #listar {
                background-color: #001a00;
                border: 2px solid #00ff66;
            }

            #listar:hover {
                background-color: #003300;
                border: 2px solid #00ff88;
            }

            #cadastrar {
                background-color: #001133;
                border: 2px solid #00aaff;
            }

            #cadastrar:hover {
                background-color: #002266;
                border: 2px solid #33bbff;
            }
        """)

    def criar_botoes(self):
        self.botao_listar = QPushButton("Listar")
        self.botao_listar.setObjectName("listar")

        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_cadastrar.setObjectName("cadastrar")

        efeito_verde = QGraphicsDropShadowEffect()
        efeito_verde.setBlurRadius(60)
        efeito_verde.setColor(QColor(0, 255, 120))
        efeito_verde.setOffset(0)

        efeito_azul = QGraphicsDropShadowEffect()
        efeito_azul.setBlurRadius(60)
        efeito_azul.setColor(QColor(0, 170, 255))
        efeito_azul.setOffset(0)

        self.botao_listar.setGraphicsEffect(efeito_verde)
        self.botao_cadastrar.setGraphicsEffect(efeito_azul)

        self.layout.addWidget(self.botao_listar)
        self.layout.addWidget(self.botao_cadastrar)

        self.botao_listar.clicked.connect(
            lambda: self.animar_transicao(
                self.abrir_listagem,
                QColor(0, 255, 120)
            )
        )

        self.botao_cadastrar.clicked.connect(
            lambda: self.animar_transicao(
                self.abrir_cadastro,
                QColor(0, 170, 255)
            )
        )

    def animar_transicao(self, callback, color):
        self.botao_listar.setEnabled(False)
        self.botao_cadastrar.setEnabled(False)
        self.spiral.start(lambda: self.finalizar(callback), color)

    def finalizar(self, callback):
        callback()
        self.janela.close()

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())