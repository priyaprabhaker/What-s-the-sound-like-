import streamlit as st
#st.write(st.session_state["shared"])
from PIL import Image
with st.sidebar:
    st.sidebar.markdown("<h1> Musical Instrument Recognition </h1>",unsafe_allow_html=True)
    st.sidebar.markdown("## Priyadharshini Prabhakar")
    st.sidebar.markdown("##### priyaprabhaker@gmail.com")

st.markdown("# Model")
st.divider()
image1 = Image.open('./images/flowchart.png')

st.image(image1)#, caption='Sunrise by the mountains')
st.markdown('#')
confusion_matrix=Image.open('./images/model_knn_cf.png')
st.markdown("## 89% accuracy")
st.image(confusion_matrix)