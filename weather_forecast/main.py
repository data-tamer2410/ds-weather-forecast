"""Main module for the weather forecast API"""

from tensorflow import keras
from keras.models import load_model
from keras.losses import MeanSquaredError
from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import Union, Literal
import numpy as np
import pickle

keras.utils.get_custom_objects().update({"mse": MeanSquaredError()})
model = load_model("weather_forecast/weather_forecast.h5")
target_names = [
    "MaxTemp",
    "MinTemp",
    "Pressure3pm",
    "Pressure9am",
    "Rainfall",
    "Temp3pm",
    "Temp9am",
    "WindGustSpeed",
    "WindSpeed3pm",
    "WindSpeed9am",
    "RainToday",
]
with open("weather_forecast/standard_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("weather_forecast/dir_encoder.pkl", "rb") as f:
    dir_encoder = pickle.load(f)


class InputData(BaseModel):
    data: conlist(
        conlist(
            Union[
                float,
                int,
                Literal[
                    "SW",
                    "E",
                    "N",
                    "WNW",
                    "SSE",
                    "SE",
                    "S",
                    "WSW",
                    "NNE",
                    "NNW",
                    "ENE",
                    "SSW",
                    "NW",
                    "ESE",
                    "NE",
                    "W",
                ],
            ],
            min_length=17,
            max_length=17,
        ),
        min_length=7,
        max_length=7,
    )


def predicted(list_features: InputData) -> dict:
    """Predict the target values from the input features"""
    features = list_features.dict()["data"]
    features = np.array(features).reshape(1, -1)
    features = np.vectorize(lambda x: dir_encoder.get(x, x))(features)
    features = features.astype("float32")
    features = scaler.transform(features).reshape(1, 7, 17)
    res = {
        target_names[i]: float(v[0][0])
        for i, v in enumerate(model.predict(features, verbose=0))
    }
    return res


app = FastAPI()


@app.post("/predict/")
async def predict(list_features: InputData) -> dict:
    return predicted(list_features)
