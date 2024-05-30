from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open the main page')
def open_login_page(context):
    context.app.main_page.open_login_page()


@when('Login into the page with email: {email} and password: {password}')
def login_reelly(context, email, password):
    context.app.main_page.login_reelly(email, password)


@when('Click on “off plan” at the left side menu')
def click_on_off_plan_menu(context):
    context.app.main_page.click_off_plan_menu()