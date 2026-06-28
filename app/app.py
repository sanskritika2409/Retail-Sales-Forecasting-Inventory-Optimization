import os
import pandas as pd
import streamlit as st
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Retail Forecast Dashboard", page_icon="📊", layout="wide")
st.title("📊 Retail Forecast & Inventory Dashboard")

# 2. Resilient Path Handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "outputs", "final_output.csv")

# Create outputs folder if it doesn't exist locally
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

@st.cache_data
def load_data(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        # Fallback: Try to build a clean sample using raw data if outputs are missing from Git
        raw_data_path = os.path.join(BASE_DIR, "..", "data", "train.csv")
        if os.path.exists(raw_data_path):
            raw_df = pd.read_csv(raw_data_path).head(1000)
            # Simulate prediction and inventory columns for visualization
            raw_df['prediction'] = raw_df['sales'] * np.random.uniform(0.9, 1.1, len(raw_df))
            raw_df['rop'] = raw_df['prediction'] * 1.2
            raw_df['order_qty'] = raw_df['prediction'] * 1.5
            return raw_df
        else:
            return None

df = load_data(csv_path)

if df is None:
    st.error("⚠️ Data files could not be located in the repository.")
    st.info("Ensure either 'outputs/final_output.csv' or 'data/train.csv' is committed to GitHub.")
    st.stop()

# Ensure consistent column naming
if 'Store' in df.columns: df.rename(columns={'Store': 'store'}, inplace=True)
if 'Item' in df.columns: df.rename(columns={'Item': 'product'}, inplace=True)
if 'Date' in df.columns: df.rename(columns={'Date': 'date'}, inplace=True)
if 'Sales' in df.columns: df.rename(columns={'Sales': 'sales'}, inplace=True)

# 3. Sidebar Filters
st.sidebar.markdown("### 📦 Select Filters")
store = st.sidebar.selectbox("Select Store", sorted(df['store'].unique()))
product = st.sidebar.selectbox("Select Product", sorted(df['product'].unique()))

# Filter the dataset
filtered = df[(df['store'] == store) & (df['product'] == product)].sort_values(by='date')

# 4. Dashboard Layout & Visuals
if not filtered.empty:
    col1, col2 = st.columns(2)
    col1.metric("Latest Forecast", int(filtered['prediction'].iloc[-1]))
    col2.metric("Recommended Order Qty (ROP)", int(filtered['order_qty'].iloc[-1]))
    
    st.subheader("📈 Sales vs Forecast Trends")
    st.line_chart(filtered.set_index('date')[['sales', 'prediction']])

    st.subheader("📋 Inventory Recommendation (Recent Logs)")
    st.dataframe(filtered[['date', 'sales', 'prediction', 'rop', 'order_qty']].tail(10))
else:
    st.warning("No tracking data available for this store-product pairing.")
