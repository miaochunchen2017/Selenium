# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()  # Get local session of firefox
browser.get("http://192.168.137.141:8088/DSVS_JSP/")  # Load page
assert "百度一下，你就知道" in browser.title
elem = browser.find_element_by_name("kw")  # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2)  # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()
