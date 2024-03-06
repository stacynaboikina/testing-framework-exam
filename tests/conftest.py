"""
conftest is responsible for storing the fixtures. Its main idea is to define or import fixtures
and make them available in the tests inside current folder and deeper in the folder structure.

This conftest is the first one that will be run and it will run for ALL tests.
"""

import json
import pathlib

import allure
import pytest

from frontend.pages import Pages
from selenium import webdriver


@pytest.fixture(scope='session')
def config():
    """Read env_configuration.json and make it a dictionary"""
    current_path = pathlib.Path(__file__)

    with open(current_path.parent.parent / "env_configuration.json") as c:
        config = c.read()
        configuration = json.loads(config)

    return configuration


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='session')
def pages(driver):
    return Pages(driver)


@allure.step("Open browser and navigate to home page")
@pytest.fixture(autouse=True, scope="function")
def open_browser_home_page(driver, pages, config):
    driver.get(config["app_url"])
    driver.maximize_window()



