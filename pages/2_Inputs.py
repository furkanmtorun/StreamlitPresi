import time
from typing import Any, Dict

import streamlit as st

st.set_page_config(
    page_title="Data Storyteller @furkanmtorun",
    page_icon="./assets/prague.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://furkanmtorun.github.io",
        "Report a bug": "https://furkanmtorun.github.io",
        "About": "# Welcome! This is an *extremely* cool app!",
    },
)

st.header("Input elements / callbacks")

# To collect all the user selections
user_selections: Dict[str, Any] = {}

st.warning(":warning: Based on your version selection, the form will be updated.")
user_selections["build_state"] = st.radio(
    "Pick the build state",
    ["Stable", "Beta"],
    index=1,
    horizontal=True,
    key="build_state",
)

if user_selections["build_state"] == "Stable":
    user_selections["version"] = st.session_state.version = st.radio(
        "Pick the version", ["v.1.1", "v.1.0"], index=0, horizontal=True
    )
elif user_selections["build_state"] == "Beta":
    user_selections["version"] = st.session_state.version = st.radio(
        "Pick the version",
        ["v.1.2"],
        index=0,
        horizontal=True,
    )


st.markdown("<br>", unsafe_allow_html=True)

with st.form("Form", clear_on_submit=False):
    st.write(
        f"Register Form with :rainbow[{user_selections['version']} ({user_selections['build_state']})]"
    )
    user_selections["name"] = st.text_input("Name", placeholder="Furkan", key="name")
    user_selections["favorite_city"] = st.selectbox(
        "Favorite city", options=["İstanbul", "Prague", "Munich"]
    )
    if user_selections["version"] == "v.1.2":
        user_selections["favorite_colors"] = st.multiselect(
            "Favorite color(s)",
            ["Green", "Yellow", "Red", "Blue", "White"],
            ["Red", "White"],
        )
        user_selections["activate_beta_features"] = st.toggle(
            "Activate beta features", help="This is handy information that can aid you."
        )
        user_selections["birthday"] = st.date_input(
            "When's your birthday", format="DD/MM/YYYY"
        )
    form_submit = st.form_submit_button("Register")

    if form_submit:
        with st.status("Working on the data...", expanded=False) as status:
            status.update(
                label="Performing data validation", state="running", expanded=False
            )
            time.sleep(0.5)
            status.update(label="Data is validated", state="running", expanded=False)
            time.sleep(0.5)
            status.update(label="Connecting to the DB", state="running", expanded=False)
            time.sleep(0.5)
            status.update(
                label="Registeration is complete!", state="complete", expanded=False
            )
            time.sleep(0.5)
        st.success(
            f"Welcome aboard **{user_selections['name']}** on {user_selections['build_state']} version!"
        )
        st.write("Here is your selections:")
        st.json(user_selections)
