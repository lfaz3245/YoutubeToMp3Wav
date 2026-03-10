🎵 YouTube to MP3/WAV Downloader
Um aplicativo em Python com interface gráfica moderna (via CustomTkinter) que permite baixar e converter vídeos do YouTube em MP3 ou WAV, com suporte a múltiplos links, barra de progresso, normalização automática de URLs e conversão confiável via yt-dlp + FFmpeg.

🚀 Funcionalidades
- Download de áudio do YouTube em MP3 ou WAV.
- Fila de downloads: cole vários links de uma vez e o programa baixa todos em sequência.
- Barra de progresso mostrando quantos arquivos já foram processados.
- Normalização de links: aceita tanto youtube.com/watch?v=... quanto youtu.be/... com parâmetros extras.
- Interface moderna com CustomTkinter e suporte a scrollbar.
- Conversão de áudio com qualidade configurável (bitrate para MP3, sample rate para WAV).
- Compatibilidade com Windows: pode ser transformado em executável .exe para rodar em qualquer computador.

🛠️ Tecnologias utilizadas
- Python 3.13 – linguagem principal.
- CustomTkinter – biblioteca para criar interfaces gráficas modernas e responsivas.
- yt-dlp – ferramenta robusta para download de vídeos/áudios do YouTube (substitui o pytube, que está instável).
- FFmpeg – software externo necessário para conversão de áudio (MP3/WAV).
- MoviePy (opcional) – usado em versões anteriores para manipulação de áudio, mas com yt-dlp + FFmpeg a conversão é mais estável.
- PyInstaller – usado para transformar o programa em executável .exe.

📦 Instalação
- Clone ou baixe o projeto:
git clone https://github.com/lfaz3245/YoutubeToMp3Wav.git
cd YoutubeToMp3Wav
- Instale as dependências Python:
pip install -r requirements.txt
- Instale o FFmpeg (obrigatório para conversão):
- Baixe em: ffmpeg.org/download (ffmpeg.org in Bing)
- Extraia em C:\ffmpeg\bin (Windows).
- Adicione C:\ffmpeg\bin ao PATH do sistema.
- Teste no terminal:
ffmpeg -version
ffprobe -version



🖥️ Como usar
- Execute o programa:
python YoutubeToMp3Wav.py
- Cole os links do YouTube (um por linha) no campo de texto.
- Exemplo válido:
https://www.youtube.com/watch?v=4C4EB12_PjQ
https://youtu.be/4C4EB12_PjQ?si=R2629gTYd54UfMgf
- Escolha a pasta de destino para salvar os arquivos.
- Selecione o formato (MP3 ou WAV).
- Configure a qualidade:
- MP3: bitrate (128k, 192k, 256k, 320k).
- WAV: sample rate (22050, 44100, 48000).
- Clique em “Baixar todos os links”.
- A barra de progresso mostrará o andamento.
- Mensagens de sucesso/erro aparecerão para cada vídeo.

⚠️ Problemas comuns
- Erro HTTP 400: acontece com pytube. Solução: usar yt-dlp.
- Erro “ffprobe and ffmpeg not found”: significa que o FFmpeg não está instalado ou não está no PATH.
- Links inválidos: Shorts e Playlists não são suportados. Use apenas links de vídeos normais.

📚 Estrutura do projeto
YoutubeToMp3Wav/
│
├── YoutubeToMp3Wav.py   # Código principal com interface e lógica
├── README.md            # Documentação do projeto
├── requirements.txt     # Dependências Python
└── dist/                # Executável gerado pelo PyInstaller



🔧 Gerar Executável Windows
Para transformar em .exe:
pyinstaller --onefile --noconsole YoutubeToMp3Wav.py


O executável ficará na pasta dist/.
Se quiser incluir ícone:
pyinstaller --onefile --noconsole --icon=icone.ico YoutubeToMp3Wav.py



✨ Diferenciais
- Interface moderna e intuitiva.
- Suporte a múltiplos links com fila de downloads.
- Barra de progresso integrada.
- Normalização automática de links encurtados ou com parâmetros.
- Conversão confiável via FFmpeg.
- Pode ser distribuído como .exe para qualquer computador Windows.
