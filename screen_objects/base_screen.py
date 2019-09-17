from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def driver_action(self):
        return self.driver.instance

    def is_element_present(self, element):
        try:
            self.driver_action().find_element_by_accessibility_id(element)
        except Exception as e:
            print(e)
            return False
        return True

    def wait_for_visibility(self, time, element):
        WebDriverWait(self.driver.instance, time).until(
            EC.visibility_of_element_located((
                By.XPATH, element)))
