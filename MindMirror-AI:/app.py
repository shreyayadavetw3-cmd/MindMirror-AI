import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

st.title("🧠 MindMirror AI")

journal = st.text_area(
    "Write about your day"
)

if st.button("Analyze My Wellness"):

    prompt = f"""
    You are an empathetic student wellness coach.

    Analyze this journal:

    {journal}

    Return:

    1. Main Emotion
    2. Stress Level (1-10)
    3. Burnout Risk
    4. Main Stress Triggers
    5. Personalized Advice
    """

    response = model.generate_content(prompt)

    st.write(response.text)