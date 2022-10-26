import allure
from page_objects.HomePage import HomePage
from page_objects.RegistrationPage import RegistrationPage


@allure.title(f"Регистрация нового пользователя.")
@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
def test_registration(driver):
    hp = HomePage(driver)
    rp = RegistrationPage(driver)
    hp.click_registrate()
    rp.input_name()
    rp.input_last_name()
    rp.input_mail()
    rp.input_phone()
    rp.input_pass_and_confirm()
    rp.newsletter()
    rp.privacy()
    rp.submit()
