## Youtube subtitler

This flask app will take a youtube video's url as input and generate english subtitles for the video whether it be in english or any other language. Then it burns the subtitles to an mp4 video file and outputs the original video with the new subtitles.

## Usage

1. Create a virtual env

```
python -m venv .venv
```

2. Activate the environment 

```
source .venv/bin/activate
```

3. Install python dependencies to virtual env

```
pip install -r requirements.txt
```

4. Enter the `app` directory and run the flask app

```
cd app && python app.py
```


5. Access the App and Submit the YouTube Video URL:

- Copy the provided link and paste it into a web browser.
- The app interface should load in the browser.
- Enter the URL of the YouTube video you want to process into the rendered form and submit.

**Note on proccessing time:**
The time it takes for the video to be processed depends on its size and length. Larger videos may take longer to process.

You can monitor the progress of the processing in the terminal where the Flask app is running. It will display logs indicating the status of the process.


### Sources:
Speech proccessing model and translator: [github.com/m1guelpf/auto-subtitle](https://github.com/m1guelpf/auto-subtitle)
