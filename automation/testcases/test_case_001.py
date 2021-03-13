"""
@author : Tej Prakash Sharma
Test case for capture 5 star rating hotal details
"""
import pytest
import allure
from allure_commons.types import AttachmentType
from automation.pages import *
from automation.lib import *

@pytest.mark.tests
@pytest.mark.test01
class Test_Case_001:
    f_path = "..\\automation\\Logs\\abcd.log"
    logger = LoggerHeper.log_helper(f_path)
    filepath="..\\automation\\data\\Cleartrip.xlsx"
    data = JsonHelper.readJson(jsonPath= "..\\automation\\data\\login_data.json")
    username = data["Username"]
    password = data["Password"]

    def test_001(self, setup_teardown, setup_login):
        try:
            # 3.Click on YourTrip DropDown.
            self.logger.info("***************login start*****************************")
            driver = setup_login
            time.sleep(10)
            FrameHandler.switch_to_frame_by_id(driver, 0)
            # 5.Enter the given username and password in username and password text fields.
            sign = SignIn(driver)
            sign.set_user_name(self.username)
            sign.set_password(self.password)
            # 6.Click on signin button.
            sign.click_signIn_button()
            # 7.Click on 'Hotal' module in the Left navigation bar in HomePage.
            time.sleep(10)
            home = Home(driver)
            home.click_hotal_tab()
            # 8.Enter all the Valid details in 'Search for Hotal' Page.
            # (ex: where(delhi),checkin(next to current date),checkout(any),Travellers(any))
            search = Hotal_search(driver)
            search.set_hotal_location("New Del")
            search.checkIn_date()
            time.sleep(5)
            search.checkOut_date()
            # 9.Click on the 'Search Hotal' Button.
            search.click_search_hotal_button()
            # 10.Click on 'five star rating' checkbox
            time.sleep(25)
            result = Search_Result(driver)
            result.click_fiveStarRating()
            # 11.Capture the details(name and price) of top 5 hotels with ratings >=4
            result.find_top_five_hotal_name(self.filepath, "Sheet1")
            result.find_price(self.filepath, "Sheet1")
            # 12.Capture the number of reviews
            result.review_search(self.filepath, "Sheet1")
            user = User_Account(driver)
            user.click_user_acc_link()
            user.click_signout_link()
            assert True
        except :
            CaptureScreenshot.save_screenshot_asfile(driver,"..\\automation\\screenshot\\tc_002.png")
            allure.attach(CaptureScreenshot.save_screenshot_asfile(driver,"..\\automation\\screenshot\\tc_001.png"),name="t_c001",attachment_type=AttachmentType.PNG)
            assert False















