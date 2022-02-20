import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie

def write():
    kaire, desine = st.columns([30,12])

    with desine:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        hello = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_zkbsde97.json')
        st_lottie(hello,  speed=1, reverse=False, loop=True, quality="low", height=300, width=300, key='hello')

    with kaire:
            """Used to write the about page in the app.py file"""
            st.title("Hello, my name is Brigita!")
            st.subheader( "About my journey:")
            st.write(""" Pasisėmusi įvairiapusiškos patirties tekstilės srityje apsukau kelionės burę ir pasukau IT pusėn. 
            Žingsnis po žingsnio vis labiau įsigilinu į programavimo subtilybes, atrandu naujų pomėgių ir iššukių.
            O svarbiausia, kad man tai tikrai patinka. Kodėl? nes gaunasi!""")
            st.write(""" Šoninėje skiltyje rasi daugiau apie mane ir tikiuosi, kad su manim susisieksi. ;)""")

       

        
if __name__ == "__main__":
    main()