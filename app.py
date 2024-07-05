import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pprint
import google.generativeai as palm
from google.generativeai import models
from google.generativeai import files


palm.configure(api_key='AIzaSyAIHxQwpth7S_xTpf7yUhmvp3ZmCkxUsto')
selected_model = st.sidebar.selectbox('Select a model', ['gemini-1.5-pro','gemini-1.5-flash'])
st.title('Image Analyser')

with st.container():
    col = st.columns(2)
    with col[1]:
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            img1 = Image.open(uploaded_file)
            st.image(img1, caption='Uploaded Image.', width = 200)
            st.write("")
            st.success("Image Uploaded Successfully!")

    with col[0]:
        st.info(f"Generating with {selected_model}")

with st.container():
    model = palm.GenerativeModel(f'{selected_model}')
    prompt_input = st.text_input("Enter Your Prompt") 
    if(st.button('Generate')):
        prompt_text = prompt_input.title()
        if uploaded_file is not None:
            response = model.generate_content([prompt_text,img1])
            st.info(response.text)
        else:
            response = model.generate_content(prompt_text)
            st.info(response.text)
