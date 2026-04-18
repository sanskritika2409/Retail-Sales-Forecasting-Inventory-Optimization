def clean_data(df):
    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove negative sales
    df = df[df['sales'] >= 0]

    # Fill missing values
    df.fillna(0, inplace=True)

    print("✅ Data cleaned")
    return df