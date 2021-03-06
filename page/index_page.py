"""
设置首页
"""
import page
from base.base_page import BasePage


class IndexPage(BasePage):
    # 注意: By.xxx 才能反向导包
    # 1. 使用 By方式将目标元素的定位信息封装成属性
    search_btn = page.search_btn

    # 2.根据目标元素的操作类型 + 元素名称得出封装方法名
    def click_search_btn(self):
        """点击搜索按钮方法"""
        # 3. 通过基类继承, 调用基类的元素定位方法, 并实现元素操作
        # self.find_element_func(self.search_btn).click()
        # 通过基类封装的点击方法(元素)
        self.click_func(self.find_element_func(self.search_btn))
