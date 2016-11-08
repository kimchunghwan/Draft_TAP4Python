from symbol import testlist

__author__ = 'KISSCO'

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title


elem = driver.find_element_by_name("q")
time.sleep(3)

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(3)

assert "No results found." not in driver.page_source
driver.close()

testList = "banana"
testList.__add__("apple")

print(testList)