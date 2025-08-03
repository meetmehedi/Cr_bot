import streamlit as st
import json
import os
from voice_engine.recognizer import recognize_speech

# --- Helper functions for intent matching and responses ---
def list_assignments(data):
    items = data.get("Assignment", [])
    if not items:
        return "📭 কোনো অ্যাসাইনমেন্ট পাওয়া যায়নি।"
    response = "📚 অ্যাসাইনমেন্ট তালিকা:\n"
    for a in items:
        response += f"• {a['title']} (Due: {a['due_date']})\n"
    return response

def list_lab_reports(data):
    items = data.get("lab report", [])
    if not items:
        return "🧪 কোনো ল্যাব রিপোর্ট পাওয়া যায়নি।"
    response = "🧪 ল্যাব রিপোর্ট:\n"
    for a in items:
        response += f"• {a['title']}\n"
    return response

def list_cts(data):
    items = data.get("CT", [])
    if not items:
        return "📝 কোনো সিটি নির্ধারিত নেই।"
    response = "📝 ক্লাস টেস্ট (CT):\n"
    for a in items:
        response += f"• {a['title']} (Date: {a['date']})\n"
    return response

def list_presentations(data):
    items = data.get("Presentation", [])
    if not items:
        return "🎤 কোনো প্রেজেন্টেশন নির্ধারিত নেই।"
    response = "🎤 প্রেজেন্টেশন তালিকা:\n"
    for a in items:
        response += f"• {a['title']} (Date: {a['date']})\n"
    return response

def match_intent(query, data):
    query_lower = query.lower()
    if "অ্যাসাইনমেন্ট" in query or "assignment" in query_lower:
        return "assignment", list_assignments(data)
    elif "ল্যাব" in query or "ল্যাব রিপোর্ট" in query or "lab" in query_lower:
        return "lab", list_lab_reports(data)
    elif "সিটি" in query or "ct" in query_lower:
        return "ct", list_cts(data)
    elif "প্রেজেন্টেশন" in query or "presentation" in query_lower:
        return "presentation", list_presentations(data)
    else:
        return "unknown", "আমি নিশ্চিত না আপনি কী জানতে চাচ্ছেন। আবার বলুন।"

# Load class data
DATA_FILE = "class_schedule_d90.json"
if not os.path.exists(DATA_FILE):
    st.error("Data file not found!")
    st.stop()

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

st.set_page_config(page_title="Cr_Bot", layout="centered")
st.title("🎙️ বাংলা ভয়েস-নির্ভর ভার্চুয়াল সহকারী")
st.markdown("##### ক্লাস রুটিন, 📍 স্যারদের রুম,  Assignment , Lab report")

if st.button("🎧 কথা বলো"):
    with st.spinner("শুনছে..."):
        query = recognize_speech()
    st.write(f"**তুমি বলেছো:** {query}")
    
    intent, response = match_intent(query, data)
    st.success(f"📢 {response}")

st.markdown("---")
st.info("📌 শুধুমাত্র D-90 ব্যাচের জন্য তৈরি।")
