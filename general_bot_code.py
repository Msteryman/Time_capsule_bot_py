import nextcord 
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from token_ import token
bot = commands.Bot()
guild_id_ = 1011627983410303046 # Сюда надо ввести id дс сервера
@bot.event


async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})') # Дает понять что бот заработал 
    print('------')

@bot.slash_command(name = 'test', description="тест") # создания слешь команды kus_math
async def test(interaction: Interaction,a: str): # создания функцию которая принимает аргумент task из kus_math
    await interaction.response.send_message("ы")

bot.run(token)