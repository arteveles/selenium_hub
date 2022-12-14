import allure

from page_objects.page_elements.SearchElement import SearchElement
from page_objects.page_elements.ProductCard import ProductCard
from test_data.search_values import get_searched_item
from page_objects.ProductPage import ProductPage


@allure.title(f"Проверка поиска товара.")
def test_check_product_page(driver):
    SearchElement(driver).search_product(*get_searched_item())
    ProductCard(driver).open_product_card()
    ProductPage(driver).verify_product_name()
