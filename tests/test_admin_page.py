import allure
from allure_commons.types import Severity
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from test_data.users import get_valid_user, get_invalid_user
from test_data.product_values import product_name

@allure.title("лидная регистрация")
@allure.testcase(f'https://pypi.org/project/allure-pytest/', 'Валидация авторизации.')
def test_valid_registration(driver):
    alp = AdminLoginPage(driver)
    alp.open()
    alp.authorization(*get_valid_user())
    alp.logout()


@allure.title(f"Невалидная регистрация. Тест должен пройти успешно.")
@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
def test_invalid_registration(driver):
    alp = AdminLoginPage(driver)
    alp.open()
    alp.authorization(*get_invalid_user())
    alp.validate_no_authorization()


@allure.title(f"Добавление нового продукта.")
@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
def test_add_new_product(driver):
    ap = AdminPage(driver)
    alp = AdminLoginPage(driver)
    alp.open()
    alp.authorization(*get_valid_user())
    ap.select_catalog_product_item()
    ap.add_new_product(*product_name())
    ap.alert_success_add()
    ap.verify_product_add(*product_name())


@allure.title(f"Удаление нового продукта.")
@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
def test_remove_new_product(driver):
    ap = AdminPage(driver)
    alp = AdminLoginPage(driver)
    alp.open()
    alp.authorization(*get_valid_user())
    ap.select_catalog_product_item()
    ap.remove_product(*product_name())
    ap.alert_accept()

@allure.title(f"Проверка работы allure.severity")
@allure.severity(severity_level=Severity.BLOCKER)
def test_allure_severity_blocker(driver):
    pass
