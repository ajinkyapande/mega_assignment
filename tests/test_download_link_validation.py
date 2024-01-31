import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.locators import *


class TestDownloadLinks:

    def test_mega_download_links(self, driver):

        print('1. Open Mega website')
        driver.navigate(driver.base_url)

        print('2. Find and click on the Linux platform button')
        driver.get_element(download_app_button).click()
        time.sleep(5)
        driver.get_element(linux_download_button).click()

        invalid_download_links = []
        time.sleep(5)
        linux_os_versions = driver.browser.find_elements(By.XPATH, drop_down_options)
        for os_download_element in linux_os_versions:
            driver.get_element(drop_down_selector).click()
            os_flevour_val = os_download_element.get_attribute('data-value')
            print(f'Getting download link for {os_flevour_val}')
            time.sleep(10)
            actions = ActionChains(driver.browser)
            actions.move_to_element(driver.get_element(f"{data_value_locator}'{os_flevour_val}']")).perform()

            driver.get_element(f"{data_value_locator}'{os_flevour_val}']").click()
            elements = driver.browser.find_elements(By.XPATH, f"//div[@class='product-card {os_flevour_val} desktop']//div[@class='download-buttons']//*[contains(text(),'Download')]")

            for element in elements:
                download_link = element.get_attribute('href')
                print(f'Validating download link for {os_flevour_val} - {download_link}')
                response = requests.get(download_link)
                if response.status_code != 200:
                    print('Failed to validation download link for{os_flevor_val} - {download_link}')
                    invalid_download_links.append(download_link)

        assert not invalid_download_links, f'Failed to validate download links {invalid_download_links}'




"""    def test_mega_download_links(self, driver):

        print('1. Open Mega website')
        driver.navigate(driver.base_url)

        print('2. Find and click on the Linux platform button')
        driver.get_element("//*[contains(text(),'Download MEGA Desktop App')]").click()
        time.sleep(5)
        driver.get_element("//nav[@class='os-tabs']//*[contains(text(),'Linux')]").click()


        invalid_download_links = []
        linux_os_versions = driver.browser.find_elements(By.XPATH, "//div[contains(@class, 'option active')]")
        for os_download_element in linux_os_versions:
            driver.get_element("//div[@class='selector']").click()
            os_flevour_val = os_download_element.get_attribute('data-value')
            print(f'Getting download link for {os_flevour_val}')
            time.sleep(10)
            driver.get_element(f"//div[@data-value='{os_flevour_val}']").click()
            elements = driver.browser.find_elements(By.XPATH, f"//div[@class='product-card {os_flevour_val} desktop']//div[@class='download-buttons']//*[contains(text(),'Download')]")

            for element in elements:
                download_link = element.get_attribute('href')
                print(f'Validating download link for {os_flevour_val} - {download_link}')
                response = requests.get(download_link)
                if response.status_code != 200:
                    print('Failed to validation download link for{os_flevour_val} - {download_link}')
                    invalid_download_links.append(download_link)

        assert not invalid_download_links, f'Failed to validate download links {invalid_download_links}'

"""