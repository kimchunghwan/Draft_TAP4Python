import os
import logging
import glob
import time
import yaml
from tool.Excel import Excel
from xlrd import open_workbook
from tool.Common import Common
from selenium import webdriver
from tool.CaseRunner import CaseRunner
from sys import platform

__author__ = 'KEII2K'

# check os for webdriver path 
chromedriverPath = ""
if platform == "linux" or platform == "linux2":
    # linux
    pass
elif platform == "darwin":
    # OS X
    chromedriverPath="./chromedriver"
elif platform == "win32":
    # Windows...
    chromedriverPath =""

#load customCMD
stream = open('customCMD.yaml', 'r')  
customCMD = yaml.load(stream)
print(customCMD)



common = Common()
# read testcase file
xsfilelist = glob.glob("./testCase/*.xlsx")

list_test_case = []

# load selenium
driver = webdriver.Chrome(chromedriverPath)
driver.maximize_window()
caseRunner = CaseRunner(driver)

for filePath in xsfilelist:
    # get file name
    fileName = os.path.basename(filePath)

    # tempfile  skip
    if fileName.startswith("~$"):
        continue

    print("read TC_file : " + filePath)

    wb = open_workbook(filePath)

    # read testcases
    excel = Excel()
    list_test_case = excel.read_from_workbook(wb)

    # run testcase
    for test_case in excel.read_from_workbook(wb):
        caseRunner.run_test_case(test_case, fileName, customCMD)

    time.sleep(1)

# make test Case
driver.close()
print("Test End")
# TODO EVIDENSE MERGE -> makeEvidence.py
# TODO DB CONTROL
