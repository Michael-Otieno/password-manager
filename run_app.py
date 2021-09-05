#!/usr/bin/env python3.8

from password_locker import User
from password_locker import Credentials

def create_new_user(username,email, password):
    """
        function to create_new_user
    """
    new_user = User(username,email, password)
    new_user.save_user() #to check

def save_user(user):
    """
    Function to save user
    """
    user.save_user()

def display_user(user):
    """
    function to display existing users
    """
    return User.display_user()

def login_user(username, password):
    """
    function that checks if a user exist and then logs user in
    """
    check_user = Credentials.verify_user(username, password)
    return check_user

def delete_user(user):   #
    """
    function to delete user
    """
    user.delete_user()


def create_new_credential(account, username, password):
    """
    function to create new credential for a given user
    """
    new_credential = Credentials(account, username, password)

def save_credentials(credentials):
    """
    function to save new credentials to the credential_list
    """
    credentials.save_credential()

def display_account_info():
    """
    function that returns all saved accounts
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    function to delete credentials from credential list
    """
    credentials.delete_credentials()

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


def copy_password(account):
    """
    function that copies password using pyperclip
    """
    return Credentials.copy_password(account)

def generate_password(account):
    """
    function that generates random password
    """
    _password = Credentials.generate_password()
    return _password



# def main():
#     print("Hi, Welcome to Password Manager...\n\n Please enter the following to proceed.\n\n CN -- Create a new account \n LI --Log in \n")
#     short_code = input().lower()

#     if short_code == "cn":
#         print("Sign Up")
#         print("-"*10)

#         print("Enter Username: ")
#         username = input()
#         print("Enter email: ")
#         email = input()
#         print("Enter Password: ")     
#         password = input()
        
#         save_user(create_new_user(username,email, password))
#         print(f"Hi {username}, Welcome to Password Manager. Your email is {email} and Password is {password}")


#     elif short_code == "li":
#         print("Enter your password and log in")
#         username = input("Username: ")
#         password = input("Password: ")
#         login = login_user(username,password)
#         if login_user == login:
#             print(f"Hello{username}. Welcome To Password Manager")
#             print('\n')
#         while True:
#             print('Use the short codes: \n CC - Create new credentials \n DC- Display Credentials \n FC - Find credential \n GP - Generate a random password \n D- Delete credential \n EX - exit the application \n')
#             short_code == input().lower().strip()
#             if short_code == "cc":
#                 print("Create a new contact")
#                 account = ("Account Name: ")
                
#                 account = input().lower()
#                 print("Username: ")
#                 username = input()
                




    
        # print("Please Log in")
        # username = input("username: ")
        # password = input("password: ")


   


#     else:
#         print("Enter a valid choice")

# if __name__ == '__main__':

#     main()


# def password_locker():
#     print("Hi! Welcome to Password Manager..\n Please enter the following to proceed.\n CN -- Create a new account \n LI ---Log in \n")

#     short_code = input("").lower().strip()
#     if short_code == "cn":
#         print("Sign Up")
#         username = input("Username: ")
#         while True:
#             print("TP - To type your own password: \n GP - To generate random password")
#             password_chosen = input().lower().strip()
#             if password_chosen == "tp":
#                 password = input("Enter Password\n")
#                 break
#             elif password_chosen == "gp":
#                 password = generate_password()
#                 break
#             else:
#                 print("Invalid choice please try again")
#         save_user(create_new_user(username, password))
#         print(f"Hello{username}, Your account has successfully been created. Your password is: {password}")
    
#     elif short_code == "li":
#         print("Enter your password and log in")
#         username = input("Username: ")
#         password = input("Password: ")
#         login = login_user(username,password)
#         if login_user == login:
#             print(f"Hello{username}. Welcome To Password Manager")
#             print('\n')

#     while True:
#         print('Use the short codes: \n CC - Create new credentials \n DC- Display Credentials \n FC - Find credential \n GP - Generate a random password \n D- Delete credential \n EX - exit the application \n')
#         short_code == input().lower().strip()
#         if short_code == "cc":
#             print("Create New Credential")
#             print('Account name: ')
#             account = input().lower()
#             print("Username: ")
#             username = input()
#             while True:
#                 print("TP - Type password or \n GP - To generate random password")
#                 password_chosen == input().lower().strip()
#                 if password_chosen == "tp":
#                     password = input("Enter your password: \n")
#                     break
#                 elif password_chosen == 'gp':
#                     password = generate_password()
#                     break
#                 else:
#                     print("Invalid password choice please try again")

#             save_credentials(create_new_user(account, username, password))
#             print(f"Account Credential for: {account} - Username: {username} - Password:{password} created successfully")
        
#         elif short_code == "dc":
#             if display_account_info():
#                 print("Your list of accounts")
#                 for account in display_account_info():
#                     print(f"Account: {account.account} \n Username: {username}\n Password: {password}")
#             else:
#                 print("You don't have saved credentials yet")

#         elif short_code == "fc":
#             print("Enter the account name you want to search for")
#             search_name = input().lower()
#             if find_credential(search_name):
#                 search_credential = find_credential(search_name)
#                 print(f"Account Name: {search_credential.account}")
#                 print(f"Username: {search_credential.account} Password: {search_credential.password}")
            
#             else:
#                 print("The credentials doesn't exist")

#         elif short_code == "d":
#             print("Enter account name credential to be deleted")
#             search_name = input().lower()
#             if find_credential(search_name):
#                 search_credential = find_credential(search_name)
#                 search_credential.delete_credential()
#                 print(f"Your stored credential for: {search_credential.account} successfully deleted")

#             else:
#                 print('Credentials to be deleted does not exist.')

#         elif short_code == "gp":
#             password = generate_password()
#             print(f"{password} has been successfully generated.")

#         elif short_code == 'ex':
#             print("Thanks for using password manager. Successfully logged out")
#             break
#         else:
#             print('Wrong entry. Ensure you match the suggested entries')
#     else:
#         print('Please enter a valid input to continue')
        

# if __name__ == "__main__":
#     password_locker()


 # print("Hi, Welcome to Password Manager...\n\n Please enter the following to proceed.\n\n CN -- Create a new account \n LI --Log in \n")
    # short_code == input("").lower().strip()
    # if short_code == "cn":
    #     print("Sign Up")
    #     username = input("Username: ")
    #     password = input("Password: ")
    #     while True:

    #         save_user(create_new_user(username, password))
    #         print(f"Hello{username}! Your account has been successfully created")


                
