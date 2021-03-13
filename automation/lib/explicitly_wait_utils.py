"""
@author : Tej Prakash Sharma
Class used to handle Explicit wait
"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ExplicitWait():
    @staticmethod
    def explicitly_wait_for_alert(driver,time):
        try:
            wait = WebDriverWait(driver, time).until(expected_conditions.alert_is_present())
            obj = driver.switch_to.alert()
            print(obj.text)
            obj.dismiss()
            print("alert is present")
        except TimeoutException:
            print("alert is not present")

    @staticmethod
    def explicitly_wait_for_frame_and_switchto_it(driver,time,index):
        try:
            wait = WebDriverWait(driver, time).until(expected_conditions.frame_to_be_available_and_switch_to_it(index))
            print("frame is present")
        except TimeoutException:
            print("frame not present")

    @staticmethod
    def explicitly_wait_for_title(driver,time,title):
        try:
            wait = WebDriverWait(driver, time).until(expected_conditions.title_contains(title))
            print("title is present",title)
        except TimeoutException:
            print("title not present")

    @staticmethod
    def explicitly_wait_for_element_is_clickable(driver,time,title,element):
        try:
            wait = WebDriverWait(driver, time).until(expected_conditions.element_to_be_clickable(element))
            print("element is clickable")
            element.click()
        except TimeoutException:
            print("element is not clickable")


