from PySide6.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

from view.lista_musicas import ListaMusica # receber o sinal
class LayoutInformacoes(QVBoxLayout):
    def __init__(self, layout_botoes):
        super().__init__()
        self.rotulos = []
        self.layout_botoes = layout_botoes
        self.exibir_informacoes(ListaMusica.musica_atual)
        

    def exibir_informacoes(self, sinal: object):
        for rotulo in self.rotulos:
            self.removeWidget(rotulo)
            rotulo.deleteLater()
        self.rotulos.clear()
        self.removeItem(self.layout_botoes)

        if not sinal:
           texto = QLabel("Selecione uma musica")
           texto.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
           self.addWidget(texto)
           self.rotulos.append(texto)
        else:
            for atributo, valor in sinal.__dict__.items():
                proibidos = ["caminho", "tamanho_mb", "formato", "duracao", "nome"]
                if atributo in proibidos:
                    continue

                texto = QLabel(f"{atributo}: {valor}")
                texto.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
                self.addWidget(texto)
                self.rotulos.append(texto)

        self.addLayout(self.layout_botoes)
