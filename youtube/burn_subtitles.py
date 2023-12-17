# source: https://github.com/ramsrigouthamg/Supertranslate.ai/tree/main/Burn_Subtitles_Into_Video

import sys
from moviepy.editor import *

def time_to_seconds(time_obj):
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000

def create_subtitle_clips(subtitles, videosize, language, fontsize=20, color="white", debug=False):
    subtitle_clips = []
    font = "Arial"

    for subtitle in subtitles:

        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize

        text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color, bg_color="black", size=(video_width*3/4, None), method="caption").set_start(start_time).set_duration(duration)

        subtitle_x_position = "center"
        subtitle_y_position = video_height* 4 / 5

        text_position = (subtitle_x_position, subtitle_y_position)
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips