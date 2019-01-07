# Author : Rajeev R Nair
# Email  : rajeevnair601@gmail.com

# FA6AX0300594 Android P
# ZX1G523DK5  Nexus 6

reportDirectory = '/Users/rajeevnair/Desktop/Rajeev/AppiumStudio/RefApp_Mobile_Automation/Reports'
reportFormat = 'xml'

# Supported OS is "IOS" and "Android"
os = "Android"
dc = {}
app_name = "\"com.philips.platform.referenceapp\""

# Supported modes are "single", "dual", & "multiOS"
mode = "single"

IOS_Config = {

                'reportDirectory': reportDirectory,
                'reportFormat': reportFormat,
                "testName": "IOS Reference App Test Automation Using Android Studio",
                'udid': '710f90f58ed93d584540e911c97bf79353e88f02',
                'bundleId': 'com.philips.platform.referenceapp.beta',
                'platformName': 'ios'

             }


Android_Config = {
                   'reportDirectory': reportDirectory,
                   'reportFormat': reportFormat,
                   "testName": "Android Reference App Test Automation Using Android Studio",
                   'udid': 'ZX1G523DK5',
                   'appPackage': 'com.philips.platform.referenceapp',
                   'appActivity': 'com.philips.platform.baseapp.screens.introscreen.LaunchActivity',
                   'platformName': 'android'

                }


