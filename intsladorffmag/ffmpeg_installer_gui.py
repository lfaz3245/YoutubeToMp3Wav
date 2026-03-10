import customtkinter as ctk
import subprocess
import urllib.request
import zipfile
import os
import shutil
import threading

URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

ZIP_FILE = "ffmpeg.zip"
TEMP_DIR = "temp_ffmpeg"
INSTALL_DIR = "C:\\ffmpeg"


def ffmpeg_installed():
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except:
        return False


class Installer(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("FFmpeg Installer")
        self.geometry("500x380")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title_label = ctk.CTkLabel(
            self,
            text="FFmpeg Installer",
            font=("Segoe UI", 24)
        )
        self.title_label.pack(pady=20)

        self.install_button = ctk.CTkButton(
            self,
            text="Instalar FFmpeg",
            command=self.start_install
        )
        self.install_button.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self, width=350)
        self.progress.set(0)
        self.progress.pack(pady=10)

        self.log = ctk.CTkTextbox(self, width=420, height=200)
        self.log.pack(pady=10)

        if ffmpeg_installed():
            self.write_log("FFmpeg já está instalado.")

    def write_log(self, text):

        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.update()

    def download(self):

        self.write_log("Baixando FFmpeg...")

        def progress(blocks, block_size, total_size):

            downloaded = blocks * block_size
            percent = downloaded / total_size

            self.progress.set(percent)

        urllib.request.urlretrieve(
            URL,
            ZIP_FILE,
            progress
        )

        self.write_log("Download concluído")

    def extract(self):

        self.write_log("Extraindo arquivos...")

        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(TEMP_DIR)

        folder = os.listdir(TEMP_DIR)[0]

        source = os.path.join(TEMP_DIR, folder)

        if os.path.exists(INSTALL_DIR):
            shutil.rmtree(INSTALL_DIR)

        shutil.move(source, INSTALL_DIR)

        shutil.rmtree(TEMP_DIR)
        os.remove(ZIP_FILE)

        self.write_log("Extração concluída")

    def add_path(self):

        self.write_log("Adicionando ao PATH...")

        ffmpeg_bin = os.path.join(INSTALL_DIR, "bin")

        subprocess.run(
            f'setx PATH "%PATH%;{ffmpeg_bin}"',
            shell=True
        )

        self.write_log("PATH atualizado")

    def install(self):

        try:

            if ffmpeg_installed():
                self.write_log("FFmpeg já detectado no sistema.")
                return

            self.download()
            self.extract()
            self.add_path()

            self.progress.set(1)

            self.write_log("Instalação finalizada.")

        except Exception as e:

            self.write_log("Erro: " + str(e))

    def start_install(self):

        self.install_button.configure(state="disabled")

        thread = threading.Thread(target=self.install)

        thread.start()


app = Installer()

app.mainloop()