import pandas as pd
import streamlit as st
import plotly.express as px

# Title
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

# Load Data
df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar Filters
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())

start_date = st.sidebar.date_input("Start Date", df["Date"].min())
end_date = st.sidebar.date_input("End Date", df["Date"].max())

# Filter Data
filtered_df = df[
    (df["Region"] == region) &
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

# KPIs
total_sales = int(filtered_df["Sales"].sum())
total_quantity = int(filtered_df["Quantity"].sum())

col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", total_sales)
col2.metric("📦 Total Quantity", total_quantity)

# Charts
st.subheader("📈 Sales Trend")
fig1 = px.line(filtered_df, x="Date", y="Sales", markers=True)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🏆 Sales by Product")
fig2 = px.bar(filtered_df, x="Product", y="Sales", color="Product")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🧁 Product Share")
fig3 = px.pie(filtered_df, names="Product", values="Sales")
st.plotly_chart(fig3, use_container_width=True)