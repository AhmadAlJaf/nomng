import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import asyncio
from discord import File
from discord.player import AudioSource


TOKEN = os.environ['TOKEN']  # Replace with your actual token
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'mango' in message.content.lower():
        await message.channel.send('no mango', file=discord.File('image.jpg'))

        if message.author.voice:
            channel = message.author.voice.channel
            if channel:
                try:
                    voice_client = await channel.connect()
                    voice_client.play(discord.FFmpegPCMAudio('nomango.mp3'))

                    while voice_client.is_playing():
                        await asyncio.sleep(1)
                    await asyncio.sleep(1)  # Brief delay before disconnecting
                    await voice_client.disconnect()
                except Exception as e:
                    print(f"Error in playing audio: {e}")

bot.run(TOKEN)
