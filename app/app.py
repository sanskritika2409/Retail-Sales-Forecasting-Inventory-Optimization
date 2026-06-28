import os
import pandas as pd
import streamlit as st

# 1. Page Configuration & Title
st.set_page_config(page_title="Retail Forecast Dashboard", page_icon="📊", layout="wide")
st.title("📊 Retail Forecast & Inventory Dashboard")

# 2. Safe Dynamic Path Handling
# This finds the absolute path of app.py, looks one level up (..), and targets outputs/final_output.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "outputs", "final_output.csv")

# Load the dataset
df = pd.read_csv(csv_path)

# 3. Sidebar Filters
st.sidebar.markdown("### 📦 Select Filters")
store = st.sidebar.selectbox("Select Store", df['store'].unique())
product = st.sidebar.selectbox("Select Product", df['product'].unique())

# Filter the dataset based on selections
filtered = df[(df['store'] == store) & (df['product'] == product)]

# 4. Key Performance Indicators (KPI Metrics)
if not filtered.empty:
    col1, col2 = st.columns(2)
    col1.metric("Latest Forecast", int(filtered['prediction'].iloc[-1]))
    col2.metric("Recommended Order Qty (ROP)", int(filtered['order_qty'].iloc[-1]))
    
    # 5. Data Visualization
    st.subheader("📈 Sales vs Forecast Trends")
    st.line_chart(filtered[['sales', 'prediction']])

    # 6. Inventory Recommendations Table
    st.subheader("📋 Inventory Recommendation (Recent Logs)")
    st.dataframe(filtered[['date', 'sales', 'prediction', 'rop', 'order_qty']].tail(10))
else:
    st.warning("No data available for the selected combination.")
