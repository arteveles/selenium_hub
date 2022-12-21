import allure

_alert = [
    ("accept()"),
    ("decline()")
]


@allure.step(f"Алерт: Принять.")
def accept():
    return _alert[0]


@allure.step(f"Алерт: Отклонить.")
def decline():
    return _alert[1]
