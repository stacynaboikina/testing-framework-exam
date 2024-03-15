import allure

@allure.title("Test if create account button sends user to create account page")
def test_account_creation_page(pages):
    with allure.step("Click create account button"):
        pages.wiki_home.create_account_link.click()
    with allure.step("Asserting result: Create account page has loaded"):
        assert pages.wiki_home.header.text == "Create account"

@allure.title("Test if user can ceate account without properly filled captacha")
def test_account_creation_process_without_proper_captcha(pages):
    with allure.step("Go to create account page"):
        pages.wiki_home.create_account_link.click()
    with allure.step("Input username"):
        pages.wiki_account.username_field.send_keys("Testertestowicz")
    with allure.step("Input password"):
        pages.wiki_account.password_field.send_keys("Fakepassword1234")
    with allure.step("Confirm password"):
        pages.wiki_account.confirm_password_field.send_keys("Fakepassword1234")
    with allure.step("Input email"):
        pages.wiki_account.email_field.send_keys("totallyfakeemailaddress@fakegmail.com")
    with allure.step("Input captcha"):
        pages.wiki_account.captcha_field.send_keys("Wrongcaptcha")
    with allure.step("Click create account button"):
        pages.wiki_account.create_account_button.click()
    with allure.step("Asserting result: Account creation should fail"):
        if pages.wiki_account.invalid_captcha.text == "Incorrect or missing CAPTCHA.":
            assert pages.wiki_account.invalid_captcha.text == "Incorrect or missing CAPTCHA."
        else:
            assert pages.wiki_account.invalid_captcha.text == "Visitors to Wikipedia using your IP address have created 6 accounts in the last 24 hours, which is the maximum allowed in this time period. As a result, visitors using this IP address cannot create any more accounts at the moment. If you would like to request an account be created for you, follow the instructions at Wikipedia:Request an account."