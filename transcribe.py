import whisper
import streamlit as st
# import pickle

st.title("Transcript app")

# model=pickle.load(open('transcribe.pkl','rb'))
# upload audio file
audio_file=st.file_uploader("Upload audio",type=["wav","mp3","m4a","mp4"])
model=whisper.load_model("base")
st.text("whisper model loaded")
if st.sidebar.button("Transcribe audio"):
    if audio_file is not None:
        st.sidebar.success("transcribing audio")
        st.text(audio_file.name)
        transcription=model.transcribe(audio_file.name)
        st.sidebar.success("Transcription completed")
        st.markdown(transcription["text"])
    
    else:
        st.sidebar.error("please upload file")
# @st.cache
# def load_whisper_model():
#     model=whisper.load_model("base")
#     return model

# if st.sidebar.button("Load Whisper Model"):
#     # model=load_whisper_model()
#     st.sidebar.success("Whisper model loaded") 

# if st.sidebar.button("Transcribe audio"):
#     st.sidebar.success("transcribing audio")
#     transcription=model.transcribe(audio_file)