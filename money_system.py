import os
import hashlib

if os.listdir('./') in "./DB":
    print("DB ready successful!")
elif os.listdir('./') not in "./DB":
    os.mkdir('./DB')
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

username = input("Enter your username: ")
password = input("Enter your password: ")
path = './DB'+username
fp = open(path + './password.txt', 'r')
fn = open(path + './username.txt', 'r')
username_from_DB = fn.read()
password_from_DB = fp.read()

def check_login():
    if username not in os.listdir('./'):
        print("your no have account")
        print('Sing up Start!')
        checkwrongPWandname = input('Do you have a account? (y/n)')
        checkAutoSingup = input('Do You need auto Sing up? (y/n)')
        if checkwrongPWandname == 'n':
            if checkAutoSingup == 'y':
                os.system("clear")
                os.mkdir(path)
                fp = open(path + './password.txt', 'w')
                fn = open(path + './username.txt', 'w')
                fp.write(password)
                fn.write(username)
                print("Sing up successful!")
                check_login()
            elif checkAutoSingup == 'n':
                os.system("clear")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                path = './DB'+username
                os.mkdir(path)
                fp = open(path + './password.txt', 'w')
                fn = open(path + './username.txt', 'w')
                fp.write(password)
                fn.write(username)
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
    elif username == username_from_DB and password == password_from_DB:
        os.system("clear")
        print("Login successful!")
        print("Welcome back, " + username + "!")
        adminlogin = False
        login = True
