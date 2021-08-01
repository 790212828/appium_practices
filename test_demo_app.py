"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""


from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.0'
desired_caps['deviceName']='34d694360804'
# desired_caps['appPackage']='com.android.settings'#com.xueqiu.android
# desired_caps['appActivity']='com.android.settings.MainSettings'#com.xueqiu.android.view.WelcomeActivityAlias
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='com.xueqiu.android.view.WelcomeActivityAlias'

desired_caps['automationName']="uiautomator2"
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()



