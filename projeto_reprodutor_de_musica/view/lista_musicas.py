from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Qt
from componentes.musica import Musica
from reprodutor.controlar_mp3 import ReprodutorMp3

class ListaMusica(QListWidget):
    musica_atual = None

    def __init__(self, lista_musicas: list[Musica], reprodutor: ReprodutorMp3, layout_info: object):
        super().__init__()
        self.layout_info = layout_info
        self.reprodutor = reprodutor
        self.criar_lista(lista_musicas)
        self.acoes_lista()
        print("Lista de Musica Construida com sucesso")

    def criar_lista(self, lista_musicas: list[Musica]):
    
        for musica in lista_musicas:
            item = QListWidgetItem(musica.nome)
            item.setData(Qt.UserRole, musica)
            self.addItem(item)
    
    def acoes_lista(self):
        self.itemClicked.connect(self.um_clique)
        self.itemDoubleClicked.connect(self.dois_clique)

    def um_clique(self, item):
        musica = item.data(Qt.UserRole)
        ListaMusica.musica_atual = musica
        self.layout_info.exibir_informacoes(musica)
        
        print("Musica selecionada: ", musica.nome)
    
    def dois_clique(self, item):
        musica = item.data(Qt.UserRole)
        self.reprodutor.reproduzir_mp3(musica.nome)