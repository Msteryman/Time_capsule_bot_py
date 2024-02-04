

import sqlite3

from bot_function import date_difference

# Создание таблицы при запуске скрипта


def create_table_todo():
    conn = sqlite3.connect('user_date.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_date( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        User_id text,
        msg text,   
        date text
    )""")
    conn.commit()
    conn.close()

def insert_table(User_id, msg, date):
    conn = sqlite3.connect('user_date.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_date(User_id, msg, date) VALUES(?,?,?)", (User_id, msg, date))
    conn.commit()
    conn.close()

def del_in_data(record_id):
    conn = sqlite3.connect('user_date.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_date WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

create_table_todo()