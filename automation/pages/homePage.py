"""
@author : Tej Prakash Sharma
Class for Home Page UI
"""
from selenium.webdriver import ActionChains


class Home:
    def __init__(self, driver):
        self.driver = driver

    __hotel_xpath = "//a[@title='Find hotels in destinations around the world']"

    def click_hotal_tab(self):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_xpath(self.__hotel_xpath)).click().perform()


