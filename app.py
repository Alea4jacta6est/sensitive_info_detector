"""The main part of Streamlit UI is rendered here"""
import os

import streamlit as st
import streamlit.components.v1 as components
import seaborn as sns

from sent_app.core.utils import classify_text_by_ents, extract_text_data


cm = sns.light_palette("green", as_cmap=True)

def main():
    st.set_page_config(page_title="Sensitivity checker", layout='wide', initial_sidebar_state='auto')
    st.title("Sensitive info extraction")
    task_type = st.sidebar.radio("Demo types:", ('Parsing existing texts', 'Process text input'))
    if task_type == 'Process text input':
        user_input = st.sidebar.text_area("Paste a paragraph")
        label, html = classify_text_by_ents(user_input)
        st.subheader(f"Classified as {label}")
        components.html(html, height=1000, scrolling=True)
    elif task_type == 'Parsing existing texts':
        filename_choice = st.sidebar.selectbox("Choose a file", os.listdir("data"))
        text = extract_text_data(filename_choice)
        label, html = classify_text_by_ents(text)
        st.subheader(f"Classified as {label}")
        components.html(html, height=1000, scrolling=True)
    else:
        raise ValueError
    
   
if __name__ == "__main__":
    main()