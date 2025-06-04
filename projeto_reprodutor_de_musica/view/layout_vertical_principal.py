from PySide6.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt

class LayoutVerticalPrincipal(QVBoxLayout):
    def __init__(self, layout_horizontal: QHBoxLayout):
        super().__init__()
        self.titulo()
        self.addLayout(layout_horizontal)
        print(f"Layout Vertical Principal construido com sucesso !!!")

    def titulo(self):
        titulo = QLabel("Reprodutor de Música do Tio Laba")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.addWidget(titulo)
    