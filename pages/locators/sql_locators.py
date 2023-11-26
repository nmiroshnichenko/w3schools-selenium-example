from dataclasses import dataclass

from pages.locators.base_locators import By, Locator


@dataclass
class SqlLocators:
    run_sql_button = Locator(By.XPATH, "//button[@type='button' and @class='ws-btn']")
    result_frame = Locator(By.ID, "iframeResultSQL")
    result_table = Locator(By.TAG_NAME, "table", frame=result_frame)
