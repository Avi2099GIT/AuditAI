# utils/firestore_utils.py

import os
import pandas as pd
from google.cloud import firestore
import streamlit as st
from dotenv import load_dotenv
#from pathlib import Path

load_dotenv()

print("Loaded creds path:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

def get_firestore_client():
    # Ensure the credentials are loaded
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # Fallback hardcoded path (your key path)
    if not cred_path:
        cred_path = "F:/mmm projects/auditai-secure/keys/sigma-composite-465019-q5-4747b19a78af.json"
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path

    if not os.path.exists(cred_path):
        raise ValueError("Firestore credentials not found.")

    return firestore.Client()

@st.cache_data(ttl=60)  # Cache expires after 60 seconds. Adjust as needed.
def load_all_issues():
    client = get_firestore_client()
    collection = client.collection("audit_results")
    docs = collection.stream()

    records = []
    for doc in docs:
        records.append(doc.to_dict())

    df = pd.DataFrame(records)

    # Ensure required columns exist (prevent chart crash)
    required_columns = ["severity", "confidence", "type", "file", "project_name", "commit_hash", "timestamp","repo"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = "unknown"

    return df   
