import streamlit as st
import pandas as pd

# This page reads from a shared session_state store called 'submissions'.
# For a production app, connect to a real database.

def homepage():
    st.header("🏠 Product Quality Review Platform")
    st.markdown("A simple platform to submit and track product complaints and view analytics.")

    submissions = st.session_state.get('submissions', [])
    df = pd.DataFrame(submissions)

    left, right = st.columns([3, 1])

    with left:
        st.subheader("Trending Products")
        if df.empty:
            st.info("No submissions yet — go to 'Submit Review/Complaint' to add one.")
        else:
            top = df['product_name'].value_counts().reset_index()
            top.columns = ['product_name', 'count']
            st.table(top.head(10))

        st.subheader("Most Common Complaints")
        if not df.empty and 'complaint_text' in df.columns:
            complaints = df['complaint_text'].str.split().explode().value_counts().head(20)
            st.table(complaints)

    with right:
        st.subheader("Quick Actions")
        if st.button("Submit a Review/Complaint"):
            st.experimental_set_query_params(page='submit')

        st.write("\n\n")
        st.metric("Total Submissions", len(submissions))
