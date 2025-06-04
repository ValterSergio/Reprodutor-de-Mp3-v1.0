from PySide6.QtWidgets import QHBoxLayout, QListWidget, QVBoxLayout


class LayoutHorizontalPrincipal(QHBoxLayout):
    def __init__(self, lista: QListWidget, layout_info: QVBoxLayout):
        super().__init__()
        self.adicionar_widget_musica(lista)
        self.adicionar_layout_informacoes(layout_info)
        print(f"Layout Horizontal Principal construido com sucesso !!!")

    def adicionar_widget_musica(self, lista: QListWidget):
        self.addWidget(lista)
    
    def adicionar_layout_informacoes(self, layout_informacoes: QVBoxLayout):
        self.addLayout(layout_informacoes)
    
