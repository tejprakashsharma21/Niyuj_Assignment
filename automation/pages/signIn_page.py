"""
@author : Tej Prakash Sharma
Class for SignIn UI page
"""
class SignIn:
    __user_name_xpath = "//input[@id='email']"
    __password_id = "password"
    __sign_button_id = "signInButton"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self,username):
        self.driver.find_element_by_xpath(self.__user_name_xpath).send_keys(username)

    def set_password(self,password):
        self.driver.find_element_by_id(self.__password_id).send_keys(password)

    def click_signIn_button(self):
        self.driver.find_element_by_id(self.__sign_button_id).click()





