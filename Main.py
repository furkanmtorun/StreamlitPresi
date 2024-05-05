import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Data Storyteller @furkanmtorun",
    page_icon="./assets/prague.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://furkanmtorun.github.io",
        "Report a bug": "https://furkanmtorun.github.io",
        "About": "# Welcome! This is an *extremely* cool web app!",
    },
)

st.title("Become a data storyteller with :red[Streamlit]!")
st.write("Our true mentor in life is science. - `Atatürk`")

st.divider()

image = Image.open("./assets/prague_city.jpg")
st.image(
    image, caption="Pictures are awesome like Prague.",
)

st.divider()

st.subheader("Few metrics with 3 columns")
col1, col2, col3 = st.columns(3, gap="small")
col1.metric("Temperature", "20 °C", "1.2 °C")
col2.metric("Wind", "5 kmh", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()

st.subheader("Other layouts and expander")
st.latex(r"""rmse = \sqrt{(\frac{1}{n})\sum_{i=1}^{n}(y_{i} - x_{i})^{2}}""")

with st.expander("Code block syntax highlighted and expander"):
    code = """def hello():
        print("Our true mentor in life is science. - Atatürk")"""
    st.code(code, language="python", line_numbers=True)


st.divider()

st.subheader("Colorful texts")
st.markdown(
    """
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors]."""
)
st.info("This is a purely informational message", icon="ℹ️")
st.error("This is an error", icon="🚨")
st.warning("This is a warning", icon="⚠️")
st.success("Thanks for waiting!", icon="✅")
