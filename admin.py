from PIL import Image, ImageFont, ImageDraw
import pyttsx3
import time
import subprocess
from rich.console import Console
from rich.style import Style
m = Console()
z = Console()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def clear():
	clr = subprocess.call("cls", shell = True)
clear()




#BANNER
def Banner():
	

	ShowText = '       ADMIN PANEL'

	font = ImageFont.truetype('arialbd.ttf', 15) 
	size = font.getsize(ShowText)  
	image = Image.new('1', size, 1)  
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), ShowText, font=font) 
	for rownum in range(size[1]): 

	    line = []
	    for colnum in range(size[0]):
	        if image.getpixel((colnum, rownum)): line.append(' '),
	        else: 
	        	line.append("[red]"'#'),
	    m.print (''.join(line))
clear()
Banner()
speak("ENTER THE REQUIRED INFORMATION TO ENTER ADMIN PANEL")


#Adding Books
def add_books():
	import mysql.connector as t
	connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'bookstore')
	cursor = connect.cursor()
	book_id = int(m.input("[cyan]Enter The Id Of The Book : "))
	book_name = m.input("[cyan]Enter The Name Of The Book : ")
	author = m.input("[cyan]Enter Author's Name : ")
	
	price = int(m.input("[cyan]Enter The Price Of The Book : "))
	stock = int(m.input("[cyan]Enter The Stocks : "))
	sql = "insert into books_in_store(book_id, book_name, author, price, stock) values ('{}', '{}', '{}', '{}', '{}')".format(book_id, book_name, author, price, stock)
	cursor.execute(sql)
	connect.commit()
	m.print("[green][+] BOOK ADDED SUCCESFULLY ")
	speak("BOOK ADDED SUCCESFULLY SIR")

#Delete Books
def delete():
    import mysql.connector as m 
    connect = m.connect(host = 'localhost', user = 'root', password = 'root', database = 'bookstore')
    cursor = connect.cursor()
    book_id = int(z.input("[cyan]Enter The Id Of The Book To Be Deleted : "))
    _id = str(book_id)
    query = "DELETE FROM BOOKS_IN_STORE WHERE BOOK_ID = " + _id + ";"
    cursor.execute(query)
    connect.commit()
    z.print("[green][+] BOOK DELETED SUCCESSFULLY")
    speak("BOOK DELETED SUCCESFULLY SIR")

#Stock Update
def update_stock():
    import mysql.connector as t 
    connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'bookstore')
    cursor = connect.cursor()
    book_id = int(m.input("[cyan]Enter The Id Of The Book Whose Stocks You Want To Update : "))
    _id = str(book_id)
    stock = int(m.input("[cyan]Enter The Updated Stock : "))
    _stock = str(stock)
    q = "SELECT STOCK FROM BOOKS_IN_STORE WHERE BOOK_ID = " + _id + ";"
    cursor.execute(q)
    fetch = cursor.fetchone()
    index = fetch[0]
    stock_min = stock + index
    stock_main = str(stock_min) 
    query = "UPDATE BOOKS_IN_STORE SET STOCK = " + stock_main + " WHERE BOOK_ID = " + _id + ";"
    m.print("[green][+] STOCK UPDATED SUCCESFULLY")
    speak("STOCK UPDATED SUCCESFULLY SIR")
    cursor.execute(query)
    connect.commit()


#Price Update
def update_price():
    import mysql.connector as t 
    connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'bookstore')
    cursor = connect.cursor()
    book_id = int(m.input("[cyan]Enter The Id Of The Book Whose Price You Want To Update : "))
    _id = str(book_id)
    price = int(m.input("[cyan]Enter The Updated Price : "))
    _price = str(price)
    query = "UPDATE BOOKS_IN_STORE SET PRICE = " + _price + " WHERE BOOK_ID = " + _id + ";"
    m.print("[green][+] PRICE UPDATED SUCCESFULLY")
    speak("PRICE UPDATED SUCCESFULLY SIR")
    cursor.execute(query)
    connect.commit()


#Main 
def main(): 
	import getpass
	secret_code = "160521"
	user_ = "admin"
	passwrd = "ROOT hack 90!0"
	code = getpass.getpass(prompt = "Enter The Secret Code : ")
	user__ = m.input("[cyan]Enter The Username : ")
	username = user__.lower()
	password = getpass.getpass(prompt = "Enter The Password : ")
	if username == user_ and password == passwrd and code == secret_code:
		m.print("[magenta]----------------- VERIFICATION SUCCESFULLY DONE----------------- ")
		speak("VERIFICATION Succesfully DONE")
		time.sleep(2)
		clear()
		Banner()
	if username != user_ or password != passwrd or code != secret_code:
		m.print("[red]INVALID ENTRY")
		speak("INVALID ENTRY")
		time.sleep(2)
		clear()
		Banner()
		main()


		
		


def in_admin():
	m.print("[magenta]\t\t-----------------WELCOME TO THE ADMIN PANEL-----------------\n")
	speak("WELCOME TO THE ADMIN PANEL")
	m.print("[green]1. ADD BOOKS")
	m.print("[yellow]2. DELETE BOOKS")
	m.print("[blue]3. UPDATE")
	m.print("[red]4. EXIT")
	opt = int(m.input("[cyan]Enter The Manupilation To Performed By Admin : "))
	while opt == 1 :
		add_books()
		time.sleep(2)
		clear()
		Banner()
		in_admin()
	while opt == 2 :
		delete()
		time.sleep(2)
		clear()
		Banner()
		in_admin()
	while opt == 3 :
		m.print("[magenta]1. UPDATE STOCK")
		m.print("[yellow]2. UPDATE PRICE")
		choice = int(m.input("[cyan]Enter The Thing Which Needs To Be Updated : "))
		while choice == 1 :
			update_stock()
			time.sleep(2)
			clear()
			Banner()
			in_admin()
		while choice == 2 :
			update_price()
			time.sleep(2)
			clear()
			Banner()
			in_admin()
	while opt == 4:
		clear()
		break
		clear()
	else:
		m.print("[red][!] SOMETHING WENT WRONG ")
		m.print("[red][+] TRY AGAIN ")
		speak("SOMETHING WENT WRONG")
		speak("TRY AGAIN")
		time.sleep(1)
		clear()
		Banner()
		in_admin()
	

main()
in_admin()