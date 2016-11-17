from win32com import client
import os
import sys


def main(inFile, outFile):
    try:

        if not os.path.isfile(inFile):
            print("file not exist")

        xlApp = client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open(inFile)
        books.ExportAsFixedFormat(0, outFile)
        books.Close()
        print("success")
    except:
        print("fail")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
