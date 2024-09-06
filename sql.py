import sqlite3
# connect to sqlite
connection = sqlite3.connect('students.db')

# create a cursor object to insert record , create table and retrieve
cursor = connection.cursor()

# create the table
table_info = """
Create table student(name varcha(25) , class varchar(25) , section varchar(25) , marks int);
"""

cursor.execute(table_info)

## insert more value in the table
cursor.execute('''Insert Into student values('Krish' , 'Data Science' , 'A' , 90)''')
cursor.execute('''Insert Into student values('Alok' , 'Data Science' , 'B' , 100)''')
cursor.execute('''Insert Into student values('Darius' , 'Data Science' , 'A' , 50)''')
cursor.execute('''Insert Into student values('Vikash' , 'Devops' , 'C' , 50)''')
cursor.execute('''Insert Into student values('Dipesh' , 'Devops' , 'E' , 30)''')

## display the records
print("The inserted records are")
data = cursor.execute('''Select * from student''')
for row in data:
    print(row)

# close the connection
connection.commit()
connection.close()