# simple discord py bot

import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)

@client.event
async def on_ready():
    print(f'We have logged on as {client.user}')
    await tree.sync(guild=discord.Object(id=216649835133009922))
    print("Commands Readied!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@tree.command(name="remindme",
              description="Pings the user who calls in a specified time "
                          "with a reference to the message sent before the command",
              guild=discord.Object(id=216649835133009922)
              )
async def reminder(interaction):
    await interaction.response.send_message("Command Received")




# token inside bracket
client.run("OTA2NDA2NDUzMTczMTg2NTYw.GKY5C6.4Wic60iIXYg68hILjmscYMztQ658teX0Py80Vs")

