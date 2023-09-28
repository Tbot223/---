import os

def pay(name, money):
    print("making")

def myinfo(username):
    fp = open(username +' is password'+'.txt', 'r')
    fn = open(username +'.txt', 'r')
    username_from_DB = fp.read()
    password_from_DB = fn.read()
    print("[ MY INFO ]")
    print("")
    print("name : "+username_from_DB)
    

def people():
    print("making")

def ranking():
    print("making")

if __name__ == "__main__":
    print("Starting?")