import os
from componentes.musica import Musica
from componentes.obter_detalhes_mp3 import extrair_informacoes_mp3

def validar_pastas(pasta):
    nomes_proibidos = [
        ".vscode", "app", "windows", "virtualbox", "netbeans", "oracle",
        "appdata", "program files", "__pycache__", "local", "packages",
        ".gradle", "caches", ".m2", ".cache"
    ]
    pasta = pasta.lower().replace("\\", " ")
    return not any(nome in pasta for nome in nomes_proibidos)

class LocalizarMp3:
    def __init__(self):
        self.raiz = os.environ["USERPROFILE"]
        self.musicas_encontradas = []
    
    def filtrar_arquivos(self):
        pastas_encontrados = []
        for pasta_atual, subpastas, arquivos in os.walk(self.raiz):
            passei_aqui = pasta_atual in pastas_encontrados
            if not validar_pastas(pasta_atual) or passei_aqui:
                continue

            # Evita entrar em subpastas proibidas
            for subpasta in subpastas:
                if not validar_pastas(subpasta):
                    pastas_encontrados.append(subpasta)
                    continue


            for arquivo in arquivos:
                nome, extensao = os.path.splitext(arquivo)
                if extensao.lower() != ".mp3":
                    continue

                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                # obter os dados da musicas
                dados = extrair_informacoes_mp3(caminho_arquivo)
                if dados["duracao"] <= 30 or dados["duracao"] >= 660: continue # menor que 30 segundos
                dados["nome"] = nome
        

                # criar a musica
                musica = Musica(**dados)
                self.musicas_encontradas.append(musica)
        print("Musicas encontradas")
        return self.musicas_encontradas

if __name__ == "__main__":
    localizar = LocalizarMp3().filtrar_arquivos()
    print(f"{len(localizar)} músicas encontradas.")
