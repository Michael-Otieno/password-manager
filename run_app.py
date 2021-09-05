#!/usr/bin/env python3.8
from password_locker import User
from password_locker import Credentials

def create_new_user(username,email, password):
    """
        function to create_new_user
    """
    new_user = User(username,email, password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    User.save_user(user)

def display_user():
    """
    function to display existing users
    """
    return User.display_user()

def delete_user(user):   #
    """
    function to delete user
    """
    User.delete_user(user)

def save_credential(credential):#check
    """
    function to save new credentials to the credential_list
    """
    Credentials.save_credential(credential)

def display_credential():
    """
    function that returns all saved accounts
    """
    return Credentials.display_credentials()

def delete_credential(credentials):#check
    """
    function to delete credentials from credential list
    """
    Credentials.delete_credential(credentials)

def find_credential(account):
    """
    function to check for credentials using account name and returns the account credentials
    """
    return Credentials.find_credential(account)

def check_credentials(account):
    """
    function to check if a credential account exist 
    """
    return Credentials.if_credential_exist(account)


def generate_a_password():
    '''
    Function to generate a password for the user account
    '''
    return Credentials.generate_password()
   

def main():
    print("Hi, Welcome to Password Manager...\n\n Please enter the following to proceed.\n\n CN -- Create a new account \n LI --Log in \n")
    short_code = input().lower()
    if short_code == 'cn':
        username = input("Enter username: ")
        email = input("Enter email: ")
        # password = input("Enter password:")
        while True:
            print('Would you like a generated password?\nPlease choose an option (y/n)')
            response = input().lower()
            if response == 'y':
                password = generate_a_password()
                print(f"Your Password is {password}")
                break
            elif response == 'n':
                print('Enter Password: ')
                password = input()
                break
            else:
                print("Invalid choice. Please try again")

        save_user(create_new_user(username, email, password))
        print(f"Hi {username}, Welcome to Password Manager. Your email is {email} and Password is {password}")

    elif short_code == "li":
         username = input("Enter username: ")
         password = input("Enter password:")
         print("Logged in successfully")

    else:
        print('Invalid choice. Please Try again')

    while True:
        print("Use the words : ADD - add a new account, DI - display all accounts, FI - find an account, E - exit the program")
        short_code = input().lower()
        if short_code == "add":
            print("Add account")
            print("-"*10)
            account = input("Enter application name: ")
            username = input("Enter user name: ")

            while True:
                print(f"Would you like us to generate a password for your {account} account?(y/n)")
                second_response = input().lower()
                if second_response == 'y':
                    password = generate_a_password()

                    print(f"Your password is {password}")
                    break
                elif second_response == "n":
                    print("\n")
                    password = input("Enter a password: ")
                    break
                else:
                    print("\n")
                    print("Invalid input. Please try again.")

            save_credential(create_new_user(account,username,password))
            print(f"Your is {username} for {account} and Password is {password}")

        elif short_code == "di":
            if display_credential():
                print("Here is a list of all your credentials")
                print("\n")
                for credential in display_credential():
                    print(f"{credential.account}\n{credential.username}\n{credential.password}")
                    print('\n')

            else:
                print("You don't seem to have an account use AD to add account")

        elif short_code == "fi":
            print('\n')
            print("Enter the account name: ")
            account_name = input()
            if find_credential(account_name):
                print("-"*10)
                print(f"Account: {find_credential.account}")
                print(f"Username: {find_credential.username}")
                print(f"Password: {find_credential.password}")

        elif short_code == 'E':
            print("\n")
            print("Thank you for using password generator")
            break

        else:
            print("\n")
            print("Invalid input. Please try again")
            print("\n")

    
if __name__ == "__main__":
    main()
