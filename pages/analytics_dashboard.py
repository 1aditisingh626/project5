import streamlit as st
import pandas as pd
import altair as alt

def analytics_dashboard():
    st.header("📊 Analytics Dashboard")

    submissions = st.session_state.get("submissions", [])
    df = pd.DataFrame(submissions)

    if df.empty:
        st.info("No data available yet.")
        return

    st.subheader("Top Offending Products")
    top_products = df["product_name"].value_counts().reset_index()
    top_products.columns = ["product_name", "count"]
    st.bar_chart(top_products.set_index("product_name").head(10))

    st.subheader("Ratings Distribution")
    rating_counts = df["rating"].value_counts().reset_index()
    rating_counts.columns = ["rating", "count"]
    chart = alt.Chart(rating_counts).mark_bar().encode(
        x="rating:O",
        y="count:Q"
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Complaint Trends (by Submission Order)")
    df["submission_index"] = range(len(df))
    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x="submission_index",
        y="rating",
        tooltip=["product_name", "rating", "status"]
    )
    st.altair_chart(line_chart, use_container_width=True)
