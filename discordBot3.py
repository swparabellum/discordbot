from discord.ext import commands
import discord
client = discord.Client()

            #https://softvanilla.github.io/discordbot/discord_%EB%AA%85%EB%A0%B9%EC%96%B4_%EB%A7%8C%EB%93%A4%EA%B8%B0/
            #https://gihyeon.tistory.com/1

TOKEN = 'MTE4Njg0NzUzOTU2ODMxNjUwNg.GvfZ7M.O7Yk8SDAgdiY2JOaGgJcMUWzCmi44dfpCeaH-w'
CHANNEL_ID = '338962613775892491'

class Weather(discord.Client):

    @client.event
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        print("ready!")

    
intents = discord.Intents.default()
intents.message_content = True
client = Weather(intents=intents)
client.run(TOKEN)