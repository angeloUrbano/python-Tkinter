import sqlite3
my_connect= sqlite3.connect("BIBLIOTECA")
my_cursor=my_connect.cursor()


my_cursor.execute("SELECT id , ID_LIBROS FROM ALUMNOS")



var=my_cursor.fetchall()

print(len(var))



	

print(var[-1] [0] , var[-1][1])