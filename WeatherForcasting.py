from gtts import gTTS
import requests
import socket
import datetime as dt
import random
import os 
import time

url = 'http://api.ipstack.com/49.35.247.214?access_key=/*EDIT_YOUR ACCESS_KEY*/'
js = requests.get(url).json()


api_addr='http://api.openweathermap.org/data/2.5/forecast?id=524901&Appid=02f555e5400bca1a30a29d63a4f099c5&q='

city=js['city']

url = api_addr+city


json_data = requests.get(url).json()
formatted_data = json_data['city']['name']

weather_data = json_data['list'][0]['weather'][0]['main']

desc = json_data['list'][0]['weather'][0]['description']

wind_speed = json_data['list'][0]['wind']['speed']

sys_date = json_data['list'][0]['dt_txt']
wind_speed=str(wind_speed)
period = 'afternoon'
mytext = 'Good '+period+' Amit here is todays Weather infomation it is  '+weather_data+' atmosphere outside. wind speed is '+wind_speed+'per hour atmosphere is '+desc

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
import datetime
x=datetime.datetime.today().strftime('%Y-%m-%d')
x=str(x)
file_name="Weather forcast "+x+".mp3"

myobj.save(file_name) 

os.system("mpg321"+file_name) 
