from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from moviepy.editor import VideoFileClip, CompositeVideoClip
from pytube import YouTube
import pysrt, burn_subtitles

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename="no_subtitles.mp4")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


def main():
    video_id = "rc0mws9NT-0"
    formatter = SRTFormatter()

    Download(f"https://www.youtube.com/watch?v={video_id}")

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    srt_formatted = formatter.format_transcript(transcript)

    with open("subtitles.srt", "w") as file:
        file.write(srt_formatted)

    mp4_filename = "no_subtitles.mp4"
    srt_filename = "subtitles.srt"

    video = VideoFileClip(mp4_filename)
    subtitles = pysrt.open(srt_filename)

    begin, end = mp4_filename.split("mp4")
    output_video_file = f"{begin}_subtitled.mp4"

    print(f"Output file name: {output_video_file}")

    subtitle_clips = burn_subtitles.create_subtitle_clips(subtitles, video.size)
    final_video = CompositeVideoClip([video] + subtitle_clips)

    final_video.write_videofile(output_video_file)


if __name__ == "__main__":
    main()
