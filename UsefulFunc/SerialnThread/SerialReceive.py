import serial
import time
import binascii
import struct
import sys
import glob
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QDialog
import IQgui2
from SerialThread import SerialReadPW, SerialReadVpi, SerialReadBV, SerialReadPL, StatusReading,SerialConnection
from ControlThread import ControlPause, ControlResume, SystemReset, ManualMode, AutoMode, PolarSet, Dither, SetBias
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from IQgui import Ui_Dialog

class MainClass(QDialog,IQgui2.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Device Status Update
        self.pushButton_updatePW.clicked.connect(self.readPW)
        self.pushButton_updateVP.clicked.connect(self.readVpi)
        self.pushButton_updateBV.clicked.connect(self.readBV)
        self.pushButton_updatePL.clicked.connect(self.readPL)
        self.pushButton_updateOS.clicked.connect(self.readStat)

        #Control
        self.pushButton_pause.clicked.connect(self.Pause)
        self.pushButton_resume.clicked.connect(self.Resume)
        self.pushButton_reset.clicked.connect(self.Reset)

        #Connection
        self.lists = self.Comport()
        for self.com in self.lists:
            self.comboBox_comport.addItem(self.com)
        self.pushButton_refresh.clicked.connect(self.refresh)
        self.pushButton_connect.clicked.connect(self.activate)
        self.pushButton_close.clicked.connect(self.Close)

        #Status Display
        self.pushButton_clear.clicked.connect(self.Clear)

        #Setting
        self.pushButton_manual.clicked.connect(self.Manualmode1)
        self.pushButton_setPL.clicked.connect(self.Polarsetting)
        self.pushButton_setDA.clicked.connect(self.DitherS)
        self.pushButton_setBI.clicked.connect(self.BVSetting)
        self.pushButton_why.clicked.connect(self.Qbutton)

        #Groupbox False
        self.groupBox_11.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        self.groupBox_9.setEnabled(False)



    #Read Power Level
    def readPW(self):
        self.mySerial = SerialReadPW(self.comboBox_comport.currentText())
        self.mySerial.start()
        self.mySerial.send.connect(self.lineEdit_updatePW.setText)              #Receive signal and add on textbox
