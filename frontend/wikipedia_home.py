from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException

from frontend.base_page import BasePage

from selenium.webdriver.common.by import By


class WikipediaHomePage(BasePage):

    @property
    def welcome_message(self):
        return self.driver.find_element(By.ID, "Welcome_to_Wikipedia")

    @property
    def welcome_message_details(self):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.ID, "mp-free")))

    @property
    def anyone_can_edit(self):
        all_a_tags = self.welcome_message_details.find_elements(By.TAG_NAME, "a")
        for tag in all_a_tags:
            if tag.get_attribute("title") == "Help:Introduction to Wikipedia":
                return tag

    @property
    def input_search_field(self):
        return WebDriverWait(self.driver, 10, 1, ignored_exceptions=ElementNotInteractableException).until(
            expected_conditions.presence_of_element_located((By.NAME, 'search')))

    @property
    def search_button(self):
        return WebDriverWait(self.driver, 10, 1, ignored_exceptions=StaleElementReferenceException).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[id="searchform"] button')))

    @property
    def left_rail_content_menu(self):
        return self.driver.find_element(By.ID, 'vector-toc')

    @property
    def header(self):
        return self.driver.find_element(By.ID, 'firstHeading')

    @property
    def create_account_link(self):
        return WebDriverWait(self.driver, 10, 1, ignored_exceptions=StaleElementReferenceException).until(
            expected_conditions.element_to_be_clickable((By.ID, 'pt-createaccount-2')))