import matplotlib.pyplot as plt
import streamlit as st

st.title('Data Visualization App') 
st.header('Create a Bar Chart')

# Get user input
x_labels = st.text_input('Enter data separated by comma for x-axis:')
y_values = st.text_input('Enter data separated by comma for y-axis:')

# Convert the data to list
x_list = x_labels.split(",")
y_list = [int(i) for i in y_values.split(",")]

# Draw the chart
plt.bar(x_list, y_list)

# Render the chart with matplotlib
st.pyplot()