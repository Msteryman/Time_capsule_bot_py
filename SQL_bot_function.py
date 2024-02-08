

import sqlite3

from bot_function import date_difference




def create_table_todo(): # Создание таблицы при запуске скрипта
    
    conn = sqlite3.connect('user_date.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_date( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        User_id INTEGER,
        msg text,   
        date text
    )""")
    conn.commit()
    conn.close()

def insert_table(User_id: str, msg: str, date: str): # Создание функция для добавления в таблицу 
    """Добавляет инфу о юзере в таблицу"""
    conn = sqlite3.connect('user_date.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_date(User_id, msg, date) VALUES(?,?,?)", (User_id, msg, date))
    conn.commit()
    conn.close()

def del_in_data(record_id): # Удаления строки из базы 
    conn = sqlite3.connect('user_date.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_date WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

create_table_todo()