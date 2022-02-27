
#Specifying Encoding
#Encoding = ANSI
#Clearing Terminal Screen
def clear():
    import time
    import subprocess
    clr = subprocess.call("cls", shell = True)
    time.sleep(1)
clear()



#Checking For Modules
def check_modules():
    import subprocess
    import time
    print("[+] CHECKING REQUIRED MODULES")
    try:
        import PIL
        import pyttsx3
        import rich
        import tabulate
        import prettytable
        print("[+] REQUIREMENT SATISFIED")
        print("[+] REDIRECTING TO HACKER HUB.....")
        time.sleep(2)
        subprocess.call('cls', shell = True)
    except ModuleNotFoundError:
        print("[+] INSTALLING REQUIRED MODULES")
        print("[-] PLEASE WAIT.....")
        time.sleep(2.5)
        subprocess.call("pip install Pillow", shell = True)
        subprocess.call("pip install pyttsx3", shell = True)
        subprocess.call("pip install rich", shell = True)
        subprocess.call("pip install tabulate", shell = True)
        subprocess.call("pip install prettytable", shell = True)
        print("[+] REQUIREMENT SATISFIED")
        print("[+] REDIRECTING TO HACKER HUB.....")
        subprocess.call('cls', shell = True)
        time.sleep(2)
check_modules()


def loading_bar():
	import time
	time.sleep(1.5)
	from rich.progress import Progress
	with Progress() as progress:
		task1 = progress.add_task("[red]DOWNLOADING...", total=100)
		task2 = progress.add_task("[green]INITIALIZING...", total=100)
		while not progress.finished:
			progress.update(task1, advance=0.9)
			progress.update(task2, advance=0.6)
			time.sleep(0.02)
loading_bar()


# Importing Externally Used Modules
from rich.console import Console
from rich.style import Style
import pyttsx3

import time
import subprocess
import re
from prettytable import PrettyTable
from tabulate import tabulate
c = Console()
m = Console()



#audio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


clear()


# Banner Of The Hakcer Hub Book Library
def Banner():
	c.print("\t\t[red]88----------------------------------------   HACKERS ARE HERE WHERE ARE YOU !?    ---------------------------------------------88")
	c.print("\t\t[red]88   _           _                                                                       _           _                         88")
	c.print("\t\t[red]88  | |         | |                                                                     | |         | |                        88")
	c.print("\t\t[red]88  | |         | |                                                                     | |         | |                        88")
	c.print("\t\t[red]88  | |         | |                                                                     | |         | |                        88")
	c.print("\t\t[red]88  | |         | |    _______                                                          | |         | |  _     _   ________    88")
	c.print("\t\t[red]88  | |_________| |   / _____ \    ______   _     __   ______   _______                 | |_________| | | |   | | |   __   \   88")
	c.print("\t\t[red]88  |  _________  |  / /     \ \  |  ____| | |   / /  |  ____) |  ___  |                |  _________  | | |   | | |  |  \   |  88")
	c.print("\t\t[red]88  | |         | | | |_______| | | |      | |__/ /   | |___   | |___| |                | |         | | | |   | | |  |__/ _/   88")
	c.print("\t\t[red]88  | |         | | |  _______  | | |      |  __ /    |  ___)  |  _  __|                | |         | | | |   | | |  |  \  \   88")
	c.print("\t\t[red]88  | |         | | | |       | | | |____  | |  \ \   | |____  | | \ \                  | |         | | | |___| | |  |__/   |  88")
	c.print("\t\t[red]88  |_|         |_| | |       | | |______| |_|   \_\  |______) |_|  \_\                 |_|         |_| |_______| |________/   88")
	c.print("\t\t[red]88----------------------------------------  A PLACE ALL ABOUT HACKING / HACKERS  ----------------------------------------------88")
	c.print("\t\t[red]88----------------------------------------            BY TEAM INFINITY           ----------------------------------------------88\n")
Banner()
speak("WELCOME TO HACKERS HUB")


# Wrong Username
def wrong_username():
	ask = c.input("[cyan]Entered Wrong Username By Mistake [Y/N] [DEFAULT N] : ")
	case = ask.upper()
	while not re.match("^[Y&N]*$",case):
		c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
		speak("ERROR ONLY Y AND N ALLOWED")
		more = c.input("[cyan]Entered Wrong Username By Mistake [Y/N] [DEFAULT N] : ")
		case = more.upper()
	while not re.match("^[Y&N]*$",case):
		c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
		speak("ERROR ONLY Y AND N ALLOWED")
		break
		continue
	while case == "Y":
		validation()
		break
	while case == "N" or " ":
		Register()
		break



#Validating The Login Of User
def validation():
    global username
    import getpass
    import mysql.connector as t 
    connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'user_login')
    cursor = connect.cursor()
    ask = c.input("[cyan]Enter Your Username : ")
    username = ask.lower()
    while username == ';' or ':' or '"' or "'" or '/' or '?' or '.' or ',' or '!' or '@' or '#' or '$' or '%' or '^' or '&' or '*' or '(' or ')' or '-' or '_' or '=' or '+' or '[' or ']' or '{' or '}' or '|' or "`" or '~' or '<' or '>'or' \ ':
        break
        continue 
    query = "SELECT USERNAME FROM LOGIN_INFO WHERE USERNAME = " + "'" + username + "'" + ";"
    while True:
        try:
            cursor.execute(query)
        except t.ProgrammingError:
            print("")
        fetch = cursor.fetchone()
        break
        continue
    while fetch == None:
        m.print("[red][!] NO SUCH USERNAME FOUND !")
        speak("NO SUCH USERNAME FOUND")
        wrong_username()
        break
    while fetch != None:
        password = getpass.getpass(prompt = "Enter Your Password : ")
        query = "SELECT USERNAME, PASSWORD FROM LOGIN_INFO WHERE USERNAME = " + "'" + username + "'" + " AND PASSWORD = " + "'" + password + "'" + ";"
        cursor.execute(query)
        fetch1 = cursor.fetchone()
        while fetch1 != None:
            index0 = fetch1[0]
            index1 = fetch1[1]
            c.print("[green][+] LOGIN SUCCESS !")
            speak("LOGIN SUCCESS")
            time.sleep(3)
            clear()
            Banner()
            in_login()
            break
        while fetch1 == None:
            c.print("[red][!] WRONG PASSWORD")
            speak("WRONG PASSWORD")
            c.print("[green]REDIRECTING TO PASSWORD RECOVERY PAGE...")
            speak("REDIRECTING TO PASSWORD RECOVERY PAGE")
            time.sleep(2.5)
            clear()
            Banner()
            c.print("[green]\t\t  -------------------------------------------------- PASSWORD RECOVERY PAGE --------------------------------------------------")
            speak("WELCOME TO PASSWORD RECOVERY PAGE")
            forgot()
            break
        break



#Registering User If Directly Approaches Login
def Register():
	register = c.input("[cyan]Wanna Register To Hacker Hub [Y/N] [DEFAULT Y] : ")
	case = register.upper()
	while not re.match("^[Y&N]*$",case):
		c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
		speak("ERROR ONLY Y AND N ALLOWED")
		more = c.input("[cyan]Wanna Resgister To Hacker Hub [Y/N] [DEFAULT Y] : ")
		case = more.upper()
	while not re.match("^[Y&N]*$",case):
		c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
		speak("ERROR ONLY Y AND N ALLOWED")
		break
		continue
	while case == "N":
		c.print("[green]-------------------------------------------------- REDIRECTING TO THE START PAGE --------------------------------------------------")
		speak("REDIRECTING TO THE START PAGE")
		time.sleep(1)
		clear()
		Banner()
		start()
		break
	while case == "Y" or " ":
		time.sleep(0.5)
		c.print("[green]\t-------------------------------------------- REDIRECTING TO THE REGISTRATION FORM --------------------------------------------")
		speak("REDIRECTING TO THE REGISTRATION FORM")
		time.sleep(0.3)
		clear()
		Banner()
		new()
		c.print("[green]-------------------------------------------------- REDIRECTING TO LOGIN FORM --------------------------------------------------")
		speak("REDIRECTING TO LOGIN FORM")
		time.sleep(1.5)
		clear()
		Banner()
		c.print("[green]\t\t ------------------------------------------- WELCOME TO LOGIN FORM OF HACKER HUB -------------------------------------------")
		speak("WELCOME T0 LOGIN FORM OF HACKER HUB")
		validation()
		break		


#Registering New User Directly
def new():
    from rich.console import Console
    from rich.style import Style
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    c = Console()
    m = Console()
    import time
    import getpass
    import random
    
    import mysql.connector as t
    from mysql.connector import errorcode
    connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'user_login')
    c = connect.cursor()
    m.print("[green]\t\t     -------------------------------------------- WELCOME TO REGISTRATION FORM -------------------------------------------")
    speak("ENTER THE REQUIRED INFORMATION FOR REGISTRATION")
    name = m.input("[cyan]Enter Your Full Name : ")
    check = name.isspace()
    while check is True or name == "":
        m.print("[red][!] NAME CANNOT BE EMPTY")
        speak("NAME CANNOT BE EMPTY")
        name = m.input("[cyan]Enter Your Full Name : ")
        check = name.isspace()
        while check is True or name == "":
            break
            continue
    else:
        email = m.input("[cyan]Enter Your Email : ")
        check1 = email.isspace()
        while check1 is True or email == "":
            m.print("[!] EMAIL CANNOT BE EMPTY")
            speak("EMAIL CANNOT BE EMPTY")
            email = m.input("[cyan]Enter Your Email : ")
            check1 = email.isspace()
            while check1 is True or email == "":
                break
                continue
        password = getpass.getpass(prompt = "Enter Your Password : ")
        check3 = password.isspace()
        while check3 is True:
            m.print("[red][!] PASSWORD CANNOT CONTAIN EMPTY SPACES")
            speak("PASSWORD CANNOT CONTAIN EMPTY SPACES")
            password = getpass.getpass(prompt = "Enter Your Password : ")
            check3 = password.isspace()
            while check3 is True:
                break
                continue
        length_chk = len(password)
        while length_chk < 8 :
            m.print("[red]PASSWORD MUST HAVE A LENGTH OF EIGHT")
            speak("PASSWORD MUST HAVE A LENGTH OF EIGHT")
            password = getpass.getpass(prompt = "Enter Your Password : ")    
            length_chk = len(password)
            continue
        while length_chk >= 8:
            confirm_pass = getpass.getpass(prompt = "Confirm Password : ")
            break
        while password == confirm_pass :
            username = m.input("[cyan]Choose A Username For Your Account : ")
            check2 = username.isspace()
            while check2 is True or username == "":
                m.print("[red][!] USERNAME CANNOT BE EMPTY")
                speak("USERNAME CANNOT BE EMPTY")
                username = m.input("[cyan]Choose A Username For Your Account : ")
                check2 = username.isspace()
                while check2 is True or username == "":
                    break 
                    continue
            else:
                length = 8
                char = "0123456789"
                secret_code = ''.join(random.choice(char) for _ in range(length))
                query = "insert into LOGIN_INFO (NAME, EMAIL, PASSWORD, USERNAME, SECRET_CODE) values ('{}','{}','{}','{}','{}')".format(name, email, password, username, secret_code)
                try:
                    c.execute(query)    
                    m.print("[magenta]Your Secret Code Is : ", secret_code)
                    m.print("[red][!] WARNING [!]")
                    speak("WARNING")
                    m.print("[red]This Secret Key Must Be Remembered In Case You Forget Your Password. Once Your Lose This Your Access To Your Account Will Be Lost.")
                    speak("This Secret Key Must Be Remembered In Case You Forget Your Password. Once Your Lose This Your Access To Your Account Will Be Lost.")
                    m.print("[red]REGARDS :- SECURITY TEAM HACKER HUB")
                    m.print("[green]-------------------------------------------------- CONGRATULATION REGISTRATION SUCCESS --------------------------------------------------")
                    speak("REGARDS :- SECURITY TEAM HACKER HUB")
                    speak("CONGRATULATION REGISTRATION SUCCESS")
                except t.IntegrityError:
                    m.print("[red]USERNAME ALREADY TAKEN")
                    speak("USERNAME ALREADY TAKEN")
                    continue
                else:
                    connect.commit()
                    break
        while password != confirm_pass :
            m.print("[red]Oops...! PASSWORD AND CONFIRM PASSWORD DOESN'T MATCH")
            speak("PASSWORD AND CONFIRM PASSWORD DOESN'T MATCH")
            password = getpass.getpass(prompt = "Enter Your Password : ")        
            check4 = password.isspace()
            while check4 is True:
                m.print("[red][!] PASSWORD CANNOT CONTAIN EMPTY SPACES")
                speak("PASSWORD CANNOT CONTAIN EMPTY SPACES")
                password = getpass.getpass(prompt = "Enter Your Password : ")
                check4 = password.isspace()
                while check4 is True:
                    break
                    continue
            length_chk = len(password)
            while length_chk < 8 :
                m.print("[red]PASSWORD MUST HAVE A LENGTH OF EIGHT")
                speak("PASSWORD MUST HAVE A LENGTH OF EIGHT")
                password = getpass.getpass(prompt = "Enter Your Password : ")
                length_chk = len(password)
                continue
            while length_chk >= 8:
                confirm_pass = getpass.getpass(prompt = "Confirm Password : ")
                break
            while password == confirm_pass :
                username = m.input("[cyan]Choose A Username For Your Account : ")
                check2 = username.isspace()
                while check2 is True or username == "" :
                    m.print("[!] USERNAME INVALID")
                    username = m.input("[cyan]Choose A Username For Your Account : ")
                    check2 = username.isspace()
                    while check2 is True or username == "" :
                        break 
                        continue
                else:
                    length = 8
                    char = "0123456789"
                    secret_code = ''.join(random.choice(char) for _ in range(length))
                    query = "insert into LOGIN_INFO (NAME, EMAIL, PASSWORD, USERNAME, SECRET_CODE) values ('{}','{}','{}','{}','{}')".format(name, email, password, username, secret_code)
                    try:
                        c.execute(query)
                        m.print("[red]Your Secret Code Is : ", secret_code)
                        m.print("[red][!] WARNING [!]")
                        speak("WARNING")
                        m.print("[red]This Secret Key Must Be Remembered In Case You Forget Your Password. Once Your Lose This Your Access To Your Account Will Be Lost.")
                        speak("This Secret Key Must Be Remembered In Case You Forget Your Password. Once Your Lose This Your Access To Your Account Will Be Lost.")
                        m.print("[red]REGARDS :- SECURITY TEAM HACKER HUB")
                        m.print("[green]-------------------------------------------------- CONGRATULATION REGISTRATION SUCCESS --------------------------------------------------")
                        speak("REGARDS :- SECURITY TEAM HACKER HUB")
                        speak("CONGRATULATION REGISTRATION SUCCESS")
                    except t.IntegrityError:
                        m.print("[red]USERNAME ALREADY TAKEN")
                        speak("USERNAME ALREADY TAKEN")
                        continue
                    else:
                        connect.commit()
                        break


#ForGot Password
def forgot():
    import mysql.connector as t
    connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'user_login')
    cursor = connect.cursor()
    ask = c.input("[cyan]Enter Your Username : ")
    username = ask.lower()
    query = "SELECT USERNAME FROM LOGIN_INFO WHERE USERNAME = " + "'" + username + "'" + ";"
    cursor.execute(query)
    fetch = cursor.fetchone()
    while True:
    	try:
    		secret = int(c.input("[cyan]Enter Your Secret Key : "))
    		break
    	except ValueError:
    		c.print("[red][!] INVALID SECRET CODE ")
    		speak("INVALID SECRET CODE")

    		c.print("[green]REDIRECTING TO START PAGE.......")
    		speak("REDIRECTING TO START PAGE")
    		
    		time.sleep(2)
    		clear()
    		Banner()
    		start()
    		continue
    secret_key = str(secret)
    query1 = "SELECT USERNAME, PASSWORD, SECRET_CODE FROM LOGIN_INFO WHERE USERNAME = " + "'" + username + "'" " AND SECRET_CODE = " + secret_key + ";"
    cursor.execute(query1)
    fetch2 = cursor.fetchone()
    while True:
	    while fetch2 != None:
	        index = fetch2[1]
	        c.print("[magenta]Your Password Is : ",index)
	        validation()
	    while fetch2 == None:
	        c.print("[red][!] NO SUCH SECRET KEY FOUND")
	        speak("NO SUCH SECRET KEY FOUND")

	        c.print("[green]REDIRECTING TO START PAGE.......")
	        speak("REDIRECTING TO START PAGE")

	        time.sleep(3)
	        clear()
	        Banner()
	        start()
	        break
	    break

#Order details
def order_details():
    import mysql.connector as t
    connect = t.connect(host  = 'localhost', user = 'root', password = 'root', database = 'bookstore')
    cursor = connect.cursor()
    query = "SELECT * FROM TRANSACTION_DETAILS WHERE USERNAME = " + "'" + username + "'" + ";"
    cursor.execute(query)
    fetch = cursor.fetchall()
    while fetch == []:
        print("[+] YOU HAVEN'T PURCHASED ANYTHONG FROM HACKER HUB")
        break
    else:
        print("[+] YOUR ORDER DETAILS ARE ...\n")
        m.print(tabulate(fetch, headers = ["ORDER ID", "USERNAME", "BOOK PURCHASED", "BOOK NAME", "PRICE", "DATE OF PURCHASE"], tablefmt = 'psql'))

#Asking Choices After Login
def in_login():
    c.print("\n[magenta]1. Available Books")
    c.print("[blue]2. Buy Books")
    c.print("[green]3. Review Book")
    c.print("[yellow]4. Order Summary")
    c.print("[red]5. To Main Menu\n")
    while True:
        try:
            opt = int(c.input("[cyan]Enter The Task To Be Performed : "))
        except ValueError:
            c.print("[red][!] INVALID INPUT")
            speak("INVALID INPUT")
            continue
        break
        continue
    if opt == 1 :
        avail()
        in_login()
    while opt == 2 :
        c.print("[green]REDIRECTING YOU.... HAVE PATIENCE....")
        speak("REDIRECTING YOU  HAVE PATIENCE")
        time.sleep(1.5)
        clear()
        Banner()
        c.print("[green]\t-------------------------------------------------- WELCOME TO BUYING SECTION OF HACKER HUB --------------------------------------------------\n")
        speak("WELCOME TO BUYING SECTION OF HACKER HUB")
        buy()
        more = c.input("[green]Want To Buy More Books [Y/N] [DEFAULT N] : ")
        case = more.upper()
        while not re.match("^[Y&N]*$",case):
            c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED ")
            speak("ERROR ONLY Y AND N ALLOWED")
            more = c.input("[green]Want To Buy More Books [Y/N] [DEFAULT N]: ")
            case = more.upper()
        while not re.match("^[Y&N]*$",case):
            c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
            speak("ERROR ONLY Y AND N ALLOWED")
            break
            continue
        while case == 'Y':
            time.sleep(2.5)
            c.print("[green]-------------------------------------------------- REDIRECTING BACK TO BUYING PAGE --------------------------------------------------")
            speak("REDIRECTING BACK TO BUYING PAGE")
            time.sleep(2.5)
            clear()
            Banner()
            c.print("[green]\t-------------------------------------------------- WELCOME TO BUYING SECTION OF HACKER HUB --------------------------------------------------\n")
            speak("WELCOME TO BUYING SECTION OF HACKER HUB")
            buy()
            more = c.input("[green]Want To Buy More Books [Y/N] [DEFAULT N]: ")
            case = more.upper()
            continue
        while case == 'N' or ' ':
            c.print("[green][+] THAKNS FOR VISITING HACKER HUB..!")
            speak("THAKNS FOR VISITING HACKER HUB")
            c.print("[green][+] HAVE A GOOD DAY ♥ ")
            speak("HAVE A GOOD DAY")
            c.print("[green]-------------------------------------------------- PLEASE BE PATIENCE REDIRECTING TO MAIN PAGE --------------------------------------------------")
            speak("PLEASE BE PATIENCE REDIRECTING TO MAIN PAGE")
            time.sleep(10)
            clear()
            Banner()
            in_login()
            break
    if opt == 3 :
        review()
        time.sleep(10)
        clear()
        Banner()
        in_login()
    if opt == 4:
        order_details()
        in_login()
    if opt == 5:
        print("---------------------------------------- REDIRECTING TO START PAGE ----------------------------------------")
        speak("REDIRECTING TO START PAGE HAVE PATIENCE")
        time.sleep(5)
        clear()
        Banner()
        start()
    if opt > 5:
        c.print("[red][!] INVALID INPUT")
        speak("INVALID INPUT")
        c.print("[red][+] TRY AGAIN")
        speak("TRY AGAIN")
        time.sleep(5)
        clear()
        Banner()
        in_login()
        if opt < 1:
            c.print("[red][!] INVALID INPUT")
            speak("INVALID INPUT")
            c.print("[red][+] TRY AGAIN")
            speak("TRY AGAIN")
            time.sleep(5)
            clear()
            Banner()
            in_login()




#If User Asks For Available Books
def avail():
	from rich.console import Console
	from rich.style import Style
	m = Console()
	import mysql.connector as t
	conn = t.connect(host='localhost', database='bookstore', user='root', password='root')
	c = conn.cursor()
	m.print("\n[magenta][+] BOOKS CURRENTLY AVAILABLE WITH US..")
	while True:
		q = "SELECT BOOK_ID, BOOK_NAME, PRICE FROM BOOKS_IN_STORE"
		c.execute(q)
		d = c.fetchall()
		m.print(tabulate(d, headers = ["BOOK ID", "BOOK NAME", "PRICE"], tablefmt = 'psql'))
		break





#If User Chooses To Buy Books
def buy():
    import time 
    import random
    import mysql.connector as t  
    from mysql.connector import errorcode
    connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'bookstore')
    c = connect.cursor()
    m.print("[red]1. Search By Book Name  ")
    m.print("[blue]2. Search By Author Name  ")
    m.print("[yellow]3. Search By Price ")
    m.print("[purple]4. Exit  \n")

    while True:
        try:
            opt = int(m.input("[cyan]Enter The Method Of Searching : "))
            break
        except ValueError:
            m.print("[red][!] INVALID INPUT")
            speak("INVALID INPUT")
            m.print("[red][+] TRY AGAIN")
            speak("TRY AGAIN")
            continue
    while opt == 1:
        book_name = m.input("[cyan]Enter The Name Of The Book : ")
        query = "SELECT BOOK_ID, BOOK_NAME, AUTHOR, PRICE, STOCK FROM BOOKS_IN_STORE WHERE BOOK_NAME = " + "'" + book_name + "'" + ";"
        c.execute(query)
        d = c.fetchall()
        while d == []:
            m.print("[red][!] NO RECORD FOUND...")
            speak("NO RECORD FOUND")
            break
        while d != []:
            query = "SELECT COUNT(DISTINCT BOOK_ID) FROM BOOKS_IN_STORE WHERE BOOK_NAME = " + "'" + book_name + "'" + ";"
            c.execute(query)
            d = c.fetchall()
            stk = list(sum(d, ()))
            m.print("[magenta][+] YOUR SEARCH RESULTS ARE...\n")
            speak("YOUR SEARCH RESULTS ARE")
            for i in range (stk[0]):
                try:
                    q = "SELECT BOOK_ID, BOOK_NAME, AUTHOR, PRICE, BOOK_DESCP, STOCK FROM BOOKS_IN_STORE WHERE BOOK_NAME = " + "'" + book_name + "'" + ";"
                    c.execute(q)
                    L = c.fetchall()
                    x = list(sum(L, ()))
                    print(tabulate(L, headers=['Book ID', 'Book Name','Author','Book Description','Price','Stock'], tablefmt='psql'))
                except TypeError:
                    break
                id_ = []
                for i in range (len(x)):
                    try:
                        initial_id = 6
                        index_id = initial_id * i
                        _xz= x[index_id]
                        id_.append(_xz)
                    except IndexError:
                    	m.print("[yellow][+] SEARCH COMPLETED ")
                    	speak("SEARCH COMPLETED")
                    	break
                break
            while True:
                try:
                    id = int(m.input("[cyan]Enter The Id Of The Book : "))
                    break
                except ValueError:
                    m.print("[red][!] INVALID INPUT")
                    speak("INVALID INPUT")
                    continue
                print(id_)
            if id not in id_:
                m.print("[red][!] NO SUCH ID FOUND")
                speak("NO SUCH ID FOUND")
                m.print("[red][+] REGENERATING YOUR SEARCH RESULTS...")
                speak("REGENERATING YOUR SEARCH RESULTS")
                continue
            else:
                while True:
                	try:
                		id1 = str(id)
                		l = []
                		amt = m.input("[cyan]Enter The Number Of Books You Want To Buy : ")
                		amt1 = int(amt)
                	except ValueError:
                		m.print("[red][!] INVALID AMOUNT")
                		speak("INVALID AMOUNT")
                		continue
               		l.append((amt1,))
               		query = "SELECT STOCK FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
               		s = c.execute(query)
               		d = c.fetchmany(s)
               		if l[0] > d[0]:
               			m.print("[purple][!] THIS MUCH AMOUNT IS CURRENTLY UNAVAILABLE IN THE STOCKS")
               			speak("THIS MUCH AMOUNT IS CURRENTLY UNAVAILABLE IN THE STOCKS")
               			c.execute("UPDATE BOOKS_IN_STORE SET STOCK = STOCK")
               			connect.commit()
               			STK = list(sum(d, ()))
               			m.print("[green]CURRENTLY AVAILABLE STOCKS ARE : ", STK[0])
               			break
               		else:
                          com = "UPDATE BOOKS_IN_STORE SET STOCK = STOCK - " + amt + " WHERE BOOK_ID = " + id1 + ";"
                          c.execute(com)
                          connect.commit()
                          m.print("[green]-------------------------------------------------- VALIDATING YOUR TRANSACTION --------------------------------------------------")
                          speak("VALIDATING YOUR TRANSACTION")
                          time.sleep(2.5)
                          length = 8
                          num = "0123456789"
                          trans_id = ''.join(random.choice(num) for _ in range(length))
                          query = "SELECT BOOK_NAME FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
                          c.execute(query)
                          XA = c.fetchone()
                          query1 = "SELECT PRICE FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
                          c.execute(query1)
                          XM = c.fetchone()
                          m.print("[magenta]YOUR TRANSACTION DETAILS ARE...")
                          speak("YOUR TRANSACTION DETAILS ARE")
                          total_price = XM[0]*amt1
                          details = PrettyTable(["TRANSACTION ID", "BOOK ID", "BOOK NAME", "PRICE", "BOOK PURCHASED"])
                          details.add_row([trans_id, id1, XA[0], total_price, amt1])
                          print(details)
                          date = "SELECT CURDATE();"
                          c.execute(date)
                          fetch_ = c.fetchone()
                          index = fetch_[0]
                          query2 = "INSERT INTO TRANSACTION_DETAILS(transaction_id, username, books_purchased, price, books_name, date_of_purchase) values('{}','{}','{}','{}','{}','{}') ".format(trans_id, username, amt1, XM[0]*amt1, XA[0], index)
                          c.execute(query2)
                          connect.commit()
                          break
                	break
            break
        break        
    while opt == 2:
        author = m.input("[cyan]Enter The Name Of The Author : ")
        query = "SELECT BOOK_ID, BOOK_NAME, AUTHOR, PRICE, STOCK FROM BOOKS_IN_STORE WHERE AUTHOR = " + "'" + author + "'" + ";"
        c.execute(query)
        d = c.fetchall()
        while d == []:
            m.print("[red][!] NO RECORD FOUND...")
            speak("NO RECORD FOUND")
            break
        while d != []:
            query = "SELECT COUNT(DISTINCT BOOK_ID) FROM BOOKS_IN_STORE WHERE AUTHOR =  " + "'" + author + "'" + ";"
            c.execute(query)
            d = c.fetchall()
            stk = list(sum(d, ()))
            m.print("[magenta][+] YOUR SEARCH RESULTS ARE...\n")
            speak("YOUR SEARCH RESULTS ARE")
            for i in range (stk[0]):
                try:
                    q = "SELECT BOOK_ID, BOOK_NAME, AUTHOR, BOOK_DESCP, PRICE, STOCK FROM BOOKS_IN_STORE WHERE AUTHOR = " + "'" + author + "'" + ";"
                    c.execute(q)
                    L = c.fetchall()
                    x = list(sum(L, ()))
                    print(tabulate(L, headers=['Book ID', 'Book Name','Author','Book Description','Price','Stock'], tablefmt='psql'))
                except TypeError:
                    break
                __xz = []
                for i in range (len(x)):
                    try:
                        initial_id = 6
                        index_id = initial_id * i
                        _xz = x[index_id]
                        __xz.append(_xz)
                    except IndexError:
                        m.print("[yellow][+] SEARCH COMPLETED ")
                        speak("SEARCH COMPLETED")
                        break
                break
            while True:
                try:
                    id = int(m.input("[cyan]Enter The Id Of The Book : "))
                    break
                except ValueError:
                    m.print("[red][!] INVALID INPUT")
                    speak("INVALID INPUT")
                    continue
            if id not in __xz:
                m.print("[red][!] NO SUCH ID FOUND")
                speak("NO SUCH ID FOUND")
                m.print("[green][+] REGENERATING YOUR SEARCH RESULTS...")
                speak("REGENERATING YOUR SEARCH RESULTS")
                continue
            else:
            	while True:
                	try:
                		id1 = str(id)
                		l = []
                		amt = m.input("[cyan]Enter The Number Of Books You Want To Buy : ")
                		amt1 = int(amt)
                	except ValueError:
                		m.print("[red][!] INVALID AMOUNT ")
                		speak("INVALID AMOUNT")
                		continue
               		l.append((amt1,))
               		query = "SELECT STOCK FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
               		s = c.execute(query)
               		d = c.fetchmany(s)
               		if l[0] > d[0]:
               			m.print("[purple][!] THIS MUCH AMOUNT IS CURRENTLY UNAVAILABLE IN THE STOCKS")
               			speak("THIS MUCH AMOUNT IS CURRENTLY UNAVAILABLE IN THE STOCKS")
               			c.execute("UPDATE BOOKS_IN_STORE SET STOCK = STOCK")
               			connect.commit()
               			STK = list(sum(d, ()))
               			m.print("[green]CURRENTLY AVAILABLE STOCKS ARE : ", STK[0])
               			break
               		else:
                          com = "UPDATE BOOKS_IN_STORE SET STOCK = STOCK - " + amt + " WHERE BOOK_ID = " + id1 + ";"
                          c.execute(com)
                          connect.commit()
                          m.print("[green]-------------------------------------------------- VALIDATING YOUR TRANSACTION --------------------------------------------------")
                          speak("VALIDATING YOUR TRANSACTION")
                          time.sleep(2.5)
                          length = 8
                          num = "0123456789"
                          trans_id = ''.join(random.choice(num) for _ in range(length))
                          query = "SELECT BOOK_NAME FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
                          c.execute(query)
                          XA = c.fetchone()
                          query1 = "SELECT PRICE FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
                          c.execute(query1)
                          XM = c.fetchone()
                          m.print("[magenta]YOUR TRANSACTION DETAILS ARE...")
                          speak("YOUR TRANSACTION DETAILS ARE")
                          details = PrettyTable(["TRANSACTION ID", "BOOK ID", "BOOK NAME", "PRICE", "BOOK PURCHASED"])
                          details.add_row([trans_id, id1, XA[0], XM[0]*amt1, amt1])
                          print(details)
                          date = "SELECT CURDATE();"
                          c.execute(date)
                          fetch_ = c.fetchone()
                          index = fetch_[0]
                          query2 = "INSERT INTO TRANSACTION_DETAILS(transaction_id, username, books_purchased, price, books_name, date_of_purchase) values('{}','{}','{}','{}','{}','{}') ".format(trans_id, username, amt1, XM[0]*amt1, XA[0], index)
                          c.execute(query2)
                          connect.commit()
                          break
                	break
            break
        break
    while opt == 3:
        try:
            min1 = m.input("[cyan]Enter The Minimum Price Of The Book : ")
            max1 = m.input("[cyan]Enter The Maximum Price Of The Book : ") 
            query = "SELECT BOOK_ID, BOOK_NAME, AUTHOR, PRICE, STOCK FROM BOOKS_IN_STORE WHERE PRICE BETWEEN " + min1 + " AND " + max1 + ";"
            c.execute(query)
            d = c.fetchall()
        except t.ProgrammingError:
            m.print("[red][!] INVALID INPUT")
            speak("INVALID INPUT")
            continue
            break
        while d == []:
            m.print("[red][!] NO RECORD FOUND...")
            speak("NO RECORD FOUND")
            break
        while d != []:
            query = "SELECT COUNT(DISTINCT BOOK_ID) FROM BOOKS_IN_STORE WHERE PRICE BETWEEN " + min1 + " AND " + max1 + ";"
            d = c.execute(query)    
            s = c.fetchall()
            stk = list(sum(s, ()))
            m.print("[magenta][+] YOUR SEARCH RESULTS ARE... \n")
            speak("YOUR SEARCH RESULTS ARE")
            for i in range (stk[0]):
                try:
                    q = "SELECT BOOK_ID, BOOK_NAME, AUTHOR, BOOK_DESCP, PRICE, STOCK FROM BOOKS_IN_STORE WHERE PRICE BETWEEN " + min1 + " AND " + max1 + ";"
                    c.execute(q)
                    L = c.fetchall()
                    x = list(sum(L, ()))
                    print(tabulate(L, headers=['Book ID', 'Book Name','Author','Book Description','Price','Stock'], tablefmt='psql'))
                except TypeError:
                    break
                _id = []
                for i in range (len(x)):
                    try:
                        initial = 6
                        id_index = initial * i
                        _xz = x[id_index]
                        _id.append(_xz)
                    except IndexError:
                        m.print("[yellow][+] SEARCH COMPLETED ")
                        speak("SEARCH COMPLETED")
                        break
                break
            while True:
                try:
                    id = int(m.input("[cyan]Enter The Id Of The Book : "))
                    break
                except ValueError:
                    m.print("[red][!] INVALID INPUT")
                    speak("INVALID INPUT")
                    continue
            
            if id not in _id:
                m.print("[red][!] NO SUCH ID FOUND")
                m.print("[red][+] REGENERATING YOUR SEARCH RESULTS...")
                speak("NO SUCH ID FOUND")
                speak("REGENERATING YOUR SEARCH RESULTS")
                continue
            else:
            	while True:
                	try:
                		id1 = str(id)
                		l = []
                		amt = m.input("[cyan]Enter The Number Of Books You Want To Buy : ")
                		amt1 = int(amt)
                	except ValueError:
                		m.print("[red][!] INVALID INPUT")
                		speak("INVALID INPUT")
                		continue
               		l.append((amt1,))
               		query = "SELECT STOCK FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
               		s = c.execute(query)
               		d = c.fetchmany(s)
               		if l[0] > d[0]:
               			m.print("[purple][!] THIS MUCH AMOUNT IS CURRENTLY UNAVAILABLE IN THE STOCKS ")
               			speak("THIS MUCH AMOUNT IS CURRENTLY UNAVAILABLE IN THE STOCKS")
               			c.execute("UPDATE BOOKS_IN_STORE SET STOCK = STOCK")
               			connect.commit()
               			STK = list(sum(d, ()))
               			m.print("[magenta]CURRENTLY AVAILABLE STOCKS ARE : ", STK[0])
               			break
               		else:
                          com = "UPDATE BOOKS_IN_STORE SET STOCK = STOCK - " + amt + " WHERE BOOK_ID = " + id1 + ";"
                          c.execute(com)
                          connect.commit()
                          m.print("[green]-------------------------------------------------- VALIDATING YOUR TRANSACTION --------------------------------------------------")
                          speak("VALIDATING YOUR TRANSACTION")
                          time.sleep(2.5)
                          length = 8
                          num = "0123456789"
                          trans_id = ''.join(random.choice(num) for _ in range(length))
                          query = "SELECT BOOK_NAME FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
                          c.execute(query)
                          XA = c.fetchone()
                          query1 = "SELECT PRICE FROM BOOKS_IN_STORE WHERE BOOK_ID = " + id1 + ";"
                          c.execute(query1)
                          XM = c.fetchone()
                          m.print("[magenta]YOUR TRANSACTION DETAILS ARE...")
                          speak("YOUR TRANSACTION DETAILS ARE")
                          details = PrettyTable(["TRANSACTION ID", "BOOK ID", "BOOK NAME", "PRICE","BOOKS PURCHASED"])
                          details.add_row([trans_id, id1, XA[0], XM[0]*amt1, amt1])
                          print(details)
                          date = "SELECT CURDATE();"
                          c.execute(date)
                          fetch_ = c.fetchone()
                          index = fetch_[0]
                          query2 = "INSERT INTO TRANSACTION_DETAILS(transaction_id, username, books_purchased, price, books_name, date_of_purchase) values('{}','{}','{}','{}','{}','{}') ".format(trans_id, username, amt1, XM[0]*amt1, XA[0], index)
                          c.execute(query2)
                          connect.commit()
                          break
                	break
            break
        break
    if opt == 4:
    	clear()
    	Banner()
    	start()





#If User Reviews A Book 
def review():
	import mysql.connector as t 
	connect = t.connect(host = 'localhost', user = 'root', password = 'root', database = 'reviews')
	c = connect.cursor()
	name = m.input("[cyan]Enter Your Full Name : ")
	email = m.input("[cyan]Enter Your Email : ")
	book_name = m.input("[cyan]Enter The Name Of The Book : ")
	review = m.input("[cyan]Enter Your Review : ")
	query = "insert into reviews(NAME, EMAIL, BOOK_NAME, REVIEW) values ('{}','{}','{}','{}')".format(name, email, book_name, review)
	c.execute(query)
	connect.commit()
	m.print("[green][+] THANKS FOR YOUR PRECIOUS REVIEW ♥")
	speak("THANKS FOR YOUR PRECIOUS REVIEW")
	m.print("[green][+] KEEP VISITING US ☺")
	speak("KEEP VISITING US")






#About Us
def About():
	c.print("\n[green]---------------------------------------- WELCOME TO THE ABOUT SECTION OF HACKER HUB ----------------------------------------\n")
	c.print("[green]Hello ! Greetings User Of Hacker Hub Library.")
	c.print("[green]Hope Using This Book Library You Got Great Books Embbeded With Powerful Knowledge About CyberSpace And Much More !")
	c.print("[green]We Are A Curious Team Working And Researching On Hacking And Programming.")
	c.print("[green]Here We Present Some Information About The Programmer Of This FrameWork ...")
	c.print("[green]Names :- \n   RAHUL DIXIT   \n   SAKSHAM AGARWAL   \n   LOV DWIVEDI")
	c.print("[green]This FrameWork Was Divided Into Pieces In Order To Maintain The Accuracy Of The FrameWork.") 
	c.print("[green]Each Of Our Programmers Worked Efficiently And Gave Their Best In Designing And Obtaining Such An Amazing Output.\n")
	c.print("[green]Name And Work Of Each Programmer :-")
	c.print("\t\t[red] RAHUL DIXIT \t\t")
	c.print("\t[green]        Desginer Of Main Page, Login Page, In Login Page\n")
	c.print("\t\t[red] SAKSHAM AGARWAL \t\t")
	c.print("\t[green]        Desginer Of Resgistration Page, Review Page, Admin Panel\n")
	c.print("\t\t[red] LOV DWIVEDI \t\t")
	c.print("\t[green]        Creator Of Databases, Maintaing Databases \n")
	c.print("[green]We Thanks All Our Supporters And Teachers For All The Help In Building This Amazing FrameWork ♥.")
	c.print("[green]There Were Bug Hunters Who Helped Us Finding The Bugs And We Rectified Them To Make The FrameWork Work To The Maximum Efficiency.")
	c.print("[green]A Special Thanks To Bug Hunters ♥.")
	c.print("[green]Once Again A ♥ Hearty ♥ Thanks To All The Helping Hands And Supporters Who Contributed In This FrameWork.\n\n")
	c.print("[green]REGARDS :- TEAM INFINITY \n")






#About Hacker Hub
def About_Hacker_Hub():
	c.print("\n[green]---------------------------------------- WELCOME TO THE ABOUT SECTION OF HACKER HUB ----------------------------------------\n")
	c.print("[green]Hello ! Greetings User Of Hacker Hub Library.")
	c.print("[green]Hope Using This Book Library You Got Great Books Embbeded With Powerful Knowledge About CyberSpace And Much More !")
	c.print("[green]The Aim Of Building This Library Was To Provide Tech Geeks With A Centralised Place Which Has Got All The Powerful Books.",end = "")
	c.print("[green]Written By Expirenced People Of Their Respective Fields And To Provide People Expensive Books At A Low Rate.", end = "")
	c.print("[green]Spread Knowledge About CyberSecurity And It's Importance.")
	c.print("[green]In Today's World People/Students Those Who Are Willing To Start Their Career In Ethical Hacking And Programming.")
	c.print("[green]Are Facing The Most Common Problem That's From Where To Start And Which Books To Refer And From Where To Get These Books For A Affordable Price.")
	c.print("[green]Hacker Hub Library Solves All These Problems By Centralising The Best Books At Low Rates.")
	c.print("[green]We Are Thankful For Having Huge Number Of Users And Thankful To The Designers For Designing Such An Beautiful Place.")
	c.print("[green]Thanks Everyone For Giving Us Love ♥.")
	c.print("[green]We Will Upgrade Ourseleves Of The Latest So Every Reader Of Our Library Gets Best Expirence.\n\n")
	c.print("[green]REGARDS :- TEAM INFINITY \n")






#Anonymous Login 
def anonymous():
	c.print("[green]1. Available Books")
	c.print("[red]2. Review Book")
	c.print("[magenta]3. About Us")
	c.print("[yellow]4. About Hacker Hub")
	c.print("[red]5. Exit\n")
	opt = int(c.input("[cyan]Enter The Task To Be Performed : "))
	if opt == 1:
		avail()
		anonymous()
	if opt == 2:
		review()
		anonymous()
	if opt == 3:
		About()
		anonymous()
	if opt == 4:
		About_Hacker_Hub()
		anonymous()
	if opt == 5:
		out()






#Exiting 
def out():
	clear()
	exit()
	




#Main 
def start():
    c.print("[magenta]1. Login")
    c.print("[yellow]2. Register")
    c.print("[red]3. Anonymous Login")
    c.print("[green]4. About Us")
    c.print("[green]5. About Hacker Hub")
    c.print("[red]6. Exit\n") 
    import time
    while True:
        try:
            choice = int(c.input("[cyan]Enter Your Login Method : "))
            break
        except ValueError:
            c.print("[red][!]INVALID INPUT")
            speak("INVALID INPUT")
            time.sleep(0.9)
            clear()
            Banner()
            start()
            continue
    while choice < 1:
        c.print("[red][!] OPTION OUT OF RANGE")
        speak("OPTION OUT OF RANGE") 
        c.print("[red][+]Try Again")
        speak("Try Again")
        time.sleep(0.9)
        clear()
        Banner()
        start()
        while True:
            try:
                choice = int(c.input("[cyan]Enter Your Login Method : "))
                break
            except ValueError:
                c.print("[red][!] INVALID INPUT ")
                speak("OPTION OUT OF RANGE")
                c.print("[red][+] TRY AGAIN\033[0m")
                speak("Try Again")
                time.sleep(0.9)
                clear()
                Banner()
                start()
                continue
    while choice > 6:
        c.print("[red][!] OPTION OUT OF RANGE ")
        speak("OPTION OUT OF RANGE")
        c.print("[red][+] TRY AGAIN")
        speak("TRY AGAIN")
        time.sleep(0.9)
        clear()
        Banner()
        start()
        while True:
            try:
                choice = int(c.input("[cyan]Enter The Login Method : "))
                break
            except ValueError:
                c.print("[red][!] INVALID INPUT" )
                speak("INVALID INPUT")
                c.print("[red][+] TRY AGAIN")
                speak("TRY AGAIN")
                time.sleep(0.9)
                clear()
                Banner()
                start()
                continue
    if choice == 1:
        c.print("[green]-------------------------------------------------- WELCOME TO LOGIN FORM OF HACKER HUB --------------------------------------------------")
        speak("WELCOME TO LOGIN FORM OF HACKER HUB")
        validation()
        time.sleep(0.5)
    if choice == 2:
        new()
        time.sleep(1.5)
        c.print("[green]-------------------------------------------------- REDIRECTING TO LOGIN FORM --------------------------------------------------")
        speak("REDIRECTING TO LOGIN FORM")
        time.sleep(1.5)
        clear()
        Banner()
        c.print("[green]\t\t ------------------------------------------- WELCOME TO LOGIN FORM OF HACKER HUB -------------------------------------------")
        speak("WELCOME TO LOGIN FORM OF HACKER HUB")
        validation()
        time.sleep(0.3)
        c.print("[green]-------------------------------------------------- REDIRECTING TO THE MAIN PAGE --------------------------------------------------")
        speak("REDIRECTING TO THE MAIN PAGE")
        time.sleep(0.5)
        c.print("[green]-------------------------------------------------- WELCOME TO THE MAIN PAGE OF HACKER HUB --------------------------------------------------\n\033[0m")
        speak("WELCOME TO THE MAIN PAGE OF HACKER HUB")
        in_login()
    if choice == 3:
        c.print("[green]-------------------------------------------------- REDIRECTING TO THE ANONYMOUS PAGE --------------------------------------------------")
        speak("REDIRECTING TO THE ANONYMOUS PAGE")
        time.sleep(1)
        clear()
        Banner()
        time.sleep(2)
        c.print("\t\t\t\t\t\t\t[red] [!] WARNING [!]\n")
        speak("WARNING")
        c.print("\t\t\t\t[red] You Are Logged In As Anonymous You Will Not Be Allowed To Perform Task That Is Buying Books")
        speak("You Are Logged In As Anonymous You Will Not Be Allowed To Perform Task That Is Buying Books")
        c.print("\t\t\t\t[red] Kindly Login/Register To Get Every Feature Offered By Hakcer Hub Library.")
        speak("Kindly Login or Register To Get Every Feature Offered By Hakcer Hub Library")
        ask = c.input("[cyan]Do You Want To Resgister To Hakcer Hub [Y/N] [DEFAULT Y] : ")
        case = ask.upper()
        while not re.match("^[Y&N]*$",case):
            c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
            speak("ERROR ONLY Y AND N ALLOWED")
            ask = input("Want To Resgister To Hakcer Hub[Y/N] [DEFAULT N] : ")
            case = ask.upper()
        while not re.match("^[Y&N]*$",case):
            c.print("[red][!] ERROR ! ONLY Y AND N ALLOWED")
            speak("ERROR ONLY Y AND N ALLOWED")
            break
            continue
        while case == "N":
            c.print("[green]-------------------------------------------------- REDIRECTING IN ANONYMOUS PAGE --------------------------------------------------")
            speak("REDIRECTING IN ANONYMOUS PAGE")
            time.sleep(1)
            clear()
            Banner()
            anonymous()
        while case == "Y" or " ":
            c.print("[green]-------------------------------------------------- REDIRECTING TO REGISTRATION PAGE --------------------------------------------------")
            speak("REDIRECTING TO REGISTRATION PAGE")
            time.sleep(1.5)
            clear()
            Banner()
            new()
    if choice == 4:
        About()
        start()
    if choice == 5:
        About_Hacker_Hub()
        start()
    if choice == 6:
        clear()
        out()
start()
