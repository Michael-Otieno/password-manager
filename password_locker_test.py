import unittest
from password_locker import User
from password_locker import Credentials

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
        test_save_user test to test if the user object is saved into contact list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)



class TestCredentials(unittest.TestCase):
    """
    Test class to define credentials class
    """
    def setUp(self):
        """
         Set up method to run before each test case for credential class
        """
        self.new_credential = Credentials("email", 'Michael', 'otienO2')

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account, "email")
        self.assertEqual(self.new_credential.username, "Michael")
        self.assertEqual(self.new_credential.password, "otienO2")

    def test_save_credential(self):
        """
        test_save_credential test to test if the credential object is saved into credential_list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)


    def tearDown(self):   #
        """
        method that does clean up after each test
        """
        Credentials.credentials_list = []


    def test_save_multiple_credential(self):
        """
        test_save_multiple_contact to check if we can save multple contact objects to our credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credentials("email", "Michael", "otieno2")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        """
        test_delete_credential to test if we can remove a credential from our credential list
        """
        self.new_credential.save_credential()
        test_credential = Credentials("email", "Michael", "otieno2")
        test_credential.save_credential()

        self.new_credential.delete_credential() #deleting a contact object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credential_by_account(self):
        """
        test to check if we can findd a credential by account and display the details of the credential
        """
        self.new_credential.save_credential()
        test_credential = Credentials("email", "Michael", "otieno2")
        test_credential.save_credential()

        find_credential = Credentials.find_credential("email")
        self.assertEqual(find_credential.account, test_credential.account)


    def test_credential_exists(self):
        """
        test to check if credentials exists
        """
        self.new_credential.save_credential()
        test_credential = Credentials("email", "Michael","otienO2")
        test_credential.save_credential()
        found_credential = Credentials.if_credential_exist('email')
        self.assertTrue(found_credential)

    def test_display_saved_credential(self):
        """
        test to display contacts saved
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)



    
if __name__ == '__main__':
    unittest.main()
