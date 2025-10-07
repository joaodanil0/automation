import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("automationName", "UIAutomator2")
options.set_capability("deviceName", "RQCX40600ZP")
options.set_capability("appPackage", "com.android.settings")
options.set_capability("appActivity", ".Settings")
options.set_capability("language", "en")
options.set_capability("locale", "US")
options.set_capability("platformVersion", "16")  # Versão do Android
options.set_capability("noReset", True)

appium_server_url = f"http://{pytest.APPIUM_SERVER_IP}:{pytest.APPIUM_SERVER_PORT}/wd/hub"

class ExampleAppium():

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        self.driver.execute_script("mobile: shell", {
            "command": "am start -a android.settings.SETTINGS"
        })
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Connections"]')
        el.click()

        