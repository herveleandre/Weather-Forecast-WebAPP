import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox("Select Data Below", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:

        filter_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]

            figure = px.line(x=dates, y=temperature,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}

            sky_condition = [dict["weather"][0]["main"] for dict in filter_data]
            image_path = [images[condition] for condition in sky_condition]
            print(sky_condition)
            st.image(image_path, width=80)
except KeyError:
    (st.subheader(f"{place} is not on the list"))
