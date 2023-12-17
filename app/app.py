# import os
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import SRTFormatter
# from translate import Translator # Use translator library instead
# import moviepy.editor as mp
# from pytube import YouTube

# # Get video ID
# video_id = input("Enter YouTube Video ID: ")  

# # Get language to translate to
# language = input("Enter language to translate to (e.g. 'es', 'de'): ")

# # Download video 
# yt = YouTube(f"https://youtu.be/{video_id}")
# video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# video.download()

# # Get subtitles
# transcript = YouTubeTranscriptApi.get_transcript(video_id)

# # Translate subtitles 
# translator = Translator(from_lang="en", to_lang=language)
# translated = []

# for line in transcript:
#     translated.append(translator.translate(line['text']))

# # Generate SRT
# formatter = SRTFormatter()
# translated_srt = formatter.format_transcript(translated)

# # Add subtitles to video
# final_video = mp.CompositeVideoClip([mp.VideoFileClip(video.default_filename),  
#                                       mp.TextClip(translated_srt, fontsize=24, color='white', stroke_color='black', stroke_width=1, font='Arial', method='caption')])
# final_video.write_videofile(f"{video.title}_{language}.mp4", remove_temp=True)

# # Delete original video
# os.remove(video.default_filename) 

# print("Video downloaded and subtitled file generated")