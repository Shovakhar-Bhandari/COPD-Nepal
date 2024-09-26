import streamlit as st
import pandas as pd
import pickle

with open('Best_Random_Forest_Model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict(input_data):
    input_df = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(input_df)
    return prediction[0]

st.title("COPD Diagnosis Prediction")

age = st.number_input("Age", min_value=0, max_value=120, value=30)
biomass_fuel_exposure = st.selectbox("Biomass Fuel Exposure", [0, 1])
occupational_exposure = st.selectbox("Occupational Exposure", [0, 1])
family_history_copd = st.selectbox("Family History of COPD", [0, 1])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
air_pollution_level = st.number_input("Air Pollution Level", min_value=0, value=50)
respiratory_infections_childhood = st.selectbox("Respiratory Infections in Childhood", [0, 1])
smoking_status_encoded = st.number_input("Smoking Status (Encoded)", min_value=0.0, max_value=1.0, value=0.0)
gender_encoded = st.selectbox("Gender (Encoded)", [0, 1])  


locations = ['Biratnagar', 'Butwal', 'Chitwan', 'Dharan', 'Hetauda', 'Kathmandu', 'Lalitpur', 'Nepalgunj', 'Pokhara']
location_features = {f'Location_{loc}': st.checkbox(f"Location: {loc}") for loc in locations}

age_bmi_interaction = age * bmi

# Prepare the input data for prediction
input_data = {
    'Age': age,
    'Biomass_Fuel_Exposure': biomass_fuel_exposure,
    'Occupational_Exposure': occupational_exposure,
    'Family_History_COPD': family_history_copd,
    'BMI': bmi,
    'Air_Pollution_Level': air_pollution_level,
    'Respiratory_Infections_Childhood': respiratory_infections_childhood,
    'Smoking_Status_encoded': smoking_status_encoded,
    'Gender_encoded': gender_encoded,
    'Age_BMI_Interaction': age_bmi_interaction,
}

for loc in locations:
    input_data[f'Location_{loc}'] = int(location_features[f'Location_{loc}'])

if st.button("Predict"):
    prediction = predict(input_data)
    st.write("Prediction:", "COPD" if prediction == 1 else "No COPD")
