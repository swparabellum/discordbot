
"""
2023년 12월 30일 강승우
디스코드봇 소스코드.
"""
from discord.ext import commands
import discord
from datetime import datetime
import time

#날씨를 불러오기 위한 모듈
#https://smstudyroom.tistory.com/27
import requests
import json
import datetime as dt

TOKEN = '토큰을여기에입력해넣을것'
CHANNEL_ID = '338962613775892491'

class MyClient(discord.Client):

    

    async def on_ready(self):
        
        channel = self.get_channel(int(CHANNEL_ID))
        
        nowTime = datetime.today().strftime("%H시 %M분 %S초 가동")
        await channel.send(nowTime)
    
    async def on_message(self,message):
        if message.content == '!날씨':
            #인자값도 받게 하려면?
            #https://softvanilla.github.io/discordbot/discord_%EB%AA%85%EB%A0%B9%EC%96%B4_%EB%A7%8C%EB%93%A4%EA%B8%B0/
            #https://gihyeon.tistory.com/1
            dateTime = dt.datetime.now() - dt.timedelta(hours = 1)

            getDate = dateTime.strftime("%Y%m%d")
            getTime = dateTime.strftime("%H00")
            
            
            #출처: https://developertools.tistory.com/entry/PYHTON-파이썬-OpenWeatherMap-api-이용하여-날씨-확인하기-OpenWeatherMap [개발자도구:티스토리]
            city_name = 'Seoul'
            api_key = '1ae441ee91fd8b672d19bab8e4b605e1'
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
            'q' : city_name,
            'appid' : api_key,
            'units' : 'metric' #섭씨로 결과를 얻기위해 미터릭 사용.
            }
            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp']
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                print(f"도시: {city_name}")
                print(f"온도: {temperature}")
                print(f"습도: {humidity}")
                print(f"기압: {pressure}")
                print(f"날씨: {report[0]['description']}")
                
                nowTime = datetime.today().strftime("%H시 %M분")
                city = {'Seoul':'서울','Busan':'부산'}

                await message.channel.send("오늘 "+city[city_name]+"시, "+nowTime+"의 온도는 "+str(temperature)+"이며 습도는"+str(humidity)+"% 이며 날씨는 "+report[0]['description']+ "입니다.")
            else:
                print("Error in the HTTP request")
                await message.channel.send("ERROR: Error in the HTTP request")
            

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)