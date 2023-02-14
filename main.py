from pytube import YouTube

def on_progress_callback(stream, chunk:bytes, remaining:int):
    sizeDownloaded=stream.filesize - remaining
    print(f"total download  {(sizeDownloaded/stream.filesize*100)} %") 
 


def downloadVideo(url):
    yt = YouTube(url, on_progress_callback=on_progress_callback)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path="./download")
       
downloadVideo(input("enter your url >>> "))
 