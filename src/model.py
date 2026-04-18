from xgboost import XGBRegressor
import joblib
import os

def train_model(X, y):
    model = XGBRegressor(n_estimators=200, learning_rate=0.1)

    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

    print("✅ XGBoost Model trained")
    return model