import psycopg2
connection = psycopg2.connect(host='localhost', user='postgres',password='g30d@t@', port="5432")
connection.autocommit = True
cursor = connection.cursor()
cursor.execute('CREATE DATABASE chapter122')

cursor.execute('CREATE EXTENSION postgis')
connection.close() 


