import streamlit as st
import pandas as pd

st.title("Gym Attendance Analysis")

df = pd.read_excel("../Dataset/Gym_Attendance_Dataset.xlsx")

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("Basic Stats")
st.write(df.describe(include="all"))
