import streamlit as st
import random
import time

st.title("🍑 Get Spanked by LeBron")

reactions = [
    "LeBron squints at you like you're JR Smith in Game 1.",
    "He sighs… takes off the headband… it's over for you.",
    "He chuckles menacingly. You done goofed.",
    "He smirks and says, 'You brought this on yourself.'",
    "He doesn’t even blink. Just raises the arm…",
    "LeBron grabs you by the waist like a rebound and whispers, 'Don't run now.'",
    "He pins you to the hardwood, breath hot in your ear. 'You asked for this.'",
    "LeBron backs you into the paint and murmurs, 'I go hard in all positions.'",
    "He stares into your soul, jaw clenched. 'Call me Daddy Goat.'",
    "You feel his hand hovering—then BOOM. 'That’s for disrespecting my legacy.'",
    "He pushes you to the floor, kneels beside you, and whispers, 'You good down there, lil one?'",
    "LeBron grins. 'I’m not done until you can’t sit for a week.'",
    "He slaps, pauses, and says, 'Now tell the media it was consensual.'",
    "He looks down at you like you’re a rookie in the Finals. 'Let me teach you something.'",
    "He bites his lip, flexes, and says, 'You know I’ve been in the league for 21 years, right?'",
]

spanks = [
    "🫱 Light tap. You survived. For now.",
    "🫲 Mid-level whoop. You spinning like a fidget spinner.",
    "🖐️ Full-palm contact. Your ancestors felt it.",
    "🧤 Gloved spank. NBA-regulation legal.",
    "🦵 He jumped and spanked. You are airborne.",
    "💥 Atomic SLAP. You're now part of the court paint.",
]

quotes = [
    "“You flop more than Harden.”",
    "“You think you can guard me in bed?”",
    "“I got 4 rings. You got one cheek.”",
    "“You know I’m 6'9”, 250 right?”",
    "“Now hold still.”",
    "“You think I dropped 40 for you to keep your pants on?”",
    "“I’ve dominated courts harder than I’m about to dominate you.”",
    "“I play 48 minutes… but I can go all night.”",
    "“I’ve scored in every position—on the court *and* off it.”",
    "“This ain’t load management, baby. You getting all of me.”",
    "“You flinched? That was the warmup slap.”",
    "“Open up like you guarding the paint.”",
    "“You better arch that back like my free throw form.”",
    "“You ever been posterized in bed?”",
    "“You like post moves? I got one you won’t forget.”",
    "“I’ll break your ankles and your self-control.”",
    "“Call me King for a reason. Now kneel.”",
    "“You moaning louder than the crowd at Staples.”",
    "“Lakers in 4, but you in missionary.”",
    "“Don’t tap out now. We’re only in the first quarter.”",
]

health = random.randint(0, 100)

if "last_spank" not in st.session_state:
    st.session_state.last_spank = ""

if st.button("👋 Get Spanked", key="lebron_spank"):
    with st.spinner("LeBron is winding up..."):
        time.sleep(1)
        st.session_state.last_spank = random.choice(spanks)

    st.subheader("SPANK RESULT:")
    st.markdown(f"**{random.choice(reactions)}**")
    st.markdown(f"**{st.session_state.last_spank}**")
    st.success(f'LeBron said: *{random.choice(quotes)}*')

    st.markdown("---")
    st.subheader("Survivability Meter")
    st.progress(health)
    if health < 30:
        st.error("You may not walk again.")
    elif health < 70:
        st.warning("You’re dizzy but standing.")
    else:
        st.success("You took it like a champ.")
