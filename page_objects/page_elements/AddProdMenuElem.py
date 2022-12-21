import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class AddProdMenuElem(BasePage):
    MENU_BAR = (By.XPATH, "//input[@id='input-meta-title1']")

    def choose_data(self):
        with allure.step(f"Выбор пункта в меню"):
            try:
                self.element(self.MENU_BAR)[1].click
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
