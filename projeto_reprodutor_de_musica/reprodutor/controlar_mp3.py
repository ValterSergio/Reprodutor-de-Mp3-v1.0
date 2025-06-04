from pygame import mixer
from threading import Thread
from time import sleep
from componentes.repositorio_json import Repositorio
from ferramentas.pesquisa_binaria import pesquisa_binaria, ordenar_por

class ReprodutorMp3:
    def __init__(self, musicas: list):
        mixer.init()
        self.musicas = ordenar_por(musicas, "nome")
        # numerar as musicas conforme a ordenação
        for num, musica in enumerate(self.musicas):
            musica.set_indice(num)
        
        self_total_musicas = len(self.musicas)
        self.reproduzindo = False
        self.musica_atual = None
        self.indice_atual = None

    def reproduzir_mp3(self, nome_musica: str):
        """
        Localiza e reproduz uma música pelo nome utilizando busca binária.
        """
        try:
            # Obtem a musicca por n log n ( mais eficiente para buscas)
            indice = pesquisa_binaria(self.musicas, nome_musica)

            # Adiciona o indice com a musica atual
            self.indice_atual = indice

            # reproduz a musica
            musica = self.musicas[indice]
            mixer.music.load(musica.caminho)
            mixer.music.play()

            # altera o estado da classe - musica sendo reproduzida e estado de reprodução
            self.musica_atual = musica
            self.reproduzindo = True
            print(f"Reproduzindo: {musica.nome}")

        except Exception as erro:
            print(f"Erro: Não foi possivel reproduzir a música -> {erro}")

    def pausar(self):
        if self.reproduzindo:
            mixer.music.pause()
            self.reproduzindo = False
            print("Música pausada.")

    def continuar(self):
        if not self.reproduzindo and self.musica_atual:
            mixer.music.unpause()
            self.reproduzindo = True
            print("Música retomada.")

    def parar(self):
        mixer.music.stop()
        self.reproduzindo = False
        print("Música parada.")

    def proxima(self, proxima: bool=True):
        # indice atual da musica
        indice_atual = self.musica_atual.get_indice()
        self.parar()
        
        if proxima:
            proxima_musica = self.musicas[indice_atual + 1]
            self.reproduzir_mp3(proxima_musica.nome)
        else:
            musica_anterior = self.musicas[indice_atual - 1]
            self.reproduzir_mp3(musica_anterior.nome)

# ========== Ponto de entrada para teste ==========
if __name__ == "__main__":
    from random import choice
    
    def atualizar_repositorio(repositorio):
        repositorio.atualizar_repositorio()

    def cronometro_thread(musica):
        """
        Simula um cronômetro com base na duração da música (em segundos).
        """
        tempo_restante = int(musica.duracao)
        while tempo_restante:
            sleep(1)
            print(f"Tempo restante: {tempo_restante} s")
            tempo_restante -= 1

    # Inicializa repositório
    repositorio = Repositorio()

    # Carrega músicas salvas
    musicas_salvas = repositorio.carregar_arquivo()

    # Cria cópia temporária da lista
    lista_para_reproducao = musicas_salvas.copy()

    # Faz backup dos dados atuais
    repositorio.fazer_backup()

    # Instancia reprodutor
    reprodutor = ReprodutorMp3(lista_para_reproducao)

    # Seleciona uma música aleatória para teste
    for x in lista_para_reproducao:
        musica_escolhida = x
    
        # Inicia threads de reprodução e cronômetro
        thread_reproducao = Thread(target=reprodutor.reproduzir_mp3, args=(musica_escolhida.nome,))
        thread_cronometro = Thread(target=cronometro_thread, args=(musica_escolhida,))
        thread_atualizar_dados = Thread(target=atualizar_repositorio, args=(repositorio,))

        thread_reproducao.start()
        thread_cronometro.start()
        thread_atualizar_dados.start()

        thread_reproducao.join()
        thread_atualizar_dados.join()
        thread_cronometro.join()

        # Restaura backup anterior
        (repositorio).recuperar_backup()
