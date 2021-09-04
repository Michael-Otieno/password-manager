
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