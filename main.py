import streamlit as st 

st.title("Web scraper")
url = st.text_input("Enter the URL: ")

if st.button("Begin"):
    st.write(url)

