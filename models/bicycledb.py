#\models\bicycledb.py
import sqlite3

def insert(*bicycle):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql ='''CREATE TABLE IF NOT EXISTS BICYCLE(
    BRAND TEXT,
    COUNTRY TEXT,
    YEAR INT,
    AMOUNT INT,
    PRICE FLOAT
  )
  '''

  cursor.execute(sql)

  cursor.execute("INSERT INTO BICYCLE VALUES (?, ?, ?, ?, ?)", bicycle)
  
  conn.commit()
  conn.close()


def select():
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql ='''CREATE TABLE IF NOT EXISTS BICYCLE(
    BRAND TEXT,
    COUNTRY TEXT,
    YEAR INT,
    AMOUNT INT,
    PRICE FLOAT
  )
  '''

  cursor.execute(sql)

  cursor.execute("SELECT * from BICYCLE")

  bicycles = cursor.fetchall()
  
  conn.commit()
  conn.close()

  return bicycles

def edit(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("SELECT * from BICYCLE WHERE ROWID = " + str(id))

  bicycle = cursor.fetchone()
  
  conn.commit()
  conn.close()

  return bicycle


def update(*args):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql = "UPDATE BICYCLE SET BRAND=?, COUNTRY=?, YEAR=?, AMOUNT=?, PRICE=? WHERE ROWID=?"
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()

def delete(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("DELETE FROM BICYCLE WHERE ROWID=?", (id,))

  conn.commit()
  conn.close()