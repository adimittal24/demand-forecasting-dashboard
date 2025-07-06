# save this as app.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# connect to your Postgres
engine = create_engine("postgresql+psycopg2://postgres:202754@localhost:5432/demand_forecasting")

st.title("📦 Inventory & Demand Forecast Dashboard")

# get inventory data
inventory_df = pd.read_sql("SELECT * FROM inventory", engine)
alerts_df = pd.read_sql("SELECT * FROM alerts", engine)

# product filter
product_list = inventory_df['product_id'].unique()
selected_product = st.selectbox("Select a product:", product_list)

# filter inventory
product_data = inventory_df[inventory_df['product_id'] == selected_product]

st.subheader("Current Inventory")
st.dataframe(product_data)

# show recent alerts
st.subheader("Reorder Alerts")
st.dataframe(alerts_df[alerts_df['product_id'] == selected_product])

# plot placeholder
st.subheader("Forecast Plot")
st.write("You could add a matplotlib / Prophet plot here in a later step!")

st.success("✅ Dashboard loaded successfully")
