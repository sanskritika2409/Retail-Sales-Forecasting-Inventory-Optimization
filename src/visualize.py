def plot_sales(df):
    import matplotlib.pyplot as plt

    sample = df[(df['store'] == df['store'].iloc[0]) &
                (df['product'] == df['product'].iloc[0])]

    plt.figure(figsize=(10,5))
    plt.plot(sample['date'], sample['sales'], label='Actual')
    plt.plot(sample['date'], sample['prediction'], label='Forecast')

    plt.title("Actual vs Forecast (Sample SKU)")
    plt.legend()
    plt.grid()

    plt.savefig("outputs/forecast_plot.png")  # 🔥 important
    plt.show()

    print("✅ Plot saved")