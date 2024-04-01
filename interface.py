import numpy as np
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
from joblib import load
rfc = load('rfc_model.joblib')

# Function to predict using the trained model
def predict(age, gender, marital_status, occupation, income, education, family_size, pin_code, review):
    features = np.array([[age, gender, marital_status, occupation, income, education, family_size, pin_code, review]])
    prediction = rfc.predict(features)
    return prediction[0]

st.title("ONLINE FOOD ORDER PREDICTION")

# User inputs
age = st.number_input("Age of the Customer", min_value=0, max_value=150, value=30)
gender = st.selectbox("Gender", ["Female", "Male"])
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Not Revealed"])
occupation = st.selectbox("Occupation", ["Student", "Employee", "Self Employed", "Housewife"])
income = st.number_input("Monthly Income", min_value=0, max_value=1000000, value=15000)
education = st.selectbox("Educational Qualification", ["Graduate", "Post Graduate", "Ph.D", "School", "Uneducated"])
family_size = st.number_input("Family Size", min_value=1, max_value=20, value=3)
pin_code = st.number_input("Pin Code", min_value=560001, max_value=560110, value=560001)
review = st.selectbox("Review of the Last Order", ["Negative", "Positive"])

# Convert categorical inputs to numerical
gender = 1 if gender == "Male" else 0
marital_status_dict = {"Single": 1, "Married": 2, "Not Revealed": 3}
marital_status = marital_status_dict[marital_status]
occupation_dict = {"Student": 1, "Employee": 2, "Self Employed": 3, "Housewife": 4}
occupation = occupation_dict[occupation]
education_dict = {"Graduate": 3, "Post Graduate": 4, "Ph.D": 5, "School": 2, "Uneducated": 1}
education = education_dict[education]
review = 1 if review == "Positive" else 0

# Predict button
if st.button("Predict"):
    prediction = predict(age, gender, marital_status, occupation, income, education, family_size, pin_code, review)
    st.write("# Will order again:", prediction)
