import xlrd
import os
import glob
from shutil import copyfile
from tool.Common import Common

common = Common()

# evidence merge tool
screenShotPath = "./screenShot/"
evidencePath = "./evidence/"
dirList = glob.glob(screenShotPath + "*.xlsx")

templetePath = "./templete/EVI_templete.xlsx"

for dir in dirList:
    # set evidence file list
    targetPath = evidencePath + os.path.basename(dir).replace(".xlsx", "_EVI.xlsx")
    common.mkdirifexist(evidencePath)
    copyfile(templetePath, targetPath)

    # get casename list
    caseList = glob.glob(dir + "/*")

    wb = xlrd.open_workbook(targetPath)
    sheets = wb.sheet_by_index(0)
    sheets.append()
    for casename in caseList:
        print(str(casename))
        imgList = glob.glob(casename + "/*")




        # wb = xlrd.open_workbook(targetPath)


# TODO 디렉토리 구조는 파일명 > 시트명  순으로 작성
#
