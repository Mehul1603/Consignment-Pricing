from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_data
from app.model.model import __version__ as model_version

app = FastAPI()

class PredictionOut(BaseModel):
    output: float

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model = PredictionOut)
def predict(item_value, item_quantity, weight, item_insurance):
    output = predict_data(item_value, item_quantity, weight, item_insurance)
    return {"output": output}