"""
@author : Tej Prakash Sharma
All function automatically available for all the test cases according to scope
"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from dynamic_table.pages.data import *


@pytest.yield_fixture(params=[BROWSER],scope='class')
def init_driver(request):
    if request.param=="chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param=="firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif request.param=="ie":
        driver = webdriver.Ie(IEDriverManager().install())
    else:
        print("not a valid browser")
    request.cls.driver=driver


    yield
    driver.quit()
"""
@pytest.yield_fixture(scope="module")
def init_driver(request,browser=BROWSER):
    global driver
    if browser=="chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser=="firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser=="ie":
        driver = webdriver.Ie(IEDriverManager().install())

    else:
        print("not a valid browser")
    return driver

@pytest.yield_fixture()
def setup_teardown():
    driver.get(URL)
    yield
    driver.quit()




"""

