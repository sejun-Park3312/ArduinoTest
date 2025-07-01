import time
import numpy as np
from ArduinoConnect import ArduinoConnect
from RealTimeData import RealTimeData

AC = ArduinoConnect('COM7', 115200)

RTD = RealTimeData()
RTD.DefineData('Current', ['A', 'PWM'])

freq = 0.2
pwmMax = 255

print("Start Sensing!")
StartTime = time.time()
while time.time() - StartTime < 10:
    t = time.time() - StartTime
    desired_A = (0.75 + 0.25 * np.sin(2 * np.pi * freq * t))
    pwmValue = int((desired_A + 0.015)/1.125 * 255)
    AC.SendArduino(pwmValue)
    Current = AC.ReadArduino()

    RTD.AppendData('Current', [Current[0], desired_A])
    time.sleep(2/1000)

RTD.Running = False
print("End Sensing!")

AC.DisconnectArduino()
# print(sum(RTD.Avg_Data["Current"]["Value"]["A"][-40:])/40)
RTD.SaveData(RTD.Data["Current"], 'Ex')