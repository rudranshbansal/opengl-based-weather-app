import streamlit as st
import requests
import json
import streamlit.components.v1 as components

st.title("Weather App") # Displays title
st.subheader("Exploring RapidAPI's weather Endpoints") # Displays subheader

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
    'X-RapidAPI-Key': '9313132d8bmsh3b12348597c1003p19f0dcjsn74c0ee15b248',
    'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
}

location = st.text_input("Enter the location", "Chennai")
querystring = {"q":{location}}

response = requests.request("GET", url, headers=headers, params=querystring)
result = response.text

data = json.loads(result)

st.json(data)

col1, col2 = st.columns(2)

with col1:
    st.write(f'Name: {data["location"]["name"]}')
    st.write(f'Region: {data["location"]["region"]}')
    st.write(f'Country: {data["location"]["country"]}')
    st.write(f'Local Time: {data["location"]["localtime"]}')
    st.metric(label="wind_kph", value= f'{data["current"]["wind_kph"]}')
    st.write(f'Feels like: {data["current"]["feelslike_c"]} ℃')

with col2: 
    st.write(f'Temp in Celcius: {data["current"]["temp_c"]}')
    st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
    st.write(f'Condition: {data["current"]["condition"]["text"]}')
    st.image(f'http:{data["current"]["condition"]["icon"]}')
    st.metric(label = "Humidity", value = f'{data["current"]["humidity"]}')
    
st.info('⛅ Current weather or realtime weather API method allows a user to get up-to-date current weather information in json and xml. The data is returned as a Current Object.')

components.html(
    """
    <a href="https://www.weatherapi.com/" title="Free Weather API"><img src='//cdn.weatherapi.com/v4/images/weatherapi_logo.png' alt="Weather data by WeatherAPI.com" border="0" target="_blank"></a>
    """
)
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 