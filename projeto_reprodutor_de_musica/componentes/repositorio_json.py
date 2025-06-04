from componentes.localizador_de_mp3 import LocalizarMp3
from componentes.musica import Musica
from componentes.backup import Backup
from pathlib import Path
import json
import os

# o controlador define onde vai ficar armazenado tudo, esse repositorio armazena
# todas as musicas encontradas no computador cliente
CAMINHO_RAIZ = os.path.join(Path(__file__).parent.parent, "dados")
CAMINHO_ARQUIVO = os.path.join(CAMINHO_RAIZ, "RepositorioMusicas.json")

class Repositorio:
    # garantir apenas a criação de um repositorio durante o tempo de execução
    limite_repositorio = 1
    total_repositorios = 0
    def __init__(self):
        self.__class__.permitir_chamada()
        self.musicas_armazenadas = []
        self.caminho_arquivo = CAMINHO_ARQUIVO
        # criar pasta de backup
        os.makedirs(CAMINHO_RAIZ, exist_ok=True)
        if not os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "w"):
                pass
        
        # Manipular Backup
        self.backup = Backup(self.caminho_arquivo)

    @classmethod
    def permitir_chamada(cls):
        if cls.total_repositorios >= cls.limite_repositorio:
            raise RuntimeError("ERRO: Só pode ser criado um repositorio !!!")
        
        cls.total_repositorios = 1
        return True

    def salvar_arquivo(self, musicas_armazenadas: list=None):
        salvar_musicas = musicas_armazenadas or self.musicas_armazenadas
        
        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            # como estou lidando com objetos devo passar os atributos para dicionario
            temporaria = []
            for musica in salvar_musicas:
                temporaria.append(vars(musica))
            
            json.dump(temporaria, arquivo, ensure_ascii=True, indent=1)
    
    def carregar_arquivo(self):
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                if not isinstance(dados, list):
                    raise ValueError("Erro: Passe uma lista de objetos como parâmetro")
                
            self.musicas_armazenadas =  [Musica(**musica) for musica in dados]
        except json.JSONDecodeError:
            self.musicas_armazenadas = LocalizarMp3().filtrar_arquivos()
            
        finally:
            self.salvar_arquivo()
            return self.musicas_armazenadas
        
    def atualizar_repositorio(self):
        self.musicas_armazenadas = LocalizarMp3().filtrar_arquivos()
    
    def fazer_backup(self):
        self.backup.adicionar_backup()
    
    def recuperar_backup(self):
        # altera o caminho de carregamento do arquivo
        self.caminho_arquivo = self.backup.recuperar_ultimo_backup() # retorna o caminho do armazenamento

        # faz o carregamento do novo arquivo
        novo_arquivo = self.carregar_arquivo()

        # torna o caminho do arquivo para o caminho raiz
        self.caminho_arquivo = CAMINHO_ARQUIVO

        # agora eu salvo o novo arquivo com os dados restaurados
        self.salvar_arquivo(novo_arquivo)

        # carrego o novo arquivo restaurado
        self.musicas_armazenadas = self.carregar_arquivo()
        