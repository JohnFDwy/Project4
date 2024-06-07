import streamlit as st
import pandas as pd
import plotly.express as px
import altair as al

data= pd.read_csv('vehicles_us.csv')

st.header('Vehicles\' Price by Mileage')

st.write(data.head())