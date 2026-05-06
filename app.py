import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Trust & Safety Escalation Review System",
    layout="wide"
)

st.title("🚨 Trust & Safety Escalation Review System")

st.markdown("""
This system simulates a real-world escalation review workflow used in Trust & Safety operations.
""")

# Sample escalation cases
cases = [
    {
        "comment": "너 같은 인간은 없어져야 해",
        "risk_score": 88,
        "category": "Indirect Threat",
        "status": "Pending Review"
    },
    {
        "comment": "오늘 날씨 좋다",
        "risk_score": 5,
        "category": "Safe",
        "status": "Allow"
    },
    {
        "comment": "죽여버릴거야",
        "risk_score": 95,
        "category": "Violence / Threat",
        "status": "Escalated"
    }
]

df = pd.DataFrame(cases)

st.subheader("📋 Escalation Queue")
st.dataframe(df, use_container_width=True)

st.subheader("📝 Moderator Review")

selected_comment = st.selectbox(
    "Select a comment for review",
    df["comment"]
)

moderator_note = st.text_area(
    "Moderator Notes",
    placeholder="Write review notes here..."
)

decision = st.radio(
    "Final Decision",
    ["Allow", "Review", "Remove", "Escalate"]
)

if st.button("Submit Review"):
    st.success(f"Decision submitted: {decision}")

st.subheader("📊 Escalation Analytics")

st.metric("Pending Cases", 3)
st.metric("Escalated Cases", 1)
st.metric("High Risk Cases", 2)

st.markdown("---")

st.markdown("""
### 🔍 Key Features
- Escalation queue management
- Moderator review workflow
- Risk score analysis
- Final enforcement decision simulation
- Trust & Safety operational dashboard
""")
