import streamlit as st
import os
import random
import datetime

if "lebron_pic" not in st.session_state:
    st.session_state.lebron_pic = None

def get_random_lebron_image():
    pic_dir = "data/lebron_pics"
    if not os.path.exists(pic_dir):
        return None
    pics = [f for f in os.listdir(pic_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not pics:
        return None
    return os.path.join(pic_dir, random.choice(pics))

if st.button("Next LeBron Pic", key="next_lebron"):
    st.session_state.lebron_pic = get_random_lebron_image()

if st.session_state.lebron_pic:
    st.image(st.session_state.lebron_pic, caption="All hail the King.", use_container_width=True)
else:
    st.info("Click the button to see LeBron in high-res greatness.")


st.title("LeBron Glazer Tool")

#Legendary LeFacts
facts = [
    "LeBron is the **only player in NBA history** with 30K+ points, 10K+ rebounds, and 10K+ assists.",
    "At 38, he dropped **40 points** and still looked like he was 25.",
    "He passed Kareem to become the **NBA’s all-time leading scorer.**",
    "LeBron has made the **NBA Finals 10 times** — more than some franchises.",
    "He dropped **25+ points in 16 straight Finals games** — the longest in NBA history.",
    "He once led a Finals series in **points, rebounds, assists, steals, and blocks**… at the same time.",
    "In 2016, he brought a **3–1 comeback** to Cleveland against a 73–9 team.",
    "He played **55,000+ minutes** and is still elite. Most people can’t walk after that.",
    "He spends **$1.5M a year on his body**, and it shows. Literal tank.",
    "He’s the only player to score **40+ against every NBA franchise.**",
]

# Glaze Engine
def generate_glaze_essay():
    praise = [
        "LeBron James is not just a basketball player — he's a divine entity in sneakers. A generational mind housed in a 6'9'', 250 lb war machine.",
        "Watching LeBron is like witnessing Greek mythology in real time. Zeus who? Poseidon where? LeBron created Mt. Olympus himself.",
        "He’s not playing basketball. He’s redefining the laws of physics every time he touches the court. NASA has been suspiciously silent.",
        "LeBron doesn’t age — he levels up. Each year, he decides to add something new to his bag just because he’s bored of being perfect.",
        "They said ‘Father Time is undefeated’ — LeBron beat that man in Game 7 with a chasedown block.",
        "Daddy LeBron has been dominating for 21 years. Hope he stays for more",
        "MJ has nothing against this guy. LeBron do be bursting into everyone",
        "LeBron my sunshine, My only sunshine, You make me happy, when sky's are grey",
        "Boy oh boy where do I even begin. Lebron... honey, my pookie bear. I have loved you ever since I first laid eyes on you. The way you drive into the paint and strike fear into your enemies eyes. Your silky smooth touch around the rim, and that gorgeous jumpshot. I would do anything for you. I wish it were possible to freeze time so I would never have to watch you retire. You had a rough childhood, but you never gave up hope. You are even amazing off the court, you're a great husband and father, sometimes I even call you dad. I forever dread and weep, thinking of the day you will one day retire. I would sacrifice my own life it were the only thing that could put a smile on your beautiful face. You have given me so much joy, and heartbreak over the years. I remember when you first left clevenland and its like my heart got broken into a million pieces. But a tear still fell from my right eye when I watched you win your first ring in miami, because deep down, my glorious king deserved it. I just wanted you to return home. Then allas, you did, my sweet baby boy came home and I rejoiced. 2015 was a hard year for us baby, but in 2016 you made history happen. You came back from 3-1 and I couldn't believe it. I was crying, bawling even, and I heard my glorious king exclaim these words, 'CLEVELAND, THIS IS FOR YOU!' Not only have you changed the game of basketball and the world forever, but you've eternally changed my world. And now you're getting older, but still the goat, my goat. I love you pookie bear, my glorious king, Lebron James."

    ]
    return random.choice(praise)

# Layout
st.subheader("Legendary LeFact of the Day")
st.success(random.choice(facts))

st.markdown("---")
st.subheader("Generate an AI Glaze Essay")

if st.button("Glaze Him"):
    st.markdown(f"**{generate_glaze_essay()}**")


    image_path = get_random_lebron_image()
    if image_path:
        st.image(image_path, caption="All hail the King.", use_container_width=True)
    else:
        st.warning("No LeBron pics found. Add some to `data/lebron_pics/`")

st.markdown("---")
st.subheader("How many years elite?")
lebron_debut = datetime.date(2003, 10, 29)
today = datetime.date.today()
years = (today - lebron_debut).days // 365
st.info(f"LeBron James has been elite for **{years} years** straight. You weren’t even born when he started.")

st.markdown("---")
st.caption("This module is dedicated to The King. Glaze responsibly.")
st.markdown("---")
st.subheader("Highlight of The King")
st.video("https://youtu.be/cwK1YHZ1AGc?feature=shared")

st.markdown("---")
st.subheader("Official GOAT Scale")
st.bar_chart({
    "GOAT Level": {
        "LeBron": 100,
        "Jordan": 89,
        "Kobe": 82,
        "Curry": 79,
        "KD": 74
    }
})

