# Author : Rajeev R Nair
# Email  : rajeevnair601@gmail.com

from testutilities import config


class Utilities:

    def __init__(self, context):
        self.driver = context.driver

    def kill_app(self):
        script = "seetest:client.applicationClose(" + config.app_name + ")"
        self.driver.execute_script(script)

    def launch_app(self):
        self.driver.launch_app()

    def get_ios_devicelog(self):
        self.driver.execute_script("seetest:client.getDeviceLog()")

    # To monitor the app performance and CPU consumption
    def start_monitor(self):
        script = "seetest:client.startMonitor(" + config.app_name + ")"
        self.driver.execute_script(script)

    def stop_monitor(self):
        script = "seetest:client.getMonitorsData('monitors.csv')"
        self.driver.execute_script(script)
