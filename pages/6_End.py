import streamlit as st
from PIL import Image
with st.sidebar:
    st.sidebar.markdown("<h1> Musical Instrument Recognition </h1>",unsafe_allow_html=True)
    st.sidebar.markdown("## Priyadharshini Prabhakar")
    st.sidebar.markdown("##### priyaprabhaker@gmail.com")
scikit = Image.open('./images/1920px-Scikit_learn_logo_small.svg.png')
python= Image.open('./images/Python_logo.png')
pandas=Image.open('./images/Pandas_logo.svg.png')
streamlit=Image.open('./images/streamlit_logo.png')
numpy=Image.open('./images/1280px-NumPy_logo.png')
librosa=Image.open('./images/librosa_logo.png')
grouppicture=Image.open('./images/group_picture.jpg')
thankyou=Image.open('./images/Thank_you.jpg')

st.image([scikit,python],width=300)
st.image([pandas,streamlit],width=300)#, caption='Sunrise by the mountains')
st.image([numpy,librosa],width=300)#, caption='Sunrise by the mountains')
st.markdown('#')
st.markdown('#')
st.markdown("<h1 style='text-align:center;'>Thank You Nigelas!</h1>",unsafe_allow_html=True)
st.image(grouppicture)







