# Auto Subtitle Translater

## Overview
This tool fetches YouTube video captions, translates them into a specified language, and generates a video with the translated subtitles. It's built to work across Windows, macOS, and Linux, but there are some platform-specific issues that you should be aware of.

## Dependencies

[ImageMagick](https://imagemagick.org/) is required. On Windows, it should be added to the system PATH. On macOS and Linux, there might be some issues with font conflicts. Instructions for platform specific setup may be found [here](https://moviepy-tburrows13.readthedocs.io/en/improve-docs/install.html); please follow these to ensure that ImageMagick is correctly detected; the most important step that must be taken for Linux users is the following:

After installing MoviePy on the terminal with `sudo apt install imagemagick`, IMAGEMAGICK will not be detected by moviepy. This bug can be fixed. 
Modify the file in this directory:`/etc/ImageMagick-6/policy.xml`
- Comment out the statement `<!– <policy domain=”path” rights=”none” pattern=”@*” /> –>`.

Once again, I urge you to read through [this](https://moviepy-tburrows13.readthedocs.io/en/improve-docs/install.html) more thoroughly if you are still facing ImageMagick related bugs

### Known Issues on macOS and Linux
1. **Font Conflict:** There might be font conflicts preventing translation into Arabic and other non-Latin character languages. This issue is currently being addressed.2
2. **Translation to Arabic:** There's a bug when fetching Arabic subtitles on macOS and Linux, but translation to Arabic works on Windows.
3. **MoviePy and ImageMagick on Linux:** If you encounter issues with MoviePy not detecting ImageMagick on Linux, try modifying `/etc/ImageMagick-6/policy.xml` by commenting out the line `<!-- <policy domain="path" rights="none" pattern="@*" /> -->`.

## Usage
Enter the `app` directory for the output file to be correctly generated and run `python main.py`

1. Provide the YouTube video URL when prompted.
2. Select the desired source language of the video's captions.
3. Enter the target language for translation.
4. The tool will attempt to fetch and translate the subtitles. 

## Known Limitations
Translating to Arabic or other non-Latin character languages might have issues due to font conflicts on macOS and Linux. In addition, Arabic subtitle fetching might not work on macOS and Linux, but translation to Arabic works on Windows - this is a font related issue.

## Contributions and Bug Reports
Contributions to address platform-specific issues are welcome. For bug reports or assistance, feel free to open an issue in the repository.
