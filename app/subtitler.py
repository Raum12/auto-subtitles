from pytube import YouTube
import os, urllib.parse, requests
from flask import send_file

video_path = "upload_folder/output.mp4"

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename=video_path)
    except:
        print("An error has occurred")
    print("Successfully downloaded video")
    
def generate_translated_subs(is_youtube: bool, video_url_or_path: str):
    output_dir = "output"
    path = os.path.join(os.getcwd(), output_dir)
    if not os.path.exists(path):
        os.mkdir(path)
        
    if is_youtube == "F":
        video_path = video_url_or_path
        
        os.rename(video_path, "upload_folder/video.mp4")
        os.system("auto_subtitle upload_folder/output.mp4 --task translate")
    else:
        video_url = video_url_or_path
        url_data = urllib.parse.urlparse(video_url)
        query = urllib.parse.parse_qs(url_data.query)
        video_id = query["v"][0]

        Download(f"https://www.youtube.com/watch?v={video_id}")
    
        os.rename(video_path, "upload_folder/output.mp4")
        os.system("auto_subtitle upload_folder/output.mp4 --task translate")
        # os.rename("video.mp4", "upload_folder/video.mp4")

if __name__ == "__main__":
    generate_translated_subs(input("Youtube (T/F): "), input("Video url/path: "), )