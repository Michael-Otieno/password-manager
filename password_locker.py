
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