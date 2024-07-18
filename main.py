import streamlit as st
import plotly.express as px


st.title("Weather forecast for the next Days")
place = st.text_input("place: ")
days = st.slider("forecast days", min_value = 1,max_value=5,
                 help ="select the number of days")
option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option}for the next {days} days at {place}")


def  get_data(days):
    dates = ["22-10-1880","23-10-1880","24-10-1880"]
    temperatures = [10,13,15]
    temperatures = [days * i for i in temperatures]
    return dates , temperatures

d, t = get_data(days)
figure = px.line(x=d,y=t, labels = {"x": "date","y":"temperature"} )
st.plotly_chart(figure)





