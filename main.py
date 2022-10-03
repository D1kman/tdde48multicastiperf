from reader import *
from generate import *

x=[]
files = find("m_cck5.5_close")
for file in files:
    x.append(read(file))
generate_graph(x)