"""
PO文件基类
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    # 封装代码过程中, 如果需要驱动对象, 直接编写此方法
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=10, poll=.5):
        """
            元素定位方法
            :param location: 元素定位信息
            :param timeout: 超时时长
            :param poll: 定位方法执行间隔
            :return: 元素对象
            """
        # 1. 添加显式等待
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda driver: driver.find_element(location[0], location[1]))
        # 2. 返回定位到的元素对象
        return element

    def input_func(self, element, text):
        """
        元素输入
        :param element: 元素对象
        :param text: 输入的内容
        :return:无
        """
        element.clear()  # 元素清空
        element.send_keys(text)  # 元素输入

    def click_func(self, element):
        """
        元素点击
        :param element: 元素对象
        :return: 无
        """
        element.click()  # 元素点击
