import time
import allure
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver


@allure.title("Search from phrase and verify if phrase is correct")
def test_search_from_main_page(pages):
    with allure.step("Search for first phrase"):
        pages.wiki_home.search_bar.send_keys("Python")
        with allure.step("click enter"):
            pages.wiki_home.search_bar.send_keys(Keys.ENTER)
        time.sleep(5)
        with allure.step("Verify search"):
            assert pages.wiki_article.main_header.text == "Python"

    with allure.step("Search for another phrase, directly from the article view"):
        pages.wiki_home.search_bar.send_keys("Selenium")
        with allure.step("click enter"):
            pages.wiki_home.search_bar.send_keys(Keys.ENTER)
        with allure.step("Verify second search"):
            assert pages.wiki_article.main_header.text == "Selenium"
