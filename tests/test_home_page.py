import allure
from page_objects.HomePage import HomePage
from page_objects.page_elements.SearchElement import SearchElement
from page_objects.CatalogPage import CatalogPage
from test_data.search_values import get_searched_item


@allure.title(f"Тест валидирующий тайтла.")
@allure.testcase('https://pypi.org/project/allure-pytest/', 'Test_case_name')
def test_home_page_positive(driver):
    HomePage(driver).validate_title()


@allure.title(f"Подсчет количества элементов меню")
def test_home_page_menu(driver):
    HomePage(driver).validate_count_menu_items()


@allure.title(f"Поиск товара")
def test_home_page_search(driver):
    SearchElement(driver).search_product(*get_searched_item())
    CatalogPage(driver).verify_cart_product_searched(*get_searched_item())
