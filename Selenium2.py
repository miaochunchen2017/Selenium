# -*- coding:utf-8 -*-
# 转码utf-8
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

import time
from selenium import webdriver

# 使用IE浏览器打开脚本
driver = webdriver.Ie()
# 测试URL
driver.get("http://192.168.137.141:8088/DSVS_JSP/")
# 打印页面title
print driver.title
# 休眠0.5s
time.sleep(0.5)
# 获取密码输入框控件
elem_signData = driver.find_element_by_xpath('//*[@id="UserPwd"]')
# elem1 = driver.find_element_by_name("pwd1")
# 输入密码"111111"
elem_signData.send_keys("111111")
# 点击登录
driver.find_element_by_name("B1").click()
# 进入数据签名页面
driver.find_element_by_link_text("数据签名").click()
# driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/a').click()
time.sleep(0.5)

# 进行签名验签操作
driver.find_element_by_xpath('//*[@id="TestForm"]/table/tbody/tr[2]/td[1]/input').click()
driver.find_element_by_xpath('//*[@id="TestForm"]/table/tbody/tr[3]/td[1]/input').click()
# 获取签名原文
result0 = driver.find_element_by_xpath('//*[@id="plainData"]').text
# 获取验签结果
result1 = driver.find_element_by_xpath('//*[@id="verifySign"]').text
print "数据签名结果为：" + result1

# 比较验签结果
# text1 = "验证签名成功！"
# if result1 == text1:
#     print "Success!"

driver.quit()
