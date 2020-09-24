import sqlite3
import datetime


def connect_db():
  con = sqlite3.connect('database/Automatic_Licence_Number_Plate_Recognition_db.db')
  return con

def create_user(value):
  conn = connect_db()
  email = value[1]
  password = value[2]
  name = value[0]
  sql = f"INSERT INTO users(name,email,password) VALUES('{name}','{email}','{password}')"
  conn.execute(sql)
  res = conn.commit()

def validate_user(value):
  user_pass  = ''
  conn = connect_db()
  email = value
  sql = f"SELECT *FROM users WHERE email = '{email}'"
  cursor = conn.execute(sql)
  for res in cursor:
    print(res[3])
    user_pass = res[3]
  return user_pass
