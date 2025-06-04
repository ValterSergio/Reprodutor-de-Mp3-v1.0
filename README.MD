# 🎵 Reprodutor Simples de Músicas

Um reprodutor simples de músicas com uma interface básica e funcionalidade limitada. Ideal para testes e versões iniciais de um projeto de tocador de áudio.

## 📋 Funcionalidades

- Executa músicas em **segundo plano**
- Interface simples e intuitiva
- Suporte aos comandos:
  - ▶️ Play
  - ⏸️ Pause
  - ⏭️ Próxima
  - ⏮️ Anterior
- Exibição de informações da música com um clique
- Reprodução de **uma música por vez**

> ⚠️ Atualmente o usuário deve selecionar uma música da lista. Um clique exibe as informações da faixa; pressionar o botão "Play" em seguida inicia a reprodução em segundo plano.

## 🚧 Melhorias futuras

- Adicionar botão **"Continuar"** na interface (o método `continuar()` já existe no arquivo `controlar_mp3.py`, localizado na pasta `reprodutor`)
- Suporte para playlists ou múltiplas músicas
- Melhorias na interface gráfica
- Feedback visual de controle (ex: música tocando ou pausada)

## 📁 Estrutura do Projeto

projeto/

├── componentes/ # Módulos auxiliares e objetos principais

│ ├── localizador_mp3.py # Localiza arquivos MP3 no sistema

│ ├── musica.py # Classe que representa uma música

│ ├── obter_detalhes.py # Extrai metadados das músicas

│ ├── repositorio_json.py # Gerencia persistência de dados em JSON

│ └── backup.py # Planejado para controle de backup (ainda não implementado)

├── ferramentas/

│ └── pesquisa_binaria.py # Algoritmo para busca eficiente na lista de músicas

├── reprodutor/

│ └── controlar_mp3.py # Controla lógica de reprodução (play, pause, continuar, etc.)

├── view/ # Interface gráfica (GUI)

│ ├── janela_principal.py # Tela principal do aplicativo

│ ├── layout_botoes.py # Layout dos botões de controle

│ ├── layout_horizontal_principal.py # Layout horizontal da interface

│ ├── layout_vertical_principal.py # Layout vertical da interface

│ └── lista_musicas.py # Lista de músicas disponíveis

├── executar_aplicacao.py # Ponto de entrada da aplicação (arquivo principal)

├── requirements.txt # Lista de dependências do projeto

└── README.md # Este arquivo
