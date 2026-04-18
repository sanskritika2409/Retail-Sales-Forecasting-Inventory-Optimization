def create_features(df):
    df = df.copy()

    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday

    # Encode product & store
    df['product_code'] = df['product'].astype('category').cat.codes
    df['store_code'] = df['store'].astype('category').cat.codes

    df['lag_1'] = df.groupby(['store','product'])['sales'].shift(1)
    df['rolling_mean_7'] = df.groupby(['store','product'])['sales'].shift(1).rolling(7).mean()

    df = df.dropna()

    print("✅ Features created (multi-product)")
    return df