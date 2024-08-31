import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Oncology Dashboard")

# Header
st.title("Oncology Data Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")

# Mock data (replace with real data in production)
@st.cache_data
def load_data():
    data = {
        'Cancer Type': ['Lung', 'Breast', 'Prostate', 'Colorectal', 'Melanoma'],
        'Incidence Rate': [54, 126, 109, 38, 22],
        'Survival Rate': [19, 90, 98, 64, 92]
    }
    return pd.DataFrame(data)

df = load_data()

# Display raw data
st.subheader("Raw Data")
st.dataframe(df)

# Create a bar chart
st.subheader("Cancer Incidence Rates")
fig, ax = plt.subplots()
ax.bar(df['Cancer Type'], df['Incidence Rate'])
ax.set_ylabel('Incidence Rate (per 100,000)')
ax.set_title('Cancer Incidence Rates by Type')
st.pyplot(fig)

# Create a line chart
st.subheader("Cancer Survival Rates")
fig, ax = plt.subplots()
ax.plot(df['Cancer Type'], df['Survival Rate'], marker='o')
ax.set_ylabel('5-Year Survival Rate (%)')
ax.set_title('Cancer 5-Year Survival Rates by Type')
plt.xticks(rotation=45)
st.pyplot(fig)

# Add some interactivity
selected_cancer = st.sidebar.selectbox("Select Cancer Type", df['Cancer Type'])
st.subheader(f"Details for {selected_cancer} Cancer")
cancer_data = df[df['Cancer Type'] == selected_cancer].iloc[0]
st.write(f"Incidence Rate: {cancer_data['Incidence Rate']} per 100,000")
st.write(f"5-Year Survival Rate: {cancer_data['Survival Rate']}%")