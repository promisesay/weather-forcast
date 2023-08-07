import streamlit as st


st.title = "weather forcast for the next days"

place = st.text_input("place:")

slid_bar = st.slider("forcast days:", min_value=1, max_value=5,
                     help="the amount of future days data that will be calculated")

weather = st.selectbox("select data to view", ("sky", "weather"))

st.header(f"{weather} of {place} in next {slid_bar} days:")
