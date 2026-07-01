# 📉 Customer Churn Prediction Streamlit App

A Streamlit application that predicts customer churn using a saved Logistic Regression model.

## ✨ Features

- 🤖 **ML-Powered Predictions**: Uses a trained scikit-learn model
- 🖥️ **Streamlit UI**: Simple, responsive interface
- 📊 **Probability Visualization**: Displays churn probability and risk level
- 🧠 **Same model schema**: Uses the saved feature mapping from training

## 🔧 Tech Stack

- **App Framework**: Streamlit
- **ML Library**: scikit-learn
- **Data Processing**: pandas, numpy
- **Serialization**: joblib

## 📋 Prerequisites

- Python 3.8+
- pip

## 🚀 Run Locally

```bash
cd ~/Documents/Customer_Churn_Prediction
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the URL shown in the terminal to use the app.

## 📦 File Structure

```
.
├── churn.ipynb                     # Jupyter notebook with ML training
├── models/
│   ├── churn_model.pkl             # Trained model file
│   └── feature_names.pkl           # Feature names mapping
├── streamlit_app.py                # Streamlit application
├── Telco-Customer-Churn.csv        # Training dataset
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── STREAMLIT_README.md             # Streamlit usage guide
└── .gitignore                      # Git ignore rules
```

## 📊 Model Info

- **Model type**: Logistic Regression
- **Output**: churn prediction, probability, risk level
- **Inputs**: tenure, billing, services, contract, and other customer features

## 🧪 How It Works

The app loads the saved model from `models/churn_model.pkl` and applies the feature mapping stored in `models/feature_names.pkl`.

## 🔄 Retraining the Model

1. Update `Telco-Customer-Churn.csv` with new data
2. Retrain using `churn.ipynb`
3. Save the updated model and feature names to `models/`