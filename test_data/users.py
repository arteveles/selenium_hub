import random

import allure

_user = [
    ("123test@gmail.com", "password"),
    ("user", "bitnami"),
    ("admin", "bitnami1")
]


@allure.step(f"Выбор рандомного юзера. Юзер = {_user}")
def get_user():
    return random.choice(_user)


@allure.step(f"Валидный юзер. {_user[1]}")
def get_valid_user():
    return _user[1]


@allure.step(f"Невалидный юзер. {_user[2]}")
def get_invalid_user():
    return _user[2]


@allure.step(f"Юзер по дефолту. {_user[0]}")
def login_user():
    return _user[0]
