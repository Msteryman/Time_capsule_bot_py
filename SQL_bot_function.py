import sqlite3 
conn = sqlite3.connect('user_date.db')
cursor = conn.cursor() 

 
def create_table_todo(): 
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_date( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        User_id text,
        msg text,   
        date text
    )""") 
    

def insert_table(User_id, msg, date): 
    cursor.execute("INSERT INTO user_date( User_id, msg, date) VALUES(?,?,?)", (User_id, msg, date)) 
    conn.commit() # save data in DB 
    

def getMetaData():
    cursor.execute("PRAGMA table_info(user_date)") 
    fields = cursor.fetchall() 
    for field in fields: 
        print(field[1]) 
    
def get_Data():
    cursor.execute("SELECT * FROM user_date")
    records = cursor.fetchall()
    print(records)
    
create_table_todo()


