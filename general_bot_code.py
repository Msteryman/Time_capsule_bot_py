import nextcord 
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from token_ import token
import datetime
from SQL_bot_function import insert_table
bot = commands.Bot()
guild_id_ = 1011627983410303046 # Сюда надо ввести id дс сервера
@bot.event


async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})') # Дает понять что бот заработал 
    print('------')


@bot.slash_command( name = 'time_capsule', description="Отпраляет сообщения в будущая ",guild_ids=[guild_id_ ]) # создания слешь команды time_capsule
async def test(interaction: Interaction,
                msg: str = SlashOption(description="введите сообщения которая вы хотите прислать себе в будущая ") ,
                data: str = SlashOption(description="Укажите дату в виде ГГГГ.ММДД чч:мм:cc 'в 24 часовом формате' ") , 
                ): 
    
    User_id = interaction.user 
    print(User_id)
    insert_table(str(User_id),str(msg),str(data))

bot.run(token)
