import unittest
from password_locker import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours
    Args: unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases

        """
        self.new_user = User("Michael", "otienO2")

    
if __name__ == '__main__':
    unittest.main()
