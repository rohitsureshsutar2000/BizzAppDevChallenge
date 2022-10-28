# you can direct paste file "employ.db " in website https://inloop.github.io/sqlite-viewer/ to see data in file

import sqlite3

conn = sqlite3.connect('employ.db')

c = conn.cursor()


# To Create new Table
# c.execute("""CREATE TABLE employ (
#
# name TEXT,
#
# department TEXT,
#
# project TEXT
# )""")


# DATA LIKE (Employee, Department,Project)
# ('david', 'cse', 'ML')
# ('John', 'entc', 'Robotics')



all_employ = [

 ]


# To Insert data
all_employ2=[]
for i in range(0,3):
    all_employ2.append(input())
all_employ.append((all_employ2[0],all_employ2[1],all_employ2[2]))



c.executemany("INSERT INTO employ VALUES (?,?,?)",all_employ)
c.execute("SELECT * FROM employ")
data= c.fetchall()
for i in data:
    print(i)
conn.commit()
conn.close()