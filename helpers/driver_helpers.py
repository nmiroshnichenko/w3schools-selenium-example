from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import WebElement

from pages.locators.base_locators import Locator


def get_new_driver():
    # Initialize the Chrome driver
    options = webdriver.ChromeOptions()
    options.set_capability(
        "pageLoadStrategy", "eager"
    )  # Possible values: "normal", "eager", "none"
    _driver = webdriver.Chrome(options=options)

    # Set a custom page load timeout (in seconds)
    _driver.set_page_load_timeout(10)
    return _driver


class Driver:
    def __init__(self):
        self._driver = get_new_driver()

    def __getattr__(self, item):
        return getattr(self._driver, item)

    def close(self):
        try:
            self._driver.close()
            self._driver.quit()
        except WebDriverException:
            pass

    def find_element(self, locator: Locator) -> WebElement:
        return self._driver.find_element(locator.by, locator.value)

    def find_elements(self, locator: Locator) -> list[WebElement]:
        return self._driver.find_elements(locator.by, locator.value)
