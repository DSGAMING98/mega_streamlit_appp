import streamlit as st
import os
from datetime import datetime

CONTACT_DIR = "data/contact_messages"
os.makedirs(CONTACT_DIR, exist_ok=True)

st.title("Contact Form")
st.markdown("Submit your message or feedback here. Messages are saved locally.")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message", height=200)

if st.button("Submit"):
    if not name.strip() or not email.strip() or not message.strip():
        st.warning("All fields are required.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(CONTACT_DIR, f"message_{timestamp}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write("Message:\n")
            f.write(message.strip())
        st.success("Message submitted successfully.")
