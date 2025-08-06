import streamlit as st
import random

st.title("Fanfic Generator")
st.markdown("Choose your poison. We’ll cook you a scene. No GPT, just pure chaos and vibes.")

# Fanfic tags
genres = ["Romance", "Angst", "Fluff", "Smut", "Crack", "Enemies to Lovers", "Slow Burn"]
pairings = ["Reader x Celebrity", "OC x OC", "F/F", "M/M", "F/M", "Throuple", "You x Your Crush"]
styles = ["Cute", "Wild", "Steamy", "Emotional", "Dark", "Wholesome", "Chaotic"]

# User input
genre = st.selectbox("Choose Genre", genres)
pairing = st.selectbox("Choose Pairing", pairings)
style = st.selectbox("Choose Style", styles)
custom_prompt = st.text_area("Want to add something specific? (Optional)", placeholder="e.g. rooftop kiss, jealous ex, kitchen table, vampire AU")

if st.button("Generate Scene"):
    # Random scene templates
    intros = [
        "The tension was unbearable as their eyes met.",
        "Rain poured outside, but the storm inside them raged harder.",
        "They were never supposed to fall for each other, and yet...",
        "It started with a text at 2AM and ended on the kitchen counter.",
        "Their lips met before either of them could think twice."
    ]

    twists = [
        "But then someone walked in.",
        "One of them whispered the other's name like a secret.",
        "The air crackled as emotions burst into flame.",
        "They pulled away, only to be dragged back by desire.",
        "Everything they held back came pouring out in one heated breath."
    ]

    endings = [
        "And just like that, they knew they were doomed.",
        "They didn’t speak — they didn’t need to.",
        "This was only the beginning.",
        "Neither of them could ever go back to normal.",
        "One word from them, and the world would burn."
    ]

    scene = f"""
**Genre:** {genre}  
**Pairing:** {pairing}  
**Style:** {style}  

---

**{random.choice(intros)}**  
{custom_prompt if custom_prompt else ""}
**{random.choice(twists)}**  
**{random.choice(endings)}**
"""

    st.markdown(scene)
