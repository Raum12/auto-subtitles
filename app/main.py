from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from moviepy.editor import VideoFileClip, CompositeVideoClip
from pytube import YouTube
import pysrt, burn_subtitles, os

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename="output/no_subtitles.mp4")
    except:
        print("An error has occurred")
    print("Successfully downloaded video")


def main():
    output_dir = "output"
    path = os.path.join(os.getcwd(), output_dir)
    if not os.path.exists(path):
        os.mkdir(path)

    video_id = input("Enter the video ID: ")
    language = input("Enter language to translate to (e.g. 'ar', 'de'): ")
    formatter = SRTFormatter()

    Download(f"https://www.youtube.com/watch?v={video_id}")

    # transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['en'])

    translated_transcript = transcript.translate(language)
    srt_formatted = formatter.format_transcript(translated_transcript.fetch())

    print("Writing SRT file...")
    with open("output/subtitles.srt", "w", encoding="utf-8") as file:
        file.write(srt_formatted)
    print("Successfully wrote SRT file")

    mp4_filename = "output/no_subtitles.mp4"
    srt_filename = "output/subtitles.srt"

    video = VideoFileClip(mp4_filename)
    subtitles = pysrt.open(srt_filename)

    output_video_file = "output/subtitled.mp4"

    print("Burning subtitles into video...")
    subtitle_clips = burn_subtitles.create_subtitle_clips(subtitles=subtitles, videosize=video.size, language=language)
    print("Successfully burned subtitles into video")

    final_video = CompositeVideoClip([video] + subtitle_clips)

    print("Writing output file...")
    final_video.write_videofile(output_video_file)
    print("Successfully wrote output file")


if __name__ == "__main__":
    main()
