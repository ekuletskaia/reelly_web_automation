from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
# from support.logger import logger

#  Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = './chromedriver.exe'
    # context.driver = webdriver.Chrome(executable_path=driver_path)
    # #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/18-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--window-size=1920,1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'lenakuletsky_SKaVUT'
    bs_key = 'W9FLyyLLHFBYCqawWphz'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'osVersion': 'monterey',
        'os': 'OS X',
        # 'deviceName': 'Samsung Galaxy Note 20 Ultra',
        'browserName': 'chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # logger.info(f'Started scenario: , {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started scenario: , {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger.warning(f'Step failed: , {step}')
        context.app.base_page.save_screenshot(step)
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
