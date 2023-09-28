import os
import hashlib
import datetime as date

if os.path.isdir('./DB') == True:
    print("DB ready successful!")
elif os.path.isdir('./DB/') == False:
    os.mkdir('./DB')
    print("DB make!")
    print("DB ready successful!")
else:
    print('exit Error : not found directory or not make directory')
    os.system("pause")

#this function by bing AI
def enc(input_string, key):
    # 입력 문자열과 키를 결합합니다.
    combined_input = input_string + key

    # SHA256 해시 객체를 생성합니다.
    encres = hashlib.sha256(combined_input.encode()).hexdigest()

    return encres

username = input("Enter your username : ")
password = input("Enter your password : ")
path = './DB/'+username
pathB = os.getcwd()

def check_login():
    global path, username, password, login, adminlogin
    os.chdir(pathB)
    if username not in os.listdir("./DB"):
        checkwrongPWandname = input('Do you have a account? (y/n) : ')
        checkAutoSingup = input('Do You need auto Sing up? (y/n) : ')
        if checkwrongPWandname == 'n':
            if checkAutoSingup == 'y':
                print('Sing up Start!')
                os.mkdir(path)
                os.chdir(path)
                with open(username +' is password'+'.txt', 'w') as file:
                    file.write(password)
                with open(username +'.txt', 'w') as file:
                    file.write(username)
                with open(username +'.txt', 'a') as file:
                    a = str(date.datetime)
                    file.write("\n"+a)
                with open(username +' is money'+'.txt', 'w') as file:
                    file.write("100000")
                print("Sing up successful!")
                check_login()
            elif checkAutoSingup == 'n':
                print('Sing up Start!')
                usernameB = input("Enter your username: ")
                passwordB = input("Enter your password: ")
                path = './DB/'+usernameB
                os.mkdir(path)
                os.chdir(path)
                with open(usernameB +' is password'+'.txt', 'w') as file:
                    file.write(passwordB)
                with open(usernameB +'.txt', 'w') as file:
                    file.write(usernameB)
                with open(usernameB +'.txt', 'a') as file:
                    file.write("\n"+date.timedelta)
                with open(usernameB +' is money'+'.txt', 'w') as file:
                    file.write(100000)
                print("Sing up successful!")
                check_login()
        elif checkwrongPWandname == 'y':
            os.system("clear")
            print("Login failed!")
            print("Please check your username and password!")
            check_login()
    elif username == "admin" and password == "123456789":
        os.system("clear")
        print("Login successful!")
        print("Welcome back, Admin!")
        adminlogin = True
        login = True
    else:
        os.chdir(path)
        fp = open(username +' is password'+'.txt', 'r')
        fn = open(username +'.txt', 'r')
        username_from_DB = fp.read()
        password_from_DB = fn.read()
        if username == username_from_DB and password == password_from_DB:
            os.system("clear")
            print("Login successful!")
            print("Welcome back, " + username + "!")
            adminlogin = False
            login = True

check_login()

