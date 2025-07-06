import streamlit as st
import pandas as pd
import plotly.express as px
from utils.firestore_utils import load_all_issues

st.set_page_config(page_title="AuditAI Dashboard", layout="wide")

st.title("🚨 AuditAI - Dashboard")
st.markdown("Get a quick overview of your codebase security status.")

data = load_all_issues()

if not data.empty:
    st.subheader("🔍 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total PRs Scanned", data["commit_hash"].nunique())
    col2.metric("Total Issues", len(data))
    col3.metric("High Severity Issues", (data["severity"] == "HIGH").sum())

    st.subheader("📈 Issues by Severity")
    severity_chart = data["severity"].value_counts().reset_index()
    fig1 = px.bar(severity_chart, x="severity", y="count", labels={"severity": "Severity", "count": "Count"})
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📉 Issue Confidence Levels")
    if "confidence" in data.columns:
        color_discrete_map = {"HIGH": "red", "MEDIUM": "orange", "LOW": "green"}
        confidence_chart = data["confidence"].value_counts().reset_index()
        confidence_chart.columns = ["confidence", "count"]
        fig2 = px.pie(confidence_chart, names="confidence", values="count", title="Confidence Breakdown")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("⚠️ No confidence data found in Firestore records.")

    st.subheader("🏷️ Issues by Project")
    project_chart = data["project_name"].value_counts().reset_index()
    fig3 = px.bar(
    project_chart,
    x="project_name",
    y="count",
    labels={"project_name": "Project", "count": "Issues"},
    title="📁 Issues by Project"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📅 Scan Timeline")
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    timeline = data.groupby(data["timestamp"].dt.date).size().reset_index(name="count")
    fig4 = px.line(timeline, x="timestamp", y="count", title="📅 Scan Timeline")
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("🧠 Analysis Type Distribution")
    if "type" in data.columns:
        type_chart = data["type"].value_counts().reset_index()
        fig5 = px.pie(
        data,
        names="type",
        title="🧠 Analysis Type Distribution",
        color_discrete_sequence=px.colors.qualitative.Pastel
        )

        st.plotly_chart(fig5, use_container_width=True)

    st.subheader("🧾 Raw Issues Table")
    st.dataframe(data.sort_values(by="timestamp", ascending=False), use_container_width=True)
    st.download_button("📥 Download Issues CSV", data.to_csv(index=False), "auditai_issues.csv")


    top_files = data["file"].value_counts().head(5).reset_index()
    top_files.columns = ["File", "Issue Count"]
    st.subheader("🐍 Top Offending Files")
    st.dataframe(top_files)






else:
    st.info("No audit data found. Connect Firestore or run a scan.")