#This is example of selecting tablewidget's row and enter into assigning LineEdit. 


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import InventoryGUI11
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector

############################## Select whole row #####################################
self.tableWidget_show.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)           

############################## Table size stretch#####################################
        header = self.tableWidget_show.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)

############################## Table No Edit Enable #####################################
self.tableWidget_show.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

def selectedCell(self):
        connection = mysql.connector.connect(host="22.33.44.555",
                                             user="exUser",
                                             password="exPW",
                                             database="inventory"
                                             )

        self.index = self.tableWidget_show.selectedItems()
        self.lineEdit_pn.setText(self.index[0].text())
        self.lineEdit_sku.setText(self.index[1].text())
        self.comboBox_category.setCurrentText(self.index[3].text())
        self.lineEdit_sn.setText(self.index[2].text())
        self.lineEdit_note_info.setText(self.index[4].text())
        self.lineEdit_description.setText((self.index[6].text()))

        if self.index[5].text() == "IN":
            self.lineEdit_status.setText(self.index[5].text())
        else:
            updateq = "SELECT * FROM log WHERE sn = %s"
            values = (self.lineEdit_sn.text(),)

            try:
                c = connection.cursor()
                c.execute(updateq, values)
                result = c.fetchall()
                self.tableWidget_log.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableWidget_log.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_log.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                emp = self.tableWidget_log.item(0,0).text()
                time = self.tableWidget_log.item(0,4).text()
                self.lineEdit_status.setText("OUT by " + emp + " " + time)
                print("ok")

            except:
                print("no")

        self.lineEdit_location.setText((self.index[7].text()))
