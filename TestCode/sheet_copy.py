##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2016, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter



#필요한건 , 이미지 , 이미지 타이틀 그리고 폰트 지정정도

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')

worksheet = workbook.add_worksheet()
worksheet = workbook.add_worksheet()
worksheet = workbook.add_worksheet()
worksheet = workbook.add_worksheet()

#set sheetname
worksheet.name = "KKKKKK"
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')


# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()