from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Retail Forecast API"}

@app.get("/data")
def get_data():
    df = pd.read_csv("outputs/final_output.csv")
    return df.tail(5).to_dict()