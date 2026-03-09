# ❤️ Heart Disease Risk Prediction System

An AI-powered web application that predicts the **risk of heart disease** based on patient health indicators.

The system analyzes medical features such as blood pressure, cholesterol levels, heart rate, and ECG results to estimate the **probability of heart disease**.

This project demonstrates a **complete Machine Learning pipeline** from data preprocessing to model deployment using an interactive web application.

---

## 🚀 Features

- Predicts heart disease risk using Machine Learning
- Displays **risk probability (%)**
- Interactive medical dashboard
- Health indicator analysis
- Personalized health suggestions
- Visual risk meter using Plotly
- Real-time predictions via Streamlit

---

## Dataset

The dataset used in this project is the **UCI Heart Disease Dataset**.

It contains various medical attributes used to predict the presence of heart disease.

Key attributes include:

- Age
- Blood Pressure
- Cholesterol
- Maximum Heart Rate
- ECG Results
- Exercise-induced Angina
- ST Depression
- Fasting Blood Sugar

---

## 📊 App Preview

The screenshots below show different prediction scenarios based on different health conditions.

### Example Prediction 1
Low-risk patient profile with healthy indicators.
![alt text](<images/image 1.png>)

---

### Example Prediction 2
Moderate risk patient with some abnormal indicators.

![alt text](<images/image 2.png>)

---

### Example Prediction 3
High risk patient with multiple health concerns.

![alt text](<images/image 3.png>)

---

## 🧠 Machine Learning Pipeline

This project follows a complete ML workflow:

1. Data Collection
2. Data Cleaning
3. Feature Encoding
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Cross Validation
8. Model Deployment

---

## 🤖 Model Used

The model used in this project is:

**Logistic Regression**

Reasons for choosing Logistic Regression:

- Performs well on medical classification tasks
- Provides probability-based predictions
- Interpretable model coefficients
- Good generalization for tabular datasets

---

## 📊 Input Features

The model predicts heart disease risk using the following features:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-induced Angina
- ST Depression
- ST Slope

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit

The web application interface is built using **Streamlit**.

---

## 💻 Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aryan-222005/Heart-Disease-Prediction.git
```

### 2️⃣ Navigate to the project folder 

```bash
cd Heart-Disease-Prediction
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application
```bash
streamlit run app/app.py
```

## 📂 Project Structure
```
Heart-Disease-Prediction
│
├── app
│   └── app.py
│
├── Models
│   ├── logistic_heart.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── Notebook
│   └── Heart.ipynb
│
├── Data
│   └── heart.csv
│
├── images
│   ├── image-1.png
│   ├── image-2.png
│   ├── image-3.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🌐 Live Demo
https://heart-disease-risk-ai.streamlit.app/