import os

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.features import create_features
from src.model import train_model
from src.forecast import forecast
from src.inventory import calculate_inventory
from src.visualize import plot_sales

# Ensure folders exist
os.makedirs("outputs", exist_ok=True)

# Load data
df = load_data("data/retail_data.csv")

# Clean data
df = clean_data(df)

# Feature engineering
df = create_features(df)

# Split features
X = df.drop(['sales', 'date', 'store', 'product'], axis=1)
y = df['sales']

# Train model
train_model(X, y)

# Forecast
df = forecast(df)

# Inventory optimization
df = calculate_inventory(df)

# Save output
df.to_csv("outputs/final_output.csv", index=False)

# Visualization
plot_sales(df)

print("\n🎉 PROJECT EXECUTED SUCCESSFULLY!")
# Save clean outputs for GitHub/demo
df[['date','store','product','sales','prediction','rop','order_qty']] \
    .to_csv("outputs/final_output_clean.csv", index=False)

print("📁 Clean output saved for demo")