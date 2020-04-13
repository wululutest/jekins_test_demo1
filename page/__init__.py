"""元素独立文件(对元素定位信息进行统一管理)"""
from selenium.webdriver.common.by import By

# 设置首页
search_btn = (By.ID, 'com.android.settings:id/search')  # 搜索按钮
# 设置搜索页
search_bar = (By.ID, 'android:id/search_src_text')  # 输入框
