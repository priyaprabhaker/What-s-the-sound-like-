import streamlit as st
from PIL import Image
with st.sidebar:
    st.sidebar.markdown("<h1> Musical Instrument Recognition </h1>",unsafe_allow_html=True)
    st.sidebar.markdown("## Priyadharshini Prabhakar")
    st.sidebar.markdown("##### priyaprabhaker@gmail.com")
image = Image.open('./images/background1.jpg')

st.image(image,width=720)#, caption='Sunrise by the mountains')
st.markdown("<h1 style='text-align:center; font-size:350%;'>What's the sound like?</h1>",unsafe_allow_html=True)
