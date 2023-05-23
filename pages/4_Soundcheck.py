import streamlit as st
#import os
#from io import BytesIO
#import pydub as AudioSegment
import numpy as np
import streamlit.components.v1 as components
#from scipy.io.wavfile import write
import pickle
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import wave
with st.sidebar:
    st.sidebar.markdown("<h1> Musical Instrument Recognition </h1>",unsafe_allow_html=True)
    st.sidebar.markdown("## Priyadharshini Prabhakar")
    st.sidebar.markdown("##### priyaprabhaker@gmail.com")

st.markdown("## Play any solo instrument audio and record")
audio_bytes= audio_recorder(energy_threshold=(-1.0, 1.0),pause_threshold=3.0,)
if audio_bytes is None:
    st.write("### I did not receive any recording. Please! Do it again")
if audio_bytes is not None:
    st.write("### Got it!")
    st.audio(audio_bytes, format="audio/wav",)
    with wave.open('audio.wav', 'wb') as audio_file:
        audio_file.setnchannels(2)  # Set number of channels (1 for mono, 2 for stereo)
        audio_file.setsampwidth(2)  # Set sample width (in bytes)
        audio_file.setframerate(44100)  # Set sample rate (in Hz)
        audio_file.writeframesraw(audio_bytes) 

# if st.button('Load an audio file'):
#     uploaded_file = st.file_uploader("Choose a wav file")
#     if uploaded_file is not None:
#     # To read file as bytes:
#         bytes_audio = uploaded_file.read()
#         st.audio((bytes_audio),format="audio/mp3")
#         sound=AudioSegment.from_mp3('./sound/audio')
#         with wave.open('audio.wav', 'wb') as audio_file:
#             audio_file.setnchannels(2)  # Set number of channels (1 for mono, 2 for stereo)
#             audio_file.setsampwidth(2)  # Set sample width (in bytes)
#             audio_file.setframerate(44100)  # Set sample rate (in Hz)
#             audio_file.writeframesraw(audio_bytes)


music_instruments=['Clarinet','Voice','flute','Organ','Violin','Acoustic Guitar','Cello','Electric Guitar',
                   'Trumpet','Piano','Saxophone']


st.markdown('#')
st.markdown('#')

if st.button('Predict!'):
    import librosa
    import pickle
    with open('./pages/model_knn_mfcc.pkl', 'rb') as file_out:
        knn_mfcc = pickle.load(file_out)
    with open('./pages/model_knn_mel.pkl', 'rb') as file_out:
        knn_mel = pickle.load(file_out)
    with open('./pages/model_knn_join.pkl', 'rb') as file_out:
        knn_joint = pickle.load(file_out)
    with open('./pages/svm_join.pkl', 'rb') as file_out:
        svm_join = pickle.load(file_out)
    with open('./pages/scaler_mfcc.pkl', 'rb') as file_out:
        scaler_mfcc = pickle.load(file_out)
    with open('./pages/scaler_mel.pkl', 'rb') as file_out:
        scaler_mel = pickle.load(file_out)
    y_,sr=librosa.load('audio.wav',sr=44100)
    X_ = librosa.feature.melspectrogram(y=y_,sr=44100,n_fft=2048,hop_length=512,n_mels=129)
    X_mean_=np.mean(X_,1)
    X_mean_resh=X_mean_.reshape(1,-1)
    X_mel_scaled=scaler_mel.transform(X_mean_resh)
    X_mfcc=librosa.feature.mfcc(S=librosa.power_to_db(X_),n_mfcc=129)
    X_mfcc_=np.mean(X_mfcc,1)
    p=X_mfcc_.reshape(1,-1)
    X_mfcc_scaled=scaler_mfcc.transform(p)
    scaled=np.column_stack([X_mfcc_scaled,X_mel_scaled])

    models=["K_nearest_neighbour with MFCC alone","K_nearest_neighbour with MEL alone","K_nearest_neighbour with MFCC and MEL","SVM classifier with MFCC and MEL"  ]
    predictions=[]
    import time
    time.sleep(3)
    result_mfcc=knn_mfcc.predict(X_mfcc_scaled)
    predictions.append(music_instruments[result_mfcc[0]])
    st.write(f"This sound's like {music_instruments[result_mfcc[0]]}")
    result_mel=knn_mel.predict(X_mel_scaled)
    predictions.append(music_instruments[result_mel[0]])
    # st.write(f"This sound's like {music_instruments[result_mel[0]]}")
    result_scaled=knn_joint.predict(scaled)
    predictions.append(music_instruments[result_scaled[0]])
    # st.write(f"This sound's like {music_instruments[result_scaled[0]]}")
    result_svm=svm_join.predict(scaled)
    predictions.append(music_instruments[result_svm[0]])
    # st.write(f"This sound's like {music_instruments[result_svm[0]]}")
    import time
    time.sleep(3)
    import pandas as pd
    pred=pd.DataFrame({'Models':models[0:],'Predictions':predictions[0:]})
    st.table(pred)





