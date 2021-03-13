"""
@author : Tej Prakash Sharma
Class used to handle Browser
"""
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



class BrowserHelper:

    @staticmethod
    def select_helper(webdriver, browser_name):
        if browser_name == "chrome":
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
            return driver
        elif browser_name=="firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "ie":
            driver = webdriver.Ie(IEDriverManager().install())
        elif browser_name == "opera":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        else:
            print("please enter correct browser")

