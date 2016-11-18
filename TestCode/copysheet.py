from copy import deepcopy
from xlrd import open_workbook
from xlutils.copy import copy as copy
from xlwt import Workbook
rb = open_workbook('EVI_templete.xlsx')
wb = copy(rb)
new_book = Workbook()

sheets = []
for distinct_employee in ["asdf","sdfasfd","sd1fasfd","s123dfasfd","s1231dfasfd","1123125sdfasfd","sdfa1231sfd","s125412512dfasfd"]:
    w_sheet = deepcopy(wb.get_sheet(0))
    w_sheet.write(6,6,distinct_employee)

    # give the sheet a new name (distinct_employee.id_number)
    w_sheet.set_name(distinct_employee)

    # add w_sheet  to the sheet list
    sheets.append(w_sheet)

    # set the sheets of the workbook

wb._Workbook__worksheets = sheets
wb.save("result.xlsx")



