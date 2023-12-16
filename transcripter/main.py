from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
import moviepy.editor as mp
from pytube import YouTube
import os

# the video id 
video_id = "rc0mws9NT-0"
formatter = SRTFormatter()

transcript = YouTubeTranscriptApi.get_transcript(video_id)
srt_formatted = formatter.format_transcript(transcript)
print(srt_formatted)


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

Download("https://www.youtube.com/watch?v=rc0mws9NT-0")


video = mp.VideoFileClip("video.mp4")
subtitles = mp.SubtitlesClip("subtitles.srt", video.size) 

final_video = mp.CompositeVideoClip([video, subtitles])
final_video.write_videofile("output.mp4")

