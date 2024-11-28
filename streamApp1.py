import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model (make sure the model is saved first using joblib.dump)
model = joblib.load('trained_model.pkl')

# Define the Streamlit form for user inputs
st.title("Financial Inclusion Prediction")
st.write("Enter the features below to predict the likelihood of having a bank account.")

country = st.selectbox('COUNTRY', ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
locationType = st.selectbox('LOCATION', ['Rural', 'Urban'])
cellphone = st.selectbox('CELL PHONE', ['No', 'Yes'])
numberOfPeople = st.number_input('HOUSEHOLD SIZE', min_value=1, max_value=20, step=1)
age = st.number_input('AGE', min_value=18, max_value=100, step=1)
gender = st.selectbox('GENDER', ['Female', 'Male'])
relationship = st.selectbox('RELATIONSHIP', ['Child', 'Head of Household', 'Other non-relative', 'Other relative', 'Parent', 'Spouse'])
status = st.selectbox('MARITAL STATUS', ['Divorced/Seperated', "Don't know", 'Married/Living together', 'Single/Never Married', 'Widowed'])
education = st.selectbox('EDUCATION LEVEL', ['Secondary education', 'No formal education', 'Vocational/Specialised training', 'Primary education', 'Tertiary education', 'Other/Dont know/RTA'])	
job = st.selectbox('JOB TYPE', ['Self employed', 'Government Dependent', 'Formally employed Private', 'Informally employed',
       'Formally employed Government', 'Farming and Fishing', 'Remittance Dependent', 'Other Income', 'Dont Know/Refuse to answer', 'No Income'])

# Convert categorical variables to numerical
country = {'Kenya': 0, 'Rwanda': 1, 'Tanzania':2, 'Uganda':3}[country]
locationType = {'Rural': 0, 'Urban': 1}[locationType]
cellphone = {'No': 0, 'Yes': 1}[cellphone]
gender = 0 if gender == 'Male' else 1
relationship = {'Child': 0, 'Head of Household': 1, 'Other non-relative': 2, 'Other relative': 3, 'Parent': 4, 'Spouse': 5}[relationship]
status = {'Divorced/Seperated': 0, "Don't know": 1, 'Married/Living together': 2, 'Single/Never Married': 3, 'Widowed': 4}[status]
education = {'Secondary education': 3, 'No formal education': 0, 'Vocational/Specialised training': 5, 'Primary education': 2, 'Tertiary education': 4, 'Other/Dont know/RTA': 1}[education]
job = {'Self employed': 0, 'Government Dependent': 4, 'Formally employed Private': 3, 'Informally employed' : 5,
       'Formally employed Government': 2, 'Farming and Fishing': 1, 'Remittance Dependent': 8, 'Other Income': 7, 'Dont Know/Refuse to answer': 0, 'No Income': 6}[job]

# Create input feature vector
input_features = np.array([[country, locationType, cellphone, numberOfPeople, age, gender, relationship, status, education, job]])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_features)
    st.write("Prediction: ", "Has Bank Account" if prediction == 1 else "Doesn't Have Bank Account")