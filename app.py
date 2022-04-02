
import streamlit as st
import numpy as np
import speech_recognition as sr
from googletrans import Translator
from helper import draw_embed, create_spectrogram, read_audio, record, save_record

# Add Streamlit dropdown menu to select audio file and record audio
st.header(" Record your own voice/select an audio file")
choice =  st.selectbox("Select an option", ["Record", "Choose an audio file"])

def recognize_audio(path_audio):
# use Assempbly.ai to get the embedding for speech to text
    r = sr.Recognizer()
    with sr.AudioFile(path_audio) as source:
        audio = r.record(source)
        st.text("Recognizing...")
        try:
            text = r.recognize_google(audio)
            
        except:
            text="Could not recognize your voice"
    return text

def record_audio():
    filename = st.text_input("Choose a filename: ")
    if st.button(f"Click to Record"):
        if filename == "":
            st.warning("Choose a filename.")
        else:
            record_state = st.text("Recording...")
            duration = 5  # seconds
            fs = 48000
            myrecording = record(duration, fs)
            record_state.text(f"Saving sample as {filename}.mp3")

            path_audio = f"./samples/{filename}.mp3"

            save_record(path_audio, myrecording, fs)
            record_state.text(f"Done! Saved sample as {filename}.mp3")

            st.audio(read_audio(path_audio))

            fig = create_spectrogram(path_audio)
            st.pyplot(fig)
            return recognize_audio(path_audio)

                

def choose_audio():
    
    audio_file = st.file_uploader("Choose an audio file", type=[".wav", ".wave", ".flac", ".mp3", ".ogg"])
    if audio_file is not None:
        #get the filename
        filename = audio_file.name
        print(filename)
        path_audio = f"./samples/{filename}"
        #save the file
        with open(path_audio, 'wb') as f:
            f.write(audio_file.read())
        st.audio(read_audio(path_audio))
        fig = create_spectrogram(path_audio)
        st.pyplot(fig)
        return recognize_audio(path_audio)
        
if choice == "Record":
    text = record_audio()
    
elif choice == "Choose an audio file":
    text = choose_audio()

def translate_text(text):
    try:
        lang_list={
            "English": "en",
            "Hindi": "hi",
            "Telugu": "te",
            "Tamil": "ta",
            "Malayalam": "ml",
            "Kannada": "kn",
            "Spanish": "es",
            "French": "fr",
            "Chinese": "zh",
            "Japanese": "ja",
            "Korean": "ko",
            "Portuguese": "pt",
            "Russian": "ru",
            "German": "de",
            "Italian": "it",
            "Arabic": "ar",
            "Turkish": "tr",
            "Vietnamese": "vi"
        }
        translate=Translator()
        lan = lang_list[language]
        return translate.translate(text, dest=lan).text
    except Exception as e:
        return " "


language = st.selectbox("Select an option", ["English","Hindi","Telugu","Tamil","Malayalam","Kannada", "Spanish", "French", "Chinese", "Japanese", "Korean", "Portuguese", "Russian", "German", "Italian", "Arabic", "Turkish", "Vietnamese"], index=0)
st.text(translate_text(text))
