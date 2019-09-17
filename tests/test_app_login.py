import unittest
from setup.app_driver import AppDriver
from screen_objects.login_screen import LoginScreen


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = AppDriver()

    def tearDown(self):
        self.driver.instance.quit()

    def test_enter_username(self):
        login_screen = LoginScreen(self.driver)
        login_screen.click_email_field()
        login_screen.fill_email_field("test@test.test")
        login_screen.click_password_field()
        login_screen.fill_password_field("password")
        login_screen.click_login_btn()


if __name__ == '__main__':
    unittest.main(verbosity=2)
