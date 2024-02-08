
from nextcord import Interaction, SlashOption # Импорты
import nextcord
from nextcord.ext import commands
from token_ import token
from SQL_bot_function import insert_table
import threading
import time
from bot_function import date_difference
from SQL_bot_function import create_table_todo, del_in_data
import sqlite3
import asyncio

bot = commands.Bot()
def dif_in_data(): # создания бесконечного цыкла для перебора Данных в sql таблице
    while True:
        conn = sqlite3.connect('user_date.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_date")
        records = cursor.fetchall()
        conn.close()

        for i in records:
            print("s")
            if date_difference(i[-1]) == 'null':
                asyncio.run_coroutine_threadsafe(send_msg(i[1],i[2]), bot.loop)
                del_in_data(i[0])
        time.sleep(60)


async def send_msg(user_id: int,msg: str):
    """Отпраляет сообщения в лс пользователю """
    user = await bot.fetch_user(user_id) 
    await user.send(msg)

infinite_thread = threading.Thread(target=dif_in_data) # Создания нового потока
infinite_thread.start()

bot = commands.Bot()
guild_id_ = 1011627983410303046 # Сюда надо ввести id дс сервера
@bot.event


async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})') # Дает понять что бот заработал 
    print('------')



@bot.slash_command( name = 'time_capsule', description="Отпраляет сообщения в будущая ",guild_ids=[guild_id_ ]) # создания слешь команды time_capsule
async def test(interaction: Interaction,
                msg: str = SlashOption(description="введите сообщения которая вы хотите прислать себе в будущая ") ,
                data: str = SlashOption(description="Укажите дату в виде ГГГГ.ММ.ДД чч:мм:cc в 24 часовом формате' "), 
                time_zon: int =  SlashOption(choices = {'23кпваааааааааааааааааааааааааааааааааааааааааааааааааааа': 12, "2": 32} , description="Укажите часовой поес по UTC Вводите только число плюсов не надо. 'По умалчанию равно UTC + 0'"), 
                ): 
    print(time_zon)
    User_id = interaction.user
    User_id = User_id.id # определяет id юзера 
    print(User_id)
    try:
        date_difference(str(data))
        insert_table(int(User_id),str(msg),str(data)) # отправляет id сообщения и дату 
        await interaction.response.send_message('Сообщения успешно принято.')
    except ValueError:
        await interaction.response.send_message('Ты вел что-то не так. проверь правильность написания даты  ')




# Обработчик нажатия на кнопку

bot.run(token)




