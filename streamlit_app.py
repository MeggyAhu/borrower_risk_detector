import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


st.title("Borrower Risk Detector App")
st.write(
    "This App dectects borrowers who are likely to default"
)




#sidebar for user input
st.sidebar.header("Enter the Borrower's Information")
log_annual_inc = st.sidebar.number_input("Log of Annual Income", min_value=0.0, step =10000.0)
int_rate = st.sidebar.number_input("Interest Rate", min_value=0.2, format = "%.1f")
revol_util = st.sidebar.number_input("Revolving Utilization", min_value=0.1, step =0.1, format = "%.1f")
installment = st.sidebar.number_input("Installment", min_value=0.0, step = 1000.0)
revol_bal_to_income = st.sidebar.number_input("Revolving Balance to Income", min_value=0.1, step = 1000.0)
inq_last_6mths = st.sidebar.number_input("Inquiry in Last 6months", min_value=0.0, step = 1000.0)
income_to_debt_ratio = st.sidebar.number_input("Income to Debt Ratio", min_value=0.1, step = 1000.0)
fico = st.sidebar.number_input("FICO Score", min_value=0.0, step = 1.0, format = "%.1f")
Credit_age = st.sidebar.number_input("Credit Age (in years)", min_value=0.0, step = 1.0)
credit_policy = st.sidebar.selectbox("Credit Policy", options =["Meets Policy", "Does not Meet Policy"])

#Mapping credit policy to numerical values
credit_policy_value = 1.0 if credit_policy == "Meets Policy" else 0.0

#Create a DataFrame with the user input
input_data = pd.DataFrame({
    'log_annual_inc': [log_annual_inc],
    'int_rate': [int_rate],
    'revol_util': [revol_util],
    'installment': [installment],
    'revol_bal_to_income': [revol_bal_to_income],
    'inq_last_6mths': [inq_last_6mths],
    'income_to_debt_ratio': [income_to_debt_ratio],
    'fico': [fico],
    'Credit_age': [Credit_age],
    'credit_policy (1=Meets, 0=Does Not Meet)' :[credit_policy_value]
})

# Display the input data as a table
st.subheader("User Input Data")
st.table(input_data)



# Make prediction
st.header("Prediction Results")
if st.button("Predict"):
    prediction = model.predict(input_data_scaled)
    prediction_proba = model.predict_proba(input_data_scaled)[0][1]
    
    # Display the prediction result
    if prediction[0] == 1:
        st.error("The borrower is likely to default on the loan.")
    else:
        st.success("The borrower is likely to repay the loan.")
    
    # Display the prediction probability
    st.subheader("Prediction Probability")
    st.write(f"Probability of Default: {prediction_proba:.2f}")
    st.write(f"Probability of No Default: {prediction_proba:.2f}")
