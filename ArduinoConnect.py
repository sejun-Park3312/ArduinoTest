import serial
import time

class ArduinoConnect:
    def __init__(self, PortNum, BaudRate):
        self.ArduinoSerial = serial.Serial(PortNum, BaudRate)
        self.Connection = True
        time.sleep(2)
        print("Arduino Connected!")


    def ReadArduino(self):
        try:
            line = self.ArduinoSerial.readline().decode().strip()
            StringValue = line.split(',')
            Value = [float(v.strip()) for v in StringValue]
            return Value
        except Exception as e:
            print(f"Read Failed: {e}")
            return None


    def SendArduino(self, Value):
        try:
            self.ArduinoSerial.write(f"{Value}\n".encode())
        except Exception as e:
            print(f"Send Failed: {e}")


    def DisconnectArduino(self):
        self.ArduinoSerial.write(b'999\n')
        self.ArduinoSerial.close()
        time.sleep(1)
        self.Connection = False
        print("Arduino Disconnected!")
