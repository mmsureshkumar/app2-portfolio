import streamlit as st

st.header("Contact Me")

with st.form(key="form_upload"):
    st.text_input("Your Email Address")
    st.text_area("Your Message")
    button = st.form_submit_button()
    if button:
        print("Submit button pressed")
