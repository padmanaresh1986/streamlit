import streamlit as st
# -- Page Setup --
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/bar_chart:",
)

dashboard_page = st.Page(
    page="views/dashboard.py",
    title="Dashboard",
    icon=":material/smart_toy:",
)

pg = st.navigation(pages=[about_page, chatbot_page, dashboard_page])
pg.run()
