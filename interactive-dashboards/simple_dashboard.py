import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Customer Churn Dashboard")

df = pd.read_csv('https://raw.githubusercontent.com/blastchar/telco-customer-churn/master/WA_Fn-UseC_-Telco-Customer-Churn.csv')
selected_gender = st.sidebar.selectbox("Select Gender", df['gender'].unique())
filtered_df = df[df['gender'] == selected_gender]

st.subheader(f"Churn Distribution for {selected_gender}")
churn_counts = filtered_df['Churn'].value_counts()
st.bar_chart(churn_counts)

if st.checkbox("Show raw data"):
    st.write(filtered_df.head())
