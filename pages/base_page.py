import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import WebElement

from helpers.driver_helpers import Driver
from pages.locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver: Driver):
        self.driver = driver

    def open(self):
        raise NotImplemented

    @allure.title("Get a table rows")
    def get_table_data(self, table: WebElement) -> list[list[str]]:
        rows = table.find_elements(BaseLocators.rows.by, BaseLocators.rows.value)

        table_rows = []
        for row in rows:
            cells = row.find_elements(BaseLocators.cells.by, BaseLocators.cells.value)
            columns = []
            for cell in cells:
                columns.append(cell.text.strip())
            table_rows.append(columns)
        return table_rows
