from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Uber Trip Analytics API")

df = pd.read_csv("../data/cleaned_dataset.csv")

@app.get("/")
def home():
    return {
        "Project":"Transportation Analytics using Uber Trip Data",
        "Status":"Running Successfully"
    }

@app.get("/summary")
def summary():

    return {
        "Total Trips": len(df),
        "Average Fare": round(df["fare_amount"].mean(),2),
        "Average Distance": round(df["distance_km"].mean(),2)
    }

@app.get("/cities")
def cities():
    return df["city"].value_counts().to_dict()