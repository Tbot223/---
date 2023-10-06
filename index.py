import os
import hashlib
from datetime import datetime

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

def pay(name, money):
    print('?')

def check_login():
    global path, username, password, login
    os.chdir(pathB)
    if username not in os.listdir("./DB"):
        checkacchave = input('Do you have a account? (y/n) : ')
        checkAutoSingup = input('Do You need auto Sing up? (y/n) : ')
        if checkacchave == 'n':
            if checkAutoSingup == 'y':
                print("")
                print('Sing up Start!')
                os.mkdir(path)
                os.chdir(path)
                with open(username +' is password'+'.txt', 'w') as file:
                    file.write(password)
                with open(username +'.txt', 'w') as file:
                    file.write(username)
                with open(username +'.txt', 'a') as file:
                    a = str(datetime.today())
                    file.write("\n"+a)
                with open(username +' is money'+'.txt', 'w') as file:
                    file.write("100000")
                print("Sing up successful!")
                check_login()
            elif checkAutoSingup == 'n':
                print('Sing up Start!')
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                path = './DB/'+username
                os.mkdir(path)
                os.chdir(path)
                with open(username +' is password'+'.txt', 'w') as file:
                    file.write(password)
                with open(username +'.txt', 'w') as file:
                    file.write(username)
                with open(username +'.txt', 'a') as file:
                    a = str(datetime.today())
                    file.write("\n"+a)
                with open(username +' is money'+'.txt', 'w') as file:
                    file.write("10000")
                print("Sing up successful!")
                check_login()
        elif checkacchave == 'y':
            print("")
            print("Login failed!")
            print("Please check your username and password!")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            check_login()
    else:
        os.chdir(path)
        fp = open(username +' is password'+'.txt', 'r')
        fn = open(username +'.txt', 'r')
        username_from_DB = fn.read().split('\n')
        print(username_from_DB)
        password_from_DB = fp.read()
        if username == username_from_DB[0] and password == password_from_DB:
            print("")
            print("Login successful!")
            print("Welcome back, " + username + "!")
            login = True
            system()

def system():
    print("")
    print('help = "?" enter')
    print("")
    command = input("Enter command : ")
    if command == '?':
        print("")
        print('[ COMMANDS ]')
        print("")
        print("? - commands print")
        print("info - my info print")
        print('exit - exit')
        print('member_list - member list print')
        system()
    elif command == "info":
        print("")
        fp = open(username +' is password'+'.txt', 'r')
        fn = open(username +'.txt', 'r')
        fm = open(username +' is money'+'.txt', 'r')
        username_from_DB = fn.read().split('\n')
        password_from_DB = fp.read()
        money_from_DB = fm.read()
        print("[ MY INFO ]")
        print("")
        print("name : "+username_from_DB[0])
        money_from_DB = int(money_from_DB)
        print("money : "+format(money_from_DB, ",")+"won")
        print("Account created date : "+username_from_DB[1][:-7])
        system()
    elif command == "exit":
        os.system("pause")
        os.chdir("./DB")
    elif command == "member_list":
        os.chdir(pathB)
        os.chdir("./DB")
        users = os.listdir()
        print("")
        print("[ MEMBER_LIST ]")
        print("")
        for i in range(len(users)):
                print(users[i])
        system()
    else:
        print("")
        print("wrong command")
        system()

check_login()

