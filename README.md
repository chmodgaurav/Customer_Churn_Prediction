# 📊 Customer Churn Prediction System

A machine learning-powered web application that predicts customer churn likelihood for telecom companies using Logistic Regression.

## ✨ Features

- 🤖 **ML-Powered Predictions**: Uses trained Logistic Regression model
- 🎨 **Modern UI**: Beautiful, responsive web interface
- 📱 **Mobile Friendly**: Works seamlessly on desktop and mobile devices
- ⚡ **Fast API**: Built with FastAPI for high performance
- 🚀 **Production Ready**: Deployable on Render, Heroku, or any cloud platform
- 📊 **Risk Assessment**: Categorizes customers into Low, Medium, High risk levels
- 📈 **Probability Visualization**: Interactive probability bar chart

## 🎯 What the Model Predicts

The model analyzes customer data including:
- Demographics (tenure, senior citizen status)
- Service usage (internet, streaming, security)
- Contract type (month-to-month, 1-year, 2-year)
- Billing information (charges, payment method)
- Additional services

And predicts the probability of customer churn with categories:
- **High Risk**: >70% churn probability
- **Medium Risk**: 40-70% churn probability
- **Low Risk**: <40% churn probability

## 🔧 Tech Stack

### Backend
- **Framework**: FastAPI
- **Server**: Uvicorn
- **ML Library**: scikit-learn
- **Data Processing**: pandas, numpy
- **Serialization**: joblib

### Frontend
- **Language**: HTML5, CSS3, JavaScript (ES6+)
- **Design**: Responsive Grid Layout
- **Features**: Real-time form validation, animated results

### Deployment
- **Platform**: Render
- **Language**: Python 3.11+
- **Container**: Docker (automatic via Render)

## 📋 Prerequisites

- Python 3.8+
- pip
- Git (for deployment)
- GitHub account (for linking to Render)

## 🚀 Quick Start

### Local Development

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

The application will start at `http://localhost:8000`

### Live Demo

Visit the deployed application: [churn-prediction.onrender.com](https://churn-prediction.onrender.com)

## 📦 File Structure

```
.
├── app.py                          # FastAPI application (backend)
├── churn.ipynb                     # Jupyter notebook with ML training
├── static/
│   └── index.html                 # Frontend web interface
├── models/
│   ├── churn_model.pkl            # Trained model file
│   └── feature_names.pkl          # Feature names mapping
├── Telco-Customer-Churn.csv       # Training dataset
├── requirements.txt               # Python dependencies
├── Procfile                       # Render deployment config
├── render.yaml                    # Advanced Render config
├── DEPLOYMENT.md                  # Deployment guide
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🌐 Deployment

### Deploy to Render (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository
   - Configure as follows:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

3. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Access your app at the provided URL

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 💡 Usage

### Via Web Interface

1. Open the application in your browser
2. Fill in customer information
3. Click "Predict Churn"
4. View the prediction results with risk level

### Via API

```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "tenure": 12,
    "monthly_charges": 65.0,
    "total_charges": 780.0,
    "senior_citizen": 0,
    "internet_service_dsl": 1,
    "internet_service_fiber_optic": 0,
    "contract_month_to_month": 1,
    "contract_one_year": 0,
    "contract_two_year": 0,
    "online_security_yes": 0,
    "online_backup_yes": 0,
    "device_protection_yes": 0,
    "tech_support_yes": 0,
    "streaming_tv_yes": 0,
    "streaming_movies_yes": 0,
    "paperless_billing_yes": 0,
    "payment_method_credit_card": 0,
    "payment_method_electronic_check": 0,
    "payment_method_mailed_check": 0,
    "tenure_group_0_1_year": 0,
    "tenure_group_1_2_years": 0,
    "tenure_group_2_4_years": 0,
    "tenure_group_4_6_years": 0
  }'
```

## 📊 Model Performance

**Test Set Metrics:**
| Metric | Score |
|--------|-------|
| Accuracy | 79.03% |
| Precision | 63.39% |
| Recall | 50.00% |
| F1 Score | 55.90% |

## 🔄 Retraining the Model

To retrain the model with new data:

1. Update `Telco-Customer-Churn.csv` with new data
2. Run the Jupyter notebook (`churn.ipynb`)
3. The model files will be updated in the `models/` directory
4. Push to GitHub and Render will automatically redeploy

## 🎨 Customization

### Change Colors/Styling
Edit the `<style>` section in `static/index.html`

### Add More Features
1. Add input fields to the HTML form
2. Update the JavaScript payload mapping
3. Retrain the model with additional features
4. Update `app.py` input schema

### Change Risk Thresholds
Edit the risk level calculation in `app.py`:
```python
if probability > 0.7:
    risk_level = "High"
elif probability > 0.4:
    risk_level = "Medium"
else:
    risk_level = "Low"
```

## 🐛 Troubleshooting

### Port already in use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9  # Linux/Mac
netstat -ano | findstr :8000    # Windows
```

### Model loading error
```bash
# Verify models exist
ls models/
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Deployment fails on Render
1. Check build logs in Render dashboard
2. Ensure all files are committed to git
3. Verify requirements.txt has all dependencies
4. Check that models/ directory is included

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Render Deployment Guide](https://render.com/docs)
- [scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)

## 🔐 Security Notes

- The application is designed for demonstration purposes
- For production use, add authentication/authorization
- Implement rate limiting to prevent abuse
- Validate and sanitize all user inputs
- Use HTTPS in production (automatic on Render)

## 📄 License

This project is provided for educational and demonstration purposes.

## 👨‍💻 Author

Created as a customer churn prediction machine learning project.

## 🙏 Acknowledgments

- Dataset from IBM Telco Customer Churn
- Built with open-source libraries: FastAPI, scikit-learn, pandas

---

**Status**: ✅ Production Ready
**Last Updated**: 2026-07-02
**Version**: 1.0.0

For questions or improvements, please open an issue or submit a pull request!
