import xlrd
import os
import glob
from shutil import copyfile
from tool.Common import Common
import xlsxwriter
import configparser

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

    workbook = xlsxwriter.Workbook(targetPath)
    for casename in caseList:
        print(str(casename))
        imgList = glob.glob(casename + "/*")

        if imgList.__len__() == 0:
            continue

        sheet = workbook.add_worksheet()
        row_div = 25
        idx = 0
        for imgPath in imgList:
            sheet.insert_image("A" + str(1 + row_div * idx), imgPath, {'x_scale': 0.29, 'y_scale': 0.29})

            idx += 1

    workbook.close()

    # wb = xlrd.open_workbook(targetPath)


# TODO 디렉토리 구조는 파일명 > 시트명  순으로 작성

