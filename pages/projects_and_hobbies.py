import streamlit as st

def write():
    st.title("Projects")
    col1, col2, col3 = st.columns([5,5,5])
    with col1:
        st.markdown(''' 
    <a href="https://github.com/BrigitaPetk/ESP32_color_control">
    <img src="https://github.com/BrigitaPetk/Streamlit_resume/blob/main/pages/projects_images/ESP32_project.png?raw=true" alt="alt" style="width:300px;height:300px;">
    </a>
    ''', unsafe_allow_html=True)
        st.subheader("ESP32 Project")
        st.write("")
    with col2:
        st.markdown(''' 
    <a href="https://github.com/BrigitaPetk/Streamlit_resume">
    <img src="https://github.com/BrigitaPetk/Streamlit_resume/blob/main/pages/projects_images/Resume_project.png?raw=tru" alt="alt" style="width:300px;height:300px;">
    </a>
    ''', unsafe_allow_html=True)
        st.subheader("Resume Project")
        st.write("")
    with col3:
        st.markdown(''' 
    <a href="https://github.com/BrigitaPetk/support_department_dashboard">
    <img src="https://github.com/BrigitaPetk/Streamlit_resume/blob/main/pages/projects_images/Dashboard_project.png?raw=true" alt="alt" style="width:300px;height:300px;">
    </a>
    ''', unsafe_allow_html=True)
        st.subheader("Support Department Dashboard Project")
        st.write("")



