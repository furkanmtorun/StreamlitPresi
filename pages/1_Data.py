import random
import time
from datetime import date

import numpy as np
import pandas as pd
import streamlit as st
from faker import Faker

st.set_page_config(
    page_title="Data | Become A Data Storyteller",
    page_icon="./assets/prague.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://furkanmtorun.github.io",
        "Report a bug": "https://furkanmtorun.github.io",
        "About": "# Welcome! This is an *extremely* cool app!",
    },
)
st.title("Dataframes and Editors")
st.caption("Play with data: sort, edit, engage, remove, add")


@st.cache_data
def get_profile_dataset(number_of_items: int = 100, seed: int = 0) -> pd.DataFrame:
    new_data = []

    def calculate_age(born):
        today = date.today()
        return (
            today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        )

    fake = Faker()
    random.seed(seed)
    Faker.seed(seed)

    for i in range(number_of_items):
        profile = fake.profile()
        new_data.append(
            {
                "avatar": f"https://picsum.photos/400/200?lock={i}",
                "name": profile["name"],
                "age": calculate_age(profile["birthdate"]),
                "active": random.choice([True, False]),
                "daily_activity": np.random.rand(25),
                "homepage": profile["website"][0],
                "email": profile["mail"],
                "activity": np.random.randint(2, 90, size=25),
                "gender": random.choice(["male", "female", "other", None]),
                "birthdate": profile["birthdate"],
                "status": round(random.uniform(0, 1), 2),
            }
        )

    profile_df = pd.DataFrame(new_data)
    profile_df["gender"] = profile_df["gender"].astype("category")
    return profile_df


column_configuration = {
    "name": st.column_config.TextColumn(
        "Name", help="The name of the user", max_chars=100
    ),
    "avatar": st.column_config.ImageColumn("Avatar", help="The user's avatar"),
    "active": st.column_config.CheckboxColumn("Is Active?", help="Is the user active?"),
    "homepage": st.column_config.LinkColumn(
        "Homepage", help="The homepage of the user"
    ),
    "gender": st.column_config.SelectboxColumn(
        "Gender", options=["male", "female", "other"]
    ),
    "age": st.column_config.NumberColumn(
        "Age", min_value=0, max_value=120, format="%d years", help="The user's age",
    ),
    "activity": st.column_config.LineChartColumn(
        "Activity (1 year)",
        help="The user's activity over the last 1 year",
        width="large",
        y_min=0,
        y_max=100,
    ),
    "daily_activity": st.column_config.BarChartColumn(
        "Activity (daily)",
        help="The user's activity in the last 25 days",
        width="medium",
        y_min=0,
        y_max=1,
    ),
    "status": st.column_config.ProgressColumn(
        "Status", min_value=0, max_value=1, format="%.2f"
    ),
    "birthdate": st.column_config.DateColumn(
        "Birthdate", help="The user's birthdate", min_value=date(1920, 1, 1),
    ),
    "email": st.column_config.TextColumn(
        "Email",
        help="The user's email address",
        validate="^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
    ),
}

profile_df = get_profile_dataset(number_of_items=100)


@st.cache_data
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


# Date editor
st.subheader("Data editor")
st.data_editor(
    profile_df, column_config=column_configuration, hide_index=True, num_rows="dynamic",
)
st.download_button(
    label=":floppy_disk: Download data as CSV",
    data=convert_df_to_csv(profile_df),
    file_name="profile_df.csv",
    mime="text/csv",
)

if st.button(":recycle: Check for updates on data"):
    # Progress bar for updates
    progress_text = "Update in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()

    # Toast -- Notification
    st.toast("Data is up-to-date!", icon="🎉")
    st.balloons()
    time.sleep(0.5)


st.divider()

st.subheader("Data table")
st.table(profile_df[["name", "age", "active"]].sample(5))
