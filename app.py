### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.skills
import pages.experience
import pages.edu
import pages.contacts
import pages.projects_and_hobbies

# Page title:
st.set_page_config(page_title="My Resume",
                   page_icon=":raising_hand:",  #icon: https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout="wide")

def write_page(page):  
    page.write()

 
PAGES = {
    "About": pages.about,
    "Education" : pages.edu,
    "Experience": pages.experience,  
    "Skills": pages.skills,
    "Projects and hobies": pages.projects_and_hobbies,
    "Contact me": pages.contacts,

}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        write_page(page)


hidden_objects = """
                   <style>
                    MainMenu {visibility: hidden;}
                   footer {visibility: hidden;}
                   header {visibility: hidden;}
                   </style>                   
                   """
st.markdown(hidden_objects,unsafe_allow_html=True)


if __name__ == "__main__":
    main()