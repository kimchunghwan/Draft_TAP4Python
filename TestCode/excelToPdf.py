from win32com import client
xlApp = client.Dispatch("Excel.Application")
books = xlApp.Workbooks.Open('F:\\06_Python\\Workspace\\TAP4python\\excel\\TC_TEMPLETE_00.xlsx')
# ExportAsFixedFormat(type, filePath) type : 0 pdf , 1 xps
books.ExportAsFixedFormat(0, 'F:\\06_Python\\Workspace\\TAP4python\\excel\\TC_TEMPLETE_0000.pdf')
books.SaveAs('F:\\06_Python\\Workspace\\TAP4python\\excel\\TC_TEMPLETE_0000.html')
# books.ExportAsFixedFormat(1, 'F:\\06_Python\\Workspace\\TAP4python\\excel\\TC_TEMPLETE_0000.xps')
books.Close()
# ws = books.Worksheets[0]
# ws.Visible = 1
# ws.ExportAsFixedFormat(0, 'F:\\06_Python\\Workspace\\TAP4python\\excel\\TC_TEMPLETE_00.pdf')
