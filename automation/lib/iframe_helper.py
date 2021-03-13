"""
@author : Tej Prakash Sharma
Class used to handle IFrame
"""


class FrameHandler:

    @staticmethod
    def switch_to_frame_by_id(driver,id):
        driver.switch_to.frame(id)

    @staticmethod
    def switch_to_frame_by_element(driver,ele):
        driver.switch_to.frame()

    @staticmethod
    def switch_to_frame_by_name(driver,nameele):
        driver.switch_to.frame(nameele)

    @staticmethod
    def switch_to_frame_by_index(driver,index):
        driver.switch_to.frame(index)

    @staticmethod
    def switch_to_parent_frame(driver):
        driver.switch_to.parent_frame()

    @staticmethod
    def switch_to_main_frame(driver):
        driver.switch_to.default_content()