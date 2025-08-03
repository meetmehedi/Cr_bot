import streamlit as st
import json
import os
from voice_engine.recognizer import recognize_speech
from voice_engine.intent_matcher import match_intent

# Load class data
DATA_FILE = "class_schedule_d90.json"
if not os.path.exists(DATA_FILE):
    st.error("Data file not found!")
    st.stop()

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

st.set_page_config(page_title="ShikkhokBot", layout="centered")
st.title("🎙️ বাংলা ভয়েস-নির্ভর ভার্চুয়াল সহকারী")
st.markdown("##### ক্লাস রুটিন, 📍 স্যারদের রুম, 📣 ইভেন্ট জানতে বাংলায় বলো!")

if st.button("🎧 কথা বলো"):
    with st.spinner("শুনছে..."):
        query = recognize_speech()
    st.write(f"**তুমি বলেছো:** {query}")
    
    intent, response = match_intent(query, data)
    st.success(f"📢 {response}")

st.markdown("---")
st.info("📌 শুধুমাত্র D-90 ব্যাচের জন্য তৈরি।")
