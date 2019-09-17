from element_locators.login_screen_locators import LoginLocators
from screen_objects.base_screen import BaseScreen


class LoginScreen(BaseScreen):

    def __init__(self, driver):
        self.driver = driver

    def click_email_field(self):
        email_field = self.driver_action().find_element_by_id(LoginLocators.email_field_id)
        email_field.click()

    def fill_email_field(self, email):
        field = self.driver_action().find_element_by_id(LoginLocators.email_field_id)
        field.clear()
        field.send_keys(email)

    def click_password_field(self):
        password_field = self.driver_action().find_element_by_id(LoginLocators.password_field_id)
        password_field.click()

    def fill_password_field(self, password):
        field = self.driver_action().find_element_by_id(LoginLocators.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login_btn(self):
        btn = self.driver_action().find_element_by_id(LoginLocators.login_btn_id)
        btn.click()
