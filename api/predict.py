import joblib
import pandas as pd
import json
from io import StringIO


def predict(inpt):

    data = json.loads(inpt)
    model_name = "RandomForsetClassifier"
    artifacts = joblib.load(f"api/{model_name}.joblib")


    # Unpack the artifacts
    numerical_features = artifacts["features"]["numerical_features"]
    categorical_features = artifacts["features"]["categorical_features"]
    model = artifacts["model"]

    # Make predictions
    prediction_df = pd.DataFrame(model.predict(data))
    prediction = prediction_df.astype(float)

    return prediction.to_numpy()[0][0]