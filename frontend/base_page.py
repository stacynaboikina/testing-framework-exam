from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base Page class, ancestor of all page objects. Provides common methods, attributes and properties
    for all page objects.
    """
    def __init__(self, driver: Chrome):
        self.driver = driver

    def find_by_data_event_name(self, tag_name, element_name):
        found_element = self.driver.find_element(By.CSS_SELECTOR, f'{tag_name}[data-event-name="{element_name}"]')
        return found_element
