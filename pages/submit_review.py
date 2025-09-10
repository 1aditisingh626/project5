import streamlit as st

def submit_review():
    st.header("📝 Submit a Review / Complaint")

    with st.form("review_form"):
        product_name = st.text_input("Product Name")
        vendor = st.text_input("Vendor / Brand")
        rating = st.slider("Rating", 1, 5, 3)
        complaint_text = st.text_area("Complaint / Review")
        uploaded_file = st.file_uploader("Upload Image / Document", type=["png", "jpg", "jpeg", "pdf"])
        submitted = st.form_submit_button("Submit")

        if submitted:
            new_entry = {
                "product_name": product_name,
                "vendor": vendor,
                "rating": rating,
                "complaint_text": complaint_text,
                "file_name": uploaded_file.name if uploaded_file else None,
                "status": "Pending"
            }
            if "submissions" not in st.session_state:
                st.session_state["submissions"] = []
            st.session_state["submissions"].append(new_entry)
            st.success("✅ Your complaint / review has been submitted!")
