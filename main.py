import streamlit as st
import requests

# Account Email: farukh.mushtaq@gmail.com
# Account ID: 1f6c6a2d-bb02-4aea-b9b7-fb10857a7358
# API Key NASA: Hh27AU7km8deDrquSEUU93TviJ8Z4q2H6RNGb8oC
# API APOD, Astronomy Picture of the Day.
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

API_KEY = "Hh27AU7km8deDrquSEUU93TviJ8Z4q2H6RNGb8oC"
start_end_date = "&start_date=2024-05-10&end_date=2024-05-19"
URL = "https://api.nasa.gov/planetary/apod?api_key="+API_KEY+start_end_date



req = requests.get(URL)
content = req.json()
print(content)
print(type(content))


for data in content:
    if data['media_type'] == "image":
        st.title(data['title'])
        st.subheader(data['date'])
        st.write(data['explanation'])
        st.image(data['url'])
        imgName = data['date']+'.png'
        imgData = requests.get(data['url'])

        with open(imgName, 'wb') as file: #wb= web binary
            file.write(imgData.content)
