from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load Model
with open('svc_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get('/')
def home():
    return {'message': 'API Working'}

@app.post('/predict')
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return {
        'prediction': int(prediction[0])
    }