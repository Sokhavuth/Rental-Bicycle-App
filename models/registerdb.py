#\models\registerdb.py
import sqlite3

def insert(*register):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql ='''CREATE TABLE IF NOT EXISTS REGISTER(
    ID INT,
    CUSTOMER TEXT,
    BRAND TEXT,
    RENTDATE DATE,
    RETURNDATE DATE
  )
  '''

  cursor.execute(sql)

  cursor.execute("INSERT INTO REGISTER VALUES (?, ?, ?, ?, ?)", register)
  
  conn.commit()
  conn.close()


def select():
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql ='''CREATE TABLE IF NOT EXISTS REGISTER(
    ID INT,
    CUSTOMER TEXT,
    BRAND TEXT,
    RENTDATE DATE,
    RETURNDATE DATE
  )
  '''

  cursor.execute(sql)

  cursor.execute("SELECT ROWID, * from REGISTER")

  registers = cursor.fetchall()
  
  conn.commit()
  conn.close()

  return registers

def setReturnDate(*args):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql = "UPDATE REGISTER SET RETURNDATE=? WHERE ROWID=?"
  
  cursor.execute(sql, args)
  
  conn.commit()
  conn.close()

def delete(id):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  cursor.execute("DELETE FROM REGISTER WHERE ROWID=?", (id,))

  conn.commit()
  conn.close()

def sort(key):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  cursor.execute("SELECT ROWID, * from REGISTER ORDER BY " + key)
  registers = cursor.fetchall()

  conn.commit()
  conn.close()

  return registers

def search(query):
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  sql = "SELECT ROWID, * from REGISTER WHERE CUSTOMER LIKE '%"+query+"%'"
  sql += " OR BRAND LIKE '%"+query+"%'"
  sql += " OR RENTDATE LIKE '%"+query+"%'"
  sql += " OR RETURNDATE LIKE '%"+query+"%'"

  cursor.execute(sql)
  registers = cursor.fetchall()

  conn.commit()
  conn.close()

  return registers

def getTopRental():
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()

  sql = "SELECT CUSTOMER, COUNT(*) FROM REGISTER GROUP BY CUSTOMER ORDER BY COUNT(*) DESC LIMIT 10"

  cursor.execute(sql)
  customers = cursor.fetchall()

  sql = "SELECT BRAND, COUNT(*) FROM REGISTER GROUP BY BRAND ORDER BY COUNT(*) DESC LIMIT 10"

  cursor.execute(sql)
  brands = cursor.fetchall()
  
  conn.commit()
  conn.close()

  return (customers, brands)