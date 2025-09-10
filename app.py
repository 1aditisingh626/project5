import sys
import os
from pathlib import Path


# ensure pages folder is importable
sys.path.append(os.path.join(os.path.dirname(__file__), "pages"))


import streamlit as st


from pages.homepage import homepage
from pages.submit_review import submit_review
from pages.complaint_tracker import complaint_tracker
from pages.vendor_dashboard import vendor_dashboard
from pages.analytics_dashboard import analytics_dashboard


PAGES = {
"Homepage": homepage,
"Submit Review/Complaint": submit_review,
"Complaint Tracker": complaint_tracker,
"Vendor / Product Profile": vendor_dashboard,
"Analytics Dashboard": analytics_dashboard,
}


st.set_page_config(page_title="Product Quality Reviews", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", list(PAGES.keys()))


# Run selected page
page_fn = PAGES[choice]
page_fn()