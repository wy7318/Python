#This example display database into tablewidget of PyQt


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import InventoryGUI11
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector

def LoadData(self):
        connection = mysql.connector.connect(host="22.55.66.777",
                                             user="exampleUSER",
                                             password="examplePW",
                                             database="inventory"
                                             )

        query = "SELECT * FROM inventory"

        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        self.tableWidget_show.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_show.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_show.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        cur.close()
