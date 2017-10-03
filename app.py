import os
import logging
import glob
import time
from tool.Excel import Excel
from xlrd import open_workbook
from tool.Common import Common
from selenium import webdriver
from tool.CaseRunner import CaseRunner

__author__ = 'KEII2K'

common = Common()
# read testcase file
xsfilelist = glob.glob("./testCase/*.xlsx")

list_test_case = []

# load selenium
driver = webdriver.Chrome()
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
        caseRunner.run_test_case(test_case, fileName)

    time.sleep(1)

# make test Case
driver.close()
print("Test End")
# TODO EVIDENSE MERGE -> makeEvidence.py
# TODO DB CONTROL
