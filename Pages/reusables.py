from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions
from Framework.utilities import Utilities
from Pages import locators


class HomePageMethods:
    @staticmethod
    def VerifyHomePage(driver):
        print '## Verifying home page ##'
        Utilities.wait_for_element(driver, locators.HomePage.xpath_home_page_header)
        ele_page_header = driver.find_element_by_xpath(locators.HomePage.xpath_home_page_header)
        header_text = ele_page_header.text
        assert header_text == locators.HomePage.home_page_header_text, "Actual header %s should be same as Expected header %s" % (
        header_text, locators.HomePage.home_page_header_text)

    @staticmethod
    def SelectHindi(driver):
        print '## Selecting option : Hindi ##'
        Utilities.wait_for_element(driver, locators.HomePage.xpath_hindi)
        ele_hindi = driver.find_element_by_xpath(locators.HomePage.xpath_hindi)
        ele_hindi.click()


class VideoMethods:
    @staticmethod
    def VerifySignUpPopUpAndNavigateToHomePage(driver):
        print '## Verifying signup pop-up and skipping to previous page ##'
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_signup_popup)
        assert Utilities.is_elemet_present(driver, locators.VideoPage.xpath_signup_popup), "Sign up pop-up should appear on screen."
        driver.back()

    @staticmethod
    def SelectTitle(driver):
        print '## Clicking on video title ##'
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_title)
        ele_title = driver.find_element_by_xpath(locators.VideoPage.xpath_title)
        ele_title.click()
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_play_button)
        assert Utilities.is_elemet_present(driver, locators.VideoPage.xpath_play_button), "Play Video button should appear on screen."

    @staticmethod
    def PlayVideo(driver):
        print '## Clicking on play button to play video ##'
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_play_button)
        ele_play = driver.find_element_by_xpath(locators.VideoPage.xpath_play_button)
        ele_play.click()

    @staticmethod
    def PlayNextVideo(driver):
        print '## Clicking on next video button to play next video ##'
        actions = TouchActions(driver)
        Utilities.wait_for_loading_diappear(driver, locators.VideoPage.xpath_video_loading)
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_video_frame)
        assert Utilities.is_elemet_present(driver, locators.VideoPage.xpath_video_frame), "Video should get played."

        ele_video_frame = driver.find_element_by_xpath(locators.VideoPage.xpath_video_frame)
        actions.tap(ele_video_frame).perform()

        Utilities.wait_for_element(driver, locators.VideoPage.xpath_play_next_video)
        ele_next_video = driver.find_element_by_xpath(locators.VideoPage.xpath_play_next_video)
        ele_next_video.click()

        Utilities.wait_for_loading_diappear(driver, locators.VideoPage.xpath_video_loading)
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_video_frame)
        assert Utilities.is_elemet_present(driver, locators.VideoPage.xpath_video_frame), "Next video should get played."

        ele_video_frame = driver.find_element_by_xpath(locators.VideoPage.xpath_video_frame)
        actions.tap(ele_video_frame).perform()
        Utilities.wait_for_element(driver, locators.VideoPage.xpath_play_next_video)
        ele_next_video = driver.find_element_by_xpath(locators.VideoPage.xpath_play_next_video)
        print "# Next video title - %s " % ele_next_video.text
        assert "Ep-2" in ele_next_video.text, "Ep-2 should be present in video title %s"%ele_next_video.text

