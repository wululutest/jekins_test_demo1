# 导包
import time
from appium import webdriver


def get_driver():
    # 实例化驱动对象
    capabilities = {
        # 设备类型
        "platformName": "Android",
        # 系统版本
        "platformVersion": "5.1.1",
        # 设备名称
        "deviceName": "模拟器",
        # 待测应用包名  com.android.settings/.Settings
        "appPackage": "com.android.settings",
        # 待测应用启动名
        "appActivity": ".Settings",
        # 解决中文无法输入问题
        "resetKeyboard": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver  # 为提供给外界调用, 需要添加返回值
