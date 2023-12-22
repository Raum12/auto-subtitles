# Auto Subtitle Translater
Allows subtitle addition or translation of captions to or on a youtube video or any video file. To input video files scroll to the `Video Files` section; otherwise, go down to the `Youtube Videos` section.

-----
## Video Files
Takes any video file as input and generates subtitles of any language ontop of this video. 

Navigate to the `subtitle_generator` directory.

-----
## Youtube Videos
This will fetch a YouTube video's captions, translate them into a specified language, and generate a video with the translated subtitles.

Navigate to the `youtube` directory.

### Dependencies

[ImageMagick](https://imagemagick.org/) is required. On Windows, it should be added to the system PATH. This is not necessary on macOS or Linux. Instructions for platform specific setup may be found [here](https://moviepy-tburrows13.readthedocs.io/en/improve-docs/install.html); please follow these to ensure that ImageMagick is correctly detected. 

The most important step that must be taken for Linux users is the following:

After installing MoviePy on the terminal with `sudo apt install imagemagick`, IMAGEMAGICK will not be detected by moviepy. This bug can be fixed. 
Modify the file in this directory:`/etc/ImageMagick-6/policy.xml`

Comment out the statement `<!– <policy domain=”path” rights=”none” pattern=”@*” /> –>`.

Once again, I urge you to read through [this](https://moviepy-tburrows13.readthedocs.io/en/improve-docs/install.html) more thoroughly if you are still facing ImageMagick related bugs.

## Usage
Enter the `app` directory for the output file to be correctly generated and run `python main.py`

1. Provide the YouTube video URL when prompted.
2. Select the desired source language of the video's captions.
3. Enter the target language for translation.
4. The tool will attempt to fetch and translate the subtitles.

## Contributions and Bug Reports
Contributions to address platform-specific issues are welcome. For bug reports or assistance, feel free to open an issue in the repository or email me [here](mailto:shibani.raum@gmail.com?subject=[GitHub])
