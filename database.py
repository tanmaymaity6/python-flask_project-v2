from sqlalchemy import create_engine, text
from pymysql import cursors
import pymysql
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
timeout=10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="tangent-careers-tangent-careers.h.aivencloud.com",
    password=db_connection_string,
    read_timeout=timeout,
    port=20931,
    user="avnadmin",
    write_timeout=timeout,
)

def load_jobs_from_db():
  cursor = connection.cursor()
  cursor.execute("select * from jobs")
  jobs=[]
  for row in cursor.fetchall():
    jobs.append(dict(row))
  return jobs



# try:  
#   cursor = connection.cursor()
#   result = cursor.execute("select * from jobs")

###for understanding---
#   result_dicts=[]
#   for row in cursor.fetchall():
#     result_dicts.append(dict(row))
#   print(result_dicts)
  
  # print("type(result):", type(result))

  # result_all = cursor.fetchall()
  # print("type(result.all()):",type(result_all))
  # first_result=result_all[0]
  # print("type(first_result):",type(first_result))
  # print(first_result)

 #  print(cursor.fetchall())
 # print("type:type(cursor):", type(cursor))
# finally:
#   connection.close()
