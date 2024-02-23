import allure


@allure.title("Test wikipedia home page welcome section has expected elements")
def test_wikipedia_home_page(pages):
    with allure.step("Verify wikipedia welcome message text is 'Welcome to Wikipedia'"):
        assert pages.wiki_home.welcome_message.text == "Welcome to Wikipedia"

    with allure.step("Verify there is a link to 'anyone can edit' section and you can click it"):
        assert pages.wiki_home.anyone_can_edit.text == "anyone can edit"
        pages.wiki_home.anyone_can_edit.click()
