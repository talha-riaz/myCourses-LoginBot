from selenium import webdriver
from time import sleep
from secrets import username,  pw


class LoginBot():
    def __init__(self):
        self.driver = webdriver.Chrome()



    def login(self):
        self.driver.get("https://mycourses2.mcgill.ca/d2l/loginh/")
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="link1"]')
        login_btn.click()

        email_in = self.driver.find_element_by_xpath('//*[@id="userNameInput"]')
        email_in.send_keys(username)

        pwd_in = self.driver.find_element_by_xpath('//*[@id="passwordInput"]')
        pwd_in.send_keys(pw)

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="submitButton"]')
        sign_in_btn.click()


bot = LoginBot()
bot.login()