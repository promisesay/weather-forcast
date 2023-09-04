import streamlit as st
import plotly.express as plotly
from backend import get_data


# adding options
st.header("weather forcast for the future days")

place = st.text_input("place:")

slid_bar = st.slider("forcast days:", min_value=1, max_value=5,
                     help="the amount of future days data that will be calculated")

weather = st.selectbox("select data to view", ("temperature", "sky"))

st.subheader(f"{weather} of {place} in next {slid_bar} days:")


# getting the data and times of the day
if place:
    try:
        data = get_data(place=place, forcast_days=slid_bar)

        if weather == "temperature":
            temp = [dict["main"]["temp"] / 10 for dict in data]
            time = [dict["dt_txt"] for dict in data]
            nem = {"temperature": temp, "time of the day": time}
            figur = plotly.line(x=time, y=temp, labels=nem)
            st.plotly_chart(figur)

        if weather == "sky":
            data = [dict["weather"][0]["main"] for dict in data]
            #        time = [dict["dt_txt"] for dict in data]
            conditions_paths = {"Clear": "images/clear.png", "cloud": "images/clear.png",
                                "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [conditions_paths[conditions] for conditions in data]
            print(conditions_paths)
            print(sky_conditions)
            st.image(image=sky_conditions, width=112)
    except KeyError:
        st.header(body="what the fuck is that :+1", help="check your place input")
