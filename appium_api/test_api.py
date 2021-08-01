from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestApi:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['udid']='emulator-5554'#多设备时候可以根据udid作为唯一标识找到设备
        desired_caps['autoGrantPermissions']=True#将app获取权限功能勾选为同意，前提不能开启noReset
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity']="com.xueqiu.android.view.WelcomeActivityAlias"
        # desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false
        desired_caps['fullReset']=True#Android 停止之前app操作，清空app之前的数据缓存信息等，iOS是卸载aoo和之前的数据缓存
        # desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        desired_caps['skipDeviceInitialization'] = True
        #需要用到中文输入sendkeys("中文")，设置两个参数
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        # desired_caps['automationName'] = 'uiautomator2'
        desired_caps['settings[waitForIdleTimeout]'] = 0
        desired_caps['avd']='60012'
        # desired_caps['chromedriverExecutable'] = r'E:\Softwork\Driver\appDriver\\'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_api(self):
        self.driver.make_gsm_call('13160658208',GsmCallActions.CALL)
        self.driver.send_sms('13160658208','hello appium api')
        sleep(5)
        self.driver.set_network_connection(1)
        sleep(5)
        self.driver.set_network_connection(4)
        sleep(5)

        # self.driver.get_screenshot_as_file('../photos/img.png')
        # self.driver.start_recording_screen()
        # sleep(10)
        # self.driver.stop_recording_screen()
