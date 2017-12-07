# -*- coding:utf-8 -*-
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

import time
from selenium import webdriver

driver = webdriver.Ie()

driver.get("http://192.168.137.141:8088/DSVS_JSP/")

print driver.title

time.sleep(0.5)

elem_signData = driver.find_element_by_xpath('//*[@id="UserPwd"]')
# elem1 = driver.find_element_by_name("pwd1")
elem_signData.send_keys("111111")
elem2 = driver.find_element_by_name("B1")
elem2.click()

driver.find_element_by_link_text("数据签名").click()
time.sleep(0.5)

driver.find_element_by_link_text("数据签名").click()
driver.find_element_by_xpath('//*[@id="TestForm"]/table/tbody/tr[2]/td[1]/input').click()
driver.find_element_by_xpath('//*[@id="TestForm"]/table/tbody/tr[3]/td[1]/input').click()

result1 = driver.find_element_by_xpath('//*[@id="verifySign"]').text
print "数据签名结果为：" + result1
# if(result1 is "验证签名结果显示！"):
#     print "Done!"





# driver.quit()
