Live : https://a4u-youtubedownloder.herokuapp.com/

I have made a simple web app with Streamlit to allow for audio and video downloading. Under the hood, I've used youtube_dl's ancestor, yt_dlp. so I've just converted the video to audio using moviepy.

The video defaults to 1080p and gets the highest resolution if 1080p is not available.

Installation
We recommended to install it and all its dependencies, inside a virtual environnement and through the Python Package Index.

Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

Creating a virtual environment
  virtualenv env
  
Install dependencies
  pip install streamlit
  pip install -r requirements.txt  
Run
  streamlit run streamlit_app.py
