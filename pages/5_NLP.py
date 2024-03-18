import random
import time

import numpy as np
import streamlit as st
from annotated_text import annotated_text
from streamlit.errors import StreamlitAPIException

OPENAI_API_KEY = "YOUR_API_KEY"
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
st.header("NLP & Chatbots")
st.subheader("NLP Applications")

try:
    st.info(
        f"Random seed is **{st.session_state['random_state']}**. Change it on **ML** page if you want.",
        icon="ℹ️",
    )
except KeyError:
    st.error("Random seed was not setted yet, go to the **ML** page!")

st.divider()

st.subheader("Use Streamlit extensions :heart:")
annotated_text(
    "This ",
    ("is", "Verb", "red", "white"),
    " some ",
    ("annotated", "Adj"),
    ("text", "Noun"),
    " for those of ",
    ("you", "Pronoun"),
    " who ",
    ("like", "Verb"),
    " this sort of ",
    ("thing", "Noun"),
    ". ",
    "And here's a ",
    ("word", ""),
    " with a fancy background but no label. ",
    "Check `st-annotated-text` extension!",
)
st.write(
    "Great use case can be to annotate SHAP value attributed to the tokens."
    "Check SHAP explainer for text inputs (BERT example): https://shap.readthedocs.io/en/latest/example_notebooks/api_examples/plots/text.html"
)

video_bytes = open("./utils/shap-text.mov", "rb").read()
st.video(video_bytes)

st.divider()

st.subheader("Random Chatbot")
st.caption("Just use built-in streamlit `chat` components")
st.markdown(
    """
- Check: https://llm-examples.streamlit.app/
- Check: https://streamlit.io/generative-ai
"""
)

# Chatbot

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    assistant_response = random.choice(
        [
            "Hello Pythonista! How can I assist you today?",
            "Hi PyData people! Is there anything I can help you with?",
            "Do you need help?",
            "Now, I'm throwing some random hard-coded texts!",
            "Definitely not AI-powered, hard-code is better. Change my mind!",
        ]
    )
    # Simulate stream of response with milliseconds delay
    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.05)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

# Add assistant response to chat history
st.session_state.messages.append({"role": "ai", "content": full_response})
