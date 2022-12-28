import logging
import os.path
import datetime
import pytest
import requests
import allure
import time
import json

from allure_commons.types import AttachmentType
from selenium import webdriver


@allure.step("Waiting for resource availability {url}")
def wait_url_data(url, timeout=10):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--bversion", action="store", default="")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=True)
    parser.addoption("--url", default="http://10.0.2.15:8081")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")
    url = request.config.getoption("--url")

    """Создается новый логгер, и берется имя теста который сейчас выполняеся.
       Чтоб на отдельный тест создавался отдельный лог."""
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(filename=f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    """Запуск тестов в selenoid"""
    if executor != "localhost":

        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "enableLog": True
            },
            "name": "Veles"
        }
        executor_url = f"http://{executor}:4444/wd/hub"
        driver = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url
        )

    else:
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Загрузки/driver/chromedriver"))
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=os.path.expanduser("~/Загрузки/driver/geckodriver"))

    # Attach browser data
    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    driver.logger = logger
    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def finalizer():
        logger.info("===> Test {} passed at {}".format(request.node.name, datetime.datetime.now()))
        driver.quit()

    driver.get(url)
    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG
    driver.maximize_window()

    request.addfinalizer(finalizer)

    return driver
