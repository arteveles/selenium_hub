import allure
from selenium.common.exceptions import NoSuchElementException as e
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class WishListPage(BasePage):
    TABLE_DEL_BTN = (By.XPATH, "//table/tbody/tr/td[@class='text-right']/a")
    WL_BTN = (By.XPATH, "//a[@id='wishlist-total']")

    def check_items_in_list(self):
        with allure.step(f"Валидация добавления товара в список желаний."):
            try:
                self.element(self.WL_BTN).click()
                assert self.element(self.TABLE_DEL_BTN)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
