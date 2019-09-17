from screen_objects.base_screen import BaseScreen
from element_locators.qa_screen_locators import QAScreenLocators as q


class QAScreen(BaseScreen):

    def __init__(self, driver):
        self.driver = driver

    def image_is_displayed(self):
        img = self.driver_action().find_element_by_accessibility_id(q.house_image_access_id)
        img.is_displayed()

    def assert_image_description(self):
        img_desc = self.driver_action().find_element_by_accessibility_id(q.house_image_access_id)
        assert "Picture of a house" in img_desc.title