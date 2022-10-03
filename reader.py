import csv
from types import SimpleNamespace

def read(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        data = []
        for row in reader:
            time=int(row[6].split(".")[0])
            bytes=int(row[7])
            lostpacket=int(row[10])
            packets=int(row[11])
            jitter=float(row[9])
            loss=float(row[12])
            outoforder=int(row[13])
            if(loss=="-nan"): break
            obj = SimpleNamespace()
            obj.time = time
            obj.bytes = bytes
            obj.jitter = jitter
            obj.loss = loss
            obj.outoforder = outoforder
            data.append(0)
            data[time] = obj
    return data

cck1_05 = read("C:/projects/tdde48multicastiperf/data/m_cck1_close_0.5.csv")

cck1_1 = read("C:/projects/tdde48multicastiperf/data/m_cck1_close_1.csv")


