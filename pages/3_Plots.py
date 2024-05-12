import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Data | Become A Data Storyteller",
    page_icon="./assets/munich.jpg",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://furkanmtorun.github.io",
        "Report a bug": "https://furkanmtorun.github.io",
        "About": "# Welcome! This is an *extremely* cool app!",
    },
)

st.title("Plots & Charts")
st.caption("Built-in streamlit graphs, Matplotlib, Altair, Vega, Plotly, Bokeh")

# Map
st.subheader("Map")
df_for_map = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)
st.map(df_for_map, latitude="col1", longitude="col2", size="col3", color="col4")

st.divider()

# Charts
st.subheader("Charts/Plots in Tabs")
plotly_chart = px.scatter(
    px.data.gapminder(),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="Life exp. vs GDP Per Capita",
)

bar_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


# Tabs
tab1, tab2, tab3 = st.tabs(
    [
        "Parallel Categories Chart",
        "Plotly Interactive Chart",
        "Streamlit built-in Chart",
    ]
)
with tab1:
    st.plotly_chart(
        px.parallel_categories(
            px.data.tips(),
            dimensions=["sex", "smoker", "day"],
            color="size",
            color_continuous_scale=px.colors.sequential.Sunset,
            labels={
                "sex": "Payer sex",
                "smoker": "Smokers at the table",
                "day": "Day of week",
            },
        )
    )
with tab2:
    st.plotly_chart(plotly_chart, theme="streamlit", use_container_width=True)
with tab3:
    st.bar_chart(bar_chart_data)
