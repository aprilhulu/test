import discord
from discord import app_commands
import requests
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
API = os.getenv("API_KEY")
AGENT = os.getenv("AGENT_KEY")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期
 
@tree.command(name="test",description="テストコマンドです。")
async def gpd(interaction: discord.Interaction,text:str=None):
    await interaction.response.defer()
    url = "https://api-mebo.dev/api"
    headers = {'content-type': 'application/json'}
    item_data = {
      "api_key": API,
      "agent_id": AGENT,
      "utterance": text
  }
    r = requests.post(url,json=item_data,headers=headers)
    print(r)
    print(r.json()["utterance"])
    print(r.json()["bestResponse"]["utterance"])
    e=r,r.json()["utterance"],r.json()["bestResponse"]["utterance"]
    await interaction.followup.send(e)
client.run(TOKEN)
