import sqlite3

def connect():
    conn= sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer,ibsn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,ibsn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,ibsn))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def search(title="",author="",year="",ibsn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or ibsn=?",(title,author,year,ibsn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,ibsn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=? , author=? , year=? , ibsn=? WHERE id=?",(title,author,year,ibsn,id))
    conn.commit()
    conn.close()


connect()
# insert("atomic habits","shia",'2002','12')
# id = search(title="",author="shia",year="",ibsn="")[0][0]
# delete(id)
# update(1,"elasticsearch","shiawase","1220","12")
print(view())