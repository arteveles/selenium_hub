import json
import logging

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as e


class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.action = ActionChains(driver)
        self._logger_config()

    def _logger_config(self):
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def performance_log(self):
        with allure.step(f"Запись логов браузера в файл performance.json"):
            performance_logs = []
            for line in self.driver.get_log("performance"):
                performance_logs.append(line)
            with open("performance.json", "w+") as f:
                f.write(json.dumps(performance_logs))
    def browser_log(self):
        with allure.step(f"Запись логов браузера в файл browser.json. Level WARNING and ERROR"):
            browser_logs = []
            for line in self.driver.get_log("browser"):
                browser_logs.append(line)
            with open("logs/browser.json", "w+") as f:
                f.write(json.dumps(browser_logs))
            f.close()
    def click(self, element):
        with allure.step(f"Клик на элемент."):
            try:
                self.logger.info("Clicking element: {}".format(element))
                ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def _input(self, element, value):
        with allure.step(f"Ввод данных."):
            try:
                self.logger.info(f"Input {value} in {element}".format(value, element))
                self.click(element)
                element.clear()
                element.send_keys(value)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        with allure.step(f"Поиск элемента в элементе."):
            try:
                self.logger.info(f"Find {child_locator} in {parent_locator}".format(parent_locator, child_locator))
                return self.element(parent_locator).find_element(*child_locator)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def element(self, locator: tuple):
        with allure.step(f"Поиск и ожидание элемента. XPATH = {locator}"):
            try:
                self.logger.info(f"Find element: {locator}".format(locator))
                return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError(f"Не дождался видимости элемента {locator}")

    def verify_product_item(self, product_name):
        with allure.step(f"Проверка наименования продукта."):
            try:
                self.logger.info(f"Verify product item: {product_name}".format(product_name))
                return self.element((By.LINK_TEXT, product_name))
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def switch_to_alert_frame(self, accept_or_decline):
        with allure.step(f"Переключение на алерт, с целью принять или отклонить."):
            try:
                self.logger.info(f"Accept or decline alert: {accept_or_decline}".format(accept_or_decline))
                WebDriverWait(self.driver, 5).until(EC.alert_is_present(), "Не появился алерт")
                return eval(f"self.driver.switch_to.alert.{accept_or_decline}")
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def open(self, url):
        with allure.step(f"Открываю странцу"):
            try:
                self.logger.info("Opening url: {}".format(url))
                self.driver.get(url)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
