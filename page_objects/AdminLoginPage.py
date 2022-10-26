import time

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminLoginPage(BasePage):
    INPUT_USERN = (By.XPATH, "//input[@name='username']")
    INPUT_PASS = (By.XPATH, "//input[@name='password']")
    LOG_BTN = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BTN = (By.XPATH, "//span[text()='Logout']")
    ALERT_TEXT = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    path = "/admin"
    url = "http://10.0.2.15:8081"

    def open(self):
        with allure.step(f"Прикрепил HTML. Перехожу на страницу {self.url + self.path}"):
            allure.attach(
                body=self.driver.page_source,
                name="Attach_with_HTML_type",
                attachment_type=allure.attachment_type.HTML
            )
            try:
                self.logger.info(f"Open page {self.url + self.path}")
                self.driver.get(self.url + self.path)
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def authorization(self, username, password):
        with allure.step("Ввод логина и пароля:"):
            try:
                self.logger.info(f"Input login '{username}' and password '{password}'".format(username, password))
                self._input(self.element(self.INPUT_USERN), username)
                self._input(self.element(self.INPUT_PASS), password)
                self.click(self.element(self.LOG_BTN))
                return self
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def validate_no_authorization(self):
        with allure.step(f"Проверка авторизации. Alert XPATH = {self.ALERT_TEXT}"):
            try:
                self.logger.info(f"Validate authorization")
                self.element(self.ALERT_TEXT)
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def logout(self):
        with allure.step(f"Клик на кнопку разлогиниться. XPATH = {self.LOGOUT_BTN}"):
            try:
                logout_btn = self.element(self.LOGOUT_BTN)
                time.sleep(2)
                self.click(logout_btn)
                self.logger.info(f"Click 'Logout' button:")
            except NoSuchElementException as e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                self.browser_log()
                raise AssertionError(e.msg)


