import streamlit as st
if "shared" not in st.session_state:
   st.session_state["shared"] = True
    
with st.sidebar:
    st.sidebar.markdown("<h1> Musical Instrument Recognition </h1>",unsafe_allow_html=True)
    st.sidebar.markdown("## Priyadharshini Prabhakar")
    st.sidebar.markdown("##### priyaprabhaker@gmail.com")
import pandas as pd
import numpy as np
import time
import streamlit as st
# add_selectbox = st.sidebar.selectbox(
#     'Sections',
#     ('Main Page', 'Page 1', 'Page 2')
# )

st.title("What's the sound:violin::long_drum: like?")
st.divider()
st.markdown("### Using Machine learning model to Identify Musical Instruments")

# st.sidebar.markdown("# Main page 🎈")

#st.markdown("""##### Musical instrument recognition is the task of identifying the musical instrument that is being played in an audio recording. This is a challenging problem because different instruments can produce similar sounds, and the sound of a single instrument can vary depending on the playing style, technique, and context.""")
st.divider()
st.markdown("""<body><p style="color:white; font-family:Sans Serif; font-size:18px">
            This is a challenging problem because different instruments can produce similar 
            sounds, and the sound of a single instrument can vary depending on 
            the playing style, technique, and context.
            </p></body>""",unsafe_allow_html=True)
