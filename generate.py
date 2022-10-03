import csv
import matplotlib.pyplot as plt
# with open('./data/m_cck1_close_1.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     x = []
#     y = []
#     for row in spamreader:
#         time=float(row[6].split("-")[0])
#         bytes=float(row[7])
#         lostpacket=float(row[10])
#         packets=row[11]
#         jitter=row[9]
#         loss=float(row[12])
#         outoforder=row[13]
#         if(loss=="-nan"): break
#         x.append(time)
#         y.append(loss)
#         print(time,bytes,jitter,loss,outoforder)

def generate_graph(datas):
    
    x = range(0, 30)
    for j in range(0, len(datas)):
        y= []
        for i in x:
            if i > len(datas[j]):
                break
            y.append(datas[j][i].bytes)
        plt.plot(x, y, marker='o')
            
    # plotting the points 
    

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title('My first graph!')
    
    # function to show the plot
    plt.show()
