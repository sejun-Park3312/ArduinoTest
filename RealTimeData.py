import time
import threading
import pandas as pd

class RealTimeData:
    def __init__(self):
        self.Running = False
        self.Data = {}
        self.Avg_Data = {}
        self.Buffer = {}
        self.lock = threading.Lock()


    def DefineData(self, DataName, Keys):
        if DataName not in self.Data:
            self.Data[DataName] = {}
            self.Data[DataName]['Value'] = {key: [] for key in Keys}
            self.Buffer = {key: [] for key in Keys}
            self.Data[DataName]['Time'] = {'TimeStamp': [], 'StartTime': None}

            print(self.Data[DataName])
            print(f"Data Storage '{DataName}' Created!")
        else:
            print(f"Data Storage '{DataName}' Already Exists!")


    def AppendData(self, DataName, Value):
        Keys = list(self.Data[DataName]['Value'].keys())

        for key, value in zip(Keys, Value):
            self.Data[DataName]['Value'][key].append(value)
            self.Buffer[key].append(value)

        if self.Data[DataName]['Time']['StartTime']:
            self.Data[DataName]['Time']['TimeStamp'].append(time.time() - self.Data[DataName]['Time']['StartTime'])
        else:
            StartTime = time.time()
            self.Data[DataName]['Time']['StartTime'] = StartTime
            self.Data[DataName]['Time']['TimeStamp'].append(0)

        self.Running = True


    def Define_AvgData(self, DataName, SamplingTime):
        Keys = list(self.Data[DataName]['Value'].keys())
        self.Avg_Data[DataName] = {}
        self.Avg_Data[DataName]['Value'] = {key: [] for key in Keys}
        self.Avg_Data[DataName]['Time'] = {'TimeStamp': [], 'SamplingTime': SamplingTime}
        for keys in Keys:
            self.Avg_Data[DataName]["Value"][keys].append(self.Data[DataName]["Value"][keys][0])
        self.Avg_Data[DataName]['Time']["TimeStamp"].append(0)


    def Append_AvgData(self, DataName, SamplingTime):
        Keys = list(self.Data[DataName]['Value'].keys())
        Flag = True
        RefTime = time.time()
        sleeptime = SamplingTime
        while Flag:
            while self.Running:

                Flag = False
                with self.lock:
                    if DataName not in self.Avg_Data:
                        self.Define_AvgData(DataName, SamplingTime)

                    else:
                        self.Avg_Data[DataName]['Time']["TimeStamp"].append(
                            time.time() - self.Data[DataName]["Time"]["StartTime"])
                        for keys in Keys:
                            if self.Buffer[keys]:
                                avg_value = sum(self.Buffer[keys]) / len(self.Buffer[keys])
                            else:
                                avg_value = self.Data[DataName]['Value'][keys][-1]
                            self.Avg_Data[DataName]['Value'][keys].append(avg_value)
                            self.Buffer[keys] = []
                        sleeptime = 2*SamplingTime - (self.Avg_Data[DataName]['Time']["TimeStamp"][-1] - self.Avg_Data[DataName]['Time']["TimeStamp"][-2])

                time.sleep(sleeptime)

    def Collect_AvgData(self, DataName, SamplingTime):
        threading.Thread(target=self.Append_AvgData, args=(DataName, SamplingTime), daemon=True).start()



    def SaveData(self, Data, FileName):
        FileName += '.xlsx'
        TimeStamp = Data["Time"]["TimeStamp"]
        Value = Data["Value"]

        ExelData = {'Time': TimeStamp}
        for key in Value:
            ExelData[key] = Value[key]

        df = pd.DataFrame(ExelData)
        df.to_excel(FileName, index=False)
        print(f"Data Saved!")