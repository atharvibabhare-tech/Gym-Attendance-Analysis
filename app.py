import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gym Attendance", page_icon="🏋️", layout="wide")

# Load data
df = pd.read_excel("Datasets/Gym_Attendance_Dataset.xlsx")

# Header
st.markdown("<h1 style='text-align:center;'>🏋️ Gym Attendance App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Check who came to the gym and view attendance trends</p>", unsafe_allow_html=True)
st.divider()

# Quick stats (KPIs)
c1, c2, c3 = st.columns(3)
c1.metric("👥 Members", df["Member_Name"].nunique())
c2.metric("📅 Days Recorded", df["Date"].nunique())
c3.metric("📄 Total Entries", len(df))

st.divider()

# Filters
st.subheader("🔎 Filter Records")
member = st.selectbox("Choose Member", ["All"] + sorted(df["Member_Name"].dropna().unique().tolist()))
date = st.selectbox("Choose Date", ["All"] + sorted(df["Date"].astype(str).dropna().unique().tolist()))

data = df.copy()
if member != "All":
    data = data[data["Member_Name"] == member]
if date != "All":
    data = data[data["Date"].astype(str) == date]

# Tabs
tab1, tab2 = st.tabs(["📄 Attendance Table", "📊 Summary"])

with tab1:
    st.dataframe(data, use_container_width=True)

with tab2:
    st.info("Summary statistics for the selected data")
    st.dataframe(data.describe(include="all"), use_container_width=True)

st.divider()

# Graph
st.subheader("📈 Daily Attendance Trend")
daily_counts = data.groupby("Date").size().reset_index(name="Visits")
st.line_chart(daily_counts.set_index("Date"))

st.divider()
st.caption("Made with ❤️ using Streamlit")
