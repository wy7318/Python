from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import csv, xlwt, unicodedata, datetime
from functions import barcode
import mysql.connector

self.checkBox_label.stateChanged.connect(self.checkState_label)

def checkState_label(self):
        if self.checkBox_label.isChecked():
            self.label_label.setText("YES")
        else:
            self.label_label.setText("NO")
