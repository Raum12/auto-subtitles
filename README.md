# Auto Subtitle Translater
Allows subtitle addition or translation of captions to or on a youtube video or any video file. To input video files scroll to the `Video Files` section; otherwise, go down to the `Youtube Videos` section.

-----
## Video Files
Takes any video file as input and generates subtitles of any language ontop of this video. 

Navigate to the `subtitle_generator` directory.

-----
## Youtube Videos
This will fetch a YouTube video's captions, translate them into a specified language, and generate a video with the translated subtitles. It is built to work across Windows, macOS, and Linux, but there are some platform-specific issues that you should be aware of.

Navigate to the `youtube` directory.

### Dependencies

[ImageMagick](https://imagemagick.org/) is required. On Windows, it should be added to the system PATH. This is not necessary on macOS or Linux. Instructions for platform specific setup may be found [here](https://moviepy-tburrows13.readthedocs.io/en/improve-docs/install.html); please follow these to ensure that ImageMagick is correctly detected. 

The most important step that must be taken for Linux users is the following:

After installing MoviePy on the terminal with `sudo apt install imagemagick`, IMAGEMAGICK will not be detected by moviepy. This bug can be fixed. 
Modify the file in this directory:`/etc/ImageMagick-6/policy.xml`
- Comment out the statement `<!– <policy domain=”path” rights=”none” pattern=”@*” /> –>`.

Once again, I urge you to read through [this](https://moviepy-tburrows13.readthedocs.io/en/improve-docs/install.html) more thoroughly if you are still facing ImageMagick related bugs.

### Known Issues on macOS and Linux
1. **Font Conflict:** There may be font conflicts preventing translation into Arabic and other non-Latin character languages on macOS and Linux; conversely, this seems to work well on windows. This issue is currently being addressed.
2. **MoviePy and ImageMagick on Linux:** If you encounter issues with MoviePy not detecting ImageMagick on Linux, try modifying `/etc/ImageMagick-6/policy.xml` by commenting out the line `<!-- <policy domain="path" rights="none" pattern="@*" /> -->`.
3. **Translating videos from languages such as arabic:** I have found trouble fetching transcripts for videos that are in arabic; this does not apply for many other languages-please email me with specific language updates.

## Usage
Enter the `app` directory for the output file to be correctly generated and run `python main.py`

1. Provide the YouTube video URL when prompted.
2. Select the desired source language of the video's captions.
3. Enter the target language for translation.
4. The tool will attempt to fetch and translate the subtitles. 

## Known Limitations
Translating to Arabic or other non-Latin character languages might have issues due to font conflicts on macOS and Linux. In addition, Arabic subtitle fetching might not work on macOS and Linux, but translation to Arabic works on Windows - I believe this is a font related issue.

## Contributions and Bug Reports
Contributions to address platform-specific issues are welcome. For bug reports or assistance, feel free to open an issue in the repository or email me [here](mailto:shibani.raum@gmail.com?subject=[GitHub])
