"""
@author : Tej Prakash Sharma
Class for Hotal Search Ui page
"""
import time
from selenium.webdriver.common.keys import Keys


class Hotal_search():
    def __init__(self,driver):
        self.driver=driver

    __hot_location_xpath = "//input[@id='Tags']"
    __date_from_xpath = "(//i[@class='calendarIcon datePicker'])[1]"
    cd=0
    check_out_date = str(cd+6)
    __check_out_date_xpath = "(//a[text()="+ check_out_date +"])[1]"
    __search_ho_xpath = "//input[@id='SearchHotelsButton']"

    def set_hotal_location(self,location):
        self.driver.find_element_by_xpath(self.__hot_location_xpath).send_keys(location)
        time.sleep(8)
        self.driver.find_element_by_xpath(self.__hot_location_xpath).send_keys(Keys.ENTER)

    def checkIn_date(self):
        self.driver.find_element_by_xpath(self.__date_from_xpath).click()
        current_date = "//a[@class='ui-state-default ui-state-highlight ui-state-active ']"
        self.cd = int(self.driver.find_element_by_xpath(current_date).text)
        print(self.cd)
        nd = str(self.cd + 1)
        next_day_xpath = "(//a[text()=" + nd + "])[1]"
        self.driver.find_element_by_xpath(next_day_xpath).click()

    def checkOut_date(self):
        self.driver.find_element_by_xpath(self.__check_out_date_xpath).click()

    def click_search_hotal_button(self):
        self.driver.find_element_by_xpath(self.__search_ho_xpath).click()
