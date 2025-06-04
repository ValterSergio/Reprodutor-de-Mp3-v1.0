from PySide6.QtWidgets import QApplication, QVBoxLayout
from view.janela_principal import JanelaPrincipal
from view.layout_vertical_principal import LayoutVerticalPrincipal
from view.layout_horizontal_principal import LayoutHorizontalPrincipal
from view.lista_musicas import ListaMusica
from view.layout_informacoes import LayoutInformacoes
from view.layout_botoes import LayoutBotoes

from componentes.repositorio_json import Repositorio
from reprodutor.controlar_mp3 import ReprodutorMp3

# iniciar repositorio
repositorio = Repositorio()
musicas = repositorio.carregar_arquivo()

# fazer copia dos dados armazenados
copia_repositorio = musicas.copy()

# iniciar reprodutor
reprodutor = ReprodutorMp3(copia_repositorio)

# iniciar aplicação
app = QApplication([])

# iniciar layout de botoes
layout_botoes = LayoutBotoes(reprodutor)

# iniciar layout de informações
layout_informacoes = LayoutInformacoes(layout_botoes)

# Iniciar widget lista
lista_musicas_widget = ListaMusica(copia_repositorio, reprodutor, layout_informacoes)


# Layout horizontal - principal
layout_principal_horizontal = LayoutHorizontalPrincipal(lista_musicas_widget, layout_informacoes)

# layout vertical - principal
layout_principal_vertical = LayoutVerticalPrincipal(layout_principal_horizontal)

# iniciar janela principal
janela_principal = JanelaPrincipal(layout_principal_vertical)
janela_principal.show()
app.exec()