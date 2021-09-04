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

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Michael")
        self.assertEqual(self.new_user.password, "otienO2")

    def test_save_user(self):
        """
        test_save_user test to test if the contact object is saved into contact list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


    
if __name__ == '__main__':
    unittest.main()
