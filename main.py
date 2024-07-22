import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next Days")
place = st.text_input("place: ")
days = st.slider("forecast days", min_value = 1,max_value=5,
                 help ="select the number of days")
option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option}for the next {days} days at {place}")



d, t = get_data(place, days, option)

figure = px.line(x=d,y=t, labels = {"x": "date","y":"temperature"} )
st.plotly_chart(figure)





