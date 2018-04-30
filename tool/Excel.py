from xlrd import open_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#uncomment if your os is windows  
#import win32com
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Excel:
    test_case_str = "TestNo."
    list_test_case = []

    def __init__(self):
        pass

    def get_start_point(self, sheet):
        # start point symbol
        for row in range(1, sheet.nrows):
            for col in range(1, sheet.ncols):
                cell = sheet.cell(row, col).value
                if cell == self.test_case_str:
                    return [col, row]
        return [0, 0]

    def read_from_workbook(self, workbook):
        self.list_test_case = []

        for sheet in workbook.sheets():
            start_point = self.get_start_point(sheet)
        for idx_row in range(1, sheet.nrows):
            if idx_row <= start_point[0]:
                continue
            test_case = []
            for idx_col in range(1, sheet.ncols):
                if idx_col < start_point[1] - 1:
                    continue
                test_case.append(sheet.cell(idx_row, idx_col).value)

            self.list_test_case.append(test_case)
            # get test case list
        return self.list_test_case

