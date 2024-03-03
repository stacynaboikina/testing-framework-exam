import time

import allure
from selenium.webdriver import Keys


@allure.title("Verify that hide button is hiding side menu")
def test_wikipedia_article_page_hide_button(pages):
    with allure.step("insert text in search box"):
        pages.wiki_home.search_bar.send_keys("Rihanna")
    with allure.step("click enter"):
        time.sleep(1)
        pages.wiki_home.search_bar.send_keys(Keys.ENTER)
    with allure.step("Verify header"):
        assert pages.wiki_article.main_header.text == "Rihanna"
    with allure.step("Verify side menu is available"):
        length = len(pages.wiki_article.side_menu)
        assert length == 35
    with allure.step("Hide side menu"):
        pages.wiki_article.hide_button.click()
    with allure.step("Verify side menu is not displayed"):
        assert not pages.wiki_article.hide_button.is_displayed()


@allure.title("Verify Contents for Cat article")
def test_wikipedia_article_page_see_also(pages):
    with allure.step("insert text in search box"):
        pages.wiki_home.search_bar.send_keys("Cat")
    with allure.step("click enter"):
        time.sleep(1)
        pages.wiki_home.search_bar.send_keys(Keys.ENTER)
    with allure.step("Verify header"):
        assert pages.wiki_article.main_header.text == "Cat"
    with allure.step("Verify side menu is available"):
        if not pages.wiki_article.hide_button.is_displayed():
            pages.wiki_article.unhide_button.click()
    with allure.step("Verify See also is in the list"):
        list_of_contents = pages.wiki_article.side_menu
        found_element = 0
        for element in list_of_contents:
            if element.text == "See also":
                found_element += 1
        assert found_element
    with allure.step("Verify References is in the list"):
        list_of_contents = pages.wiki_article.side_menu
        found_element = 0
        for element in list_of_contents:
            if element.text == "References":
                found_element += 1
        assert found_element


@allure.title("Verify Contents for Dog article")
def test_wikipedia_article_page_references(pages):
    with allure.step("insert text in search box"):
        if pages.wiki_home.search_bar.is_displayed():
            pages.wiki_home.search_bar.send_keys("Dog")
    with allure.step("Press enter"):
        time.sleep(1)
        pages.wiki_home.search_bar.send_keys(Keys.ENTER)
    with allure.step("Verify header"):
        assert pages.wiki_article.main_header.text == "Dog"
    with allure.step("Verify side menu is available"):
        if not pages.wiki_article.hide_button.is_displayed():
            pages.wiki_article.unhide_button.click()
    with allure.step("Verify See also is in the list"):
        list_of_contents = pages.wiki_article.side_menu
        found_element = 0
        for element in list_of_contents:
            if element.text == "See also":
                found_element += 1
        assert found_element
    with allure.step("Verify References is in the list"):
        list_of_contents = pages.wiki_article.side_menu
        found_element = 0
        for element in list_of_contents:
            if element.text == "References":
                found_element += 1
        assert found_element
