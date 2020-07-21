import serial
from PyQt5.QtCore import pyqtSignal, QThread
import struct
import binascii
import serial.tools.list_ports

class SerialReadPW(QThread):
    send = pyqtSignal(str)


    def __init__(self, portname, parent=None):
        self.portname = portname
        super(SerialReadPW, self).__init__(parent)
        #QtCore.QThread.__init__(self)

    #def __init__(self, parent=None):

        #self.setupUi(self)
        self.seriport1 = serial.Serial(port=self.portname, baudrate=57600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)


    def run(self):
        self.seriport1.write(b'\x65000000')
        time.sleep(0.1)
        #self.w = self.seriport1.readline()
        self.r = self.seriport1.readline()
        time.sleep(0.1)
        self.w = self.byteForLittleEndian(self.r)
        self.send.emit(str(self.w))
        self.seriport1.close()
        time.sleep(1)

        #print(self.veri)

    def byteForLittleEndian(self, byteInput):         ##For byte to string then cut necessary 4byte for little Endian Calculation
        stg1 = str(byteInput)                   #Convert byte to string
        cut1 = stg1[3:]                         #Cut first 3 string that does not need
        cut2 = cut1[0:-17]                      #Cut last null bytes
        byt1 = cut2.encode('utf-8')             #Change 4byte into byte type
        byt2 = byt1.decode('unicode-escape').encode('ISO-8859-1')           #Remove unnecessary backslash

        res = struct.unpack('<f', byt2)         #4 byte float precision little Endian
        strRes = str(res)
        resCut = self.between(strRes, "(", ",")
        resInt = float(resCut)
        resRound = round(resInt, 4)

        return resRound

    def between(self, value, a, b):                 #cut string
        # Find and validate before-part.
        pos_a = value.find(a)
        if pos_a == -1: return ""
        # Find and validate after part.
        pos_b = value.rfind(b)
        if pos_b == -1: return ""
        # Return middle part.
        adjusted_pos_a = pos_a + len(a)
        if adjusted_pos_a >= pos_b: return ""
        return value[adjusted_pos_a:pos_b]
