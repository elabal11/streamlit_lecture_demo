#app.py
import app
import app_image
import app_api

import streamlit as st
PAGES = {
    "DataFrame Example": app,
    "Image Example": app_image,
    "API Example": app_api
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
