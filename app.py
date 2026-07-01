from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import joblib
import numpy as np
import pandas as pd
import os
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model and feature names
model = joblib.load('models/churn_model.pkl')
feature_names = joblib.load('models/feature_names.pkl')

# Define input schema
class ChurnPredictionInput(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    senior_citizen: int
    internet_service_dsl: int
    internet_service_fiber_optic: int
    contract_month_to_month: int
    contract_one_year: int
    contract_two_year: int
    online_security_yes: int
    online_backup_yes: int
    device_protection_yes: int
    tech_support_yes: int
    streaming_tv_yes: int
    streaming_movies_yes: int
    paperless_billing_yes: int
    payment_method_credit_card: int
    payment_method_electronic_check: int
    payment_method_mailed_check: int
    tenure_group_0_1_year: int
    tenure_group_1_2_years: int
    tenure_group_2_4_years: int
    tenure_group_4_6_years: int

class PredictionResponse(BaseModel):
    churn_probability: float
    churn_prediction: str
    risk_level: str

@app.get("/")
async def read_root():
    """Serve the frontend"""
    return FileResponse("static/index.html")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "model_loaded": True}

@app.post("/api/predict")
async def predict(input_data: ChurnPredictionInput):
    """
    Make churn prediction based on customer data
    """
    try:
        # Create a dictionary from input
        data_dict = input_data.dict()
        
        # Create a DataFrame with the same features as training data
        input_df = pd.DataFrame([data_dict])
        
        # Ensure all features are present
        for feature in feature_names:
            if feature not in input_df.columns:
                input_df[feature] = 0
        
        # Select only the features used in training and reorder
        input_df = input_df[feature_names]
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]
        
        # Determine risk level
        if probability > 0.7:
            risk_level = "High"
        elif probability > 0.4:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        return PredictionResponse(
            churn_probability=round(float(probability), 4),
            churn_prediction="Yes" if prediction == 1 else "No",
            risk_level=risk_level
        )
    
    except Exception as e:
        return {"error": str(e)}

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
