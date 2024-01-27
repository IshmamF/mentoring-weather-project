from dotenv import load_dotenv
import os
import requests
from geopy.geocoders import GoogleV3
from text2image import generate_image
import streamlit as st

load_dotenv()
API_KEY = os.getenv('WEATHER_API')
GOOGLE_API = os.getenv('GOOGLE_API')
geolocator = GoogleV3(api_key=GOOGLE_API)

st.title("Weather Image")

user_input = st.text_input('Provide Location Below')
submit = st.button("Submit", type="primary")

# Use for demonstration
# CITY = 'London'
# url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"


if user_input and submit:
    location = geolocator.geocode(user_input)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={API_KEY}"
    response = requests.get(url).json()

    city = response['name'] 
    weather = response["weather"][0]["main"]
    country = response["sys"]["country"]
    description = response["weather"][0]["description"]

    image_url = generate_image(city, weather, country, description)
    st.image(image_url, caption=f"{weather} in {location},{country}")
    st.map(latitude=location.latitude, longitude=location.longitude)


