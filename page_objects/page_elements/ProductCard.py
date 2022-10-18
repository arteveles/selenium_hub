import allure
from selenium.common.exceptions import NoSuchElementException
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductCard(BasePage):
    PRODUCT_CARD = (By.XPATH, "//div[@class='product-thumb']")
    PRODUCT_CARD_NAME = (By.XPATH, "//div[@class='caption']/h4/a")
    EL1_PRODUCT_CARD = (By.XPATH, "//div[@class='product-thumb']")
    EL2_ADD_BTN = (By.XPATH, "//div[@class='button-group']/button[1]")
    EL2_ASSERTION_TEXT = "Add to Cart"
    EL3_FAVOURITE_BTN = (By.XPATH, "//div[@class='button-group']/button[2]")
    EL4_COMPARE_BTN = (By.XPATH, "//div[@class='button-group']/button[3]")
    EL5_CARD_IMAGE = (By.XPATH, "//div[@class='image']/a/img[@class='img-responsive']")

    def open_product_card(self):
        with allure.step(f"Клик по карточке продукта. XPATH = {self.PRODUCT_CARD}"):
            try:
                product_card = self.element(self.PRODUCT_CARD)
                self.click(product_card)
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def product_card_name(self):
        with allure.step(f"Скролл до поля видимости карточки XPATH = {self.PRODUCT_CARD_NAME}"):
            try:
                assert self.element(self.PRODUCT_CARD_NAME).location_once_scrolled_into_view
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def product_card_add_to_cart(self):
        with allure.step(f"Добавление товара в карзину."):
            try:
                add_btn = self.element(self.EL2_ADD_BTN).text.lower()
                add_btn_assertion = self.EL2_ASSERTION_TEXT.lower()
                assert add_btn == add_btn_assertion
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def product_card_add_to_wish_list(self):
        with allure.step(f"Добавление товара в список желаемого."):
            try:
                assert self.element(self.EL3_FAVOURITE_BTN)
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def product_card_compare_btn(self):
        with allure.step(f"Добавление товара в список сравнения."):
            try:
                assert self.element(self.EL4_COMPARE_BTN)
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def product_card_image(self):
        with allure.step(f"Проверка наличия изображения в карточке товара."):
            try:
                assert self.element(self.EL5_CARD_IMAGE)
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
