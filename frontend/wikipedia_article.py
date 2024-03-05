from frontend.base_page import BasePage
from selenium.webdriver.common.by import By


class WikipediaArticlePage(BasePage):

    @property
    def main_header(self):
        return self.driver.find_element(By.ID, "firstHeading")

    @property
    def hide_button(self):
        return BasePage.find_by_data_event_name(self, 'button', 'pinnable-header.vector-toc.unpin')

    @property
    def side_menu(self):
        list_of_objects = self.driver.find_element(By.ID, "mw-panel-toc-list")
        return list_of_objects.find_elements(By.TAG_NAME, "li")

    @property
    def unhide_button(self):
        return self.driver.find_element(By.ID, "vector-page-titlebar-toc")

    @property
    def toast_menu_button(self):
        return self.driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox")

    @property
    def main_page_button(self):
        return self.driver.find_element(By.ID, "n-mainpage-description")
