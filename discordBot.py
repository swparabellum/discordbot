
"""
2023년 12월 25일 강승우
디스코드봇 소스코드.
"""

import discord
from datetime import datetime
import time

from discord.ext import commands

#날씨를 불러오기 위한 모듈
#https://smstudyroom.tistory.com/27
import requests
import json
import datetime as dt
# https://www.data.go.kr/iim/api/selectAPIAcountView.do

# https://yunwoong.tistory.com/212

# https://yunwoong.tistory.com/214

TOKEN = 'MTE4Njg0NzUzOTU2ODMxNjUwNg.GvfZ7M.O7Yk8SDAgdiY2JOaGgJcMUWzCmi44dfpCeaH-w'
CHANNEL_ID = '338962613775892491'





class MyClient(discord.Client):


    client = commands.Bot(command_prefix='/')  

    async def on_ready(self):
        
        channel = self.get_channel(int(CHANNEL_ID))
        
        nowTime = datetime.today().strftime("%H시 %M분 %S초 가동")
        await channel.send(nowTime)
    
    async def on_message(self,message):
        if message.content == '!ping':
            await message.channel.send('pong {0.author.mention}'.format(message))

        if message.content == '!날씨':
            dateTime = dt.datetime.now() - dt.timedelta(hours = 1)

            getDate = dateTime.strftime("%Y%m%d")
            getTime = dateTime.strftime("%H00")
            await message.channel.send('오늘 서울시 06시의 기온은... '+self.getTemp()+' 도 입니다. {0.author.mention}'.format(message))

    def getTemp(self):
        # https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084
        # 초단기예보조회 사용중.
        dateTime = dt.datetime.now() - dt.timedelta(hours = 1)

        #'23.12.25 09:30 강승우
        # !날씨 서울 일경우 로케이션딕에서 서울 좌표를 가져올 수 있도록 추가하기...
        locationDic = {'서울':'nx=60&ny=127','부산':'nx=98&ny=76'}

        getDate = dateTime.strftime("%Y%m%d")
        getTime = dateTime.strftime("%H00")
        # &nx=60&ny=127 -> 서울시
        #부산시 - > 98, 76
        serviceKey= 'FRwmNG97jOhkLCeTd1P4fHx%2B5nf8Dx6SfFQV%2BBAMuc873IjQux3Fe6gC134S%2Fjdgs1XziXTjYfXe0qYeb9IvFQ%3D%3D'
        api ="http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey="+serviceKey+"&numOfRows=1&pageNo=1&base_date="+getDate+"&base_time=0500&nx=60&ny=127&dataType=JSON"

        print(api)

        result = requests.get(api)
        data = json.loads(result.text) #json 타입으로 변경시켜줌
        print(data)
        output= data["response"]["body"]["items"]["item"]
        print(output)
                #온도만 잘라서 넣게... 
                #리스트안에 딕셔너리 있어서 뽑는다...
        for i in output:
                out=i["fcstValue"]
            
        return out
    
    @client.command(name='날씨')
    async def getWeather(ctx):
         await ctx.send("날씨를알려드립니다.")



intents = discord.Intents.default()

intents.message_content = True

client = MyClient(intents=intents)

client.run(TOKEN)