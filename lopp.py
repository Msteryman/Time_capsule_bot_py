import threading
import time
from bot_function import date_difference
from SQL_bot_function import create_table_todo, del_in_data
import sqlite3


def dif_in_data():
    while True:
        conn = sqlite3.connect('user_date.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_date")
        records = cursor.fetchall()
        conn.close()

        for i in records:
            print("s")
            if date_difference(i[-1]) == 'null':
                del_in_data(i[0])
                print('Ы')
        time.sleep(60)
create_table_todo()


infinite_thread = threading.Thread(target=dif_in_data)
infinite_thread.start()
print('s')