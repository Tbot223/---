import os
import hashlib

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


if username == "admin" and password == "123456789":
    os.system("clear")
    print("Login successful!")
    print("Welcome back, Admin!")
    adminlogin = True
elif username == username_from_DB and password == password_from_DB:
    os.system("clear")
    print("Login successful!")
    print("Welcome back, " + username + "!")
    adminlogin = False
elif username not in os.listdir('./'):
    print("your no have account")
    print('Sing up Start!')
    checkwrongPWandname = input('Do you have a account? (y/n)')
    checkAutoSingup = input('Do You need auto Sing up? (y/n)')
    if checkwrongPWandname == 'n':
        if checkAutoSingup == 'y':
            os.mkdir(path)
            fp = open(path + './password.txt', 'w')
            fn = open(path + './username.txt', 'w')
            fp.write(password)
            fn.write(username)
            username_from_DB = fn.read()
            password_from_DB = fp.read()
            print("Sing up successful!")
else:
    os.system("clear")
    print("Login failed!")
    print("Please check your username and password!")

