"""
@author : Tej Prakash Sharma
Class used for Pagination UI page
"""

from selenium import webdriver


class Pagination:
    def __init__(self, driver):
        self.driver = driver

    __head = "//table[@id='example']//thead/tr/th"
    __name= "//table[@id='example']//tbody/tr/td[1]"
    __position= "//table[@id='example']//tbody/tr/td[2]"
    __office= "//table[@id='example']//tbody/tr/td[3]"
    __age= "//table[@id='example']//tbody/tr/td[4]"
    __startdate="//table[@id='example']//tbody/tr/td[5]"
    __salary="//table[@id='example']//tbody/tr/td[6]"

    def get_head(self):
        return self.driver.find_elements_by_xpath(self.__head)

    def get_name(self):
        return self.driver.find_elements_by_xpath(self.__name)

    def get_position(self):
        return self.driver.find_elements_by_xpath(self.__position)

    def get_office(self):
        return self.driver.find_elements_by_xpath(self.__office)

    def get_age(self):
        return self.driver.find_elements_by_xpath(self.__age)

    def get_startdate(self):
        return self.driver.find_elements_by_xpath(self.__startdate)

    def get_salary(self):
        return self.driver.find_elements_by_xpath(self.__salary)
