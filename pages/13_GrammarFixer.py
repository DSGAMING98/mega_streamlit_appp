import streamlit as st
from textblob import TextBlob

st.title("AI Grammar Correction Tool")

# Input text
user_input = st.text_area("Paste or write text below to check grammar:", height=200)

if st.button("Correct Text"):
    if not user_input.strip():
        st.warning("Text cannot be empty.")
    else:
        blob = TextBlob(user_input)
        corrected = str(blob.correct())

        st.subheader("Original Text")
        st.markdown(user_input)

        st.subheader("Corrected Text")
        st.success(corrected)
