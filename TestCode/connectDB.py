import pypyodbc
cnxn = pypyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.200;PORT:64555;DATABASE=EISAN;UID=eisan;PWD=eisan$2016')
cursor = cnxn.cursor()
cursor.execute("select user_id, user_name from users")
rows = cursor.fetchall()
for row in rows:
    print (row.user_id, row.user_name)
    print ("testMake well ")