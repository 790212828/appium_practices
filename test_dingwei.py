

"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""
from time import sleep

from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.0'
desired_caps['deviceName']='34d694360804'
desired_caps['appPackage']='com.xueqiu.android'
# desired_caps['appActivity']="com.xueqiu.android.common.MainActivity"
desired_caps['noReset']=True#不要在会话前重置应用状态，默认：false
desired_caps['dontStopAppOnReset'] = True#不用重新打开app
desired_caps['skipDeviceInitialization']=True
desired_caps['appActivity']="com.xueqiu.android.view.WelcomeActivityAlias"

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
sleep(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()

driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")

driver.back()
driver.back()



sleep(10)
driver.quit()