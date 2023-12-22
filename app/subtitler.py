from pytube import YouTube
import os, urllib.parse, requests
from flask import send_file

video_path = "video.mp4"

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename=video_path)
    except:
        print("An error has occurred")
    print("Successfully downloaded video")
    
def generate_translated_subs():
    output_dir = "output"
    path = os.path.join(os.getcwd(), output_dir)
    if not os.path.exists(path):
        os.mkdir(path)

    url_data = urllib.parse.urlparse(input("Enter the video url: "))
    query = urllib.parse.parse_qs(url_data.query)
    video_id = query["v"][0]

    Download(f"https://www.youtube.com/watch?v={video_id}")
    
    os.system(f"auto_subtitle {video_path} --task translate")
