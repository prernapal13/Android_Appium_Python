from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os

class Utilities:
    @staticmethod
    def wait_for_element(driver, locator):
        print "# Wait for element to appear... %s" % locator
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))


    @staticmethod
    def wait_for_element_to_disappear(driver, locator):
        print "# Wait for element to disappear... %s"%locator
        WebDriverWait(driver, 20).until_not(EC.presence_of_element_located((By.XPATH, locator)))

    @staticmethod
    def wait_for_loading_diappear(driver, locator):
        while True:
            try:
                print driver.find_element_by_xpath(locator).text
                sleep(1)
            except:
                break

    @staticmethod
    def is_elemet_present(driver, locator):
        try:
            driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def uninstall_application():
        print '## Uninstalling Viu app ##'
        os.system('adb uninstall com.vuclip.viu')
        print '# Successfully uninstalled'

