#hello!
# print("Hello world!")
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",
)

header = st.container()

with header:
    st.title("Welcome to [App Name].")
    st.image("https://pharmchoices.com/wp-content/uploads/2021/04/5a374dca6b5fa9.6831613015135738344398.png")
    st.subheader("We'll help you make smart and informed decisions about your use of medication, all while keeping you safe.")
    st.button("Get started")
