import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assistant")

youtube_url = st.sidebar.text_area(
    label="What is the YouTube video URL?",
    max_chars=50
    )

query = st.sidebar.text_area(
    label="Ask me about the video?",
    max_chars=50
    )

if query:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))