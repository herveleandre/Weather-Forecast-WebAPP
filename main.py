import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox("Select Data Below", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")





d, t = get_data(days)

figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
