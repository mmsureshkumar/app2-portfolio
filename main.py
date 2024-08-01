import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\Suresh.jpg")

with col2:
    st.title("Suresh Kumar Murugsen")
    context = '''
    Hi, I am a software professional, teacher and founder of mmsureshkumar.net. I have worked with many python projects in different countries.
    '''
    st.info(context)

context1 = '''
Below you can find some of the apps that i have build in Python. Please feel free to call me
'''
st.write(context1)

col3, col4 = st.columns(2)

ds = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in ds[:10].iterrows():
        st.header(row['title'])


with col4:
    for index, row in ds[10:].iterrows():
        st.header(row['title'])
