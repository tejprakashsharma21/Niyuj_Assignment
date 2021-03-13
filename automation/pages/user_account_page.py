"""
@author : Tej Prakash Sharma
Class for User account UI page
"""


class User_Account():
    def __init__(self,driver):
        self.driver=driver

    _user_acc_link_xpath = "//a[@id='userAccountLink']"

    _signout_xpath = "//a[@id='global_signout']"

    def click_user_acc_link(self):
        self.driver.find_element_by_xpath(self._user_acc_link_xpath).click()

    def click_signout_link(self):
        self.driver.find_element_by_xpath(self._signout_xpath).click()

