import time
import numpy as np
from ArduinoConnect import ArduinoConnect
from RealTimeData import RealTimeData

AC = ArduinoConnect('COM7', 115200)

RTD = RealTimeData()
RTD.DefineData('Current', ['A', 'PWM'])
RTD.Collect_AvgData('Current', 0.05)

freq = 0.05
pwmMax = 255
alpha = 0.7
coeff = [-11.4583,   14.4676,   -6.1424,    1.5870,   -0.0001]

print("Start Sensing!")
StartTime = time.time()
while time.time() - StartTime < 20:
    t = time.time() - StartTime
    duty = 0.75 + 0.25 * np.sin(2 * np.pi * freq * t)
    PWM = int(duty * pwmMax)
    PWM = int(pwmMax * (1-np.polyval(coeff,(1-duty))))

    AC.SendArduino(PWM)
    Current = AC.ReadArduino()
    RTD.AppendData('Current', [Current[0], float(int(duty * pwmMax))/255])

RTD.Running = False
print("End Sensing!")

AC.DisconnectArduino()
# print(sum(RTD.Avg_Data["Current"]["Value"]["A"][-40:])/40)
RTD.SaveData(RTD.Avg_Data["Current"], 'Ex')