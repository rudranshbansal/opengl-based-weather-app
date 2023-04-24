import streamlit as st
import requests
import json
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="Weather Wiz", page_icon=":partly_sunny:", layout="wide")

def add_bg_from_filesystem():
    video_path = "./animations/sun_rain.mp4"
    video_file = open(video_path, 'rb')
    video_bytes = video_file.read()
    #st.set_page_config(page_title="Weather Wiz", page_icon=":partly_sunny:", layout="wide")
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url(data:image/mp4;base64,{video_bytes.decode('latin-1')});
            background-size: cover;
            background-repeat: no-repeat;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_filesystem()

st.title("Weather Wiz")
st.subheader("Weather around the world at your doorstep!!")

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
    'X-RapidAPI-Key': '9313132d8bmsh3b12348597c1003p19f0dcjsn74c0ee15b248',
    'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
}

location = st.text_input("Enter the location", "Patiala")
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
    st.write(f'Temp in Celsius: {data["current"]["temp_c"]}')
    st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
    st.write(f'Condition: {data["current"]["condition"]["text"]}')
    st.image(f'http:{data["current"]["condition"]["icon"]}')
    st.metric(label = "Humidity", value = f'{data["current"]["humidity"]}')
    
st.info('⛅ Weather_Wiz is our Computer Graphics Project. It is aimed at providing visualizations of the real-time weather conditions using opengl concepts taught to us in this subject.')


video_file = open('./animations/sun_rain.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
image = Image.open('thapar_bg_logo.png')
st.image(image)
components.html(
    """
    <a href="https://rudranshbansal.github.io/" title="Our previous project">For More Info Click Here</a>
    """
)