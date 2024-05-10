from register import *
from bank import *

status = False
print("Welcome to Mohit Banking Project")
while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn"))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please enter valid input from options")
    except ValueError:
        print("Invalid Input try again with numbers")

account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
print(f"Welcome {user.capitalize()} choose your Banking service\n")
while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facility = int(input("1. Balance enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"))

        if 1 <= facility <= 4:

            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balancequiry()

            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter amount to deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid input ie. number")
                        continue
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter amount to withdraw"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter value imput ie. number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter receiver account number"))
                        amount = int(input("Enter money to transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid input ie. number")
                        continue
            else:
                print("Please enter valid input from options")
                continue
    except ValueError:
        print("Invalid Input try again with numbers")
        continue
