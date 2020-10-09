#\models\customerdb.py
import sqlite3

def insert(*customer):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql ='''CREATE TABLE IF NOT EXISTS CUSTOMER(
    NAME TEXT,
    PHONE TEXT
  )
  '''

  cursor.execute(sql)

  cursor.execute("INSERT INTO CUSTOMER VALUES (?, ?)", customer)
  
  conn.commit()
  conn.close()


def select():
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql ='''CREATE TABLE IF NOT EXISTS CUSTOMER(
    NAME TEXT,
    PHONE TEXT
  )
  '''

  cursor.execute(sql)

  cursor.execute("SELECT ROWID, * from CUSTOMER")

  customers = cursor.fetchall()
  
  conn.commit()
  conn.close()

  return customers

def edit(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("SELECT ROWID, * from CUSTOMER WHERE ROWID = " + id)

  customer = cursor.fetchone()
  
  conn.commit()
  conn.close()
  
  return customer


def update(*args):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql = "UPDATE CUSTOMER SET NAME=?, PHONE=? WHERE ROWID=?"
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()

def delete(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("DELETE FROM CUSTOMER WHERE ROWID=?", (id,))

  conn.commit()
  conn.close()

def sort(key):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  cursor.execute("SELECT ROWID, * from CUSTOMER ORDER BY " + key)
  customers = cursor.fetchall()

  conn.commit()
  conn.close()

  return customers

def search(query):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  sql = "SELECT ROWID, * from CUSTOMER WHERE NAME LIKE '%"+query+"%'"
  sql += " OR PHONE LIKE '%"+query+"%'"

  cursor.execute(sql)
  customers = cursor.fetchall()

  conn.commit()
  conn.close()

  return customers