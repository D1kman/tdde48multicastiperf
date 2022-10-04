from reader import *
from generate import *

x=[]
protocol="" 
files = find("u_close")
for file in files:
    x.append(read(file))

x.sort(key=lambda x: x.bandwidth)
generate_graph_throughput(x,"Unicast "+protocol.upper()+" at ~100% signal strength","u_"+protocol+"_close")
generate_graph_loss(x,"Unicast "+protocol.upper()+" at ~100% signal strength","u_"+protocol+"_close")