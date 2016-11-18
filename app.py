__author__ = 'KEII2K'

import glob
import time
from tool.Excel import Excel
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from xlrd import open_workbook
from tool.Common import Common
from selenium import webdriver

common = Common()


def page_has_loaded():
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'


# find element by ID or NAME
def find_element_by_id(id):
    if id.startswith("%"):
        while not page_has_loaded():
            pass

        id = id[1:]
        try:
            return driver.find_elements_by_xpath("//*[contains(@id, '" + id + "')]")[0]
        except:
            try:
                return driver.find_elements_by_xpath("//*[@contains(@name, '" + id + "')]")[0]
            except:
                driver.quit()
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
                driver.quit()
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("                               not find id : " + id)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                return 0


def run_test_case(test_case):
    TC_name = test_case[0]
    SS_idx = 0

    # first case is tc_name second excute flg ohters case commend
    for case in test_case:

        # check excute flg
        if "@" == test_case[1]:
            break

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
            print("id:" + element.get_attribute("id"))
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

            exportDir = "./screenShot/" + TC_name + "/"
            common.mkdirifexist(exportDir)
            driver.get_screenshot_as_file(exportDir + '{0:03d}'.format(SS_idx) + ".png")


# read testcase file
xsfilelist = glob.glob("./testCase/*.xlsx")

for filePath in xsfilelist:

    wb = open_workbook(filePath)

    # read testcases
    excel = Excel()
    list_test_case = excel.read_from_workbook(wb)

    # load selenium
    driver = webdriver.Chrome()

    # run testcase

    for test_case in list_test_case:
        run_test_case(test_case)

    driver.close()

# make test Case
print("Test End")

# TODO EVIDENSE MERGE
# TODO DB CONTROL
