from frontend.wikipedia_home import WikipediaHomePage
from frontend.wikipedia_article import WikipediaArticlePage


class Pages:
    """
    This class contains all page objects that will be used in the tests.

    Add all new pages to __init__ like this:
        self.page_name = PageClassName(driver)
    """

    def __init__(self, driver):
        self.wiki_home = WikipediaHomePage(driver)
        self.wiki_article = WikipediaArticlePage(driver)
