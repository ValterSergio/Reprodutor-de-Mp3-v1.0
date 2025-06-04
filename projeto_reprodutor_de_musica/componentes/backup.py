from pathlib import Path
from datetime import datetime
import json
import os

# Função utilitária para obter a data atual no formato "dd - mm - aaaa"
def obter_data():
    return datetime.now().date().strftime("%d - %m - %Y")

# Função utilitária para obter a hora atual no formato "hh - mm - ss"
def obter_hora():
    return datetime.now().strftime("%H - %M - %S")

# Diretório onde os arquivos de backup serão armazenados.
# A pasta "backup" é criada na raiz do projeto (um nível acima do script atual)
CAMINHO_BACKUP = os.path.join(Path(__file__).parent.parent, "backup")

class Backup:
    def __init__(self, caminho: str):
        # Caminho do arquivo original que será usado como fonte para os backups
        self.caminho = caminho

        # Lista que armazena os metadados dos backups criados
        self.lista_de_registros = []

        # Marcador usado como identificador único para os arquivos de backup
        self.marcar_registro = 0

    def adicionar_backup(self):
        """
        Realiza o processo de backup:
        - Carrega os dados do arquivo original
        - Cria um novo arquivo de backup
        - Registra os metadados do backup
        - Mantém no máximo 20 backups, excluindo o mais antigo
        """

        # Incrementa o identificador do backup atual
        self.marcar_registro += 1

        # Se o limite de 20 backups for atingido, remove o backup mais antigo (último da lista)
        if self.marcar_registro >= 20:
            self.lista_de_registros.pop()

        # Define o caminho completo do novo arquivo de backup
        CAMINHO_ARQUIVO = os.path.join(Path(CAMINHO_BACKUP, f"{self.marcar_registro}Backup.json"))

        # Garante que a pasta de backup exista
        os.makedirs(CAMINHO_BACKUP, exist_ok=True)

        # Carrega os dados do arquivo original
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if not conteudo.strip():
                raise ValueError(f"O arquivo '{self.caminho}' está vazio. Backup cancelado.")
            dados = json.loads(conteudo)

        # Define o caminho completo do novo arquivo de backup
        CAMINHO_ARQUIVO = os.path.join(Path(CAMINHO_BACKUP, f"{self.marcar_registro}Backup.json"))

        # Salva os dados carregados em um novo arquivo de backup
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)

            # Cria um registro com metadados sobre o backup realizado
            registro = {
                "Data": obter_data(),
                "Hora": obter_hora(),
                "Id": self.marcar_registro,
                "caminho": CAMINHO_ARQUIVO        
            }

            # Insere o novo registro no início da lista (o mais recente sempre vem primeiro)
            self.lista_de_registros.insert(0, registro)

    def recuperar_ultimo_backup(self):
        """
        Retorna o caminho do backup mais recente.
        """
        return self.lista_de_registros[0]['caminho']
