import unittest
from setup.app_driver import AppDriver
from screen_objects.login_screen import LoginScreen
from screen_objects.qa_screen import QAScreen
from test_data.user_info import UserInfo


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = AppDriver()

    def tearDown(self):
        self.driver.instance.quit()

    def test_login_feature(self):
        login_screen = LoginScreen(self.driver)
        login_screen.click_email_field()
        login_screen.fill_email_field(UserInfo.USERNAME)
        login_screen.click_password_field()
        login_screen.fill_password_field(UserInfo.PASSWORD)
        login_screen.click_login_btn()
        home = QAScreen(self.driver)
        home.check_navigation_to_home_screen()
        home.check_screen_readiness()
        home.image_is_displayed()


if __name__ == '__main__':
    unittest.main(verbosity=2)
