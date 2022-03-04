import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    st.title("Experience ")
    col1, col2, col3 = st.columns([5,15, 10])
    with col1:
        st.write("2022-01 – Now   \n ## ")
        st.write("2020-08 – 2021-10  \n ##")
        st.write(" 2017-03 – 2020-08")

    with col2:
        st.write("**Junior data visualization specialist**  \n  UAB  'Festo', Internship")
        st.write("**Designer-technologist**  \n  UAB  'Barker Textiles' ")
        st.write("**Graphic designer**  \n UAB  'Textilis'")
    with col3:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        hello = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_pd7m1lgk.json')
        st_lottie(hello,  speed=1, reverse=False, loop=True, quality="low", height=250, width=300, key='hello')


if __name__ == "__main__":
    main()