# 🩺 Diabetes Prediction Web App

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-WebFramework-orange?style=flat-square)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)](#)

A **user-friendly web application** built with **Flask** that predicts diabetes risk using a trained **Machine Learning model**. Enter your health details, and get real-time predictions with a clean, modern UI.

---

## ✨ Features

* Modern and responsive UI with **pastel theme**
* Input form for **8 health parameters**
* Real-time **diabetes risk prediction**
* Dynamic result display on the same page
* Easy to update with **your own ML models**

---

## 🗂 Project Structure

```
healthcare_disease_detection-web/
│
├── app.py                # Main Flask application
├── diabetes_model.pkl    # Pre-trained ML model (Logistic Regression)
├── templates/
│   └── index.html        # HTML form & result page
└── static/
    └── style.css         # Modern CSS styling
```

---

## ⚙️ Installation

1. **Clone the repo**

```bash
git clone <your-repo-url>
cd healthcare_disease_detection-web
```

2. **Create a virtual environment** (optional but recommended)

```bash
python -m venv venv
# Activate environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install required packages**

```bash
pip install flask numpy scikit-learn
```

---

## 🚀 Running the App

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000/
```

3. Fill in your health details:

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

4. Click **Predict** → see your diabetes risk instantly. ✅

---

## 🖼 Screenshots

**Home / Input Form**
![Input Form](path-to-your-screenshot.png)

**Prediction Result**
![Prediction Result](path-to-your-screenshot.png)

> Replace the `path-to-your-screenshot.png` with your actual screenshots for GitHub preview.

---

## ⚠️ Notes

* The **order of input features must match your ML model training data**.
* Currently uses **Logistic Regression**, but any scikit-learn model can be used.
* CSS is in `static/style.css` → easy to customize colors, fonts, and layout.

---

## 💡 Tips for Future Upgrades

* Add **charts** for multiple predictions
* Integrate with a **database** to save user inputs
* Enhance UI with **animations, icons, or pastel themes**
* Deploy on **Heroku or Render** for live usage

---

## 📜 License

Educational / Personal Projects – Free to modify and share.
