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

    if id.startswith("%"):
        pass
    else :
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

def wait_page_on_load():
    WebDriverWait(driver, 30).until(
        driver.execute_script()
    )


def run_test_case(test_case):
    print("TC_NAME : " + test_case[0])
    # start point caster
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
            driver.get_screenshot_as_file("screenShot/evidence01.png")


wb = open_workbook("excel/TC_TEMPLETE_00.xlsx")

rd = Reader()
list_test_case = rd.read_from_workbook(wb)

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

# TODO get evidence
