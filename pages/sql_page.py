import allure

from helpers.wait import wait
from pages.base_page import BasePage
from pages.locators.sql_locators import SqlLocators


class SqlPage(BasePage):
    @allure.title('Open page "SQL Tryit Editor"')
    def open(self):
        self.driver.get(
            "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
        )
        return self

    @allure.title(f'Fill out field "SQL Statement" with value {str}')
    def set_sql(self, sql: str):
        self.driver.execute_script(f"window.editor.setValue('{sql}');")
        return self

    @allure.title('Click on the button "Run SQL"')
    def run_sql(self):
        run_sql_button = self.driver.find_element(SqlLocators.run_sql_button)
        run_sql_button.click()
        return self

    @allure.title('Get "Result" table')
    def get_result_table(self):
        """
        Get "Result" table WebElement

        :return: webdriver.WebElement
        """
        result_frame = self.driver.find_element(SqlLocators.result_frame)
        self.driver.switch_to.frame(result_frame)
        result_table = self.driver.find_element(SqlLocators.result_table)
        # result_table = wait(waiting_for='"Result" table', condition=_get_result_table)
        return result_table

    @allure.title('Get "Result" table data')
    def get_result_rows(self):
        result_table = self.get_result_table()
        return self.get_table_data(result_table)
