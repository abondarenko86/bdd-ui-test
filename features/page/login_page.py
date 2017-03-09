import abc
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import *


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    def username(self):
        return self.find_element(By.ID, 'inputEmail')

    username1 = property(username)

    def message(self):
        return self.find_element(By.CSS_SELECTOR, ".cbox_messagebox").get_attribute('innerHTML')

    def password(self):
        return self.find_element(By.ID, 'inputPassword')

    def login_button(self):
        return self.find_element(By.CSS_SELECTOR, '.login-btn')

    def login(self, username, passwd):
        self.username().send_keys(username)
        self.password().send_keys(passwd)
        self.login_button().click()

    def open(self):
        self.visit("https://trial.bynder.com/login/")

    def is_open(self):
        try:
            result = self.username1.is_displayed()
        except NoSuchElementException:
            return False
        return result


