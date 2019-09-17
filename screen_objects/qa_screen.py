from screen_objects.base_screen import BaseScreen
from element_locators.qa_screen_locators import QAScreenLocators as q


class QAScreen(BaseScreen):

    def __init__(self, driver):
        self.driver = driver

    def image_is_displayed(self):
        img = self.driver_action().find_element_by_accessibility_id(q.house_image_access_id)
        if img.is_displayed():
            print(f'Logged in to see "The Picture of a house".')

    def check_screen_readiness(self):
        print(self.is_element_present(q.house_image_access_id))

    def check_navigation_to_home_screen(self):
        self.wait_for_visibility(15, '//android.widget.ImageView[@content-desc="Picture of a house"]')
