import allure
from selenium.common.exceptions import NoSuchElementException as e
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from test_data.search_values import _searched_item


class ProductPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-4']/h1")

    def verify_product_name(self):
        with allure.step(f"Валидация имени продукта. XPATH = {self.PRODUCT_NAME}"):
            try:
                product_name = self.element(self.PRODUCT_NAME).text
                assert product_name == _searched_item[0]
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
