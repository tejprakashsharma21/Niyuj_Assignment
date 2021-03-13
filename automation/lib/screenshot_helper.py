"""
@author : Tej Prakash Sharma
Class used to capture Screenshot
"""


class CaptureScreenshot:
    @staticmethod
    def save_screenshot_asfile(driver,filepath):
        driver.get_screenshot_as_file(filepath)

    @staticmethod
    def save_screenshot(driver, filepath):
        driver.driver.save_screenshot(filepath)

    @staticmethod
    def save_screenshot_aspng(driver, filepath):
        driver.get_screenshot_as_png(filepath)

    @staticmethod
    def save_screenshot_as_binary(driver, filepath):
        driver.get_screenshot_as_base64(filepath)