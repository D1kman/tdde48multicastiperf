import csv
import matplotlib.pyplot as plt
with open('./data/m_cck1_close_1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    x = []
    y = []
    for row in spamreader:
        time=row[6].split("-")[0]
        bytes=row[7]
        lostpacket=row[10]
        packets=row[11]
        jitter=row[9]
        loss=row[12]
        outoforder=row[13]
        if(loss=="-nan"): break
        x.append(time)
        y.append(loss)
        print(time,bytes,jitter,loss,outoforder)
    
    print(x)
    print(y)

    # plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()
