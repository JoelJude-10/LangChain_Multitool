import streamlit as st
import multitools
st.title("Demo Search Engine")
user_input = st.text_input("Enter some text:")
a=0
if user_input:
    a = multitools.multi_tool(user_input)
st.write(a)
