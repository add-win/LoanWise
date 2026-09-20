import streamlit as st
import joblib
import pandas as pd

model = joblib.load("loan_approval_decision_tree.pkl")

st.title("Loan Approval Prediction")

income = st.number_input(
    "Enter the Income",
    min_value=1.0,
    value=1.0,
    step=1.0
)

credit = st.number_input(
    "Enter the Credit Score",
    min_value=1.0,
    value=1.0,
    step=1.0
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Income": [income],
        "Credit_Score": [credit]
    })

    prediction = model.predict(input_data)

    if prediction:
        st.success("🎉 Loan Approved!")
    else:
        st.error("❌ Loan not Approved!")
