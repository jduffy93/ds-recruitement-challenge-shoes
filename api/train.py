import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    classification_report,
    f1_score,
    roc_curve,
    roc_auc_score,
    RocCurveDisplay,
)

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


### Minimum Viable Product

def train():
    "Trains a Random Forest Classifier model on the transactions data and stores output"
    
    # Load the data
    df = pd.read_parquet("api/data/transactions.parquet")


    # Preprocess the data
    # Creating new features
    df["Order_Date_FK"] = pd.to_datetime(df["Order_Date_FK"], format="%Y%m%d")
    df["Month"] = df["Order_Date_FK"].dt.month
    df["Day"] = df["Order_Date_FK"].dt.day
    df["Weekday"] = df["Order_Date_FK"].dt.weekday
    df.drop(columns=["Order_Date_FK"], inplace=True) # Drop the original date column

    # Typecasting
    df[
        [
            "Shop",
            "ProductCode",
            "CustomerID",
            "SaleDocumentNumber",
            "BrandName",
            "ModelGroup",
            "ProductGroup"
        ]
    ] = df[
        [
            "Shop",
            "ProductCode",
            "CustomerID",
            "SaleDocumentNumber",
            "BrandName",
            "ModelGroup",
            "ProductGroup"
        ]
    ].astype("O") # Typecast categorical variables to object
    df[["OriginalSaleAmountInclVAT", "RevenueInclVAT", "CostPriceExclVAT"]] = df[
        ["OriginalSaleAmountInclVAT", "RevenueInclVAT", "CostPriceExclVAT"]
    ].astype("float64") # Typecast various prices to float64
    df[["Month", "Day", "Weekday"]] = df[["Month", "Day", "Weekday"]].astype("int64")


    # Define features to use
    numerical_features = [
    "OriginalSaleAmountInclVAT",
    "RevenueInclVAT",
    "CostPriceExclVAT",
    "Month",
    "Day",
    "Weekday"
    ]
    categorical_features = [
    "Shop",
    "ProductCode",
    "CustomerID",
    "SaleDocumentNumber",
    "BrandName",
    "ModelGroup",
    "ProductGroup"
    ]


    # Split the data
    X = df[numerical_features + categorical_features]
    y = df["Returned"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # Train the model
    model_name = "RandomForestClassifier"
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    # Evaluate the model
    precision = precision_score(y_test, rf.predict(X_test))
    recall = recall_score(y_test, rf.predict(X_test))
    f1 = f1_score(y_test, rf.predict(X_test))

    print(f"Test precision score: {precision}")
    print(f"Test recall score: {recall}")
    print(f"Test f1 score: {f1}")


    # Retrain the model on the full dataset before saving it
    print("--------------------\nRetraining the model on the full dataset...")
    rf.fit(pd.concat([X_train, X_test]), pd.concat([y_train, y_test]))

    # Final evaluations
    final_precision = precision_score(y_test, rf.predict(X_test))
    final_recall = recall_score(y_test, rf.predict(X_test))
    final_f1 = f1_score(y_test, rf.predict(X_test))

    print(f"Final precision score: {final_precision}")
    print(f"Final recall score: {final_recall}")
    print(f"Final f1 score: {final_f1}")

    # Save the model
    artifacts = {
        "features": {
            "num_features": numerical_features,
            "cat_features": categorical_features,
        },
        "model": rf,
    }

    joblib.dump(artifacts, f"api/{model_name}.joblib")

if __name__ == "__main__":
    train()