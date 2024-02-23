from selenium.webdriver import Chrome


class BasePage:
    """
    Base Page class, ancestor of all page objects. Provides common methods, attributes and properties
    for all page objects.
    """
    def __init__(self, driver: Chrome):
        self.driver = driver
