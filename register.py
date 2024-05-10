# User registration Signin Signup
import random
from customer import *
from database import *
from bank import Bank

def SignUp():
    username = input("Create username:")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username already exists")
        SignUp()
    else:
        print("Username is available please proceed")
        password = input("Enter your Password:")
        name = input("Enter your Name:")
        age = input("Enter your Age:")
        city = input("Enter your City:")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your account number", account_number)
                break

    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createUser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()


def SignIn():
    username = input("Enter username:")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} enter password:")
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign In succesfully")
                return username
            else:
                print("Wrong password, try again")
                continue

    else:
        print("Enter correct username")
        SignIn()
