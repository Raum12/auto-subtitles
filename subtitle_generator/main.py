from moviepy.editor import *
from typing import Sequence, Optional
from srt_file_translator import Translator
import pvleopard, pysrt, burn_subtitles

def second_to_timecode(x: float) -> str:
    hour, x = divmod(x, 3600)
    minute, x = divmod(x, 60)
    second, x = divmod(x, 1)
    millisecond = int(x * 1000.)


    return "%.2d:%.2d:%.2d,%.3d" % (hour, minute, second, millisecond)


def to_srt(
        words: Sequence[pvleopard.Leopard.Word],
        endpoint_sec: float = 1.,
        length_limit: Optional[int] = 16) -> str:
    def _helper(end: int) -> None:
        lines.append("%d" % section)
        lines.append(
            "%s --> %s" %
            (
                second_to_timecode(words[start].start_sec),
                second_to_timecode(words[end].end_sec)
            )
        )
        lines.append(" ".join(x.word for x in words[start:(end + 1)]))
        lines.append("")


    lines = list()
    section = 0
    start = 0
    for k in range(1, len(words)):
        if ((words[k].start_sec - words[k - 1].end_sec) >= endpoint_sec) or \
                (length_limit is not None and (k - start) >= length_limit):
            _helper(k - 1)
            start = k
            section += 1
    _helper(len(words) - 1)


    return "\n".join(lines)

def main():
    access_key = "3SMe31Rwmg8A3LQarx86XCzH28k2bOdoCys/X16HkfwxfFCScppgHg=="
    leopard = pvleopard.create(access_key=access_key)

    language = input("Enter output language code: ")
    video_file = "input.mp4"
    output_video_file = "output.mp4"
    audio_file = "audio.wav" 
    srt_filename = "subtitles.srt"

    video = VideoFileClip(video_file)

    audio = video.audio 
    audio.write_audiofile(audio_file)

    transcript, words = leopard.process_file(audio_file)

    with open(srt_filename, "w") as f:
        f.write(to_srt(words))

    subtitles = pysrt.open(srt_filename)

    print("Burning subtitles into video...")
    subtitle_clips = burn_subtitles.create_subtitle_clips(subtitles=subtitles, videosize=video.size)
    print("Successfully burned subtitles into video")

    final_video = CompositeVideoClip([video] + subtitle_clips)
    
    print("Writing output file...")
    final_video.write_videofile(output_video_file)
    print("Successfully wrote output file")

if __name__ == "__main__":
    main()