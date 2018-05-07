from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from tool.Common import Common
import time

class CaseRunner:

    common = None
    driver = None

    def __init__(self, driver):
        self.common = Common()
        self.driver = driver
        pass

    # excute script one or multi 
    def excuteJS(self, javascript):
        if isinstance(javascript, list):
            for script in javascript:
                self.driver.execute_script(script)
                time.sleep(1)
        else :  
            self.driver.execute_script(javascript)        

    def wait_for_load(self):
        flg = 1
        while flg:
            page_state = self.driver.execute_script('return document.readyState;')
            if page_state == 'complete':
                flg = 0
            time.sleep(1)

    # find element by ID or NAME
    def find_element_by_id(self, id):
        if id.startswith("%"):
            # wait load
            self.wait_for_load()

            id = id[1:]
            try:
                return self.driver.find_elements_by_xpath("//*[contains(@id, '" + id + "')]")[0]
            except:
                try:
                    return self.driver.find_elements_by_xpath("//*[@contains(@name, '" + id + "')]")[0]
                except:
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    print("                               not find contain id : " + id)
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    return 0
        else:
            try:
                element = WebDriverWait(self.driver, 3).until(
                    expected_conditions.presence_of_element_located((By.ID, id))
                )
                return element

            except:
                try:
                    element = WebDriverWait(self.driver, 3).until(
                        expected_conditions.presence_of_element_located((By.NAME, id))
                    )
                    return element

                except:
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    print("                               not find id : " + id)
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Exception@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    return 0

    def run_test_case(self, test_case, fileName, customCMD):
        TC_name = test_case[0]
        SS_idx = 0

        # check excute flg
        if "@" != test_case[1]:
            return

        print("excute TestCase :" + str(test_case))
        # first case is tc_name second excute flg ohters case commend
        for case in test_case[2:]:

            # DB control
            # consol control
            # selenium control
            # TODO wait for loading

            if case in customCMD:
                self.excuteJS(customCMD[case])
#                self.driver.execute_script(customCMD[case])

            if case.startswith("open,"):
                self.driver.get(case.replace("open,", ""))

            elif case.startswith("delay,"):
                result = self.common.seperate(case, 2)
                time.sleep(int(result[1]))

            elif case.startswith("click,"):
                result = self.common.seperate(case, 2)
                element = self.find_element_by_id(result[1])

                if element == 0:
                    break

                element.click()

            elif case.startswith("input,"):
                # seperate 3parts
                result = self.common.seperate(case, 3)
                print(result)
                element = self.find_element_by_id(result[1])
                element.send_keys(result[2])

            elif case.startswith("SS"):
                # set highlight
                for elem in case.split(",")[1:]:
                    element = self.find_element_by_id(elem)
                    str_style = element.get_attribute("style") + " outline: #FF0000 dotted thick;"
                    self.driver.execute_script("arguments[0].setAttribute('style', '" + str_style + "');", element)
                SS_idx += 1

                exportDir = "./screenShot/" + fileName + "/" + TC_name + "/"
                self.common.mkdirifexist(exportDir)
                self.driver.get_screenshot_as_file(exportDir + '{0:03d}'.format(SS_idx) + ".png")