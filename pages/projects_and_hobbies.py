import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    col1, col2, col3 = st.columns([8,7,8])
    with col1:
        st.write("")
    with col2:
        st.title("In proccess...")
    with col3:
        st.write("")
        
    col1, col2, col3 = st.columns([2,6,2])
    with col1:
        st.write("")
    with col2:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        spin = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_omullrhw.json')
        st_lottie(spin,  speed=1, reverse=False, loop=True, quality="low", height=500, width=500, key='hello')
    with col3:
        st.write("")



