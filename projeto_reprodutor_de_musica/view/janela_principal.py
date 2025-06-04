from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class JanelaPrincipal(QMainWindow):
    def __init__(self, layout: QVBoxLayout):
        super().__init__()
        self.widget_central = QWidget()
        self.setWindowTitle("Reprodutor Mp3")
        self.setStyleSheet("background-color: white; color: black;")
        self.resize(500, 500)

        self.setCentralWidget(self.widget_central)
        self.widget_central.setLayout(layout)
        print(f"Janela Principal construida com sucesso !!!")
