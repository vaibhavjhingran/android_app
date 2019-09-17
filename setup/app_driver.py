
from appium import webdriver


class AppDriver:

    def __init__(self):
        caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "app": "/Users/vaibhavjhingran/code/python/babbel/app-debug.apk",
            "appPackage": "com.github.fgoncalves.qa",
            "appActivity": ".MainActivity",
            "deviceName": "Pixel"
        }
        self.instace = webdriver.Remote("http://localhost:4723/wd/hub", caps)