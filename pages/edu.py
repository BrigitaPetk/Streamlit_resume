import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie


def write():

    st.title("Education")
    col1, col2, col3 = st.columns([5,15, 10])
    with col1:
        st.write("2021-10 – 2021-12")
        st.write("2018 – 2020  \n ## ")
        st.write(" 2014 – 2018")

    with col2:
        st.write("** Code Academy **")
        st.write("** Kaunas university of technology **  \n  Master's degree, Textile sciences an engineering ")
        st.write("** Kaunas university of technology **  \n Bachelor's degree, Textile sciences an engineering")
    with col3:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        hello = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_1uetnpo3.json')
        st_lottie(hello,  speed=1, reverse=False, loop=True, quality="low", height=300, width=300, key='hello')


if __name__ == "__main__":
    main()