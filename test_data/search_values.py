import allure

_searched_item = [(
    "iPhone"
)]


@allure.step(f"Текст = {_searched_item}")
def get_searched_item():
    return _searched_item
