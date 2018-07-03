from appium import webdriver as appdriver
import unittest


class Driver(unittest.TestCase):
    @staticmethod
    def initiateDriver():
        config_apk_path = "E://viuclip//Viu_com.vuclip.viu.apk"

        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'ZX1D6376XG',
                        'noReset': True,
                        'app': config_apk_path,
                        'appPackage': 'com.vuclip.viu',
                        'appActivity': 'com.vuclip.viu.ui.screens.MainActivity',
                        'newCommandTimeout': 600}

        appiumdriver = appdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        appiumdriver.implicitly_wait(10)
        return appiumdriver

    def setUp(self):
        self.driver = Driver.initiateDriver()

    def tearDown(self):
        self.driver.quit()