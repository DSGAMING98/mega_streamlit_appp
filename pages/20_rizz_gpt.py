import streamlit as st
import random
import os
import json

st.title("RizzGPT")
st.markdown("Let AI cook your next pickup line. No GPT, just raw RIZZ.")

# Style + target input
style = st.selectbox("What's your rizz style?", ["Cute", "Wild", "Cringe", "Confident", "Emo", "Unhinged"])
target = st.text_input("Who’s the target?", placeholder="e.g. barista, crush, ex, gym rat")

# Favorite rizz storage
FAVES_PATH = "data/rizz"
os.makedirs(FAVES_PATH, exist_ok=True)
FAVES_FILE = os.path.join(FAVES_PATH, "favorites.json")
if not os.path.exists(FAVES_FILE):
    with open(FAVES_FILE, "w") as f:
        json.dump([], f)

# Rizz bank
rizz_lines = {
    "Cute": [
        "Are you made of copper and tellurium? Because you're Cu-Te.",
        "Do you have a map? I keep getting lost in your eyes.",
        "You just made my day better by existing.",
        "If kisses were snowflakes, I'd send you a blizzard."
    ],
    "Wild": [
        "Are you a microwave? Cause baby, I’m ready to explode.",
        "Let’s commit tax fraud together. Sexily.",
        "You're the human version of Friday night tequila.",
        "I don’t know your sign, but I’m sensing we’re *physically compatible*."
    ],
    "Cringe": [
        "Do you like raisins? No? How about a date then?",
        "Are you French? Because Eiffel for you.",
        "If beauty were time, you’d be eternity. But I’d still be late.",
        "You must be tired… from running through my mind all day."
    ],
    "Confident": [
        "You’re gonna fall for me. It’s inevitable.",
        "I’m not here to impress. I’m here to stay.",
        "I saw you. I wanted you. So I came over.",
        "I’m not just a catch — I’m the whole damn ocean."
    ],
    "Emo": [
        "I fell for you harder than my mental health.",
        "You're the serotonin I can't refill.",
        "Let’s make sadness romantic.",
        "You're the only chaos I’d write poems for."
    ],
    "Unhinged": [
        "I’d let you ruin my life… and do it again.",
        "You breathe? I’m into that.",
        "Are you a campfire? Cause you’re hot and I want s’more — and also I’m unstable.",
        "You and I? FBI watchlist material."
    ]
}

# Generate line
if st.button("Drop a Line"):
    if not target:
        st.warning("Give me a target, flirt god.")
    else:
        line = random.choice(rizz_lines[style])
        full_rizz = f"To your {target}: {line}"
        st.success("Rizz Generated:")
        st.markdown(f"**{full_rizz}**")
        st.session_state.rizz_output = full_rizz

# Save favorite
if "rizz_output" in st.session_state:
    if st.button("Save to Favorites"):
        with open(FAVES_FILE, "r") as f:
            favorites = json.load(f)
        favorites.append(st.session_state.rizz_output)
        with open(FAVES_FILE, "w") as f:
            json.dump(favorites, f, indent=2)
        st.success("Saved!")

# Show favorites
with st.expander("View Your Favorite Lines"):
    with open(FAVES_FILE, "r") as f:
        faves = json.load(f)
    if not faves:
        st.info("No saved rizz yet.")
    else:
        for i, line in enumerate(faves[::-1], 1):
            st.markdown(f"**{i}.** {line}")
