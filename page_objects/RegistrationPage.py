import allure
from selenium.common.exceptions import NoSuchElementException as e
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from test_data.product_values import now


class RegistrationPage(BasePage):
    FN_INPUT = (By.XPATH, "//input[@name='firstname']")
    LN_INPUT = (By.XPATH, "//input[@name='lastname']")
    MAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PHONE_INPUT = (By.XPATH, "//input[@name='telephone']")
    PASS_INPUT = (By.XPATH, "//input[@name='password']")
    CONFIRM_INPUT = (By.XPATH, "//input[@name='confirm']")
    RADIOBTN_NO = (By.XPATH, "//input[@type='radio' and @value='0']")
    PRIVACY_CHK = (By.XPATH, "//input[@type='checkbox' and @value='1']")
    SUBMIT_BTN = (By.XPATH, "//input[@type='submit']")

    def input_name(self):
        with allure.step(f"Ввод имени."):
            try:
                name = f"test_{now}"
                self._input(self.element(self.FN_INPUT), name)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def input_last_name(self):
        with allure.step(f"Ввод фамилии."):
            try:
                name = f"test_{now}"
                self._input(self.element(self.LN_INPUT), name)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def input_mail(self):
        with allure.step(f"Ввод мэила."):
            try:
                name = f"test_{now}"
                domen = "@gmail.com"
                self._input(self.element(self.MAIL_INPUT), name + domen)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def input_phone(self):
        with allure.step(f"Ввод номера."):
            try:
                phone = f"+79999999999"
                self._input(self.element(self.PHONE_INPUT), phone)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def input_pass_and_confirm(self):
        with allure.step(f"Ввод пароля. Подтверждение пароля."):
            try:
                passw = f"test_{now}"
                self._input(self.element(self.PASS_INPUT), passw)
                self._input(self.element(self.CONFIRM_INPUT), passw)
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def newsletter(self):
        with allure.step(f"Не подписываемся на рассылку новостей."):
            try:
                self.element(self.RADIOBTN_NO).click()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def privacy(self):
        with allure.step(f"Соглашаемся с политикой конфиденциальности."):
            try:
                self.element(self.PRIVACY_CHK).click()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)

    def submit(self):
        with allure.step(f"Нажиаем кнопку подтвердить."):
            try:
                self.element(self.SUBMIT_BTN).click()
            except e:
                allure.attach(
                    body=self.driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(e.msg)
