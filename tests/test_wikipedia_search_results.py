import allure
import pytest

from selenium.common.exceptions import NoSuchElementException


@allure.title("Test wikipedia input field accepts text")
def test_wikipedia_input_field_positive(pages):
    with allure.step("Sending text to search field"):
        pages.wiki_home.input_search_field.send_keys("Człopa")
    with allure.step("Clicking search button"):
        pages.wiki_home.search_button.click()
    with allure.step("Asserting result: Header with searched word should be present on the page"):
        assert pages.wiki_home.header.text == "Człopa"


@allure.title("Test wikipedia displays no results if there's no proper search input")
def test_wikipedia_input_field_negative(pages):
    with allure.step("Sending text to search field"):
        pages.wiki_home.input_search_field.send_keys(" ")
    with allure.step("Clicking search button"):
        pages.wiki_home.search_button.click()
    with allure.step("Asserting result: Results header should not be present on the page"):
        with pytest.raises(NoSuchElementException):
            assert pages.wiki_home.left_rail_content_menu
