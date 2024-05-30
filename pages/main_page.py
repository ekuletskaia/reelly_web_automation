from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    USER_EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a.login-button")
    OFF_PLAN = (By.CSS_SELECTOR, "._1-link-menu .menu-button-text")

    def open_login_page(self):
        self.driver.get("https://soft.reelly.io/sign-in")

    def login_reelly(self, email, password):
        self.input_text(email, *self.USER_EMAIL)
        self.input_text(password, *self.PASSWORD)
        self.wait_until_clickable_click(*self.CONTINUE_BTN)

    def click_off_plan_menu(self):
        self.wait_for_element_appear(*self.OFF_PLAN)
        self.wait_until_clickable_click(*self.OFF_PLAN)