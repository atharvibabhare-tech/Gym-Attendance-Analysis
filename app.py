import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Gym Attendance Dashboard",
    page_icon="🏋️",
    layout="wide"
)

# Load data
df = pd.read_excel("Datasets/Gym_Attendance_Dataset.xlsx")

# Title + subtitle
st.markdown("<h1 style='text-align: center;'>🏋️Gym Attendance Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Interactive analysis of gym member attendance</p>", unsafe_allow_html=True)
st.divider()

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Unique Members", df["Member_Name"].nunique())
col3.metric("Unique Dates", df["Date"].nunique())

st.divider()

# Filters
st.subheader("Filter Data")
member = st.selectbox("Select Member", ["All"] + sorted(df["Member_Name"].unique().tolist()))
date = st.selectbox("Select Date", ["All"] + sorted(df["Date"].astype(str).unique().tolist()))

filtered_df = df.copy()
if member != "All":
    filtered_df = filtered_df[filtered_df["Member_Name"] == member]
if date != "All":
    filtered_df = filtered_df[filtered_df["Date"].astype(str) == date]

# Tabs
tab1, tab2 = st.tabs(["Raw Data", "Basic Stats"])

with tab1:
    st.dataframe(filtered_df, use_container_width=True)

with tab2:
    st.dataframe(filtered_df.describe(include="all"), use_container_width=True)

st.divider()

# Footer
st.markdown(
    "<p style='text-align: center; color: grey;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
