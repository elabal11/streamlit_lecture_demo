import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

def app():
    uploaded_file = st.file_uploader('Upload an image',type=['jpeg','jpg','png'])

    if uploaded_file:
        im = Image.open(uploaded_file)
        st.image(im)
        st.balloons()
