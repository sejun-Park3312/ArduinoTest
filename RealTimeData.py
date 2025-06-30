import time
import numpy as np
import threading

class RealTimeData:
    def __init__(self):
        self.Running = True
        self.Data = {}


    def DefineData(self, DataName, Keys):
        if DataName not in self.Data:
            self.Data[DataName]['Value'] = {key: [] for key in Keys}
            self.Data[DataName]['Time'] = {key: [] for key in ['TimeStamp', 'StartTime']}
            print(self.Data[DataName]['Value'])
            print(f"Data Storage '{DataName}' Created!")
        else:
            print(f"Data Storage '{DataName}' Already Exists!")


    def AppendData(self, DataName, Keys, Value):
        if self.Data[DataName]['Time']['StartTime']:
            for key, value in zip(Keys, Value):
                self.Data[DataName]['Value'][key].append(value)
            self.Data[DataName]['Time']['TimeStamp'] = time.time() - self.Data[DataName]['Time']['StartTime']

        else:
            for key, value in zip(Keys, Value):
                self.Data[DataName]['Value'][key].append(value)
            StartTime = time.time()
            self.Data[DataName]['Time']['StartTime'] = StartTime
            self.Data[DataName]['Time']['TimeStamp'] = 0



    # def CollectData(self):
