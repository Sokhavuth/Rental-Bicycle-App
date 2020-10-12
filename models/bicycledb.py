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

  cursor.execute("SELECT ROWID, * from BICYCLE")

  bicycles = cursor.fetchall()
  
  conn.commit()
  conn.close()

  return bicycles

def edit(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("SELECT ROWID, * from BICYCLE WHERE ROWID = " + str(id))

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

def amountPlus(*args):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql = "UPDATE BICYCLE SET AMOUNT= AMOUNT+1 WHERE ROWID=?"
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()

def amountMinus(*args):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql = "UPDATE BICYCLE SET AMOUNT= AMOUNT-1 WHERE ROWID=?"
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()

def delete(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("DELETE FROM BICYCLE WHERE ROWID=?", (id,))

  conn.commit()
  conn.close()

def sort(brand):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  cursor.execute("SELECT ROWID, * from BICYCLE ORDER BY " + brand)
  bicycles = cursor.fetchall()

  conn.commit()
  conn.close()

  return bicycles

def search(query):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  sql = "SELECT ROWID, * from BICYCLE WHERE BRAND LIKE '%"+query+"%'"
  sql += " OR COUNTRY LIKE '%"+query+"%'"
  sql += " OR YEAR LIKE '%"+query+"%'"
  sql += " OR AMOUNT LIKE '%"+query+"%'"
  sql += " OR PRICE LIKE '%"+query+"%'"

  cursor.execute(sql)
  bicycles = cursor.fetchall()

  conn.commit()
  conn.close()

  return bicycles