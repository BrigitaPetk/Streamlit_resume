import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    st.title("Contact me!")
    col1, col2, col3= st.columns([7,1,5])
    with col1:
        st.markdown('''Write me an [**Email**](mailto:brigita.kalendraite@gmail.com)  directly or fill this form:''', unsafe_allow_html=True)
        contact_form ="""
    <form action="https://formsubmit.co/brigita.kalendraite@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="massage" placeholder="Your massage here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
        st.markdown(contact_form, unsafe_allow_html=True)

        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("pages/style_contact_form/style.css")
    with col2:
        st.write("")
    with col3:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        contact = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_6owo8hwo.json')
        st_lottie(contact,  speed=1, reverse=False, loop=True, quality="low", height=350, width=350, key='contact')


