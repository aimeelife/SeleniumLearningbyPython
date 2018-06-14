import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                              'Database=testdb;'
                              'uid=Python;pwd=qa')

cursor = connection.cursor()
SQLCommand = ("SELECT [index],search,expect FROM test ")
cursor.execute(SQLCommand)

results = cursor.fetchone()
while results:
    print("Test Table Record:" + str(int(results[0])) + " " + results[1] + " "+results[2])
    results= cursor.fetchone()

cursor.close()
connection.close()