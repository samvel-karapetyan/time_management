import streamlit as st
from src import CalendarManager


st.title("Խելացի Ժամանակի կառավարում")

manager = CalendarManager()
events = manager.get_events()

# event = Task()

# event.to_markdown() -> "*type* - *date* - *time* - *description*"

for event in events:
    st.markdown(event.to_markdown())