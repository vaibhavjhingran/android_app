import os

capabilities = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "app": os.path.abspath("../apk/app-debug.apk"),
            "appPackage": "com.github.fgoncalves.qa",
            "appActivity": ".MainActivity",
            "deviceName": "Pixel"
        }