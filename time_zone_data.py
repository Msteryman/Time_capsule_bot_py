import sqlite3

def create_table_todo(): # Создание таблицы при запуске скрипта
    
    conn = sqlite3.connect('time_date.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS time_date( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        User_id INTEGER,
        msg text,   
        date text
    )""")
    conn.commit()
    conn.close()
create_table_todo()