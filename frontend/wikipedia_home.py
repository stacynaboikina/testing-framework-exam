from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
    def search_bar(self):
        return (WebDriverWait(self.driver, 20).until(
             expected_conditions.element_to_be_clickable((By.NAME, "search"))))

    @property
    def proposals_list(self):
        list_of_proposals = self.driver.find_element(By.CLASS_NAME, "cdx-menu__listbox")
        return list_of_proposals.find_elements(By.TAG_NAME, "li")
