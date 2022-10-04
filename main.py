from reader import *
from generate import *

x=[]
files = find("m_cck1_close")
for file in files:
    x.append(read(file))

x.sort(key=lambda x: x.bandwidth)
generate_graph_throughput(x,"Multicast cck1 at ~100% signal strength")
generate_graph_loss(x,"Multicast cck1 at ~100% signal strength")