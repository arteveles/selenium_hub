import time
import pytest
from page_objects.CatalogPage import CatalogPage
from page_objects.HomePage import HomePage
from page_objects.WishListPage import WishListPage
from test_data.users import login_user
import allure


@allure.link('https://pypi.org/project/allure-pytest/')
@allure.title('Переход в каталог товаров из меню')
def test_visit_catalog_from_menu(driver):
    hp = HomePage(driver)
    cp = CatalogPage(driver)
    hp.select_all_desktops()
    cp.verify_header_of_page()
    time.sleep(15)


@pytest.mark.skip(reason="JIRA-7777")
@allure.title('Добавление товара в Wish List')
def test_catalog_add_to_favourite(driver):
    hp = HomePage(driver)
    cp = CatalogPage(driver)
    wlp = WishListPage(driver)
    cp.open()
    hp.select_all_desktops()
    cp.add_to_wish_list()
    cp.login_from_alert(*login_user())
    wlp.check_items_in_list()

