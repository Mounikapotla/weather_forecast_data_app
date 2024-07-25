import streamlit as st
import plotly.express as px
from backend import get_data

#add title ,place,slider, option and subheader
st.title("Weather forecast for the next Days")
place = st.text_input("place: ")
days = st.slider("forecast days", min_value = 1,max_value=5,
                 help ="select the number of days")
option = st.selectbox("select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option}for the next {days} days at {place}")

if place:

# Get the Temperature/sky data
 filtered_data = get_data(place, days)

# if option is Temperature
 if option == "Temperature":
     temperatures = [dict["main"]["temp"] for dict in filtered_data]
     dates = [dict["dt_txt"] for dict in filtered_data]
     figure = px.line(x=dates,y=temperatures, labels = {"x": "date","y":"Temperature(c)"} )
     st.plotly_chart(figure)

 if option == "Sky":
    images = {"Clear":"images/clear.png","Clouds":"images/cloud.png", "Rain":"images/rain.png",
              "Snow":"images/snow.png"}
    sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
    image_paths = [images[condition] for condition in sky_conditions ]
    print(sky_conditions)
    st.image(image_paths,width=115)





