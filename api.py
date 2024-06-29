import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("model_weights.joblib")


class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def do_model_prediction(data: PredictionInput):
    prediction = model.predict(
        [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    )
    prediction = int(prediction[0])
    return prediction


@app.get("/")
def read_root():
    return "This is the API for the Iris classification model."


@app.post("/predict")
async def predict(data: PredictionInput):
    prediction = do_model_prediction(data)
    return {"prediction": prediction}
