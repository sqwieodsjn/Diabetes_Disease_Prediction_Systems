# 🩺 Diabetes Disease Prediction System

An end-to-end Machine Learning web application that predicts the likelihood of diabetes based on user-provided medical parameters. The system includes a trained ML model, a Flask-based web interface, a REST API, and cloud deployment.

---

## 🌐 Live Demo

👉 [https://your-app-name.onrender.com](https://diabetes-disease-prediction-systems.onrender.com/predict)

---

## 📂 GitHub Repository

👉 [https://github.com/your-username/your-repo](https://github.com/sqwieodsjn/Diabetes_Disease_Prediction_Systems)

---

## 📌 Project Overview

This project demonstrates the complete lifecycle of a Machine Learning application:

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Model training and evaluation
* Model deployment using Flask
* API development and testing using Postman
* Cloud deployment on Render

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (SVM)
* XGBoost Classifier

📊 Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

👉 The best-performing model was selected for deployment.

---

## 📊 Dataset

* Pima Indians Diabetes Dataset

### Features:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

### Target:

* Outcome (0 = Non-Diabetic, 1 = Diabetic)

---

## ⚙️ Tech Stack

* Python
* Flask
* NumPy
* Pandas
* Scikit-learn
* XGBoost
* HTML, CSS
* Postman (API testing)
* Render (Deployment)

---

## 🔁 Project Workflow

1. Data Cleaning (handling missing values)
2. Exploratory Data Analysis (EDA)
3. Feature Scaling
4. Model Training & Evaluation
5. Model Serialization using Pickle
6. Flask Web Application Development
7. REST API Creation
8. Deployment on Render

---

## 🖥️ Web Application

* User-friendly interface to input medical data
* Real-time prediction output
* Displays probability of diabetes

---

## 🔗 API Endpoint

### 📍 POST `/predict_api`

#### Request (JSON):

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 25,
  "Insulin": 100,
  "BMI": 28,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

#### Response:

```json
{
  "prediction": "Non-Diabetic",
  "probability": 23.45
}
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

```bash
venv\Scripts\activate   # Windows
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

---

## 📈 Sample Inputs

### 🟢 Low Risk

* Glucose: 90
* BMI: 24
* Age: 25

### 🔴 High Risk

* Glucose: 165
* BMI: 36
* Age: 50

---

## 📁 Project Structure

```
disease-prediction/
│
├── model/
│   ├── diabetes_rf_model.pkl
│   ├── diabetes_scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Deployment

The application is deployed on Render and accessible via a public URL.

---

## 📌 Future Improvements

* Add input validation
* Improve UI/UX design
* Add authentication system
* Docker containerization
* Model monitoring and logging

---

## 💬 Conclusion

This project demonstrates a full-stack Machine Learning workflow—from data preprocessing to model deployment and API integration—showcasing both ML and backend development skills.

---

## 👤 Author

**Your Name**

* LinkedIn: https://linkedin.com/in/your-profile
* GitHub: https://github.com/your-username
