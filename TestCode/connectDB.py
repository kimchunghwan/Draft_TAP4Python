import mysql.connector as mycon
import xlsxwriter
import xlrd


# 필요한건 , 이미지 , 이미지 타이틀 그리고 폰트 지정정도

def select(cursor, strSql):
    exportFile = 'select.xlsx'
    cursor.execute("select * from help_topic")
    rows = cursor.fetchall()
    colNames = cursor.column_names
    workbook = xlsxwriter.Workbook(exportFile)
    sheet = workbook.add_worksheet()
    sheet.name = "result"
    idxRow = 0
    idxCol = 0

    for name in colNames:
        sheet.write(idxRow, idxCol, name)
        idxCol = idxCol + 1

    for row in rows:
        idxRow = idxRow + 1
        idxCol = 0
        for col in row:
            sheet.write(idxRow, idxCol, str(col))
            idxCol = idxCol + 1
    workbook.close()
    return exportFile


def insert(cursor, excelFile):
    wb = xlrd.open_workbook(excelFile)

    columnNames = []
    rowDatas = []
    for sheet in wb.sheets():
        tableNm = sheet.name
        # get column name

        for idxCol in range(0, sheet.ncols):
            columnNames.append(sheet.cell(0, idxCol).value)

        # get column data

        for idxRow in range(1, sheet.nrows):
            row = []
            for iCol in range(0, sheet.ncols):
                tmpStr = sheet.cell(idxRow, iCol).value
                row.append(str(tmpStr))
            rowDatas.append(row)

        # make columns string
        strColumns = ""
        for col in columnNames:
            strColumns += col
            if (col != columnNames[len(columnNames) - 1]):
                strColumns += ", "

        for row in rowDatas:
            strValue = ""
            for col in row:
                strValue += "%s"
                if col != row[len(row)-1]:
                    strValue += ", "

                #direct
                # strValue += '"'+str(col)+'"'
                # if col != row[len(row)-1]:
                #     strValue += ", "

            insertQuery = "INSERT INTO "+tableNm+" (" + strColumns+") VALUES ("+strValue+")"
            cursor.execute(insertQuery,row)




# MYSQL
conn = mycon.connect(host='localhost', user='root', password='password', database='mysql')
cursor = conn.cursor()
exportFile = 'select.xlsx'
#exportFile = select(cursor, "select * from help_topic")
insert(cursor, exportFile)

# cursor.execute("select * from help_topic")
#
# rows = cursor.fetchall()
# colNames = cursor.column_names
#
# # Create an new Excel file and add a worksheet.
# workbook = xlsxwriter.Workbook('select.xlsx')
#
# sheet = workbook.add_worksheet()
# sheet.name = "result"
#
# idxRow = 0
# idxCol = 0
#
# for name in colNames:
#     sheet.write(idxRow, idxCol, name)
#     idxCol = idxCol + 1
#
# for row in rows:
#     idxRow = idxRow + 1
#     idxCol = 0
#     for col in row:
#         sheet.write(idxRow, idxCol, col)
#         idxCol = idxCol + 1
#
# workbook.close()

# 디비 관련해서 테스트 툴에 필요한 기능은 아래와 같다.
# 엑셀 -> 데이터 , 데이터 -> 엑셀로 변환하는 처리도 필요하겠지
# truncate 혹은 테이블 초기화1
# insert
# update
# select
# run sql
# db diff
# 그리고 필요한것이
