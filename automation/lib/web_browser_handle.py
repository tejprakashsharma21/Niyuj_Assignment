"""
@author : Tej Prakash Sharma
Class used to handle Browser function
"""


class WebBrowserHandle:
    @staticmethod
    def refresh_browser(driver):
        driver.refresh()

    @staticmethod
    def navigate_back_browser(driver):
        driver.back()

    @staticmethod
    def navigate_forward_browser(driver):
        driver.forward()

    @staticmethod
    def maximize_browser(driver):
        driver.maximize_window()

    @staticmethod
    def minimize_browser(driver):
        driver.minimize_window()

    @staticmethod
    def fullscreen_browser(driver):
        driver.fullscreen_window()

    @staticmethod
    def close_browser(driver):
        driver.close()

    @staticmethod
    def quit_browser(driver):
        driver.quit()

    @staticmethod
    def get_current_url_of_browser(driver):
        print(driver.current_url)

    @staticmethod
    def get_title_of_browser(driver):
        print(driver.title)

    @staticmethod
    def get_name_of_browser(driver):
        print(driver.name)

    @staticmethod
    def get_page_source_of_browser(driver):
        print(driver.page_source)

    @staticmethod
    def set_size_of_browser(driver,width,height):
        driver.set_window_size(width,height)

    @staticmethod
    def set_position_of_browser(driver,x,y):
        driver.set_window_position(x,y)

    @staticmethod
    def set_rect_of_browser(driver,x,y,w,h):
        driver.set_window_rect(x,y,w,h)

    @staticmethod
    def get_size_of_browser(driver):
        print(driver.get_window_size())

    @staticmethod
    def get_position_of_browser(driver):
        print(driver.get_window_position())

    @staticmethod
    def get_rect_of_browser(driver):
        print(driver.get_window_rect())

    @staticmethod
    def set_pageload_timeout(driver,timeinsec):
        driver.set_page_load_timeout(timeinsec)




