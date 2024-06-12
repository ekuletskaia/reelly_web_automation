from selenium.webdriver.common.by import By
from pages.base_page import Page


class OffPlan(Page):

    PRODUCTS_ON_THE_PAGE = (By.XPATH, '//a[@wized="cardOfProperty"]')
    FILTERS_BTN = (By.CSS_SELECTOR, ".search_block1 [w-el-onclick-0-0]")
    PRICE_FROM = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    PRICE_TO = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, ".filters-block-1.hidden > .button-filter.w-button")
    PRODUCT_PRICES = (By.XPATH, '//div[@wized="projectMinimumPrice"]')

    # Emulator
    TITLE_OFF_PLAN_PAGE = (By.CSS_SELECTOR, ".off_plan.page-title")
    FILTERS_BUTTON = (By.CSS_SELECTOR, ".mobile [w-el-onclick-0-0]")

    def verify_off_plan_page_open(self):
        self.find_element(*self.FILTERS_BTN)

    def select_filter_by_price_range(self, price_from, price_to):
        self.verify_visible_all_elements(*self.PRODUCTS_ON_THE_PAGE)
        self.click(*self.FILTERS_BTN)
        self.input_text(price_from, *self.PRICE_FROM)
        self.input_text(price_to, *self.PRICE_TO)
        self.wait_until_clickable_click(*self.APPLY_FILTER_BTN)

    def verify_products_in_price_range(self, price_from, price_to):
        self.verify_visible_all_elements(*self.PRODUCT_PRICES)
        all_prices = self.find_elements(*self.PRODUCT_PRICES)
        for price in all_prices:
            price_text = price.text
            print(price_text)
            price_value = int(price_text.replace('AED', '').replace(',', '').strip())
            assert int(price_from) <= price_value <= int(price_to), \
                f'Price {price_value} not in range {price_from} to {price_to} AED'

    def verify_title_in_the_page(self, expected_text):
        self.verify_text(expected_text, *self.TITLE_OFF_PLAN_PAGE)

    def set_filter_by_price_range(self, price_from, price_to):
        self.verify_visible_all_elements(*self.PRODUCTS_ON_THE_PAGE)
        self.click(*self.FILTERS_BUTTON)
        self.input_text(price_from, *self.PRICE_FROM)
        self.input_text(price_to, *self.PRICE_TO)
        self.wait_until_clickable_click(*self.APPLY_FILTER_BTN)
