import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(layout="wide", page_title="Real Estate Market Analysis")


show_pages(
    [
        Page("streamlit_app.py", "Project description", "💻"),
        Page("pages/page_houses.py", "Houses", "🏡"),
        Page("pages/page_lands.py", "Lands", "🌳"),
        Page("pages/page_apartments.py", "Apartments", "🏢")
    ]
)

st.markdown("Data loaded")
