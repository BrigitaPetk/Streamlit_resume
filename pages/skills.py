import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests

def write():
    st.title("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("IT skills")
        st.write(""" 
- Python 
- Grafana
- Streamlit
- Pandas
- Plotly
- Docker
- SQL  """)
    with col2:
        st.subheader("Other skills")
        st.write(""" 
- Adobe illiustrator
- Adobe photoshop
- Lean
- Microsoft """)

    with col3:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        hello = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_z5loe4p9.json')
        st_lottie(hello,  speed=1, reverse=False, loop=True, quality="low", height=230, width=230, key='hello')




if __name__ == "__main__":
    main()