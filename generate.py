import csv
import matplotlib.pyplot as plt


def generate_graph_loss(datas):
    
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
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Loss (%)')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title('My first graph!')
    
    # function to show the plot
    plt.show()

def generate_graph_throughput(datas):
    
    x = range(0, 30)
    for j in range(0, len(datas)):
        y= []
        for i in x:
            if i > len(datas[j]):
                break
            y.append(datas[j][i].bytes)
        plt.plot(x, y, marker='o', label="hello world")
            
    # plotting the points 
    

    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Troughput (Mbits/s)')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title('My first graph!')
    plt.legend()
    
    # function to show the plot
    plt.show()



