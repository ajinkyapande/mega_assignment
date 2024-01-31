from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Browser:

    def __init__(self, url):
        self.browser = None
        self.base_url = url

    def launch_chrome(self, path=None):
        """

        :param path:
        :return:
        """

        self.browser = webdriver.Chrome()
        self.browser.get(self.base_url)
        return self.browser

    def refresh(self):
        self.browser.refresh()

    def navigate(self, url=''):
        self.browser.get(url)

    def get_element(self, path):
        element = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        return element
