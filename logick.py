import sqlite3 



db = sqlite3.connect('tasker.db')
sql = db.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS tasker (name TEXT, text TEXT)")
db.commit()

def create_task(name_task, text_task): 

    sql.execute("SELECT name, text FROM tasker")
    sql.execute(f"INSERT INTO tasker VALUES ('{name_task}','{text_task}')")
    db.commit() 

#def update_task(): 
    #new_text = input()
    #sql.execute(f"UPDATE tasker SET text = '{new_text}' WHERE name = '{name_task}' ") 
    #db.commit() 

def view_task(): 
    mitems = []
    for i in sql.execute('SELECT name, text FROM tasker'): 
        mitems.append(i)
    return mitems
        
def get_task_text(name): 
    
    name = sql.execute(f"SELECT name, text FROM tasker WHERE name = '{name}'")
    for i in name : 
        print(i)
    
    return i       
        

def delete_task(name): 
    sql.execute(f"DELETE FROM tasker WHERE name = '{name}'")
    db.commit()

#create_task("ультра","мега")
#get_task_text("ультра")