
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=mIOOHbnZMG8")
stream = yt.streams.filter(only_audio=True).first()
stream.download()
