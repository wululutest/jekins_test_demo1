import pytest

from data.read_ymal import build_data_func
from page.page_factory import PageFactory
from utils import get_driver


class TestSearch(object):
    # 前置条件
    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = get_driver()
        self.page_factory = PageFactory(self.driver)
        yield
        self.driver.quit()

    @pytest.mark.parametrize('text', build_data_func())
    def test_func(self, text):
        """搜索测试方法"""
        # # 点击搜索按钮跳转搜索页面
        # self.index_page = IndexPage(self.driver)
        # 实例化设置首页页面对象
        # self.index_page.click_search_btn()
        # 实例化设置首页页面对象
        # self.search_page = SearchPage(self.driver)
        # 点击搜索按钮跳转搜索页面
        # self.search_page.input_search_bar("你好")

        self.page_factory.index_page().click_search_btn()  # 点击搜索按钮跳转搜索页面
        self.page_factory.search_page().input_search_bar(text)  # 输入内容搜索结果
