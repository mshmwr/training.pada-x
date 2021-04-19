# 記錄各個操作指令 & 查詢目前使用的db

import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="myusers")

#print(mydb)
mycursor = mydb.cursor()

## create database
# mycursor.execute("CREATE DATABASE myusers")

## Check if Database Exists
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

## Creating a Table
# mycursor.execute(
#     "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP)"
# )

## Check if Table Exists
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

## Insert Into Table
# sql = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
# val = ("nametest0", "nametest0", "pwd0")
# mycursor.execute(sql, val)
# mydb.commit()

## Insert Multiple Rows: executemany()
# sql = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
# val = [('nametest1', 'test1', 'pwd1'), ('nametest2', 'test2', 'pwd2'),
#        ('nametest3', 'test3', 'pwd3')]
# mycursor.executemany(sql, val)
# mydb.commit()

## Select From a Table
# mycursor.execute("SELECT * FROM users")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

## Selecting Columns
# mycursor.execute("SELECT name, username FROM users")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

## Prevent SQL Injection 第一種
# sql = "SELECT * FROM users WHERE username = %s"
# adr = ("test2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# print(myresult[0][1])

## Prevent SQL Injection 第二種
# sql = "SELECT * FROM users WHERE username = %s and password= %s"
# adr = ("test2", "pwd2")
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# print(myresult[0][1])

## Using the fetchone() Method: return the first row of the result
# mycursor.execute("SELECT * FROM users")
# myresult = mycursor.fetchone()
# print(myresult)

# # UPDATE Table
# sql = "UPDATE users SET name = %s WHERE username = %s"
# val = ("name2", "test2")
# mycursor.execute(sql, val)
# mydb.commit()

## Delete a Table
# sql = "DROP TABLE users"
# mycursor.execute(sql)
