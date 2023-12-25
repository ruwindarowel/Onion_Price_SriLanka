import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('prices_data_filled.csv')

# Convert 'Date' column to datetime if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Create a Streamlit sidebar for user input
st.sidebar.title("Onion Price Visualization")
selected_onion_type = st.sidebar.selectbox("Select Onion Type", df['Onion Type'].unique())
selected_price_type = st.sidebar.selectbox("Select Price Type", ['Wholesale_Pettah', 'Wholesale_Dambulla', 'Retail_Pettah', 'Retail_Dambulla'])

# Filter the data based on user selection
filtered_df = df[(df['Onion Type'] == selected_onion_type)]

# Create Plotly line chart for daily prices
fig_line_chart = px.line(filtered_df, x='Date', y=selected_price_type, title=f'{selected_onion_type} - {selected_price_type} Prices Over Time', line_shape='linear', color_discrete_sequence=px.colors.qualitative.Set1)

# Calculate monthly average prices
monthly_avg_df = filtered_df.resample('M', on='Date')[selected_price_type].mean().reset_index()

# Create Plotly bar chart for monthly averages
fig_monthly_avg = px.bar(monthly_avg_df, x='Date', y=selected_price_type, title=f'Monthly Average {selected_onion_type} - {selected_price_type} Prices', color_discrete_sequence=px.colors.qualitative.Set2)

# Streamlit app layout
st.title("Onion Price Visualization App")

# Line chart
st.plotly_chart(fig_line_chart)

# Monthly average bar chart
st.header(f'Monthly Average {selected_onion_type} Prices')
st.plotly_chart(fig_monthly_avg)
