import pytest

from page_objects.CatalogPage import CatalogPage
from page_objects.HomePage import HomePage
from page_objects.WishListPage import WishListPage
from test_data.users import login_user
import allure


@allure.link('https://pypi.org/project/allure-pytest/')
@allure.title('Переход в каталог товаров из меню')
def test_visit_catalog_from_menu(browser):
    hp = HomePage(browser)
    cp = CatalogPage(browser)
    hp.select_all_desktops()
    cp.verify_header_of_page()


@pytest.mark.skip(reason="JIRA-7777")
@allure.title('Добавление товара в Wish List')
def test_catalog_add_to_favourite(browser):
    hp = HomePage(browser)
    cp = CatalogPage(browser)
    wlp = WishListPage(browser)
    hp.select_all_desktops()
    cp.add_to_wish_list()
    cp.login_from_alert(*login_user())
    wlp.check_items_in_list()


@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
@allure.title('Сравнение количества тоаров: в выпадающем списке меню и в каталоге')
def test_compare_count_prod(browser):
    hp = HomePage(browser)
    hp.check_count_of_monitors()
