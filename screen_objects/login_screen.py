class LoginScreen:

    def __init__(self, driver):
        self.driver
        self.email_field_id = "com.github.fgoncalves.qa:id/email"
        self.password_field_id = "com.github.fgoncalves.qa:id/password"
        self.login_btn_id = "com.github.fgoncalves.qa:id/email_sign_in_button"

    def click_email_field(self):
        email_field = self.driver.find_element_by_id(self.email_field_id)
        email_field.click()

    def fill_email_field(self, email):
        field = self.driver.find_element_by_id(self.email_field_id)
        field.clear()
        field.send_keys(email)

    def click_password_field(self):
        password_field = self.driver.find_element_by_id(self.password_field_id)
        password_field.click()

    def fill_email_field(self, password):
        field = self.driver.find_element_by_id(self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login_btn(self):
        btn = self.driver.find_element_by_id(self.login_btn_id)
        btn.click()