# -*- coding: utf-8 -*-
# @xufenfushi
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("自动化测试")
