from reader import *
from generate import *

x=[]
files = find("u_far")
for file in files:
    x.append(read(file))

x.sort(key=lambda x: x.bandwidth)
generate_graph_throughput(x)