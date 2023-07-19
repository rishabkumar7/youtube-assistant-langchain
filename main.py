import streamlit as st
import langchain as lch

st.title("YouTube Assistant")

youtube_url = st.sidebar.text_area(
    label="What is the YouTube video URL?",
    max_chars=30
    )

question = st.sidebar.text_area(
    label="Ask me about the video?",
    max_chars=50
    )