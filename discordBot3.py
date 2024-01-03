from discord.ext import commands

client = commands.Bot(command_prefix='/')

            #https://softvanilla.github.io/discordbot/discord_%EB%AA%85%EB%A0%B9%EC%96%B4_%EB%A7%8C%EB%93%A4%EA%B8%B0/
            #https://gihyeon.tistory.com/1

TOKEN = 'MTE4Njg0NzUzOTU2ODMxNjUwNg.GvfZ7M.O7Yk8SDAgdiY2JOaGgJcMUWzCmi44dfpCeaH-w'
CHANNEL_ID = '338962613775892491'

class Weather():

    def __init__(self):


    @client.event
    async def on_ready():
        print("ready!")

    
client.run(TOKEN)