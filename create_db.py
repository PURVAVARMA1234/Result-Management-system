import sqlite3
def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charge INTEGER, description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student( rollno INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, state text, city text, DOB  INTEGER,pincode integer,  gender text, course text , address text,date integer,contact integer)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result( rid INTEGER PRIMARY KEY AUTOINCREMENT, student text, name text, course text, marks INTEGER, fullmark INTEGER, per REAL)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS Report( rid INTEGER PRIMARY KEY AUTOINCREMENT, student text, name text, course text, marks INTEGER, fullmark INTEGER, per REAL)")
    con.commit()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,email TEXT UNIQUE,password TEXT)""")
    con.commit()
    
create_db()   
