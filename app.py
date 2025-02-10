import streamlit as st
from src import CalendarManager, Event


st.set_page_config(layout="wide")
st.title("Խելացի Ժամանակի կառավարում")

manager = CalendarManager()
events = manager.get_events()

input_container, button = st.columns([5, 1])

add_event = button.button(label="Ավելացնել")

type_radio, description_input = input_container.columns([2, 5])

selected_type = type_radio.radio(
    label=" ",
    label_visibility="collapsed",
    options=["Առաջադրանք", "Հանդիպում"],
    index=None
)

description = description_input.text_area(
    label=" ",
    placeholder="Նկարագրություն",
    label_visibility="collapsed"
)

if selected_type:
    manager.display_input(selected_type, input_container)

if add_event and selected_type:
    manager.create_event_from_input(selected_type, description)

for i, event in enumerate(events):
    st.checkbox(
        label=event.to_markdown(), 
        value=event.is_done(), 
        on_change=manager.create_event_changer(event),
        key=f"event_{i}",
    )