from moviepy.editor import TextClip

fonts = TextClip.list("font")

for i, font in enumerate(fonts): print(f"{i}. {font}\n")
# if "Noto-Sans-Arabic" in fonts:
#     print("Match")
# else:
#     print("No match")