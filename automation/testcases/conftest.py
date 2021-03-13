"""
@author : Tej Prakash Sharma
Function for setup and teardown activity
"""
from selenium import webdriver
import pytest
from automation.pages import *
from automation.lib import *

driver=''
@pytest.yield_fixture(scope="module",autouse=True)
def setup_teardown():
    global driver
    # 1.Launch the Browser.
    data = JsonHelper.readJson(jsonPath="..\\automation\\data\\login_data.json")
    browser_name = data["browser"]
    #2.Enter the valid URL in the browser search bar.
    url = data["url"]
    driver = BrowserHelper.select_helper(webdriver, browser_name)
    ImplicitlyHelper.implicitly_wait(driver,20)
    WebBrowserHandle.maximize_browser(driver)
    driver.get(url)

    yield
    #CookiesHandle.delete_all_cookies(driver)
    driver.quit()


@pytest.yield_fixture(scope="module")
def setup_login():
    # 3.Click on YourTrip DropDown.
    WebBrowserHandle.get_title_of_browser(driver)
    ExplicitWait.explicitly_wait_for_alert(driver, 20)
    login = Login(driver)
    login.click_yourTrip()
    # 4.Click on SignIn Button.
    login.click_signIn()
    return driver



















