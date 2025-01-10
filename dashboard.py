import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("dataset.csv")

# Streamlit App Title
st.title("📊 Public Consultation Feedback Dashboard")
st.write("An interactive dashboard showcasing public sentiment trends.")

# Select Feedback Type
feedback_type = st.selectbox("Select a Category:", df["Feedback_Type"].unique())

# Filter Data
filtered_data = df[df["Feedback_Type"] == feedback_type]

# Display Data
st.write("### Raw Data")
st.dataframe(filtered_data)

# Visualization: Bar Chart
st.write("### Feedback Breakdown")
fig, ax = plt.subplots()
filtered_data.set_index("Date")[["Positive", "Negative", "Neutral"]].plot(kind="bar", ax=ax)
st.pyplot(fig)

