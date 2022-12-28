import allure
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminLoginPage(BasePage):
    INPUT_USERN = (By.XPATH, "//input[@name='username']")
    INPUT_PASS = (By.XPATH, "//input[@name='password']")
    LOG_BTN = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BTN = (By.XPATH, "//span[text()='Logout']")
    ALERT_TEXT = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

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
