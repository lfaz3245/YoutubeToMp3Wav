import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
import yt_dlp

# Função para normalizar links
def normalizar_link(url: str) -> str:
    url = url.strip()
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    if "youtube.com/watch?v=" in url:
        return url.split("&")[0]
    return url

# Função principal para baixar vários links
def baixar_varios():
    links = text_links.get("1.0", "end").strip().splitlines()
    formato = formato_var.get()
    pasta_destino = pasta_var.get()
    qualidade_mp3 = qualidade_mp3_var.get()
    qualidade_wav = qualidade_wav_var.get()

    total = len(links)
    if total == 0:
        messagebox.showwarning("Aviso", "Cole pelo menos um link.")
        return

    progress_bar.set(0)
    root.update_idletasks()

    for i, link in enumerate(links, start=1):
        url = normalizar_link(link.strip())
        if not url:
            continue
        try:
            # Configurações do yt-dlp
            if formato == "MP3":
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': qualidade_mp3.replace("k", ""),
                    }],
                }
            else:  # WAV
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'wav',
                        'preferredquality': '0',  # WAV não usa bitrate, mas sample rate
                    }],
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            messagebox.showinfo("Sucesso", f"[{i}/{total}] Download concluído para:\n{url}")
        except Exception as e:
            messagebox.showerror("Erro no download", f"[{i}/{total}] Não foi possível baixar {url}\n{e}")

        # Atualiza barra de progresso
        progress_bar.set(i / total)
        root.update_idletasks()

# Função para escolher pasta
def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_var.set(pasta)

# Interface CustomTkinter com Scroll
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("YouTube to MP3/WAV Downloader")

scroll_frame = ctk.CTkScrollableFrame(root, width=600, height=500)
scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(scroll_frame, text="Cole vários links do YouTube (um por linha):").pack(pady=5)
text_links = ctk.CTkTextbox(scroll_frame, width=500, height=150)
text_links.pack(pady=5)

ctk.CTkLabel(scroll_frame, text="Pasta de destino:").pack(pady=5)
pasta_var = ctk.StringVar(value=os.getcwd())
ctk.CTkEntry(scroll_frame, textvariable=pasta_var, width=300).pack(pady=5)
ctk.CTkButton(scroll_frame, text="Escolher pasta", command=escolher_pasta).pack(pady=5)

ctk.CTkLabel(scroll_frame, text="Formato:").pack(pady=5)
formato_var = ctk.StringVar(value="MP3")
ctk.CTkOptionMenu(scroll_frame, variable=formato_var, values=["MP3", "WAV"]).pack(pady=5)

ctk.CTkLabel(scroll_frame, text="Qualidade MP3 (bitrate):").pack(pady=5)
qualidade_mp3_var = ctk.StringVar(value="192k")
ctk.CTkOptionMenu(scroll_frame, variable=qualidade_mp3_var, values=["128k", "192k", "256k", "320k"]).pack(pady=5)

ctk.CTkLabel(scroll_frame, text="Qualidade WAV (sample rate):").pack(pady=5)
qualidade_wav_var = ctk.StringVar(value="44100")
ctk.CTkOptionMenu(scroll_frame, variable=qualidade_wav_var, values=["22050", "44100", "48000"]).pack(pady=5)

progress_bar = ctk.CTkProgressBar(scroll_frame, width=400)
progress_bar.pack(pady=10)
progress_bar.set(0)

ctk.CTkButton(scroll_frame, text="Baixar todos os links", command=baixar_varios).pack(pady=20)

root.mainloop()