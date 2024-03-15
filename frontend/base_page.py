from selenium.webdriver import Chrome
from selenium import webdriver


class BasePage:
    """
    Base Page class, ancestor of all page objects. Provides common methods, attributes and properties
    for all page objects.
    """
    def __init__(self, driver: Chrome):
        self.driver = driver
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1920x1080")
