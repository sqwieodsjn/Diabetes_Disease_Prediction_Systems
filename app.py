from flask import Flask, request,render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("diabetes_rf_model.pkl", "rb"))
scalar = pickle.load(open("diabetes_scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    data_scaled = scalar.transform(np.array(data).reshape(1,-1))
    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0][1]
    result = "Diabetic" if prediction == 1 else "Non-Diabetic"
    return render_template('index.html', prediction_text=f'Prediction: {result} (Probability: {probability:.2f})')
if __name__ == "__main__":
    app.run(debug=True)
    