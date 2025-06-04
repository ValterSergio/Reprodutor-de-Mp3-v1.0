import os
from math import floor # duração garantir o ultimo inteiro
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

def extrair_informacoes_mp3(caminho: str) -> dict:
    try:
        audio = MP3(caminho, ID3=ID3)

        # Metadados
        titulo = audio["TIT2"].text[0] if "TIT2" in audio else "Desconhecido"
        artista = audio["TPE1"].text[0] if "TPE1" in audio else "Desconhecido"
        genero = audio["TCON"].text[0] if "TCON" in audio else "Desconhecido"

        # Duração
        duracao = audio.info.length  # em segundos

        # Formato
        _, extensao = os.path.splitext(caminho)
        formato = extensao.lower()

        # Tamanho do arquivo
        tamanho_bytes = os.path.getsize(caminho)
        tamanho_mb = tamanho_bytes / (1024 * 1024)

        return {
            "titulo": titulo,
            "artista": artista,
            "genero": genero,
            "duracao": floor(duracao),
            "tamanho_mb": round(tamanho_mb, 2),
            "formato": formato,
            "caminho": caminho
        }

    except Exception as e:
        return {"erro": str(e)}

    