from random import uniform as RF

class SensorsData():
    tempTMP = 0
    tempBME = 0
    hum = 0
    press = 0
    gasRes =0
    magY = 0
    magZ = 0
    magX = 0
    accX = 0
    accY = 0
    accZ = 0
    gX = 0
    gY = 0
    gZ = 0
    uva = 0
    uvaI = 0

class Precision():
    tempTMP = 4
    tempBME = 4
    hum = 4
    press = 4
    gasRes = 4
    magY = 4
    magZ = 4
    magX = 4
    accX = 4
    accY = 4
    accZ = 4
    gX = 4
    gY = 4
    gZ = 4
    uva = 4
    uvaI = 4

class StartPoint():
    tempTMP = 20
    tempBME = 20
    hum = 50
    press = 60000
    gasRes = 45000
    magY = 1300
    magZ = 2500
    magX = 1300
    accX = 0
    accY = 0
    accZ = 0
    gX = 4
    gY = 4
    gZ = 4
    uva = 4
    uvaI = 4

class Sensors():
    BME688stat = True
    TMP112stat = True
    ADXL345stat = True
    BMM150stat = True
    GUVA_C32stat = True

    def __init__(self, bus):
        print("Sensors initialized")
        self.output = SensorsData()
        self.precision = Precision()
        self.starting_point = StartPoint()
    def disable_BME688(self):
        self.BME688stat = False
    def disable_TMP112(self):
        self.TMP112stat = False
    def disable_ADXL345(self):
        self.ADXL345stat = False
    def disable_BMM150(self):
        self.BMM150stat = False
    def disable_GUVA_C32(self):
        self.GUVA_C32stat = False

    def setup(self):
        print(f"BME688: {self.BME688stat}\nTMP112: {self.TMP112stat}\nADXL345: {self.ADXL345stat}\nBMM150: {self.BMM150stat}\nGUVA_C32: {self.GUVA_C32stat}")

    def getData(self):
        if self.TMP112stat:
            self.output.tempTMP = round(RF(self.starting_point.tempTMP - 20, self.starting_point.tempTMP + 20), self.precision.tempTMP)

        if self.BME688stat:
            self.output.tempBME = round(RF(self.starting_point.tempBME - 20, self.starting_point.tempBME + 20), self.precision.tempBME)
            self.output.hum = round(RF(self.starting_point.hum - 50, self.starting_point.hum + 50), self.precision.hum)
            self.output.press = round(RF(self.starting_point.press - 10, self.starting_point.press + 10), self.precision.press)
            self.output.gasRes = round(RF(self.starting_point.gasRes - 10, self.starting_point.gasRes + 10), self.precision.gasRes)

        if self.BMM150stat:
            self.output.magY = round(RF(self.starting_point.magY - 10, self.starting_point.magY + 10), self.precision.magY)
            self.output.magZ = round(RF(self.starting_point.magZ - 10, self.starting_point.magZ + 10), self.precision.magZ)
            self.output.magX = round(RF(self.starting_point.magX - 10, self.starting_point.magX + 10), self.precision.magX)

        if self.ADXL345stat:
            self.output.accX = round(RF(self.starting_point.accX - 10, self.starting_point.accX + 10), self.precision.accX)
            self.output.accY = round(RF(self.starting_point.accY - 10, self.starting_point.accY + 10), self.precision.accY)
            self.output.accZ = round(RF(self.starting_point.accZ - 10, self.starting_point.accZ + 10), self.precision.accZ)
            self.output.gX = round(RF(self.starting_point.gX - 1, self.starting_point.gX + 1), self.precision.gX)
            self.output.gY = round(RF(self.starting_point.gY - 1, self.starting_point.gY + 1), self.precision.gY)
            self.output.gZ = round(RF(self.starting_point.gZ - 1, self.starting_point.gZ + 1), self.precision.gZ)

        if self.GUVA_C32stat:
            self.output.uva = round(RF(self.starting_point.uva - 1, self.starting_point.uva + 1), self.precision.uva)
            self.output.uvaI = round(RF(self.starting_point.uvaI - 1, self.starting_point.uvaI + 1), self.precision.uvaI)

        return self.output