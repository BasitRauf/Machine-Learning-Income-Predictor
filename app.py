import streamlit as st
import requests

st.set_page_config(page_title="Income Prediction App")

st.title("💰 Adult Income Prediction")

st.write("Enter User Information")

# =========================
# INPUTS
# =========================

age = st.number_input("Age", min_value=1)

workclass = st.selectbox(
    "Workclass",
    ["Private", "Self-emp-not-inc", "Local-gov", "State-gov"]
)

fnlwgt = st.number_input("fnlwgt", min_value=0)

education = st.selectbox(
    "Education",
    ["Bachelors", "HS-grad", "Masters", "Some-college"]
)

educational_num = st.number_input("Educational Number", min_value=1)

marital_status = st.selectbox(
    "Marital Status",
    ["Never-married", "Married-civ-spouse", "Divorced"]
)

occupation = st.selectbox(
    "Occupation",
    ["Tech-support", "Craft-repair", "Sales", "Exec-managerial"]
)

relationship = st.selectbox(
    "Relationship",
    ["Not-in-family", "Husband", "Wife", "Own-child"]
)

race = st.selectbox(
    "Race",
    ["White", "Black", "Asian-Pac-Islander"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

capital_gain = st.number_input("Capital Gain", min_value=0)

capital_loss = st.number_input("Capital Loss", min_value=0)

hours_per_week = st.number_input("Hours Per Week", min_value=1)

native_country = st.selectbox(
    "Native Country",
    ["United-States", "India", "Pakistan", "Canada"]
)

# =========================
# PREDICT BUTTON
# =========================

if st.button("Predict Income"):

    data:dict = {

        "age": age,

        "workclass": workclass,

        "fnlwgt": fnlwgt,

        "education": education,

        "educational-num": educational_num,

        "marital-status": marital_status,

        "occupation": occupation,

        "relationship": relationship,

        "race": race,

        "gender": gender,

        "capital-gain": capital_gain,

        "capital-loss": capital_loss,

        "hours-per-week": hours_per_week,

        "native-country": native_country
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    prediction = result['prediction']

    if prediction == 1:
        st.success("Income is predicted <=50K")
    else:
        st.success("Income is predicted >50K")