import csv
import matplotlib.pyplot as plt


def generate_graph_loss(datas):
    
    x = range(0, 30)
    for j in range(0, len(datas)):
        y= []
        for i in x:
            if i > len(datas[j].data):
                break
            y.append(datas[j].data[i].bytes)
        plt.plot(x, y, marker='o')
            
    # plotting the points 
    

    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Loss (%)')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title('Loss')
    
    # function to show the plot
    plt.show()

def generate_graph_throughput(datas):
    
    x = range(0, 30)
    for j in range(0, len(datas)):
        y= []
        for i in x:
            if i > len(datas[j].data):
                break
            y.append(datas[j].data[i].bytes)
        plt.plot(x, y, marker='o', label=datas[j].name)
            
    # plotting the points 
    

    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Troughput (Mbits/s)')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title('Throughput')
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)
    
    
    # function to show the plot
    plt.show()



