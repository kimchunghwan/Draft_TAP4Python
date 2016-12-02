import os
import logging
import glob
import time
from tool.Excel import Excel
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from xlrd import open_workbook
from tool.Common import Common
from selenium import webdriver

__author__ = 'KEII2K'

common = Common()


def wait_for_load():
    flg = 1
    while flg:
        page_state = driver.execute_script('return document.readyState;')
        if page_state == 'complete':
            flg = 0
        time.sleep(1)


# find element by ID or NAME
def find_element_by_id(id):
    if id.startswith("%"):
        # wait load
        wait_for_load()

        id = id[1:]
        try:
            return driver.find_elements_by_xpath("//*[contains(@id, '" + id + "')]")[0]
        except:
            try:
                return driver.find_elements_by_xpath("//*[@contains(@name, '" + id + "')]")[0]
            except:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("                               not find contain id : " + id)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                return 0
    else:
        try:
            element = WebDriverWait(driver, 3).until(
                expected_conditions.presence_of_element_located((By.ID, id))
            )
            return element

        except:
            try:
                element = WebDriverWait(driver, 3).until(
                    expected_conditions.presence_of_element_located((By.NAME, id))
                )
                return element

            except:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("                               not find id : " + id)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                return 0


def run_test_case(test_case, fileName):
    TC_name = test_case[0]
    SS_idx = 0

    # check excute flg
    if "@" != test_case[1]:
        return

    print("excute TestCase :" + str(test_case))
    # first case is tc_name second excute flg ohters case commend
    for case in test_case:

        # DB control
        # consol control
        # selenium control
        # TODO wait for loading

        if case.startswith("open"):
            driver.get(case.replace("open,", ""))
        elif case.startswith("delay"):
            result = common.seperate(case, 2)
            time.sleep(int(result[1]))
        elif case.startswith("click"):
            result = common.seperate(case, 2)
            element = find_element_by_id(result[1])

            if element == 0:
                break

            element.click()
        elif case.startswith("input"):
            # seperate 3parts
            result = common.seperate(case, 3)
            print(result)
            element = find_element_by_id(result[1])
            element.send_keys(result[2])
        elif case.startswith("SS"):
            # set highlight
            for elem in case.split(",")[1:]:
                element = find_element_by_id(elem)
                str_style = element.get_attribute("style") + " outline: #FF0000 dotted thick;"
                driver.execute_script("arguments[0].setAttribute('style', '" + str_style + "');", element)
            SS_idx += 1

            exportDir = "./screenShot/" + fileName + "/" + TC_name + "/"
            common.mkdirifexist(exportDir)
            driver.get_screenshot_as_file(exportDir + '{0:03d}'.format(SS_idx) + ".png")


# read testcase file
xsfilelist = glob.glob("./testCase/*.xlsx")

list_test_case = []

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

    # load selenium
    driver = webdriver.Chrome()
    driver.maximize_window()

    # run testcase
    for test_case in excel.read_from_workbook(wb):
        run_test_case(test_case, fileName)

    driver.close()
    time.sleep(3)

# make test Case
print("Test End")
# TODO EVIDENSE MERGE -> makeEvidence.py
# TODO DB CONTROL
