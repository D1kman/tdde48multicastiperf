import csv
import matplotlib.pyplot as plt


def generate_graph_loss(datas,title,file):
    
    x = range(0, 30)
    for j in range(0, len(datas)):
        y= []
        for i in x:
            if i > len(datas[j].data):
                break
            y.append(datas[j].data[i].loss)
        plt.plot(x, y, marker='o', label=datas[j].name, color=color(datas[j].bandwidth))
            
    # plotting the points 
    

    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Loss (%)')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title(title)
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.2,
                 box.width, box.height * 0.8])

# Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)
    
    
    # function to show the plot
    # plt.show()
    plt.savefig("./figs/"+file+"_loss.png")

    plt.close()

def generate_graph_throughput(datas,title,file):
    
    x = range(0, 30)
    for j in range(0, len(datas)):
        y= []
        for i in x:
            if i > len(datas[j].data):
                break
            y.append(datas[j].data[i].bytes)
        plt.plot(x, y, marker='o', label=datas[j].name, color=color(datas[j].bandwidth))
            
    # plotting the points 
    

    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Troughput (Mbits/s)')
    
    # plt.axis([0, 40, 0, 100])
    # giving a title to my graph
    plt.title(title)
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.2,
                 box.width, box.height * 0.8])

# Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)
    
    
    # function to show the plot
    # plt.show()
    plt.savefig("./figs/"+file+"_throughput.png")
    plt.close()

def color(bandwidth):
    if(bandwidth==0.5):
        return "b"
    if(bandwidth==1):
        return "g"
    if(bandwidth==3):
        return "r"
    if(bandwidth==6):
        return "c"
    if(bandwidth==9):
        return "m"
    if(bandwidth==18):
        return "y"
    if(bandwidth==27):
        return "k"
    if(bandwidth==54):
        return "b"
    if(bandwidth==108):
        return "orange"
    if(bandwidth==216):
        return "g"
    if(bandwidth==450):
        return "r"


