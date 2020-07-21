import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def writeCsv(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/export.csv", "CSV Files(*.csv *.txt)")
        if path:
            with open(path, 'w') as stream:
                print("saving", path)
                writer = csv.writer(stream, dialect = 'excel', delimiter = ',')
                headers = []
                for column in range(self.tableWidget_show.columnCount()):
                    header = self.tableWidget_show.horizontalHeaderItem(column)
                    if header is not None:
                        headers.append(header.text())
                    else:
                        headers.append("Column " + str(column))
                writer.writerow(headers)
                for row in range(self.tableWidget_show.rowCount()):
                    rowdata = []
                    for column in range(self.tableWidget_show.columnCount()):
                        item = self.tableWidget_show.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
