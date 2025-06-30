from ArduinoConnect import ArduinoConnect
from RealTimeData import RealTimeData
import time
import random

RTD = RealTimeData()
RTD.DefineData('Position', ['x', 'y', 'z'])
RTD.Collect_AvgData('Position', 0.5)

StartTime = time.time()
print("Data Collecting Start!")
while time.time()-StartTime < 10:
    Value = [random.random() for _ in range(3)]
    RTD.AppendData('Position', Value)

    time.sleep(0.1)
RTD.Running = False
print("Data Collecting End!")


RTD.SaveData(RTD.Avg_Data["Position"], 'RTD_Test')