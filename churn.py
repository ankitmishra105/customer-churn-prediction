import streamlit as st
import joblib
import numpy as np


model = joblib.load('random_forest_model.pkl')


st.markdown("""
    <style>
        body {
            background-image: linear-gradient(to right top, #e0eafc, #cfdef3);
            background-size: cover;
            background-attachment: fixed;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1, h2, h3, h4 {
            color: #000000;
            text-align: center;
        }
        label {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="glass-card"><h1>🔮 Customer Churn Prediction</h1>', unsafe_allow_html=True)


with st.form("input_form"):
    st.markdown("### 📋 Enter Customer Details")

    CreditScore = st.number_input("Credit Score", 300, 1000, 650)
    Geography = st.selectbox("Geography", ['France', 'Germany', 'Spain'])
    Gender = st.selectbox("Gender", ['Male', 'Female'])
    Age = st.slider("Age", 18, 92, 35)
    Tenure = st.slider("Tenure (Years)", 0, 10, 5)
    Balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
    NumOfProducts = st.slider("Number of Products", 1, 4, 1)
    HasCrCard = st.selectbox("Has Credit Card", [0, 1])
    IsActiveMember = st.selectbox("Is Active Member", [0, 1])
    EstimatedSalary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

    submitted = st.form_submit_button("🚀 Predict")


if submitted:
    geo_map = {'France': 0, 'Germany': 1, 'Spain': 2}
    gender_map = {'Male': 1, 'Female': 0}

    input_data = np.array([[
        CreditScore,
        geo_map[Geography],
        gender_map[Gender],
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        HasCrCard,
        IsActiveMember,
        EstimatedSalary
    ]])

 
    prediction = model.predict(input_data)[0]

   
    if prediction == 1:
        st.error("⚠️ This customer is likely to **churn**.")
    else:
        st.success("✅ This customer is likely to **stay**.")
