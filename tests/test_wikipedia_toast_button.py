import time
import allure
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
@allure.title("Return to the main page using toast menu")
def test_search_from_main_page(pages):
    with allure.step("Search for article"):
        pages.wiki_home.search_bar.send_keys("Terminator")
        with allure.step("click enter"):
            pages.wiki_home.search_bar.send_keys(Keys.ENTER)
        time.sleep(4)
        with allure.step("Verify search"):
            assert pages.wiki_article.main_header.text == "Terminator"

    with allure.step("Return to main page using toast menu"):
        pages.wiki_article.toast_menu_button.click()
        pages.wiki_article.main_page_button.click()
        assert pages.wiki_home.welcome_message.text == "Welcome to Wikipedia"