import allure
from page_objects.HomePage import HomePage


@allure.title(f"Тест для смены цены товара на валюту.")
@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
def test_change_currency(browser):
    hp = HomePage(browser)
    hp.change_currency_on_gbp()
    hp.verify_currency_changed_on_gbp()
