# Author : Rajeev R Nair
# Email  : rajeevnair601@gmail.com

from behave import *
from pages.locators import Locators
from testutilities import config
from testutilities.utilities import Utilities
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# use_step_matcher("re")

locator = Locators(config.os).locator()



@then("I skip product tour")
def skip_product_tour(context):
    context.driver.find_element(locator['skip'][0], locator['skip'][1])


@given('I set app environment as "{env}"')
def set_app_environment(context, env):
    action = TouchAction(context.driver)
    if config.os == "Android":
        action.long_press(context.driver.find_element(locator["hidden_button"][0], locator["hidden_button"][1]),
                          duration=3).perform()
        context.driver.find_element(locator["chg_env_dropdown"][0], locator["chg_env_dropdown"][1]).click()
        context.driver.find_element(locator[env][0], locator[env][1]).click()
        WebDriverWait(context.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator["confirm_toast"])))
        context.driver.find_element(locator["confirm_ok"][0], locator["confirm_ok"][1]).click()
        Utilities(context).kill_app()
        Utilities(context).launch_app()

    elif config.os == "IOS":
        action.long_press(context.driver.find_element(locator["hidden_button"][0], locator["hidden_button"][1]),
                          duration=3).perform()
        context.driver.find_element(locator[env][0], locator[env][1]).click()
        WebDriverWait(context.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, locator["confirm_toast"])))
        context.driver.find_element(locator["confirm_ok"][0], locator["confirm_ok"][1]).click()
        Utilities(context).kill_app()
        Utilities(context).launch_app()


@then("I navigate and verify the product tour")
def verify_product_tour(context):
    for x in range(8):
        context.driver.find_element(locator["right_arrow"][0], locator["right_arrow"][1]).click()
    context.driver.find_element(locator["done"][0], locator["done"][1]).click()


@then("I check current configuration")
def check_current_configuration(context):
    return context.driver.find_element(locator["config"][0], locator["config"][1]).gettext()


@then("I verfiy if mobile is in product tour screen")
def check_if_product_tour(context):
    if context.driver.find_element(locator["video"][0], locator["video"][1]):
        return True
    else:
        return False
