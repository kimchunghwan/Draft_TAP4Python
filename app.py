__author__ = 'KEII2K'

import time

from tool.Reader import Reader
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from xlrd import open_workbook
from tool.Common import Common

common = Common()

def get_start_point(sheet):
    # start point symbol
    test_case_str = "TestNo."

    for row in range(1, sheet.nrows):
        for col in range(1, sheet.ncols):
            cell = sheet.cell(row, col).value
            if cell == test_case_str:
                return [col, row]
    return [0, 0]

# find element by ID or NAME
def find_element_by_id(id):
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

#
# def seperate_bisect(str):
#     tmp = str.split(",")
#     result = tmp[0:1]
#     result.append(str.replace((tmp[0] + ","), ""))
#     return result
#
# def seperate_3quarter(str):
#     tmp = str.split(",")
#     result = tmp[0:2]
#     result.append(str.replace((tmp[0] + "," + tmp[1] + ","), ""))
#     return result
#
#
# def seperate_quarter(str):
#     tmp = str.split(",")
#     result = tmp[0:3]
#     result.append(str.replace((tmp[0] + "," + tmp[1] + "," + tmp[2] + ","), ""))
#     return result

def run_test_case(test_case):
    # start point caster
    for case in test_case:
        # DB control
        # consol control
        # selenium control
        # TODO wait for loading

        if case.startswith("open"):
            driver.get(case.replace("open,", ""))
        elif case.startswith("delay"):
            result = common.seperate_bisect(case)
            time.sleep(int(result[1]))
        elif case.startswith("click"):
            element = find_element_by_id(case.replace("click,", ""))
            if element == 0:
                break
            element.click()
        elif case.startswith("input"):
            # seperate 3parts
            result = common.seperate_3quarter(case)
            element = find_element_by_id(result[1])
            element.send_keys(result[2])
        elif case.startswith("SS"):
            driver.get_screenshot_as_file("screenShot/evidence01.png")


wb = open_workbook("excel/TC_TEMPLETE_00.xlsx")

rd = Reader()
list_test_case = rd.read_from_workbook(wb)

# list_test_case = []
# # get script start point
# for sheet in wb.sheets():
#
#     start_point = get_start_point(sheet)
#     for idx_row in range(1, sheet.nrows):
#         if idx_row <= start_point[0]:
#             continue
#         test_case = []
#         for idx_col in range(1, sheet.ncols):
#             if idx_col < start_point[1] - 1:
#                 continue
#             test_case.append(sheet.cell(idx_row, idx_col).value)
#
#         list_test_case.append(test_case)
#         # get test case list

# import selenium
from selenium import webdriver

driver = webdriver.Chrome()

# run test case
for test_case in list_test_case:
    run_test_case(test_case)
# first casename second excuteflg ohters case commend
driver.close()

# make test Case
print("Test End")

# TODO read commend list  by Excel
# TODO run selenium
# TODO get evidence
