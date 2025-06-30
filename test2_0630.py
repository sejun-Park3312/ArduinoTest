import time
import numpy as np
from ArduinoConnect import ArduinoConnect
from RealTimeData import RealTimeData

AC = ArduinoConnect('COM7', 115200)
RTD = RealTimeData()
RTD.DefineData('Current', ['A'])
RTD.Collect_AvgData('Current', 0.02)

freq = 0.2
pwmMax = 255

print("Start Sensing!")
StartTime = time.time()
while time.time() - StartTime < 10:
    t = time.time() - StartTime
    duty = 0.75 + 0.25 * np.sin(2 * np.pi * freq * t)
    PWM = int(duty * pwmMax)

    AC.SendArduino(PWM)
    Current = AC.ReadArduino()

    RTD.AppendData('Current', Current)

RTD.Running = False
AC.DisconnectArduino()
print("End Sensing!")

RTD.SaveData(RTD.Avg_Data["Current"], 'Current_Test')