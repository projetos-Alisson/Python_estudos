from pytubefix import YouTube
from pytubefix.cli import on_progress #Monitorar progresso do download

url =  input("Qual a URL do video que deseja baixar?")

destiny = "videosYoutube"

yt = YouTube(url, on_progress_callback= on_progress)
print(yt.title)

#To get the better resolution of youtube
ys = yt.streams.get_highest_resolution()

ys.download(output_path=destiny)