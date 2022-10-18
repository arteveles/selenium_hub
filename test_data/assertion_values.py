import allure

_admin_page_values = [
    ("Logout")
]


@allure.step(f"Текст = {_admin_page_values}")
def logout():
    return _admin_page_values
