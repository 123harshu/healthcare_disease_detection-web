from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("diabetes_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None

    if request.method == "POST":
        try:
            # Collect data from form
            data = [
    float(request.form["pregnancies"]),
    float(request.form["glucose"]),
    float(request.form["bp"]),
    float(request.form["skin"]),
    float(request.form["insulin"]),
    float(request.form["bmi"]),
    float(request.form["dpf"]),
    float(request.form["age"])
]


            # Make prediction
            prediction = model.predict([data])
            prediction_text = "Diabetes Detected ❌" if prediction[0] == 1 else "No Diabetes ✅"
        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
