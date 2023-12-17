import os, platform

if platform.system() == "Windows":
    IMAGEMAGICK_BINARY = os.getenv("IMAGEMAGICK_BINARY", "C:\Program Files\ImageMagick-7.0.8-Q16\convert.exe")

elif platform.system() == "Darwin":
    IMAGEMAGICK_BINARY = os.getenv("IMAGEMAGICK_BINARY", "/usr/local/bin/magick") 

elif platform.system() == "Linux":
    IMAGEMAGICK_BINARY = os.environ.get("IMAGEMAGICK_BINARY", "/usr/bin/convert")
