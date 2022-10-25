import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('MTAzNDIzNjk5Mzk1NTE2ODI2Nw.GYw_M_.qyje5S5SSCA0LHL-hTiB693dZLzUd65FrXaZSw')
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#client.run(token)
#Keep this last line commented until tasks are complete!
