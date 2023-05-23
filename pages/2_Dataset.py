import streamlit as st
#st.write(st.session_state["shared"])
with st.sidebar:
    st.sidebar.markdown("<h1> Musical Instrument Recognition </h1>",unsafe_allow_html=True)
    st.sidebar.markdown("## Priyadharshini Prabhakar")
    st.sidebar.markdown("##### priyaprabhaker@gmail.com")
st.markdown("# Datasets")
#st.sidebar.markdown("# Datasets")
st.divider()
st.markdown("""<body><p style="color:white; font-family:Sans Serif; font-size:18px">
            IRMAS dataset contains <b>6705 audio recordings of 11 musical instruments</b>, 
            including <b>acoustic guitar🎸, electric guitar⚡🎸, piano🎹, violin🎻, cello🎻, saxophone🎷, 
            trumpet🎺, clarinet≕≺, flute➖, organ🎼, and human singing voice🎤</b>. Each recording is 
            <b>3 seconds long</b> and was played by professional musicians in a studio setting. 
            The recordings are in <b>WAV format</b> and have a sampling rate of 0.66 kHz. 
            </p></body>""",unsafe_allow_html=True)
#st.markdown("write the code point on how you downloaded it")
st.markdown("#")
from PIL import Image
Img=Image.open('./images/bar_plot_files.png')
st.image(Img)