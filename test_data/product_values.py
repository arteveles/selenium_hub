from datetime import datetime

import allure

now = datetime.now().strftime("%Y-%m-%d")
_product = [
    (f"test_product_{now}")
]


@allure.step(f"Передача (имени продукта + текущая дата)")
def product_name():
    return _product
