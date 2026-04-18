import streamlit as st
import pandas as pd

st.title("📊 Retail Forecast Dashboard")

df = pd.read_csv("outputs/final_output.csv")

# Filters
store = st.selectbox("Select Store", df['store'].unique())
product = st.selectbox("Select Product", df['product'].unique())

filtered = df[(df['store'] == store) & (df['product'] == product)]

st.subheader("Sales vs Forecast")
st.line_chart(filtered[['sales','prediction']])

st.subheader("Inventory Recommendation")
st.dataframe(filtered[['date','rop','order_qty']].tail(10))
st.title("📊 Retail Forecast & Inventory Dashboard")

st.markdown("### 📦 Select Filters")

store = st.selectbox("Store", df['store'].unique())
product = st.selectbox("Product", df['product'].unique())

filtered = df[(df['store']==store) & (df['product']==product)]

col1, col2 = st.columns(2)

col1.metric("Latest Forecast", int(filtered['prediction'].iloc[-1]))
col2.metric("Recommended Order Qty", int(filtered['order_qty'].iloc[-1]))

st.line_chart(filtered[['sales','prediction']])

st.dataframe(filtered.tail(10))