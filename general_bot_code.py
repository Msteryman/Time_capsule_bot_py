
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from token_ import token
from SQL_bot_function import insert_table
import threading
import time
from bot_function import date_difference
from SQL_bot_function import create_table_todo, del_in_data
import sqlite3



def dif_in_data():
    a = False
    user_id = ''
    msg = ''
    while True:
        if a == True:
            async def send_message(user_id, message):
                await user_id.send(message)
            a = False
        conn = sqlite3.connect('user_date.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_date")
        records = cursor.fetchall()
        conn.close()

        for i in records:
            print("s")
            if date_difference(i[-1]) == 'null':
                del_in_data(i[0])
                a = True
                user_id = i[1]
                msg = i[2]
        time.sleep(60)



infinite_thread = threading.Thread(target=dif_in_data)
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
                data: str = SlashOption(description="Укажите дату в виде ГГГГ.ММ.ДД чч:мм:cc 'в 24 часовом формате' ") , 
                ): 
    
    User_id = interaction.user 
    print(User_id)
    insert_table(str(User_id),str(msg),str(data))


                

bot.run(token)




