import allure
from selenium.common.exceptions import NoSuchElementException
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchElement(BasePage):
    XPATH_SEARCH_INPUT = (By.XPATH, "//input[@name='search']")
    XPATH_SEARCH_BTN = (By.XPATH, "//span[@class='input-group-btn']/button")

    def search_product(self, value):
        with allure.step(f"Клик на строку поиска."):
            try:
                self._input(self.element(self.XPATH_SEARCH_INPUT), value)
                self.element(self.XPATH_SEARCH_BTN).click()
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
