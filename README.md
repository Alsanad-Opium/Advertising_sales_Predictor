# 📈 Sales Forecast Tool (ML + Flask Deployment)

A production-style machine learning web application that predicts **sales from advertising budgets** and provides **ROI insights + budget optimization recommendations**.

---

## 🚀 Live Demo

👉 [https://sales-forecast-tool-for-marketing-budgets.onrender.com](https://sales-forecast-tool-for-marketing-budgets.onrender.com)

---

## 📌 Project Overview

This project demonstrates an **end-to-end machine learning pipeline**, from model training to deployment.

It predicts sales based on advertising spend across:

* 📺 TV Ads Budget
* 📻 Radio Ads Budget
* 📰 Newspaper Ads Budget

Beyond prediction, the system also computes:

* 📊 ROI (Return on Investment)
* 🧠 Business insights
* 📉 Budget allocation recommendations

---

## 🧠 Key Features

### 🔹 Machine Learning

* Linear Regression model
* Preprocessing pipeline (Scaling + Imputation)
* Trained using scikit-learn

### 🔹 Web Application

* Flask backend (REST + form-based input)
* HTML + CSS frontend
* Real-time predictions

### 🔹 Business Intelligence Layer

* ROI calculation
* Budget efficiency analysis
* Heuristic recommendation engine

---

## 🏗️ System Architecture

```text
User Input (Web Form)
        ↓
Flask Backend (app.py)
        ↓
Data Preprocessing (Pandas DataFrame)
        ↓
ML Pipeline (Scaler + Model)
        ↓
Prediction Output
        ↓
ROI + Insights + Recommendations
        ↓
Frontend Display
```

---

## ⚙️ Tech Stack

### 🧠 Machine Learning

* Python
* scikit-learn
* pandas
* numpy

### 🌐 Backend

* Flask
* Gunicorn

### 🎨 Frontend

* HTML
* CSS (custom UI)

### ☁️ Deployment

* Render

---

## 📊 Model Pipeline

The trained model includes:

* SimpleImputer → handles missing values
* StandardScaler → feature scaling
* LinearRegression → prediction model

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── model/
│   └── Advertising_model_sales_v1.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🔥 Business Logic

### 📈 ROI Calculation

```python
ROI = Predicted Sales / Total Advertising Budget
```

---

### 🧠 Insight Engine

* High ROI → scale investment
* Medium ROI → optimize distribution
* Low ROI → re-evaluate strategy

---

### 📉 Recommendation System

* Detects highest and lowest spending channels
* Suggests budget reallocation strategies
* Acts as a simple decision-support system

---

## 🧪 Example Input

| TV    | Radio | Newspaper |
| ----- | ----- | --------- |
| 230.1 | 37.8  | 69.2      |

---

## 📤 Output Example

```text
Predicted Sales: $18.24
ROI: 0.12

Insight:
Moderate return. Consider optimizing allocation.

Recommendation:
Shift budget from Newspaper to Radio for better efficiency.
```

---

## 🚀 How to Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/Advertising_sales_Predictor

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 🌍 Deployment

Deployed using **Render**

* Flask app hosted as a web service
* Gunicorn used as production server
* CI/CD via GitHub integration

---

## 🧠 Key Learnings

* End-to-end ML pipeline design
* Model serialization using pickle
* Flask API development
* Production deployment on cloud
* Business logic layering on ML outputs

---

## 🚀 Future Improvements

* Add SHAP explainability (feature importance)
* Add real-time analytics dashboard
* Replace heuristic recommendations with ML-based optimizer
* Add user authentication system

---

## 👨‍💻 Author

**Mohammad Alsanad Sheikh**

🔗 LinkedIn: [https://www.linkedin.com/in/mohammad-alsanad-sheikh-a12818302](https://www.linkedin.com/in/mohammad-alsanad-sheikh-a12818302)

---


