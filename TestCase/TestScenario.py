from Framework.drivermanager import Driver
from Pages import reusables
from Framework import utilities
import unittest

class TestViuApp(Driver):

    def test_installAppAndVerifyHomePage(self):
        reusables.HomePageMethods.VerifyHomePage(self.driver)
        reusables.HomePageMethods.SelectHindi(self.driver)
        reusables.VideoMethods.VerifySignUpPopUpAndNavigateToHomePage(self.driver)
        reusables.VideoMethods.SelectTitle(self.driver)
        reusables.VideoMethods.PlayVideo(self.driver)
        reusables.VideoMethods.PlayNextVideo(self.driver)
        utilities.Utilities.uninstall_application()

if __name__ == '__main__':
    unittest.main()










