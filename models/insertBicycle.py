#\models\insertBicycle.py
import sqlite3

def insert(*bicycle):
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

  cursor.execute("INSERT INTO BICYCLE VALUES (?, ?, ?, ?, ?)", bicycle)
  
  conn.commit()
  conn.close()