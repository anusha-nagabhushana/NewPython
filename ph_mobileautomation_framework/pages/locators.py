# Author : Rajeev R Nair
# Email  : rajeevnair601@gmail.com

from selenium.webdriver.common.by import By


class Locators(object):

    def __init__(self, os):
        self.os = os

    def locator(self):

        if self.os == "IOS":
            objrepo = {

                            # Product Tour Page Locators
                            "skip": ("id", "Skip"),
                            "left_arrow": "welcome_leftarrow",
                            "right_arrow": "//*[@text='']",
                            "done": "Done",
                            "hidden_button": ("xpath", "(//*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAView' and ./parent::*[@class='UIAWindow']]]]]/*[@class='UIAButton'])[1]"),
                            "video": "VideoThumbnail",

                            # Change Environment
                            "set_staging": "Staging",
                            "set_development": "Development",
                            "set_test": "Test",
                            "confirm_toast": "Change configuration",
                            "confirm_ok": "OK",

                            # User Registration Getting Started
                            "usr_header_title": "Getting Started",
                            "usr_screen_title": "usr_startscreen_title_label",
                            "usr_back_button": "Back",
                            "usr_create_philips_account_btn": "usr_startscreen_createAccount_Button",
                            "usr_login_btn": "usr_startscreen_Login_Button",
                            "usr_fb_btn": "usr_startscreen_facebook_button",
                            "usr_gp_btn": "usr_startscreen_googleplus_button",
                            "usr_skip_btn": "usr_startscreen_skipregistration_button",
                            "usr_privacy_notice": "usr_startscreen_privacypolicy_hyperLinkLabel",
                            "usr_country_selection": "usr_startscreen_country_hyperLinkLabel"

                      }

        elif self.os == "Android":

            objrepo = {
                            # Product Tour Page Locators
                            "skip": ("id", "welcome_skip_button"),
                            "left_arrow": ("id", "welcome_leftarrow"),
                            "right_arrow": ("id", "welcome_rightarrow"),
                            "done": ("id", "welcome_start_registration_button"),
                            "video": ("id", "onboarding_video"),
                            "hidden_button": ("id", "environment_selection"),

                            # Change Environment
                            "chg_env_title": ("id", "test"),
                            "chg_env_dropdown": ("id", "spinner"),
                            "staging": ("name", "STAGING"),
                            "development": ("name", "DEVELOPMENT"),
                            "testing": ("name", "TEST"),
                            "config": "configuration",
                            "confirm_toast": "//*[@resource-id='com.philips.platform.referenceapp:id/alertTitle']",
                            "confirm_ok": ("id", "button1"),

                            # User Registration Getting Started
                            "usr_header_title": "uid_toolbar_title",
                            "usr_screen_title": "",
                            "usr_create_philips_account_btn": "usr_startScreen_createAccount_Button",
                            "usr_login_btn": "usr_startScreen_Login_Button",
                            "usr_fb_btn": "uid_social_media_facebook_icon",
                            "usr_gp_btn": "uid_social_media_googleplus_icon",
                            "usr_skip_btn": "usr_StartScreen_Skip_Button",
                            "usr_privacy_notice": "usr_StartScreen_privacyNotice_label",
                            "usr_country_selection": "usr_StartScreen_country_label"



                      }


        return objrepo




