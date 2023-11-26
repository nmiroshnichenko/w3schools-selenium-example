from selenium.webdriver.common.by import By

from pages.locators.locator import Locator


class BaseLocators:
    rows = Locator(By.TAG_NAME, "tr")
    cells = Locator(By.TAG_NAME, "td")
