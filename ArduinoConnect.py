import serial
import time

class ArduinoConnect:
    def __init__(self, PortNum, BaudRate):
        self.ArduinoSerial = serial.Serial(PortNum, BaudRate)
        self.Connection = True
        time.sleep(2)
        print("Arduino Connected!")


    def ReadArduino(self):
        line = self.ArduinoSerial.readline().decode().strip()
        StringValue = line.split(',')
        Value = [float(v.strip()) for v in StringValue]
        return Value


    def SendArduino(self, Value):
        self.ArduinoSerial.write(f"{Value}\n".encode())


    def DisconnectArduino(self):
        self.ArduinoSerial.write(b'999\n')
        self.ArduinoSerial.close()
        time.sleep(1)
        self.Connection = False
        print("Arduino Disconnected!")
