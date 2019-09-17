from setup import remote
from setup import desired_capabilites
from appium import webdriver


class AppDriver:

    def __init__(self):
        self.instace = webdriver.Remote(remote.remote_url, desired_capabilites.capabilities)