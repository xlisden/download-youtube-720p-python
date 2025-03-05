from pytubefix import YouTube

def download_video(url):
    yt = YouTube(url)
    try:
        video = yt.streams.filter(file_extension='mp4').order_by("resolution").desc().first()
        folder = "download_videos"
        video.download(folder)
        print("compleated!")
    except Exception as e:
        print(f"Download failed: {e}")

url = input("Enter the URL of the video: ")
video = download_video(url)
         

