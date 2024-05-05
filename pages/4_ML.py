import time

import streamlit as st

from utils.ml_utils import *

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

# Sidebar
try:
    st.session_state["random_state"] = st.sidebar.slider(
        "Random state:",
        min_value=1,
        max_value=42,
        value=st.session_state["random_state"],
        step=1,
        help="This will be available during the session and across the pages",
    )
except KeyError:
    st.session_state["random_state"] = st.sidebar.slider(
        "Random state:",
        min_value=1,
        max_value=42,
        value=23,
        step=1,
        help="This will be available during the session and across the pages",
    )

st.header("ML")
st.info(":information_source: Configure your model settings from the left sidebar")
ml_selections = {}
ml_selections["random_state"] = st.session_state["random_state"]

# Sidebar
ml_selections["n_estimators"] = st.sidebar.number_input(
    "Number of estimators", min_value=1, value=200, max_value=500, step=50
)


# Train model
with st.form("Train model", clear_on_submit=False):
    st.subheader("Train model")
    st.write(
        f"XGBoost model will be trained with `{ml_selections['n_estimators']}`"
        f"estimators and random state of `{ml_selections['random_state']}`."
    )
    ml_selections["model_name"] = st.text_input("Model name", value="iris_xgb_model")
    ml_selections["test_size"] = st.slider(
        "Test size",
        min_value=0.1,
        max_value=0.6,
        value=0.2,
        step=0.1,
    )
    train_model_button = st.form_submit_button("Train XGBoost model for Iris dataset")

    if train_model_button:
        with st.status("Model training status", expanded=True) as model_training_status:
            model_training_status.update(
                label="Loading data and train/test splitting",
                state="running",
                expanded=False,
            )
            time.sleep(0.5)
            X_train, X_test, y_train, y_test = load_data(
                test_size=ml_selections["test_size"],
                random_state=(
                    ml_selections["random_state"]
                    if ml_selections["random_state"]
                    else 23
                ),
            )
            model_training_status.update(
                label="Training the model", state="running", expanded=False
            )
            model_name = train_and_save_model(
                X_train,
                X_test,
                y_train,
                y_test,
                ml_selections["n_estimators"],
                ml_selections["model_name"],
            )
            model_training_status.update(
                label="Model saved", state="complete", expanded=False
            )
            time.sleep(0.2)
            st.success(f"Your model {model_name} trained and saved!")


# Models
list_of_models = list_the_models()

# Feature importance
st.divider()
st.subheader("Investigate model")
if len(list_of_models) > 0:
    st.caption("Select the model you trained and check the model")
    ml_selections["model_selected"] = st.selectbox(
        "Select the model", options=list_of_models
    )
    load_feat_imp(ml_selections["model_selected"])
else:
    st.warning("You have to train a model to investigate", icon="⚠️")
st.divider()


# Predict with model
st.subheader("Predict with the model")
if len(list_of_models) > 0:
    with st.form("Iris XGB Model", clear_on_submit=False):
        model_selected = st.selectbox("Select the model", options=list_of_models)
        col1, col2 = st.columns(2)
        with col1:
            st.text("Sepal characteristics")
            sepal_l = st.slider("Sepal lenght (cm)", 1.0, 8.0, 0.5)
            sepal_w = st.slider("Sepal width (cm)", 2.0, 4.4, 0.5)
        with col2:
            st.text("Petal characteristics")
            petal_l = st.slider("Petal lenght (cm)", 1.0, 7.0, 0.5)
            petal_w = st.slider("Petal width (cm)", 0.1, 2.5, 0.5)

        model_predict_button = st.form_submit_button("Predict")
        if model_predict_button:
            pred_result = predict_model(
                model_selected, sepal_l, sepal_w, petal_l, petal_w
            )
            st.success(f"Model prediction: **{pred_result.upper()}**")
else:
    st.warning("You have to train a model to investigate", icon="⚠️")
