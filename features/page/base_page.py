from selenium.webdriver.common.action_chains import ActionChains
import abc


class BasePage(object):
    def __init__(self, browser, base_url='https://trial.bynder.com/login/'):
        self.base_url = base_url
        self.browser = browser

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self,url):
        self.browser.get(url)

    @abc.abstractmethod
    def is_open(self):
        """Returns True if page is opened"""
        return

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()

