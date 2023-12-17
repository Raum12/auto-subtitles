# Auto Subtitle Translater
Fetches a youtube videos captions, translates them into a given langauge and generates a video with these new subtititles

Dependencies: 
- You must install ImageMagick [here](https://imagemagick.org/script/download.php)
If using MacOS or Linux add ImageMagick to your path.
WARNING: current code only supports windows, I am currently working on addressing bugs on mac os and linux

You must run main.py in the app directory, otherwise the output directory will not be detected

More instructions [here](https://pypi.org/project/moviepy/)

### On Linux: 
After installing MoviePy on the terminal with `sudo apt install imagemagick`, IMAGEMAGICK will not be detected by moviepy. This bug can be fixed. 
Modify the file in this directory:`/etc/ImageMagick-6/policy.xml`
- Comment out the statement <!– <policy domain=”path” rights=”none” pattern=”@*” /> –>.
