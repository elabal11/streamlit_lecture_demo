import streamlit as st
import requests

def app():
    st.title("Streamlit Lecture")

    st.header("Text in Image Api")
    input = st.text_input("Input your text For Bruzu Api")
    if input:
        url = f"https://img.bruzu.com/?backgroundImage=https://source.unsplash.com/U-Kty6HxcQc/500x500%20&a.text={input}&a.color=white&a.fontFamily=Poppins&a.fontWeight=800&a.width=450&b.text=%20@naval&b.width=450&b.top=480&b.originY=bottom&b.color=white&b.fontFamily=Playfair%20Display&b.fontSize=30"
        st.image(requests.get(url).content)

    st.header("Picsum API")
    button = st.button("Get Random Images")
    if button:
        url = f"https://picsum.photos/500"
        st.image(requests.get(url).content)
