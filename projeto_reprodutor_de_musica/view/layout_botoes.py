from PySide6.QtWidgets import QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
from view.lista_musicas import ListaMusica
from reprodutor.controlar_mp3 import ReprodutorMp3


class LayoutBotoes(QHBoxLayout):
    def __init__(self, reprodutor: ReprodutorMp3):
        super().__init__()
        self.reprodutor = reprodutor
        self.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self._criar_botoes()

    def _criar_botoes(self):
        botoes_info = [
            ("Anterior", self.acao_anterior),
            ("PLAY", self.acao_play),
            ("CONTINUE", self.acao_continuar),
            ("PAUSE", self.acao_pausar),
            ("Proxima", self.acao_proximo)
        ]
        for texto, acao in botoes_info:
            self._adicionar_botao(texto, acao)

    def _adicionar_botao(self, texto: str, slot_func):
        botao = QPushButton(texto)
        botao.clicked.connect(slot_func)
        self.addWidget(botao)

    def acao_play(self):
        musica = ListaMusica.musica_atual
        if not musica:
            print("Selecione uma música")
            return

        if self.reprodutor.reproduzindo:
            self.reprodutor.parar()
        self.reprodutor.reproduzir_mp3(musica.nome)

    def acao_pausar(self):
        self.reprodutor.pausar()

    def acao_proximo(self):
        self.reprodutor.proxima()

    def acao_anterior(self):
        self.reprodutor.proxima(False)

    def acao_continuar(self):
        self.reprodutor.continuar()