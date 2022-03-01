
print()
def bookstore():
	import mysql.connector as t 
	connect = t.connect(host = 'localhost', user = 'root', password = 'root')
	cursor = connect.cursor()
	createdb = "CREATE DATABASE BOOKSTORE;"
	cursor.execute(createdb)
	use_db = "USE BOOKSTORE;"
	cursor.execute(use_db)
	create_table = "CREATE TABLE BOOKS_IN_STORE(BOOK_ID INT(255) NOT NULL PRIMARY KEY, BOOK_NAME VARCHAR(255) NOT NULL, AUTHOR VARCHAR(255) NOT NULL, BOOK_DESCP TEXT NOT NULL, PRICE INT(255) NOT NULL, STOCK INT(255) NOT NULL);"
	table_details = "CREATE TABLE TRANSACTION_DETAILS(TRANSACTION_ID INT(8) NOT NULL PRIMARY KEY, USERNAME VARCHAR(255) NOT NULL, BOOKS_PURCHASED INT(255) NOT NULL, BOOKS_NAME VARCHAR(255) NOT NULL, PRICE INT(255), DATE_OF_PURCHASE DATE NOT NULL);"
	cursor.execute(create_table)
	cursor.execute(table_details)
	connect.commit()
bookstore()


def user_login():
	import mysql.connector as t
	connect = t.connect(host = 'localhost', user = 'root', password = 'root')
	cursor = connect.cursor()
	createdb = "CREATE DATABASE USER_LOGIN;"
	cursor.execute(createdb)
	use_db = "USE USER_LOGIN;"
	cursor.execute(use_db)
	create_table = "CREATE TABLE LOGIN_INFO(EMAIL VARCHAR(255) NOT NULL, USERNAME VARCHAR(255) NOT NULL PRIMARY KEY, NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(255) NOT NULL, SECRET_CODE INT(8) NOT NULL UNIQUE KEY);"
	cursor.execute(create_table)
	connect.commit()
user_login()

def review():
	import mysql.connector as t
	connect = t.connect(host = 'localhost', user = 'root', password = 'root')
	cursor = connect.cursor()
	createdb = "CREATE DATABASE REVIEWS"
	cursor.execute(createdb)
	use_db = "USE REVIEWS"
	cursor.execute(use_db)
	create_table = "CREATE TABLE REVIEWS(USERNAME VARCHAR(255) NOT NULL PRIMARY KEY, EMAIL VARCHAR(255) NOT NULL, REVIEW TEXT);"
	cursor.execute(create_table)
	connect.commit()
review()
