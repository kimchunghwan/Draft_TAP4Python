import mysql.connector as mycon

# MYSQL
conn = mycon.connect(host='localhost', user='root', password='password', database='TAP4PYTHON')
cursor = conn.cursor()
cursor.execute(
    "select * from tap")
rows = cursor.fetchall()

for row in rows:
    print(str(row))
