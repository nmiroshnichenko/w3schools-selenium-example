import allure

from pages.sql_page import SqlPage


def test_verify_customer_details(driver):
    with allure.step("Setup before the test: open the page"):
        sql_page = SqlPage(driver()).open()

    with allure.step("Run a simple sql request"):
        sql_page.set_sql("SELECT * FROM Customers")
        sql_page.run_sql()
        results = sql_page.get_result_rows()

    with allure.step("Check a sample entry"):
        test_entry_name = "Giovanni Rovelli"
        test_row = [result for result in results if test_entry_name in result]
        assert test_row
        test_row = test_row[0]
        test_entry_address = "Via Ludovico il Moro 22"
        assert test_entry_address in test_row
