import unittest
from selenium import webdriver

class LoginForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://example.com/login')

    def test_login_form(self):
        username_field = self.driver.find_element_by_name('user[username]')
        username_field.send_keys('bob')
        password_field = self.driver.find_element_by_name('user[password]')
        password_field.send_keys('s3cr3t')
        password_field.submit()

        # Check that we are now logged in
        welcome_message = self.driver.find_element_by_xpath('//*[contains(text(), "Welcome, bob")]')
        self.assertTrue(welcome_message)

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()