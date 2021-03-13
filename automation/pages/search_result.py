"""
@author : Tej Prakash Sharma
Class for Search result UI page
"""
from automation.lib import xlutils


class Search_Result():
    def __init__(self, driver):
        self.driver = driver

    __five_star_rating = "//span[text()='5 star (']"

    __hotal_name = "(//h2[@class='truncate span span24'])[position()<=5]"

    __hotal_price = "(//h2[@class='truncate span span24']/ancestor::div[@class='right-content-section']//h2[@id='perRoomPrDisp'])[position()<=5]"

    __hotal_review = "(//h2[@class='truncate span span24']/ancestor::div[@class='right-content-section']//a[@data-hash='#taReviews' and @class='hotelDetails'])[position()<=5]"

    __four_star_rating="//span[text()='4 star (']"

    __price_link="//a[text()='Price']"

    __wifi_access="/html/body/section[4]/div[2]/section[2]/section/aside[1]/div/div[2]/div/form/section[12]/div/div/div/nav/label[3]/span[1]"

    __trip_advisor_rating="(//a[text()='TripAdvisor rating'])[2]"

    def click_fiveStarRating(self):
        self.driver.find_element_by_xpath(self.__five_star_rating).click()

    def click_four_star_rating(self):
        self.driver.find_element_by_xpath(self.__four_star_rating).click()

    def click_price_link(self):
        self.driver.find_element_by_xpath(self.__price_link)

    def click_on_wifi_access(self):
        self.driver.find_element_by_xpath(self.__wifi_access)

    def click_on_trip_advisor_rating_link(self):
        self.driver.find_element_by_xpath(self.__trip_advisor_rating)

    def find_top_five_hotal_name(self,filepath,sheetname):
        self.a=1
        hotal = self.driver.find_elements_by_xpath(self.__hotal_name)
        for i in hotal:
            print(i.text)
            xlutils.write_data(filepath, sheetname, 1, self.a, (i.text))
            self.a+=1

    def find_price(self,filepath,sheetname):
        price = self.driver.find_elements_by_xpath(self.__hotal_price)
        self.b=1
        for j in price:
            print(j.text)
            xlutils.write_data(filepath,sheetname, 2, self.b, (j.text))
            self.b+=1

    def review_search(self,filepath,sheetname):
        review = self.driver.find_elements_by_xpath(self.__hotal_review)
        self.c=1
        for k in review:
            print(k.text)
            xlutils.write_data(filepath, sheetname, 3, self.c, (k.text))
            self.c+=1