class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def driver_action(self):
        return self.driver.instance