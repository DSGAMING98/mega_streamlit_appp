import streamlit as st
import os
import json
import datetime
import matplotlib.pyplot as plt

# Set up storage
DATA_PATH = "data/mood"
os.makedirs(DATA_PATH, exist_ok=True)

# UI
st.title("Mood Tracker")
st.markdown("Track your feelings, patterns, and progress.")

# Get username (optional session logic)
username = st.text_input("Your Name / ID", placeholder="Enter your name")

if username:
    today = datetime.date.today().isoformat()
    user_file = os.path.join(DATA_PATH, f"{username}_mood.json")

    # Load data
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            mood_data = json.load(f)
    else:
        mood_data = {}

    # Mood input
    mood = st.slider("How do you feel today?", -5, 5, 0, format="%+d")
    reason = st.multiselect("What's affecting your mood?",
                            ["Work", "School", "Friends", "Family", "Health", "Romance", "Nothing", "Everything"])
    notes = st.text_area("Wanna add a note?", placeholder="Vent away...")

    if st.button("Save Today's Mood"):
        mood_data[today] = {
            "mood": mood,
            "reason": reason,
            "notes": notes,
        }
        with open(user_file, "w") as f:
            json.dump(mood_data, f, indent=2)
        st.success("Mood saved!")

    # Display past data
    if mood_data:
        st.markdown("---")
        st.subheader("Mood History")

        dates = list(mood_data.keys())
        moods = [mood_data[d]["mood"] for d in dates]

        fig, ax = plt.subplots()
        ax.plot(dates, moods, marker='o', linestyle='-', color='purple')
        ax.axhline(0, color='gray', linestyle='--')
        ax.set_ylabel("Mood")
        ax.set_xlabel("Date")
        ax.set_title(f"Mood Chart for {username}")
        plt.xticks(rotation=45)

        st.pyplot(fig)

        with st.expander("Mood Log Entries"):
            for d in sorted(mood_data.keys(), reverse=True):
                entry = mood_data[d]
                st.markdown(f"**{d}** — Mood: `{entry['mood']}` | Reasons: `{', '.join(entry['reason'])}`")
                if entry["notes"]:
                    st.caption(entry["notes"])
