#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import itertools
import networkx
import pickle

N=90
bias=1

group_id=[]

pos={}
edge_list=[]
edge_list_now=[]

#track
for x in range(0,N):
    angle=2*numpy.pi*x/N
    pos[x]=[numpy.cos(angle),numpy.sin(angle)]
    group_id.append(x)
    if x>0:
        edge_list.append((x-1,x,10+bias))
        edge_list.append((x,x-1,10-bias))
        edge_list_now.append((x,x-1))

#loop
edge_list.append((N-1,0,10+bias))
edge_list.append((0,N-1,10-bias))
edge_list_now.append((0,N-1))

#Adjacency matrix
W=numpy.zeros([N,N])
for x in edge_list:
    W[x[0],x[1]]=x[2]

numpy.savetxt("adjacency.csv", W, delimiter=",")
numpy.savetxt("group_id.csv", group_id, delimiter=",")

G=networkx.Graph()
G.add_edges_from(edge_list_now)
plotlib.plot_network_sizefix("network_structure.svg",G,pos,(6,6))
plotlib.plot_network_label("network_label.svg",G,pos)

graph_dump=(G,pos)
pickle.dump(graph_dump, open("graph.pickle","wb"))
