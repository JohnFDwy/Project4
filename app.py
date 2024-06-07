import streamlit as st
import pandas as pd
import plotly.express as px
import altair as al

data= pd.read_csv('vehicles_us.csv')
data['model_year'].fillna(data['model_year'].median(), inplace=True)
data['cylinders'].fillna(data['cylinders'].mode()[0], inplace=True)
data['odometer'].fillna(data['odometer'].median(), inplace=True)
data['paint_color'].fillna('unknown', inplace=True)
data['is_4wd'].fillna(0, inplace=True)

st.header('Vehicles\' Price by Mileage')

Q1_price = data['price'].quantile(0.25)
Q3_price = data['price'].quantile(0.75)
IQR_price = Q3_price - Q1_price

Q1_odometer = data['odometer'].quantile(0.25)
Q3_odometer = data['odometer'].quantile(0.75)
IQR_odometer = Q3_odometer - Q1_odometer


lower_bound_price = Q1_price - 1.5 * IQR_price
upper_bound_price = Q3_price + 1.5 * IQR_price

lower_bound_odometer = Q1_odometer - 1.5 * IQR_odometer
upper_bound_odometer = Q3_odometer + 1.5 * IQR_odometer


data = data[(data['price'] >= lower_bound_price) & (data['price'] <= upper_bound_price)]
data = data[(data['odometer'] >= lower_bound_odometer) & (data['odometer'] <= upper_bound_odometer)]

print(data.shape)

fig = px.scatter(data, x='price', y='odometer', title='Price vs Odometer (Outliers Removed)')

st.header('Price vs Odometer Scatterplot')
st.plotly_chart(fig)

fig5 = px.histogram(data, x='price', y='odometer', title= 'Price vs Odometer Histogram')

st.plotly_chart(fig5)

agree = st.checkbox("I want to see a sample of the dataset")

if agree:
    st.write(data.sample(5))