#app.py
import app
import app_image
import app_api
import base64

import streamlit as st

page_bg_img = '''
<style>
body {
background-image: url("https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg");
background-size: cover;
}
</style>
'''


PAGES = {
    "Image Example": app_image,
    "DataFrame Example": app,
    "API Example": app_api
}

st.title("Streamlit Lecture")
st.markdown(page_bg_img, unsafe_allow_html=True)

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# bin_str = get_base64_of_bin_file('grapefruit-slice-332-332.jpeg')
# CSS = """
# .stApp {
#     background-image: url("data:image/png;base64,%s");
#     background-repeat: no-repeat;
#     background-position: top;
#     background-size: cover;
#     background-size: 1580px 111px;
# }
# """ % bin_str
# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

#set_png_as_page_bg('grapefruit-slice-332-332.jpeg')

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
