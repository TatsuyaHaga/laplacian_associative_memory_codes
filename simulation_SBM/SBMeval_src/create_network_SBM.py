#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import itertools
import networkx
import pickle

N = int(sys.argv[1]) #number of nodes

Nhier = int(sys.argv[2]) #number of hierarchy
Nsep = int(sys.argv[3]) #number of separation in each hierarchy

Davg = 25 #average degree
ratio = 0.1 #ratio of connection probability across/within community

#connection probability
tmp = 1.0
for i in range(Nhier):
    tmp += (Nsep-1) * (Nsep**i) * (ratio**(i+1))
Pbase = (Nsep**Nhier) * Davg / N / tmp

p_hier = [Pbase]
for i in range(Nhier):
    p_hier.insert(0, Pbase*(ratio**(i+1)))

group_num = Nsep**Nhier
group_id = numpy.zeros(N, dtype=int)
group_hier = numpy.zeros([N,Nhier], dtype=int)

for i in range(N):
    for h in range(Nhier):
        group_hier[i,h] = numpy.random.randint(Nsep)
        group_id[i] += group_hier[i,h]*(Nsep**(Nhier-1-h))

edge_list=[]
for j,k in itertools.combinations(list(range(N)),2):
    #check cluster match
    hmatch=0
    for h in range(Nhier):
        if group_hier[j,h]==group_hier[k,h]:
            hmatch=h+1
        else:
            break
    #sample connection
    if numpy.random.rand()<p_hier[hmatch]:
        edge_list.append([j,k])

print("connection prob.:", p_hier, "avg. degree:", 2*len(edge_list)/N)
map(tuple, edge_list)

#Adjacency matrix
W=numpy.zeros([N,N])
for x in edge_list:
    W[x[0],x[1]]=1.0
    W[x[1],x[0]]=1.0

numpy.savetxt("edgelist.csv", numpy.array(edge_list), delimiter=",", fmt="%d")
numpy.savetxt("group_id.csv", group_id, delimiter=",", fmt="%d")
numpy.savetxt("group_hier.csv", group_hier, delimiter=",", fmt="%d")
numpy.savetxt("adjacency.csv", W, delimiter=",")

G=networkx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from(edge_list)
pos=plotlib.get_pos_spring(G) 
graph_dump=(G,pos)
pickle.dump(graph_dump, open("graph.pickle","wb"))

import pylab
colors = ["blue", "green", "red", "cyan", "magenta", "yellow", "purple", "brown", "pink", "olive"]
nc = networkx.draw_networkx_nodes(G,pos,node_color="blue", node_size=50)
networkx.draw_networkx_edges(G,pos)
pylab.axis("off")
pylab.savefig("network_structure.svg")
pylab.close()
for h in range(Nhier):
    color_list = []
    for i in range(N):
        ind = 0
        for j in range(h+1):
            ind += int(group_hier[i,j]*(Nsep**(h-j)))
        color_list.append(colors[ind%10])
    nc = networkx.draw_networkx_nodes(G,pos,node_color=color_list, node_size=50)
    networkx.draw_networkx_edges(G,pos)
    pylab.axis("off")
    pylab.savefig("network_structure_level"+str(h+1)+".svg")
    pylab.close()
