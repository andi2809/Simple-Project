import os
import getpass
import time
import pickle

# Must Access this to continue.
Loop = True
account = {}

# Admin Account
admin_id = "Andi_2809"
admin_pw = "2809"

while Loop:
    user_input = input("""Welcome - Login
            A. Create Account
            B. Check Account
            C. Login
            D. Exit
            
            """)


    # Enter Username and password
    def login():
        UserName = input("Enter Username: ")
        PassWord = input("Enter Password: ")

        if UserName in account.keys() and PassWord in account.get(UserName):
            time.sleep(1)
            print("Login successful!")
            logged()

        else:
            print("UserName or Password did not match!")

    # If you logged as administrator
    def logged():
        time.sleep(2)
        print("""Welcome Administrator...
         This is a list of registered accounts""")


    # Create account

    def create_account():
        id = input("Enter Your username: ")
        password = input("Enter Your Password: ")
        account[id] = password
        # print(id in account.keys())


    # Check you account is exist
    def check_account():
        cek = input("Enter Username: ")
        if cek in account.keys():
            print("your username is: " + cek + "\nYour password is: " + account.get(cek))
        else:
            print("Your Username does not exits \n")

    # List account
    def account_list():
        print("You must Logged in as administrator to use this command")
        UserName = input("Enter Username: ")
        PassWord = input("Enter Password: ")

        if UserName == admin_id and PassWord == admin_pw:
            time.sleep(1)
            print("Login successful!")
            logged()

            time.sleep(1)
            a_file_open = open("data_akun", "rb")
            output = pickle.load(a_file_open)
            print(output)

        else:
            print("UserName or Password did not match!")


    if user_input.upper() == 'A':
        create_account()
    elif user_input.upper() == 'B':
        check_account()
    elif user_input.upper() == 'C':
        login()
    elif user_input.upper() == 'D':
        a_file = open("data_akun", 'wb')
        pickle.dump(account, a_file)
        a_file.close()
        break
    elif user_input.upper() == 'ADMIN':
        account_list()
    else:
        print("Your Input is Not Exits")

# main()

# password = getpass()
# print(password)
