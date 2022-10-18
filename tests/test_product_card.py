import allure
from page_objects.page_elements import ProductCard


@allure.title(f"Проверка наличия элементов в карточке товара.")
def test_product_card(browser):
    pc = ProductCard.ProductCard(browser)
    pc.product_card_name()
    pc.product_card_add_to_cart()
    pc.product_card_add_to_wish_list()
    pc.product_card_compare_btn()
    pc.product_card_image()
