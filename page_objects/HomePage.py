import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException as e

import re


class HomePage(BasePage):
    MYAKK_SELECT = (By.XPATH, "//span[text()='My Account']")
    REG_BTN = (By.XPATH, "//li/a[text()='Register']")
    CURRENCY = (By.XPATH, "//span[text()='Currency']")
    CURRENCY_GBP = (By.XPATH, "//button[@name='GBP']")
    VERIFY_GBP = (By.XPATH, "//strong[text()='£']")
    VERIFY_GBP_2 = (By.XPATH, "//div[@class='row']//p[contains(text(), '£')]")
    CATALOG_SEE_ALL = (By.XPATH, "//div[@class='dropdown-menu']/a[text() = 'Show All Desktops']")
    MENU_DESKTOP = (By.XPATH, "//ul[@class='nav navbar-nav']/li/a[text()='Desktops']")
    MENU_COMPONENTS = (By.XPATH, "//a[text()='Components']")
    CTG_COMPARE_ITEMS = (By.XPATH, "//ul[@class='nav navbar-nav']/child::li[3]//child::li[2]/a")
    COUNT_PRODUCTS = (By.XPATH, "//div[@id='content']/div[3]/div")
    TITLE = "Your Store"
    MENU_LIST = (By.XPATH, "//ul[@class='nav navbar-nav']/li")

    def click_registrate(self):
        with allure.step(f"Клик на кнопку регистрации. XPATH = {self.REG_BTN}"):
            try:
                self.element(self.MYAKK_SELECT).click()
                self.element(self.REG_BTN).click()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)

    def change_currency_on_gbp(self):
        with allure.step(
                f"Смена отображения цены товара в валюте. 1_XPATH = {self.CURRENCY}, 2_XPATH = {self.CURRENCY_GBP}"):
            try:
                self.element(self.CURRENCY).click()
                self.element(self.CURRENCY_GBP).click()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)

    def verify_currency_changed_on_gbp(self):
        with allure.step(f"Проверка смены цены товара на валюту."):
            try:
                assert self.element(self.VERIFY_GBP)
                assert self.element(self.VERIFY_GBP_2)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)

    def select_all_desktops(self):
        with allure.step(f"Выбор списка компов из менюшки"):
            try:
                self.element(self.MENU_DESKTOP).click()
                self.element(self.CATALOG_SEE_ALL).click()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)

    def check_count_of_monitors(self):
        with allure.step(f"Сверка количества мониторов: значения одинаковы в менюшке и на странице каталога товара."):
            try:
                self.element(self.MENU_COMPONENTS).click()
                num = re.findall(r"\d+", self.element(self.CTG_COMPARE_ITEMS).text)
                self.element(self.CTG_COMPARE_ITEMS).click()
                count_prod = self.elements(self.COUNT_PRODUCTS)
                assert str(len(count_prod)) == num[0]
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)

    def validate_title(self):
        with allure.step(f"Валидация наименования."):
            try:
                title = self.driver.title
                assert title == self.TITLE
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)

    def validate_count_menu_items(self):
        with allure.step(f"Валидация количества пунктов меню."):
            try:
                count_menu_items = len(self.elements(self.MENU_LIST))
                assert count_menu_items == 8
            except e:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=AttachmentType.PNG
                )
                raise AssertionError(e.msg)
