import streamlit as st
from streamlit_option_menu import option_menu
# -- Page Setup --
with st.sidebar:
    selected = option_menu(
        menu_title="My Project",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )
