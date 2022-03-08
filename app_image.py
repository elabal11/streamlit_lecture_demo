import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

img_list = ['abstract-red-color-light-oblique-1630900.jpeg','black-white-wallpaper-11.jpeg','grapefruit-slice-332-332.jpeg','images.jpeg']

def app():
    st.title("Streamlit Lecture")
    uploaded_file = st.file_uploader('Upload an image',type=['jpeg','jpg','png'])



    if uploaded_file:
        im = Image.open(uploaded_file)
        col1, col2 = st.columns(2)

        img = Image.open(img_list[0])

        col2.image(im, use_column_width=True)

        slider = st.slider('train GAN',0,len(img_list)-1,step=1,)
        if not slider:
            slider = 0 # Default Value
        img = Image.open(img_list[slider])
        col1.image(img, use_column_width=True)
