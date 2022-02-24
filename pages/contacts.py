import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    contact_form ="""
<form action="https://formsubmit.co/brigita.kalendraite@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="massage" placeholder="Your massage here"><</textarea>
     <button type="submit">Send</button>
</form>
"""

    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style_contact_form/style.css")

if __name__ == "__main__":
    main()