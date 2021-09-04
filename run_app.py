#!/usr/bin/env python3.8

from password_locker import User
from password_locker import Credentials

def create_new_user(username, password):
    """
        function to create_new_user
    """
    new_user = User(username, password)
    return new_user

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





