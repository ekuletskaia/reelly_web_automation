from pages.base_page import Page
from pages.off_plan_page import OffPlan


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.off_plan_page = OffPlan(driver)



