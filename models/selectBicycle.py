#\models\selectBicycle.py
import sqlite3

def select():
  conn = sqlite3.connect('sqlite')
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