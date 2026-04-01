from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI()

class CustomerData(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    result = predict(data.features)
    
    if result == 1:
        return {"prediction": "Customer will churn"}
    else:
        return {"prediction": "Customer will stay"}