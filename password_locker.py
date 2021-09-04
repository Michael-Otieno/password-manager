
import random
import string
import pyperclip

class User:
    """
    create a user class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, username, password):
        """
        method for class user properties
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        delete_user method that deletes a saved account from the list
        """
        User.user_list.remove(self)


class Credentials:
    """
    create credentials class that generates new instance of credentials saved
    """
    credentials_list = []

    @classmethod
    def verify_user(cls, username, password):
        """
        method to verify if user is in the system already
        """
        _user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                _user == user.username
        return _user


    def __init__(self, account, username, password):
        """
        method for class credential properties
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        """
        save_credential method saves credential objects into credential_list
        """
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes a saved credential from the credential_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        """
        method that takes in account name and returns contacts that matches the account
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential_list
        Args:
            account: account name to search if it exists
        Returns:
            Boolean: True or False depending if the credentials exists 
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credential list
        """
        return cls.credentials_list

    @classmethod
    def copy_password(cls, account):
        """
        metthod to copy password using pyperclip
        """
        find_credential = Credentials.find_credential(account)
        pyperclip.copy(find_credential.password)

    def generate_password(stringLength=6):
        """
        Generate a random password
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.choice(password) for i in range(stringLength))


    