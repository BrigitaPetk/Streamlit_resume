import streamlit as st

def write():

    st.title("Education :books:")
    col1, col2 = st.columns([3,15])
    with col1:
        st.write("2021-08-10 – 2021-10-14")
        st.write("2021-08-10 – 2021-10-14")
        st.write("2021-08-10 – 2021-10-14")
    with col2:
        st.write("Code Academy")
        st.write("Kauno technologijos universitetas")
        st.write("Kauno technologijos universitetas")

if __name__ == "__main__":
    main()