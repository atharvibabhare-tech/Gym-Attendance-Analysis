import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gym Attendance Analysis", layout="wide")
st.title("Gym Attendance Analysis")

# Load dataset
df = pd.read_excel("Datasets/Gym_Attendance_Dataset.xlsx")

st.header("Raw Data")
st.dataframe(df)

st.header("Basic Stats")
st.dataframe(df.describe(include="all"))

st.subheader("Total Records")
st.metric("Rows", len(df))

st.subheader("Unique Members")
st.metric("Members", df["Member_Name"].nunique())

st.subheader("Filter by Member")
member = st.selectbox("Select Member", ["All"] + sorted(df["Member_Name"].unique().tolist()))

if member != "All":
    st.dataframe(df[df["Member_Name"] == member])
else:
    st.dataframe(df)
