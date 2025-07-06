import streamlit as st
import pandas as pd
from utils.firestore_utils import load_all_issues

st.set_page_config(page_title="AuditAI Results", layout="wide")

st.title("📝 Scan Results")

data = load_all_issues()

if data.empty:
    st.warning("No issues found or Firestore not connected.")
else:
    with st.sidebar:
        st.header("🔎 Filters")
        repo = st.selectbox("Repo", ["All"] + sorted(data["repo"].unique().tolist()))
        severity = st.multiselect("Severity", sorted(data["severity"].unique()))
        confidence = st.multiselect("Confidence", sorted(data["confidence"].unique()))

    filtered = data.copy()
    if repo != "All":
        filtered = filtered[filtered["repo"] == repo]
    if severity:
        filtered = filtered[filtered["severity"].isin(severity)]
    if confidence:
        filtered = filtered[filtered["confidence"].isin(confidence)]

    st.dataframe(filtered, use_container_width=True)