from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from frontend.base_page import BasePage

from selenium.webdriver.common.by import By


class WikipediaAccountPage(BasePage):

    @property
    def welcome_message(self):
        return self.driver.find_element(By.ID, 'wpName2')

    @property
    def username_field(self):
        return self.driver.find_element(By.ID, 'wpName2')

    @property
    def password_field(self):
        return self.driver.find_element(By.ID, 'wpPassword2')

    @property
    def confirm_password_field(self):
        return self.driver.find_element(By.ID, 'wpRetype')

    @property
    def email_field(self):
        return self.driver.find_element(By.ID, 'wpEmail')

    @property
    def captcha_field(self):
        return self.driver.find_element(By.ID, 'mw-input-captchaWord')

    @property
    def create_account_button(self):
        return WebDriverWait(self.driver, 10, 1, ignored_exceptions=StaleElementReferenceException).until(
            expected_conditions.element_to_be_clickable((By.ID, 'wpCreateaccount')))

    @property
    def invalid_captcha(self):
        return self.driver.find_element(By.CLASS_NAME, 'cdx-message__content')