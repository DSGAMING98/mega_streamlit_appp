import streamlit as st
import os
import sys
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Path setup for backend tools
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to view analysis.")
    st.stop()

st.title("AI Diary Analysis")

ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
diary_files = list_files(ENTRIES_DIR, ".txt")

if not diary_files:
    st.info("No diary entries found.")
    st.stop()

# Load all diary content
all_text = ""
sentiments = []

for file in diary_files:
    path = os.path.join(ENTRIES_DIR, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        all_text += content + "\n"

        # Sentiment analysis using TextBlob
        blob = TextBlob(content)
        polarity = blob.sentiment.polarity
        if polarity > 0.2:
            mood = "😊 Positive"
        elif polarity < -0.2:
            mood = "😞 Negative"
        else:
            mood = "😐 Neutral"
        sentiments.append((file.replace("_", " ").replace(".txt", ""), mood))

# Display Sentiment Results
st.subheader("Entry Sentiments")
for name, mood in sentiments:
    st.markdown(f"**{name}** → {mood}")

# Generate Word Cloud
st.subheader("Most Used Words (Word Cloud)")
if all_text.strip():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("Not enough text to generate a word cloud.")
