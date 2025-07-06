import streamlit as st
from google.cloud import firestore
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")  

st.set_page_config(page_title="AuditAI Config", layout="centered")

st.title("⚙️ AuditAI Configuration")

st.subheader("LLM Settings")
llm_choice = st.selectbox("LLM Backend", ["Together AI", "OpenAI"])
st.text_input("API Key", type="password")

st.subheader("Firestore Connectivity")
if st.button("Test Firestore"):
    try:
        db = firestore.Client()
        docs = db.collection("audit_results").limit(1).stream()
        st.success("✅ Firestore connection successful")
    except Exception as e:
        st.error(f"❌ Firestore failed: {e}")
