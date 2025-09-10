import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_file = "data/Prevalence_of_Selected_Measures_Among_Adults_Aged_20_and_Over__United_States__1999-2000_through_2017-2018.csv"
df = pd.read_csv(data_file)

# Filter to hypertension
htn_df = df[df['Measure'].str.contains('Hypertension', case=False, na=False)].copy()

# Split Survey Years into start/end
htn_df[['StartYear', 'EndYear']] = htn_df['Survey Years'].str.split('-', expand=True)
htn_df['StartYear'] = htn_df['StartYear'].astype(int)

# Streamlit UI
st.title("Hypertension Data Dashboard")

# Dropdowns
sex_option = st.selectbox("Select Sex", htn_df["Sex"].dropna().unique())
age_option = st.selectbox("Select Age Group", htn_df["Age Group"].dropna().unique())

# Filter based on user choices
filtered = htn_df[(htn_df["Sex"] == sex_option) & (htn_df["Age Group"] == age_option)]

# Plot
fig, ax = plt.subplots()
ax.plot(filtered["StartYear"], filtered["Data Value"], marker="o")
ax.set_title(f"Hypertension prevalence over time ({sex_option}, {age_option})")
ax.set_xlabel("Year")
ax.set_ylabel("Prevalence (%)")

st.pyplot(fig)
