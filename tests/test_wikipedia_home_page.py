import allure
import time


@allure.title("Test wikipedia home page welcome section has expected elements")
def test_wikipedia_home_page(pages):
    with allure.step("Verify wikipedia welcome message text is 'Welcome to Wikipedia'"):
        assert pages.wiki_home.welcome_message.text == "Welcome to Wikipedia"

    with allure.step("Verify there is a link to 'anyone can edit' section and you can click it"):
        assert pages.wiki_home.anyone_can_edit.text == "anyone can edit"
        pages.wiki_home.anyone_can_edit.click()


@allure.title("Search for an article in main page")
def test_wikipedia_search_field(pages):
    with allure.step("insert text in search box"):
        time.sleep(1)
        pages.wiki_home.search_bar.send_keys("Rihanna")
        time.sleep(1)
    with allure.step("Verify first proposal"):
        list_of_proposals = pages.wiki_home.proposals_list
        assert list_of_proposals[0].text.startswith('Rihanna')
