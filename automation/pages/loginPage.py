"""
@author : Tej Prakash Sharma
Class for Login UI page
"""

class Login:
    def __init__(self, driver):
        self.driver = driver

    __your_trip_xpath = "//span[text()='Your trips']"
    __signin_id = "SignIn"

    def click_yourTrip(self):
        self.driver.find_element_by_xpath(self.__your_trip_xpath).click()

    def click_signIn(self):
        self.driver.find_element_by_id(self.__signin_id).click()

