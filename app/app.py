import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

# -------------------------
# Load Model
# -------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "Models")

model = joblib.load(os.path.join(MODEL_DIR, "logistic_heart.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
expected_columns = joblib.load(os.path.join(MODEL_DIR, "columns.pkl"))

# -------------------------
# Title
# -------------------------

st.title("❤️ Heart Disease Prediction System")
st.markdown("Enter patient health details to estimate heart disease risk.")

# -------------------------
# Inputs
# -------------------------

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)

with col2:
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Heart Disease Risk"):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    # Base model prediction
    probs = model.predict_proba(scaled_input)[0]
    healthy_prob = probs[0] * 100
    disease_prob = probs[1] * 100

    # -------------------------
    # Clinical Risk Adjustment
    # -------------------------

    risk_flags = 0

    if resting_bp >= 140:
        risk_flags += 1

    if cholesterol >= 240:
        risk_flags += 1

    if max_hr < 120:
        risk_flags += 1

    if oldpeak > 2:
        risk_flags += 1

    if fasting_bs == 1:
        risk_flags += 1

    if exercise_angina == "Y":
        risk_flags += 1

    if resting_ecg == "LVH":
        risk_flags += 1

    if st_slope == "Down":
        risk_flags += 1

    # Increase risk slightly per abnormal indicator
    adjustment = risk_flags * 3

    adjusted_risk = min(disease_prob + adjustment, 100)
    adjusted_healthy = 100 - adjusted_risk

    # -------------------------
    # Risk Level
    # -------------------------

    if adjusted_risk < 20:
        risk_level = "Low"
    elif adjusted_risk < 50:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    # -------------------------
    # Result
    # -------------------------

    st.subheader("Prediction Result")

    if risk_level == "High":
        st.error(f"⚠️ High Risk of Heart Disease ({adjusted_risk:.2f}% probability)")
    elif risk_level == "Moderate":
        st.warning(f"⚠️ Moderate Risk of Heart Disease ({adjusted_risk:.2f}% probability)")
    else:
        st.success(f"✅ Low Risk of Heart Disease ({adjusted_healthy:.2f}% healthy probability)")

    # -------------------------
    # Risk Gauge
    # -------------------------

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=adjusted_risk,
        title={'text': "Heart Disease Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 60], 'color': "yellow"},
                {'range': [60, 100], 'color': "red"}
            ],
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

    # -------------------------
    # Health Dashboard
    # -------------------------

    st.subheader("Health Dashboard")

    dashboard_data = {
        "Metric": ["Age", "Blood Pressure", "Cholesterol", "Max Heart Rate", "Oldpeak"],
        "Value": [age, resting_bp, cholesterol, max_hr, oldpeak]
    }

    st.bar_chart(pd.DataFrame(dashboard_data).set_index("Metric"))

    # -------------------------
    # Health Analysis
    # -------------------------

    st.subheader("Health Analysis")

    suggestions = []

    if age < 40:
        st.success("Age: Normal")
    elif age <= 60:
        st.warning("Age: Borderline Risk")
        suggestions.append("Schedule regular heart checkups.")
    else:
        st.error("Age: High Risk")
        suggestions.append("Consult a cardiologist.")

    if resting_bp < 120:
        st.success("Blood Pressure: Normal")
    elif resting_bp <= 139:
        st.warning("Blood Pressure: Borderline")
        suggestions.append("Reduce salt intake.")
    else:
        st.error("Blood Pressure: High")
        suggestions.append("Consult doctor for hypertension.")

    if cholesterol < 200:
        st.success("Cholesterol: Normal")
    elif cholesterol <= 239:
        st.warning("Cholesterol: Borderline")
        suggestions.append("Reduce saturated fats.")
    else:
        st.error("Cholesterol: High")
        suggestions.append("Adopt heart-healthy diet.")

    if max_hr >= 150:
        st.success("Heart Rate Fitness: Good")
    elif max_hr >= 120:
        st.warning("Heart Rate Fitness: Moderate")
    else:
        st.error("Heart Rate Fitness: Low")
        suggestions.append("Increase cardiovascular exercise.")

    if oldpeak > 2:
        st.error("High ST depression detected.")
        suggestions.append("Consult cardiologist.")

    if fasting_bs == 1:
        st.error("High fasting blood sugar detected.")
        suggestions.append("Reduce sugar intake.")

    if exercise_angina == "Y":
        st.error("Exercise-induced angina detected.")
        suggestions.append("Avoid heavy exertion.")

    if resting_ecg == "LVH":
        st.warning("Possible Left Ventricular Hypertrophy.")

    if st_slope == "Down":
        st.error("ST slope indicates possible ischemia.")

    # -------------------------
    # Suggestions
    # -------------------------

    st.subheader("Personalized Suggestions")

    if suggestions:
        for s in suggestions:
            st.write("•", s)
    else:
        st.success("All indicators appear healthy. Maintain your lifestyle.")