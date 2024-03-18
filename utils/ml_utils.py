from datetime import datetime, timezone
from glob import glob

import numpy as np
import pandas as pd
import streamlit as st
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


# Model training
@st.cache_data
def load_data(test_size, random_state):
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def train_and_save_model(X_train, X_test, y_train, y_test, n_estimators, model_name):
    clf = XGBClassifier(n_estimators=n_estimators)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # print(metrics.accuracy_score(y_test, y_pred))

    # Save the model
    now = datetime.now(tz=timezone.utc)
    now_formatted = now.strftime("%d-%m%-Y_%H-%M-%S")
    model_name = f"{model_name}-{now_formatted}"
    clf.save_model(f"./utils/{model_name}.json")
    return model_name


def list_the_models():
    return glob("./utils/*.json")


@st.cache_data
def load_the_model(model_selected):
    clf = XGBClassifier()
    clf.load_model(model_selected)
    return clf


def load_feat_imp(model_selected):
    model = load_the_model(model_selected)
    feat_importances_df = pd.DataFrame(
        model.feature_importances_, index=datasets.load_iris().feature_names
    )
    fig = feat_importances_df.plot(
        kind="barh", title=f"Top features for {model_selected}", legend=False
    ).figure
    st.pyplot(fig)


def predict_model(model_selected, sepal_l, sepal_w, petal_l, petal_w):
    model = load_the_model(model_selected)
    result_index = model.predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
    return datasets.load_iris().target_names[result_index][0]


# In case it does not work:
# train_and_save_model(*load_data(0.2, 23))
