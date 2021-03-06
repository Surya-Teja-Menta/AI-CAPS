# Real-Time Voice recognising

This repository demonstrates how a voice recognition app can be created using [Streamlit](https://www.streamlit.io/). The code for this demo is based on the repository for [Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning).

This app allows you to:
* Record your voice
* Visualize the embedding of the speaker
* Synthesize speech based on the recorded voice


## Setup

### 1. Install Requirements
**Python 3.6 or 3.7** is needed

* Create your virtual environment (e.g. [pipenv](https://pipenv.pypa.io/en/latest/), [poetry](https://python-poetry.org/) or [venv](https://docs.python.org/3/library/venv.html)).
* Install [PyTorch](https://pytorch.org/get-started/locally/) (>=1.0.1).
* Install [ffmpeg](https://ffmpeg.org/download.html#get-packages).
* Run `pip install -r requirements.txt` to install the remaining necessary packages.



### 3. Launch streamlit demo

* `streamlit run speech.py`

## Usage
---
- go to the browser and choose between the following options: "Record Audio", "Choose audio". Lets say we choose "Choose audio".</br>
<img src="images/1.png" width=550>
 
- As you can see it loads the audio and the embedding of the speaker and also draw the charts</br>

- You can also choose the translation language.</br>
<img src="images/2.png" width=550>

---

Happy Coding!


