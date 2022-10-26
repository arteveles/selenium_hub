import allure
from selenium.common.exceptions import NoSuchElementException as e
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    CATALOG_HEADER = (By.XPATH, "//div[@class='col-sm-9']/h2")
    CATALOG_BTN_ADD_TO_FVT = (By.XPATH, "//div[@class='button-group']/button[2]")
    LOGIN_LINK = (By.XPATH, "//a[text()='login']")
    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")
    EMAIL_INP = (By.XPATH, "//input[@name='email']")
    PASSW_INP = (By.XPATH, "//input[@name='password']")
    PROD_NAME = (By.XPATH, "//div[@class='product-thumb']//h4/a")
    CATALOG_HEADER_TEXT = "Desktops"
    url = "http://10.0.2.15:8081"
    path = ""

    def open(self):
        with allure.step(f"Прикрепил HTML. Перехожу на страницу {self.url + self.path}"):
            try:
                self.logger.info(f"Open page {self.url + self.path}")
                self.driver.get(self.url + self.path)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
    def verify_header_of_page(self):
        with allure.step(f"Элемент {self.CATALOG_HEADER} имеет заголовок {self.CATALOG_HEADER_TEXT}"):
            try:
                desktop_header = self.element(self.CATALOG_HEADER)
                assert desktop_header.text == self.CATALOG_HEADER_TEXT
            except e:
                allure.attach(
                    body=self.driver.save_screenshot('screen.png'),
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def add_to_wish_list(self):
        with allure.step(f"Клик на кнопку: добавить в список желаний. Селектор = {self.CATALOG_BTN_ADD_TO_FVT} "):
            try:
                self.element(self.CATALOG_BTN_ADD_TO_FVT).click()
            except e:
                allure.attach(
                    body=self.driver.save_screenshot('screen.png'),
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def login_from_alert(self, email, password):
        with allure.step(f"Логинюсь из уведомления, запрашивающего авторизацию."):
            try:
                self.element(self.LOGIN_LINK).click()
                self._input(self.element(self.EMAIL_INP), email)
                self._input(self.element(self.PASSW_INP), password)
                self.element(self.LOGIN_BTN).click()
                return self
            except e:
                allure.attach(
                    body=self.driver.save_screenshot('screen.png'),
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def verify_cart_product_searched(self, product_name_value):
        with allure.step(f"Сверяю имя продукта"):
            try:
                product_name = self.element(self.PROD_NAME).text
                assert product_name == product_name_value
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
