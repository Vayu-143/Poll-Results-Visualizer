import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Poll Dashboard", layout="wide")

# Load data
file_path = os.path.join(os.path.dirname(__file__), "../data/poll_data.csv")
df = pd.read_csv(file_path)

st.title("📊 Poll Results Dashboard")

# ---------------- FILTERS ----------------
st.sidebar.header("🔍 Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

age_filter = st.sidebar.multiselect(
    "Select Age Group",
    options=df["Age_Group"].unique(),
    default=df["Age_Group"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Age_Group"].isin(age_filter))
]

# ---------------- METRICS ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Responses", len(filtered_df))
col2.metric("Unique Regions", filtered_df["Region"].nunique())
col3.metric("Unique Age Groups", filtered_df["Age_Group"].nunique())

# ---------------- DATA ----------------
st.subheader("📂 Dataset Preview")
st.dataframe(filtered_df.head())

# ---------------- CHARTS ----------------
st.subheader("📊 Overall Preference")
st.bar_chart(filtered_df["Preference"].value_counts())

st.subheader("🌍 Region-wise Analysis")
region = pd.crosstab(filtered_df["Region"], filtered_df["Preference"])
st.bar_chart(region)

st.subheader("👥 Age Group Analysis")
age = pd.crosstab(filtered_df["Age_Group"], filtered_df["Preference"])
st.bar_chart(age)

# ---------------- INSIGHTS ----------------
st.subheader("🧠 Insights")

top_product = filtered_df["Preference"].value_counts().idxmax()
st.success(f"🏆 Most Preferred Product: {top_product}")