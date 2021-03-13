"""
@author : Tej Prakash Sharma
Class used to handle Implicit Wait
"""


class ImplicitlyHelper:
    @staticmethod
    def implicitly_wait(driver,time):
        driver.implicitly_wait(time)