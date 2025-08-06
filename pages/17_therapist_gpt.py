import streamlit as st

st.title("TherapistGPT")
st.markdown("Talk it out. This AI won’t judge you.")

# Super unique key
user_input = st.text_area(
    "What's on your mind?",
    placeholder="Write anything you want to talk about...",
    height=200,
    key="therapist_page_unique_input_box_001"
)

# Simulated therapy response
def offline_therapist_response(prompt):
    if "sad" in prompt.lower():
        return "I'm really sorry you're feeling that way. Can you tell me what’s been weighing on you the most?"
    elif "anxious" in prompt.lower():
        return "Anxiety can be overwhelming. Let's take a moment to breathe together. What’s triggering it today?"
    elif "angry" in prompt.lower():
        return "Anger often hides hurt. Do you want to unpack what’s beneath it?"
    elif "happy" in prompt.lower():
        return "That's amazing to hear! What’s bringing you that joy lately?"
    elif "lonely" in prompt.lower():
        return "Loneliness can feel heavy. You’re not alone here. What do you wish people understood?"
    else:
        return "Tell me more. I’m here for you, no matter what you’re feeling."

# Button also needs unique key
if st.button("Talk to Therapist", key="therapist_unique_submit_btn_001"):
    if user_input.strip() == "":
        st.warning("Please enter a message before submitting.")
    else:
        response = offline_therapist_response(user_input)
        st.markdown("#### Therapist Says:")
        st.success(response)

# Export feature
with st.expander("Export to Diary"):
    export_note = st.text_area(
        "Optional note to save:",
        key="therapist_unique_export_note_001"
    )
    if st.button("Save Note", key="therapist_unique_save_btn_001"):
        try:
            with open("data/entries/therapist_notes.txt", "a", encoding="utf-8") as f:
                f.write(f"\n---\n{user_input}\nTherapist: {offline_therapist_response(user_input)}\nNote: {export_note}\n")
            st.success("Note saved to therapist_notes.txt")
        except Exception as e:
            st.error(f"Failed to save: {e}")
