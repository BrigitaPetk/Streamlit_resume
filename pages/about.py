import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    st.title("Hello, my name is Brigita!")
    col1, col2, col3 = st.columns([10,1,5])
    
    with col1:
            st.subheader( "About my journey:")
            st.write(""" After gaining extensive experience in the field of textiles, I turned the sail to the IT side.
            I learned **python** basics at Code Academy and now I'm continuing self-learning and practice my knowledge at Festo.
            Step by step I get more and more into the subtleties of programming, discover new hobbies and challenges.
            """)
            st.write("I'm looking for a job position in **backend**, **data analyst** or similar roles.")
            st.write("""Learn more about me in the sidebar.""")
            st.write('''Also, check my CV in linkedin and my projects in github:''')
            st.markdown(''' 
    <a href="https://www.linkedin.com/in/brigita-petkuvien%C4%97-59b6b8144/">
    <img src="https://play-lh.googleusercontent.com/kMofEFLjobZy_bCuaiDogzBcUT-dz3BBbOrIEjJ-hqOabjK8ieuevGe6wlTD15QzOqw" alt="alt" style="width:32px;height:32px;">
    </a>
    <a href="https://github.com/BrigitaPetk">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" alt="alt" style="width:32px;height:32px;">
    </a>''', unsafe_allow_html=True)
    with col2:
        st.write("")
    with col3:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            hello = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_zkbsde97.json')
            st_lottie(hello,  speed=1, reverse=False, loop=True, quality="low", height=300, width=300, key='hello')
        
