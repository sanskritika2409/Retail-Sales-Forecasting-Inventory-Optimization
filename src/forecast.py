import joblib

def forecast(df):
    model = joblib.load("models/model.pkl")

    X = df.drop(['sales','date','store','product'], axis=1)

    df['prediction'] = model.predict(X)

    print("✅ Forecast generated")
    return df