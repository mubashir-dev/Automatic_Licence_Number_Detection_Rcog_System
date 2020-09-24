import sqlite3
import datetime

def connect():
  con = sqlite3.connect('database/Automatic_Licence_Number_Plate_Recognition_db.db')
  print("Connected")
  return con


def insert_infor_owner(list):
  con = connect()
  print(con)
  sql = f"INSERT INTO saved_plates_numbers(plate_number,owner_name,contact) VALUES('{list[2]}','{list[1]}','{list[0]}')"
  print(sql)
  con.execute(sql)
  con.commit()
  print("Record inserted successfully into SqliteDb_developers table ")
  con.close()
  
def get_info():
  list = []
  con = connect()
  # print(con)
  sql = "SELECT *FROM saved_plates_numbers"
  # print(sql)
  cursor = con.execute(sql)
  cursor = cursor.fetchall()
  for i in cursor:
    list.append(cursor[0])
    list.append(cursor[1])
    list.append(cursor[2])
    list.append(cursor[3])
  print("Record inserted successfully into SqliteDb_developers table ")
  return list
  con.close()


def get_users():
  list = []
  email = []
  data = []
  con = connect()
  sql = "SELECT *FROM users"
  cursor = con.execute(sql)
  for i in cursor:
    list.append(i[1])
    email.append(i[2])
  print("Record inserted successfully into SqliteDb_developers table ")
  data.append(list)
  data.append(email)
  return data
  con.close()


def change_password(cur_pass):
  sql = "SELECT *FROM users "
  # print(sql)
  cursor = con.execute(sql)
  data = cursor.fetchall()
  for i in data:
    list.append(i[1])
  print("Record inserted successfully into SqliteDb_developers table ")
  return list
  con.close()


def insert_in_history(res):
  # print(res)
  con = connect()
  x = datetime.datetime.now()
  sql = f"INSERT INTO history(result,time) VALUES('{res}','{x}')"
  print(sql)
  con.execute(sql)
  con.commit()
  print("History has been created in Table")
  con.close()


def get_history():
  date_time = []
  plate_found = []
  list = []
  con = connect()
  sql = ""
  cursor = con.execute("SELECT result, time FROM history")
  for i in cursor:
    plate_found.append(i[0])
    date_time.append(i[1])
    
  list.append(date_time)
  list.append(plate_found)
  return list
  con.close()


def count_data():
  data = []
  con = connect()

  cursor = con.execute("SELECT count(id) FROM history")
  for i in cursor:
    data.append(i[0])

  cursor = con.execute("SELECT count(id) FROM saved_plates_numbers")
  for i in cursor:
    data.append(i[0])

  cursor = con.execute("SELECT count(id) FROM users")
  for i in cursor:
    data.append(i[0])
    
  return data
  con.close()


