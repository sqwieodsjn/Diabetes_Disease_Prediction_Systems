from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

app = Flask(__name__)
print("THIS FILE IS RUNNING")
# Load model and scaler
model = pickle.load(open("diabetes_rf_model.pkl", "rb"))
scaler = pickle.load(open("diabetes_scaler.pkl", "rb"))

# -------------------- HOME ROUTE --------------------
@app.route('/')
def home():
    return render_template('index.html')


# -------------------- HTML FORM PREDICTION --------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        
        data_scaled = scaler.transform(np.array(data).reshape(1, -1))
        
        prediction = model.predict(data_scaled)[0]
        probability = model.predict_proba(data_scaled)[0][1]

        result = "⚠️ High Risk (Diabetic)" if prediction == 1 else "✅ Low Risk (Non-Diabetic)"

        return render_template(
            'index.html',
            prediction_text=f'{result} | Probability: {round(probability*100,2)}%'
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")


# -------------------- POSTMAN API --------------------
@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.get_json(force=True)

        print("Received JSON:", data)  # debug

        input_data = [
            float(data['Pregnancies']),
            float(data['Glucose']),
            float(data['BloodPressure']),
            float(data['SkinThickness']),
            float(data['Insulin']),
            float(data['BMI']),
            float(data['DiabetesPedigreeFunction']),
            float(data['Age'])
        ]

        input_array = np.array(input_data).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        result = "Diabetic" if prediction == 1 else "Non-Diabetic"

        return jsonify({
            "prediction": result,
            "probability": round(probability * 100, 2)
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)})
    # -------------------- TEST ROUTE --------------------
@app.route('/test')
def test():
    return "API is working"
# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)