from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import *


class DashboardPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    def admin_dropdown(self):
        return self.find_element(By.LINK_TEXT, 'Viktoriia Vasechko')

    def logout_button(self):
        return self.find_element(By.XPATH, "//button[text()[contains(.,'Logout')]]")

    def logout(self):
        self.hover(self.admin_dropdown())
        self.logout_button().click()

    def is_open(self):
        try:
            result = self.admin_dropdown().is_displayed()
        except NoSuchElementException:
            return False
        return result