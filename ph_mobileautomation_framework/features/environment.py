# Author : Rajeev R Nair
# Email  : rajeevnair601@gmail.com

from appium import webdriver
from testutilities import config
import logging
import os
import datetime


def before_all(context):
    print("Executing before all")
    if config.os == "Android":
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', config.Android_Config)
    elif config.os == "IOS":
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', config.IOS_Config)
    else:
        raise ValueError("Invalid argument passed for OS")
    print("Run Started at :" + str(datetime.datetime.now()))
    print("Appium Studio Environment Set Up")
    print("------------------------------------------------------------------")
    context.driver.implicitly_wait(3)
    print("Before scenario\n")


def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    context.logger = logging.getLogger('ph_test_automation_framework_logs')
    hdlr = logging.FileHandler('./logs/ph_test_automation_framework_logs.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)


# Scenario level objects are popped off context when scenario exits

def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    print("scenario status" + str(scenario.status))
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.driver.save_screenshot(scenario.name + "_failed.png")


def after_feature(context, feature):
    context.driver.quit()
    print("\nAfter Feature")


def after_all(context):
    print("Executing after all")
