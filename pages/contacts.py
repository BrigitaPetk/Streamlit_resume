import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    st.title("Contact me!")
    col1, col2, col3= st.columns([7,1,5])
    with col1:
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
        st_lottie(contact,  speed=1, reverse=False, loop=True, quality="low", height=300, width=300, key='contact')
    

    st.write("you also can check me on linkedin and github")
       
    st.markdown('''<a href="https://www.linkedin.com/in/brigita-petkuvien%C4%97-59b6b8144/">
    <img src="https://play-lh.googleusercontent.com/kMofEFLjobZy_bCuaiDogzBcUT-dz3BBbOrIEjJ-hqOabjK8ieuevGe6wlTD15QzOqw" alt="alt" style="width:32px;height:32px;">
    </a>
    <a href="https://github.com/BrigitaPetk">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" alt="alt" style="width:32px;height:32px;">
    </a>''', unsafe_allow_html=True)



if __name__ == "__main__":
    main()