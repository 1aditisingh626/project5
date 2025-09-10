import streamlit as st
import pandas as pd

def complaint_tracker():
    st.header("🔍 Complaint Tracker")

    submissions = st.session_state.get("submissions", [])
    df = pd.DataFrame(submissions)

    user_id = st.text_input("Enter Complaint ID (row number)")
    if user_id:
        try:
            user_id = int(user_id)
            if 0 <= user_id < len(df):
                st.success("Complaint found:")
                st.json(df.iloc[user_id].to_dict())
            else:
                st.error("❌ Complaint ID not found.")
        except ValueError:
            st.error("Please enter a valid numeric ID.")

    st.markdown("---")
    st.info("Note: Complaint ID is simply the row number in the order you submitted.")
