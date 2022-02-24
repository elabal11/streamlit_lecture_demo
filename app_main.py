#app.py
import app
import app_image
import streamlit as st
PAGES = {
    "DataFrame Example": app,
    "Image Example": app_image
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
